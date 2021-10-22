from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = '1756486242@qq.com'  # 填写完整的邮箱地址
password = 'drvmhmoeudkocgee'  # 填写你开启qq邮箱imap服务时生成的密码
to_addr = '18867144948@163.com'
smtp_server = 'smtp.qq.com'  # 写法如下 smtp.qq.com

# 下面这几部就是为了让这个msg有正文，from， to， 主题。
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('小易易<%s>' % to_addr)
msg['Subject'] = Header('来自smtp的问候', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


