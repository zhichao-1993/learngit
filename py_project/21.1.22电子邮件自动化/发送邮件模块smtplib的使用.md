# smtplib发送邮件模块
## 发送邮件步骤
 1.创建SMTP实例，并连接到SMTP服务器  
 2.加密  
 3.登录邮箱  
 4.编写邮箱正文  
 5.发送方邮件地址  
 6.接受方邮件地址  
 7.邮箱主题    
 8.发送邮件  
 9.关闭邮箱
 
 
    import smtplib  # 负责发送邮件的模块
    from email.mime.text import MIMEText  # mime包的text模块的作用：构建邮件内容
    smtpObj = smtplib.SMTP('smtp.163.com',25)  # 创建SMTP实例,链接SMTP服务器
    smtpObj.ehlo()  # 
    smtpObj.starttls  # tls加密
    smtpObj.login('17301764830@163.com','pwd')  # 登录邮箱
    msg = MIMEText('sendmail by python', 'plain', 'utf-8') #邮件正文 
    msg['From'] = 'from_add' #发送方邮箱 
    msg['To'] = 'To_add' #接收方邮箱 
    msg['Subject'] = 'My mail' #邮箱主题 
    smtpObj.sendmail('from_add','to_add',msg.as_string()) #发送邮件 
    smtpObj.quit() #关闭邮箱 
    