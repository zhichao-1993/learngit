"""
输入具体日期，返回时周几
"""
# Python程序查找
# 某一特定日期的一周
import re # 正则表达式
import calendar  # python模块提供与日历相关的有用功能
import datetime  # 模块的python获取日期和时间

def process_date(user_input):
    user_input = re.sub(r"/", " ", user_input)  # 用空格代替/用空格
    user_input = re.sub(r"-", " ", user_input)  # 用空格代替
    return user_input

def find_day(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() #此语句返回与一周中的某一天相对应的整数。
    return (calendar.day_name[born]) #此语句将对应的日期名称返回给上一条语句中生成的整数。

#从用户获取输入
#用户可键入1/2/1999或1-2-1999
#为了克服这些问题，我们必须处理用户的输入，并按照日历和时间模块的定义使其成为标准。
user_input=str(input("Enter date "))
date=process_date(user_input)
print("Day on " +user_input + " is "+ find_day(date) )