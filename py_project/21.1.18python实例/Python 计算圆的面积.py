"""
圆的面积公式为 ：
s = Πr平方
公式中 r 为圆的半径。
"""


def cal_cir_area(r):  # 输入半径，返回面积
    PI = 3.142
    area = PI*(r**2)
    return area


r = float(input("请输入半径："))
area = cal_cir_area(r)
print("圆的面积是{:.6f}".format(area))