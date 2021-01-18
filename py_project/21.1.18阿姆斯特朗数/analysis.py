"""
检测阿姆斯特朗数
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
"""
num=int(input("请输入数字:"))
f=num
n = len(str(num))
sum=0
while (f>0):  # f<=0结束循环
    a=f%10  # 取最后一位数（取模）
    sum = sum + a ** n
    f //= 10  # 取整除赋值运算符，c //= a 等效于 c = c // a。向下取整
if (sum == num):
    print("it is an armstrong number:", num)
else:
    print("it is not an armstrong number:", num)