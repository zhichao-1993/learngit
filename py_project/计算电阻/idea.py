"""
计算电阻
并联电阻：R=R1*R2/R1+R2
串联电阻：sum = R1 + R2
1.手动输入两个电阻
2.手动输入选项
3.换行
4.函数：计算电阻
5.调用函数，计算电阻
6.打印输出
"""
Resistance1 = int(input("请输入电阻R1："))
Resistance2 = int(input("请输入电阻R2："))
option = input("请输入是串联还是并联：")
print("\n")


def cal(R1, R2):
    sum = R1+R2
    if option == '串联':
        return sum
    else:
        return (R1*R2)/(R1+R2)


R = cal(Resistance1, Resistance2)
print("总电阻是{0}".format(R))
