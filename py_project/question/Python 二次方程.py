# Filename : test.py
# author by : www.runoob.com
 
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0
 
# 导入 cmath(复杂数学运算) 模块
import cmath
 
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
 
# 计算
d = (b**2) - (4*a*c)  # ? 这个公式是什么意思
 
# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)  # ? sqrt() 方法返回数字x的平方根。这一行是什么意思
sol2 = (-b+cmath.sqrt(d))/(2*a)  # ? 这一行是什么意思
 
print('结果为 {0} 和 {1}'.format(sol1, sol2))