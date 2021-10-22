from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

# 创建对象的基类:
Base = declarative_base()
# 定义User对象


class User(Base):
    # 表的名称
    __tablename__ = 'user'
    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接: 但是这里会报错，也不知道之前是怎么连接成功的。
engine = create_engine('mysql+mysqlconnector://root:gonghui21513049@localhost:3306/test')

# 创建DBSession类型: DBSession对象可视为当前数据库连接
DBsession = sessionmaker(bind=engine)

# 下面，我们看看如何向数据库表中添加一行记录。

# 创建session对象:
session = DBsession()
# 创建新User对象:
new_user = User('id=6', name='Tutu')
# 添加到session:
session.add(new_user)
# 提交到数据库
session.commit()
# 关闭session
session.close()

time.sleep(5)

# 创建session对象:
session = DBsession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭sesssion
session.close()





