"""
用python计算三角形的面积
（已知三角形的三边5，6，7，可以使用海伦公式直接计算出三角形的面积，
其中p=（a+b+c）/2，a，b，c是三角形的三条边。
公式中三角形的面积S=√p(p-a)(p-b)(p-c)，）
"""
a = float(input("请输入第一条边："))
b = float(input("请输入第一条边："))
c = float(input("请输入第一条边："))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("三角形的面积是%.2f"%area)
print("三角形的面积是{:.2f}".format(area))