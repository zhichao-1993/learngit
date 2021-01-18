"""
Python 摄氏温度转华氏温度
摄氏温度转华氏温度的公式为 celsius * 1.8 = fahrenheit - 32。所以得到以下式子：
    1.input（）
    2.%格式化字符串：%0.1f
"""
Centigrade = float(input("请输入摄氏温度："))
Fahrenheit = Centigrade*1.8+32
print("%0.1f摄氏温度转为华氏温度为%0.1f"%(Centigrade,Fahrenheit))