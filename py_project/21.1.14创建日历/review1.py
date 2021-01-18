"""
创建日历
1.创建Gui界面
    Tk()
    框架父容器.mainloop()
2.给界面命名
    框架父容器.title()
3.创建标签
    Label text
4.创建输入控件
    Spinbox from_,to,width   row,column,padx
5.创建按钮
    Button  text,command
6.创建文本框
    Text width,height,fg(颜色)
         row,columnspan
7.函数：
    1.获取输入控件的数据
    2.获取日历
        caldenar.month(年，月)
    3.日历数据插入文本框
        .delete 清空数据
        .insert 插入数据d
"""
import calendar
from tkinter import *

root = Tk()
root.title("Calendar")
label1 = Label(root, text='Month:')
label1.grid(row=0, column=0)
label2 = Label(root, text='Year:')
label2.grid(row=0, column=1)

def text():
    month_int = int(month.get())
    year_int = int(year.get())
    cal = calendar.month(year_int,month_int)
    text.delete(0.0,END)
    text.insert(INSERT,cal)


month = Spinbox(from_=1, to=12, width=7)
month.grid(row=1, column=0,padx=10)
year = Spinbox(from_=1990, to=2100, width=7)
year.grid(row=1, column=1,padx=10)

button =Button(root, text='Go', command=text)
button.grid(row=1, column=2)

text =Text(root,width=25,height=10,fg='red')
text.grid(row=2, columnspan=2)

root.mainloop()