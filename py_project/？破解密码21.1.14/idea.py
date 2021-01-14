"""
破解密码
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v','w', 'x', 'y', 'z',]
1.输入随机密码（纯英文字母），用以下代码破解
2.用列表装24个英文字母
3.创建空字符串，存随机密码
4.while循环，guess和user_pass不同就一直循环
    1.遍历字符串的位置
        1.在那个位置上随机生成字母
        2.把它们拼接起来
    2.打印guess
5.打印成功的密码
"""
from random import *
user_pass = input("请输入密码：")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v','w', 'x', 'y', 'z',]
guess = ""
while(guess !=user_pass):
    guess = ""
    for i in range(len(user_pass)):
        guess_password = password[randint(0, 25)]
        guess = str(guess) + str(guess_password)
    print(guess)
print("你的密码是：{0}".format(guess))