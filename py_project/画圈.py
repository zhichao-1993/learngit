"""
以给定的半径画圆
turtle库 ： 绘制图像的函数库
思路：
1.导入turtle库
2.实例化turtle ； 同过 turtle 库 ，调用 Turtle() 方法 ， 创建一个实例
3.调用circle()方法，以给定的半径画圆 ； 使用了 circle() 方法
"""
# 1. 导入turtle库
import turtle
# 2. 实例化turtle ； 同过 turtle 库 ，调用 Turtle() 方法 ， 创建一个实例
t = turtle.Turtle()
#  通过实例 ， 调用 circle() 方法 ， 来以给定的半径画圈
t.circle(20)
t1 = turtle.Turtle()
t1.circle(25)
t2 = turtle.Turtle()
t2.circle(50)
