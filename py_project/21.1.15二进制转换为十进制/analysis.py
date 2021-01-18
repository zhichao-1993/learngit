"""
#Program to convert binary to decimal
#将二进制转换为十进制的程序
二进制转为十进制要从右到左用二进制的每个数去乘以2的相应次方
"""


def binaryToDecimal(binary):  # 函数的作用：将输入的二进制，转换为十进制。输入二进制，输出十进制
	"""
 >>> binaryToDecimal(111110000)
	496
 >>> binaryToDecimal(10100)
	20
 >>> binaryToDecimal(101011)
	43
	"""
	decimal, i , n= 0, 0, 0  # decimal十进制；i相当与索引（位置），从右向左；
	while(binary != 0):  # while结束条件，二进制等于0时
		dec = binary % 10  # 求模，取余，就是取最后一位数
		decimal = decimal + dec * pow(2, i)  # pow(x,y) 返回x的y次方，将每一位数相加
		binary = binary//10  # 向下取整，去掉最后一位数
		i += 1  # 索引加1
	print(decimal)

binaryToDecimal(10100)