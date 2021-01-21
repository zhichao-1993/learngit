# 获取列表中整数、浮点数和字符串的数量

## 一、分析代码
    """
    获取列表中整数、浮点数和字符串的数量
    1.分析的列表
    2.给i,f,s赋值
    3.for循环
        1.判断是否是int,float,str类型(isinstance()判断)
        2.是的话，在个数上加一
    """
    a = ['Hello', 35, 'b', 45.5, 'world', 60]  # 包含字符串、整数和浮点数的列表
    i = f = s = 0
    # i代表整数的个数 f代表浮点数的个数 s代表字符串的个数
    for j in a:
        if isinstance(j, int):
            # 1.type(实例)和isinstance(实例，（类名，基本类型或它们组成的元组）)，都可以判断类型
            # 2.对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False
            i = i + 1
        elif isinstance(j, float):
            f = f + 1
        else:
            s = s + 1
    print('整数有{}个'.format(i))
    print('浮点数有{}个'.format(f))
    print('字符串有{}个'.format(s))
## 二、代码及思路
    """
    获取列表中整数、浮点数和字符串的数量
    1.分析的列表
    2.给i,f,s赋值
    3.for循环
         1.判断是否是int,float,str类型(isinstance()判断)
         2.是的话，在个数上加一
    """
    a = ['Hello', 35, 'b', 45.5, 'world', 60]
    i = f = s = 0
    for j  in a:
        if isinstance(j, int):
            i = i+1
        elif isinstance(j, float):
            f = f+1
        elif isinstance(j, str):
            s = s+1
    print("列表中整数类型有{}个".format(i))
    print("列表中浮点数类型有{}个".format(f))
    print("列表中字符串类型有{}个".format(s))
## 三、提出问题
 1.变量名用重复了，for用的是i，表示int的也是i
 
## 四、强化薄弱的基础知识
 1.isinstance(实例，(类名，类型，元组))
 
## 五、重复以上步骤
 1.记录每一次，重复写代码的时间和感悟<br>
 
| 次数 | 时间 | 感悟 |
| :---          |     :---:      |          ---: |
|   1  |  2min    |     |
|       |        |       |

