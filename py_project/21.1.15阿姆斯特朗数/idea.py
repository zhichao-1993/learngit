"""
检测阿姆斯特朗数
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
1.输入数字
2.获取数字长度
3.while循环：获取每一位数
4.输出打印
    如果等于，输出是
    不等于就不是
"""
num = int(input("请输入数字:"))
f = num
n = len(str(num))
sum = 0


while (f > 0):  # f要大于0，才能执行
    a = f%10  # 取最后一位数
    sum = sum + a ** n
    f //= 10  # 取整除赋值运算符，c //= a 等效于 c = c // a。把最后一位数给去掉


if(sum == num):
    print("it is an armstrong number:", num)
else:
    print("it is not an armstrong number:", num)
