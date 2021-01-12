"""
密码检查器
1.写一个固定的密码
2.写一个检查密码的函数
    2.1.密码输入错误等于5次，休眠30秒，继续运行本函数  #1.if语句 2.==比较运算符 3.time。sleep()方法
    2.2.循环5次 # 1.for循环 2.range()函数
        2.2.1.用户输入密码 # 1.input()函数
        2.2.2.比较 固定密码 和 用户输入密码 # 1.for循环遍历字符串的索引 2.if语句 3.==比较运算符 4.if-else语句 5.break语句
            2.2.2.1.输出密码正确或错误 # 1.if-else语句 2.break语句
"""

import time
pwd = "wzc1993"

def password_check():
  count1 =0
  for i in range(5):
    a = 0  # a是pwd的长度
    count = 0  # count是user_pwd的长度
    user_pwd = input("请输入密码：")
    for j in range(len(pwd)):  # 以固定密码的长度进行循环
      if user_pwd[j] == pwd[a]:  # 把固定密码的索引给user_pwd
        a += 1  # a是pwd的长度
        count += 1  # count是user_pwd的长度
    if count == len(pwd):  # 如果pwd长度等于user_pwd的长度，就说明密码正确
      print("密码正确")
      break  # 跳出循环
    else:  # 否则密码错误，count1加1
      count1 +=1
      print("密码错误")
  if count1 == 5:  # 如果密码输入错误等于5次，休眠30秒，继续运行本函数
    time.sleep(30)
    password_check()

password_check()

