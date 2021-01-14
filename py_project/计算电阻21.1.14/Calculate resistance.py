"""
计算电阻
串联电阻：sum = R1 + R2
并联电阻：R=R1*R2/R1+R2
1.手动输入两个电阻
    input（）函数，返回string类型
    所以输入数字的时候，必须数据类型转换(int，float)
2.手动输入选项
    input()函数
3.换行
4.函数：计算电阻
    def
    if-else
5.调用函数，计算电阻
    调用函数
6.打印输出
    format()函数

debug
1.input数字的时候，没有类型转换，所以运行结果变成了字符串的拼接了
"""
Resistance1 = int(input("请输入R1电阻："))
Resistance2 = int(input("请输入R2电阻："))
option = input("请输入是串联还是并联：")
print("\n")


def cal(R1, R2):
    if option == '串联':
        return R1+R2
    else:
        return (R1*R2)/(R1+R2)


R = cal(Resistance1, Resistance2)
print("总电阻是{0}".format(R))
