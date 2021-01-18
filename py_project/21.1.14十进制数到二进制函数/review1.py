"""
十进制到二进制
    1.bin()函数：把十进制变成二进制
"""
dec = int(input("请输入十进制数："))
bin = bin(dec)
print("十进制数{}转换成二进制数{}".format(dec,bin))