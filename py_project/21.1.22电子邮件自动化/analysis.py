"""
电子邮件自动化
"""
import smtplib  # 负责发送邮件
# mime包的三个模块是负责构建邮件
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fro_add="1522554132@qq.com"  # 发送者地址
to_add="17301764830@163.com"  # 接收者地址

message=MIMEMultipart()
message['From']=fro_add  # 发送者地址
message['To']=",".join(to_add)
message['subject']="Testinf mail"

body='Hai this is dilip ,How are you'

message.attach(MIMEText(body,'plain'))

email=" "  # 用户名
password=" "  # 用户密码


# 负责发送邮件
mail=smtplib.SMTP('smtp.163.com',25)  # 实例化SMTP(),并且连接邮箱服务器
mail.ehlo()
mail.starttls()  # tls加密
mail.login(email,password)  # 登录到邮箱
text=message.as_string()  #  text是邮件的内容，  as_string()将message变成str
mail.sendmail(fro_add,to_add,text)  # 发送邮件，sendmail(from_addr（发送者地址）,to_addrs（接收者地址）,msg（邮件内容）)
mail.quit()  # 结束SMTP会话