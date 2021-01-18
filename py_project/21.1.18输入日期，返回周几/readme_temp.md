# 题目
输入具体日期，返回时周几
## 一、分析代码
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
## 二、代码及思路
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
    
    debug:
    1.datetime.datetime.strptime() 输入2021，参数写的是%y，对不上，所以报错
        %y 两位数的年份表示（00-99）
        %Y 四位数的年份表示（000-9999）
        %m 月份（01-12）
        %d 月内中的一天（0-31）
        %H 24小时制小时数（0-23）
        %I 12小时制小时数（01-12）
        %M 分钟数（00=59）
        %S 秒（00-59）
    
    问题：
    1.re.sub()替换的作用：就是让你的输入格式多一点，如果没有正则替换，你就要指定输入的格式
    """
    import re
    import datetime
    import calendar
    
    def replace_date(user_input):
        user_input = re.sub('/', ' ',user_input)
        user_input = re.sub('-', ' ', user_input)
        return user_input
    
    
    def find_date(date):
        week = datetime.datetime.strptime(date, "%d %m %Y").weekday()
        return calendar.day_name[week]
    
    
    user_input = str(input("请输入日期："))
    date = replace_date(user_input)
    weekday = find_date(date)
    print("日期{0}是{1}".format(user_input, weekday))


## 三、提出问题
 1.re.sub()替换的作用
    就是让你的输入格式多一点，如果没有正则替换，你就要指定输入的格式
 
## 四、强化薄弱的基础知识
 1.正则
 2.datetime模块
 3.calendar模块
 4.input()
 
## 五、重复以上步骤
 1.记录每一次，重复写代码的时间和感悟<br>
 
| 次数 | 时间 | 感悟 |
| :---          |     :---:      |          ---: |
|   1  |  2min    |     |
|       |        |       |

