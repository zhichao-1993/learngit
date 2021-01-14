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
user_pass = input("Enter your password: ")  # 输入随机密码
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v','w', 'x', 'y', 'z',]  # 24个英文字母
guess = ""  # 存贮破解的密码
while (guess != user_pass):  # while循环，当密码不等于用户输入的密码，就一直循环
    guess = ""  # ？循环里的guess和循环外的guess有什么区别

    # 使用的是user_pass的长度，所以随机密码的长度和user_pass是一样的
    # 因为是随机密码，所以和user_pass本身一点关系都没有，只和他的长度有关
    for letter in range(len(user_pass)):  # range用户输入的长度，相当于遍历字符串的索引（就是位置）；
        guess_letter = password[randint(0, 25)]  # randint(0,25)随机生成0到24范围内的数字；随机生成一个字母
        guess = str(guess) + str(guess_letter)  # 将随机生成的字母进行拼接



    print(guess)
print("Your password is", guess)
