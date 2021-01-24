"""
debug:
1.ModuleNotFoundError: No module named 'email.mime'; 'email' is not a package
    解决：文件名和模块名字一样，冲突了
"""
import smtplib
from email.mime.text import MIMEText

fro_add="17301764830@163.com"
to_add="1522554132@qq.com"

smtpObj = smtplib.SMTP('smtp.163.com',25)  # 创建SMTP实例,链接SMTP服务器
smtpObj.ehlo()  #
smtpObj.starttls  # tls加密
smtpObj.login('17301764830@163.com','XWNRJMELACZEFSTR')  # 登录邮箱
msg = MIMEText('sendmail by python', 'plain', 'utf-8') #邮件正文

msg['From'] = fro_add #发送方邮箱
msg['To'] = to_add #接收方邮箱
msg['Subject'] = 'My mail' #邮箱主题

smtpObj.sendmail(fro_add,to_add,msg.as_string()) #发送邮件
smtpObj.quit() #关闭邮箱
