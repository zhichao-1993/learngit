from tkinter import *  # 导入thinter模块中的所有类   thinter是python中处理Gui的模块
import calendar        # 导入calendar整个模块               calendar是python的处理日历的模块
# from tkinter import * 和 import tkinter 有什么区别？以下是例子
#    import Tkinter            root = Tkinter.Tk()
#    from Tkinter import *     root = Tk()

root = Tk()  # root = Tk()，root.mainloop() 创建了以Gui窗口

# root.geometry("400x300")
root.title("Calendar")  # .title("窗口标题")方法   给窗口取一个标题

# Function
def text():
 month_int = int(month.get())  # 获取月份输入控件的数据
 year_int = int(year.get())    # 获取年份输入控件的数据
 cal = calendar.month(year_int, month_int)  # calendar.month（year，month）方法，返回给定年份、月份的日历
 textfield.delete(0.0, END)     # 删除文本框的内容 ？参数什么意思不理解
 textfield.insert(INSERT, cal)  # 插入文本内容


# Creating Labels 创建标签
label1 = Label(root, text="Month:")  # w = Label ( 框架的父容器, 可选参数16种,text设置文本 )，Label是tkinter的标签控件
label1.grid(row=0, column=0)  # grid()是tkinter的几何管理，管理网格；row行，column列

label2 = Label(root, text="Year:")  # w = Label ( 框架的父容器, 可选参数16种,text设置文本 )，Label是tkinter的标签控件
label2.grid(row=0, column=1)  # grid()是tkinter的几何管理，管理网格；row行，column列

# Creating spinbox
# 创建输入控件，可以指定输入的范围值
month = Spinbox(root, from_=1, to=12, width=8)
# w   = Spinbox(框架的父容器, 从1到12，宽度为8 )
month.grid(row=1, column=0, padx=5)
# padx是外部间隔  ipadx是内部间隔

year = Spinbox(root, from_=2000, to=2100, width=10)
# w   = Spinbox(框架的父容器, 从2000到2100，宽度为8 )
year.grid(row=1, column=1, padx=10)
# padx是外部间隔  ipadx是内部间隔

# Creating Button
#创建按钮
button = Button(root, text="Go", command=text)  # w = Button ( 框架的父容器, text文本内容，command按钮关联的函数 )
button.grid(row=1, column=2, padx=10)
# 第二行的第三列，外部间隔10

# Creating Textfield
# thinter的文本控件Text
textfield = Text(root, width=25, height=10, fg="red")  # w = Text(框架的父容器, 宽25, 高10, fg文本颜色)
textfield.grid(row=2, columnspan=2)  # 第三行，横跨列数二

root.mainloop()