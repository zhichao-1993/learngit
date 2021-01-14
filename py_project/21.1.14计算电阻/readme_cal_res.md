# 计算电阻
## 一、解题思路
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
 
## 二、代码及解答
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

    
## 三、提出问题
 1.
 
## 四、强化薄弱的基础知识
 1.input()函数
 
## 五、重复以上步骤
 1.记录每一次，重复写代码的时间和感悟<br>
 
| 次数 | 时间 | 感悟 |
| :---          |     :---:      |          ---: |
|   1  |  2min    |     |
|       |        |       |

