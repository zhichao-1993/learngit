# 题目
## 一、解题思路
### 解题思路都在对代码的分析里面
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
 
## 二、代码及解答
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
    
## 三、提出问题
 1.提出问题<br>
   + from tkinter import * 和 import tkinter 有什么区别？从模块导入所有的类 和 导入模块 有什么区别？
     + 从模块导入指定的类，速度会快一点；导入模块会导入所有的类，速度要慢一点
   + 1.import Tkinter root = Tkinter.Tk()  
     2.from Tkinter import *     root = Tk()  
     + 问题：import里有的方法，from里没有
   
## 四、强化薄弱的基础知识
 1. 类的实例化 root = Tk()
 2. 调用方法 .title()
 3. int强制类型转换  int(month.get()) 
 4. 函数
 5.thinter：python的Gui模块
 6.calendar：python的日历模块
  
## 五、重复以上步骤
 1.记录每一次，重复写代码的时间和感悟<br>
 
| 次数 | 时间 | 感悟 |
| :---          |     :---:      |          ---: |
|     |      |     |
|       |        |       |

