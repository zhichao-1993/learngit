"""
Python 判断奇数偶数
    1.运用了%取模运算
"""
num = int(input("请输入数字："))
if num%2 ==0:
    print("{}是偶数".format(num))
else:
    print("{}是奇数".format(num))
