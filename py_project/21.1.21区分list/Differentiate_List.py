"""
获取列表中整数、浮点数和字符串的数量
1.分析的列表
2.给i,f,s赋值
3.for循环
     1.判断是否是int,float,str类型(isinstance()判断)
    2.是的话，在个数上加一

debug:
 1.变量名用重复了，for用的是i，表示int的也是i
"""
a = ['Hello', 35, 'b', 45.5, 'world', 60]
i = f = s = 0
for j in a:
    if isinstance(j, int):
        i += 1
    elif isinstance(j, float):
        f += 1
    elif isinstance(j, str):
        s += 1
print("整数类型有{}个".format(i))
print("浮点数类型有{}个".format(f))
print("字符串类型有{}个".format(s))
