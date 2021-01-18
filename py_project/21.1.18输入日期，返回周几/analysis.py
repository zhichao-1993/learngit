"""
输入具体日期，返回时周几
"""
# Python程序查找
# 某一特定日期的一周
import re # 正则表达式
import calendar  # python模块提供与日历相关的有用功能
import datetime  # 模块的python获取日期和时间

def process_date(user_input):  #  函数的作用：将你输入的日期，空格、/和-换成空格。处理好的数据，传入find_day（）函数，查找是周几
    user_input = re.sub(r"/", " ", user_input)  # 用空格代替/
    # re.sub re正则表达式，re.sub表示替换
    user_input = re.sub(r"-", " ", user_input)  # 用空格代替-
    # re.sub re正则表达式，re.sub表示替换
    return user_input

def find_day(date):  #
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() #此语句返回与一周中的某一天相对应的整数。
    #  datetime.datetime.strptime（string日期，format字符串的格式化）返回的是一个格式化日期
    #  date.weekday() 返回0-6，代表周一到周日
    return (calendar.day_name[born]) # 此语句将对应的日期名称返回给上一条语句中生成的整数。
    #  calendar.day_name 是calendar模块内置的一个列表，等于这个list =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday ']

#从用户获取输入
#用户可键入1/2/1999或1-2-1999
#为了克服这些问题，我们必须处理用户的输入，并按照日历和时间模块的定义使其成为标准。
user_input=str(input("Enter date: "))
date=process_date(user_input)
print("Day on " +user_input + " is "+ find_day(date) )