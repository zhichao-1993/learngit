"""
计算电阻
并联电阻：R=R1*R2/R1+R2
串联电阻：sum = R1 + R2
"""


def res(R1, R2):  # 计算电阻的函数，输入两个电阻，输出计算好的电阻
    sum = R1 + R2  # 串联电阻的计算方式
    if (option == "series"):  # 如果是串联，返回计算好的串联电阻
        return sum
    else:  # 否则，就返回计算好的并联电阻
        return (R1 * R2) / (R1 + R2)


Resistance1 = int(input("Enter R1 : "))  # 手动输入电阻R1
Resistance2 = int(input("Enter R2 : "))  # 手动输入电阻R2
option = str(input("Enter series or parallel :"))  # 手动输入选项是串联还是并联
print("\n")  # 换行
R = res(Resistance1, Resistance2)  # 调用计算电阻的函数
print("The total resistance is", R)  # 打印计算好的函数

