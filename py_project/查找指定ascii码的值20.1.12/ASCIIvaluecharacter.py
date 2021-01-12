"""
用于查找给定字符的ASCII值的程序
"""
# 1.输入需要查找的字符
c = input("输入要查找的字符：")  # 1.input()函数，返回string类型
# 2.查找指定的字符的ASCII值 # 1. ord()函数，返回字符对应的ASCII值
asc = ord(c)
# 3.打印ASCII值
print("{0}的ASCII值是{1}".format(c, asc))  # 1.print()函数 2.format()函数
