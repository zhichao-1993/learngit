"""
输入具体日期，返回时周几
1.函数：用正则替换年月日的格式。输入日期（格式：日月年），返回日期（格式被替换了）
    1.re.sub()函数，替换
2.函数：发现日期
    1.datetime.datetime.strptime（）
    2.日期.weekday()
    3.calendar.day_name[] 用calendar内置的列表，访问对应的元素
3.手动输入日期
    1.input()
    2.string是一个模块，str是一个类型。string不推荐使用
4.调用以上函数
5.打印日期和周几
"""
import re
import calendar
import datetime


def replace_date(user_input):
    user_input = re.sub('/', ' ', user_input)
    user_input = re.sub('-', ' ', user_input)
    return user_input


def find_date(date):
    weekday = datetime.datetime.strptime(date, "%d %m %Y").weekday()
    return calendar.day_name[weekday]


user_input = str(input("请输入日期："))
date = replace_date(user_input)
weekday = find_date(date)
print("日期{0}是{1}".format(user_input, weekday))
