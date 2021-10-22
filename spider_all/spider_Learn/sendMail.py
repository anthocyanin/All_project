from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '18867144948@163.com'
password = 'wangyi123456'
to_addr = '1756486242@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('Python 爬虫遇到异常，异常信息为http 403', 'plain', 'utf-8')
msg['From'] = _format_addr('一号爬虫<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('一号爬虫运行状态', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
