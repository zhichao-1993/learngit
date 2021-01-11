"""
输入两个数字，求和
思路：
1.输入两个数字（换行） ； input语句 ， 创建两个对象
2.求和（可能会出现小数） ； float类型转换
3.输出打印（用format函数） ； format格式化函数
"""
#添加两个数字
num1 = input("first number:")
num2 = input("\nsecond number:")
#两个数字相加
#可以输入浮点数
sum = float(num1) + float(num2)
#以浮点形式打印值
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))