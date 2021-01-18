"""
#Program to convert binary to decimal
#将二进制转换为十进制的程序
二进制转为十进制要从右到左用二进制的每个数去乘以2的相应次方
1.写函数：输入二进制，输出十进制
"""

def binaryToDecimal(binary):
    decimal = 0
    i = 0
    while(binary !=0):
        dec = binary%10
        decimal = decimal + dec*pow(2, i)
        binary= binary//10
        i += 1
    print(decimal)

binaryToDecimal(10100)
