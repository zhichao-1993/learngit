"""
用python计算三角形的面积
（已知三角形的三边5，6，7，可以使用海伦公式直接计算出三角形的面积，
其中p=（a+b+c）/2，a，b，c是三角形的三条边。
公式中三角形的面积S=√p(p-a)(p-b)(p-c)，）
"""
# 1.输入边长
a = float(input("输入第一个边："))  # 1.float()函数，返回浮点值  2.input（）函数，接受数据，返回string类型
b = float(input("输入第二个边："))
c = float(input("输入第三个边："))

# 2.计算半周长
s = (a+b+c)/2

# 3.计算面积
area = (s*(s-a)*(s-b)*(s-c))**0.5

# 4.打印面积(保留2位小数的两种方法)
print("三角形的面积是%0.2f" % area)  # %格式化字符串，"%.2f"%area
print("三角形的面积是{:.2f}".format(area))  # format()格式化字符串，"{:.2f}".format(area)
