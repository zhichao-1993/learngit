# 题目
二进制转十进制
## 一、分析代码
       """
    #Program to convert binary to decimal
    #将二进制转换为十进制的程序
    二进制转为十进制要从右到左用二进制的每个数去乘以2的相应次方
    """
    def BinarytoDecimal(Binary):
        decimal = 0
        i = 0
        while(Binary != 0 ):
            dec = Binary % 10
            decimal= decimal + dec*pow(2, i)
            Binary = Binary//10
            i += 1
        print(decimal)
    
    BinarytoDecimal(100)
## 二、代码及思路
       """
    #Program to convert binary to decimal
    #将二进制转换为十进制的程序
    二进制转为十进制要从右到左用二进制的每个数去乘以2的相应次方
    """
    def BinarytoDecimal(Binary):
        decimal = 0
        i = 0
        while(Binary != 0 ):
            dec = Binary % 10
            decimal= decimal + dec*pow(2, i)
            Binary = Binary//10
            i += 1
        print(decimal)
    
    BinarytoDecimal(100) 
## 三、提出问题
 1.
 
## 四、强化薄弱的基础知识
 1.while循环，结束条件，为false时，结束
 2.pow(x,y)
 
## 五、重复以上步骤
 1.记录每一次，重复写代码的时间和感悟<br>
 
| 次数 | 时间 | 感悟 |
| :---          |     :---:      |          ---: |
|   1  |  2min    |     |
|       |        |       |

