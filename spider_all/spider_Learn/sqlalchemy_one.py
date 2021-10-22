from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import time

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:gonghui21513049@localhost:3306/test')


# 创建DBSession类型， 可理解为创建一个连接数据库的会话，但他又是一个类
DBSession = sessionmaker(bind=engine)

# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
session = DBSession()  # 实例化一个对象
new_user = User(id='5', name='Bob')
session.add(new_user)

session.commit()
session.close()

time.sleep(5)
# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：
session = DBSession()
user = session.query(User).filter(User.id == '5').one()
print('type: ', type(user))
print('name:', user.name)
session.close()

