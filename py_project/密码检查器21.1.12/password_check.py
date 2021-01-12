"""
密码检查器
"""
# 1.一个固定的密码
import time
pwd = "wzc1993"

# 2.写一个密码检查的函数 #在函数里面输入密码 #输出密码是否正确
def password_check():

    count1 = 0
    # 2.2循环5次
        # 2.2.1.用户输入密码   1.input()函数，接受用户输入的密码，返回string类型
        # 2.2.2.比较固定密码和用户输入密码
    for i in range(5):
        a = 0  # a是pwd的索引
        count = 0  # count是用来计user_pwd的个数的
        user_pwd = input("请输入密码：")
        for j in range(len(pwd)):
            if user_pwd[j] == pwd[a]:
                a += 1
                count += 1
        if count == len(pwd):
            print("密码正确")
            break
        else:
            count1 += 1
            print("密码错误")

    # 2.1密码输入错误等于5次，休眠30秒，继续运行函数
         #  1.if语句  2.==比较运算符  3.time.sleep()函数  4. count1对象，初始为0，放最前面
    if count1 == 5:
        time.sleep(30)
        password_check()


password_check()

