"""
Python 判断字符串是否为数字
1.写一个函数判断字符串是否是数字:输入字符串，返回True或Flase
    1.处理异常-->数据类型转换
    2.处理异常-->导入字符数据库unicodedata-->numeric()把表示数字的字符串转换为浮点数返回
    3.如果不是数字，返回False

问题：
1.异常处理不熟练
2.异常类型：
    ZeroDivisionError：分母为0的异常
    TypeError：类型有误的异常
    NameError：没有定义就使用的异常
    IndexError：下标越界的异常
    FileNotFoundError：文件找不到的异常
    SyntaxError：语法错误　
    ValueError：常见于：传入一个调用者不期望的值，即使值的类型是正确的
"""


def is_number(s):  # 输入字符串，返回True或Flase
    try:
        float(s)  # 数据类型转换
        return True
    except ValueError:
        pass  # 空语句，就是用来占位置的

    try:
        import unicodedata  # unicodedata是一个字符数据库
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回
        return True
    except (TypeError, ValueError):
        pass

    return False

a = is_number('5')
print(a)