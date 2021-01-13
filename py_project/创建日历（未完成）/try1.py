from tkinter import *
import calendar

# 1.创建一个Gui窗口，
root = Tk()

# 2.并给窗口去一个名字
root.title("Calendar")

# 3.添加标签
label1 = Label(root, text="month:")
label1.grid(row=0, column=0)
label2 = Label(root, text="year:")
label2.grid(row=0, column=1)

# 4.创建一个输入控件Spinbox
month = Spinbox(root, from_=1, to=12, width=7)
month.grid(row=1, column=0, padx=5)
year = Spinbox(root,from_=1990, to=2100, width=7)
year.grid(row=1, column=1, padx=5)

# 5.创建按钮
button = Button(root, text="Go")  # command=text()
button.grid(row=1, column=2, padx=10)

# 6.创建空的文本框
textfield = Text(root, width=25, height=10, fg='red')
textfield.grid(row=2, columnspan=2)

# 7.获取末年某月的日历
cal = calendar.month(2016, 1)
print(cal)

# 8.删除文本框的内容
textfield.delete(0.0, 'end')  # 删除文本框的内容
textfield.insert(INSERT, cal)  # 插入文本内容

root.mainloop()


