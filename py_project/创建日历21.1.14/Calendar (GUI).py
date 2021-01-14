"""
创建日历
1.创建Gui界面
    Tk()
    框架父容器.mainloop()
2.给界面命名
    框架父容器.title()
3.创建标签
    Label
4.创建输入控件
    Spinbox
5.创建按钮
    Button
6.创建文本框
    Text
7.函数：
    1.获取输入控件的数据
    2.获取日历
        caldenar.month(年，月)
    3.日历数据插入文本框
        .delete 清空数据
        .insert 插入数据

debug
1.Button按钮的参数command=a写错了，写成了a()方法
    command=方法的名字，不可以等于方法
"""

from tkinter import *
import calendar

root = Tk()
root.title("Calendar")


def a():
    month_int = int(month.get())
    year_int = int(year.get())
    cal = calendar.month(year_int,month_int)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)


label1 = Label(root, text="Month:")
label1.grid(row=0, column=0)
label2 = Label(root, text="Year:")
label2.grid(row=0, column=1)

month = Spinbox(root, from_=1, to=12, width=7)
month.grid(row=1, column=0, padx=5)
year = Spinbox(root, from_=1990, to=2100, width=7)
year.grid(row=1, column=1, padx=7)

button = Button(root, text='Go', command=a)
button.grid(row=1, column=2, padx=10)


textfield = Text(root, width=25, height=10, fg="red")
textfield.grid(row=2, columnspan=2)

root.mainloop()




