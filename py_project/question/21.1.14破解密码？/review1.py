"""
破解密码
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v','w', 'x', 'y', 'z',]
1.输入随机密码（纯英文字母），用以下代码破解
2.用列表装24个英文字母
3.创建空字符串，存随机密码
4.while循环，guess和user_pass不同就一直循环
    1.遍历字符串的位置 range()函数：生成数字列表；遍历的是位置
        1.在那个位置上随机生成字母 randint()函数：生成随机数
        2.把它们拼接起来
    2.打印guess
5.打印成功的密码
"""
import random
user_pwd = input("请输入密码：")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v','w', 'x', 'y', 'z',]
guess = ""
while(guess != user_pwd):
    guess = ""
    for i in range(len(user_pwd)):
        ran = random.randint(0,25)
        guess_pass = password[ran]
        guess = guess + guess_pass
    print(guess)
print("你的密码是：{}".format(guess))