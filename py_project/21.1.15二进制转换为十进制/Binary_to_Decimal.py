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