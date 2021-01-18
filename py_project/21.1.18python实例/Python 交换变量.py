"""
Python 交换变量
"""
x = input("请输入x的值：")
y = input("请输入y的值：")
# 交换赋值
temp = x
x = y
y = temp
print("交换后x的值为：{}".format(x))
print("交换后y的值为：{}".format(y))
