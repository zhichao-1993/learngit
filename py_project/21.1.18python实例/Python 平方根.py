"""
Python 平方根
1.用户输入一个数字
    input()函数，返回string类型（所以输入数字的时候，需要类型转换）
2.计算平方根
    python平方根为：**0.5
3.打印
"""
num = float(input("请输入数字："))
square_root = num ** 0.5
print("{0}平方根是{1}".format(num,square_root))