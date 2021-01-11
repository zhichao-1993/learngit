"""
冒泡 排序（升序）：相邻的两个元素进行比较，如果顺序(如从大到小或从小到大)错误就交换它们的位置
交换元素以按顺序排列
"""

# 方法一：
def bubblesort(list): # 函数解决的问题：对列表进行冒泡排序  #输入：列表  输出：排好序的列表
    for i in range(len(list)-1,0,-1): # 冒泡次数：需要排序的列表的长度减一
        # 外层循环：range函数创建的整数列表的长度：代表需要冒泡的次数
        # 整数列表中的元素：代表着每次内层循环需要比较的次数
        for j in range(i):  # 内层循环：i代表着每次内层循环需要比较的次数
            if list[j]>list[j+1]: # 如果前面>后面，用赋值的方法，把它们的值赋给对方
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list


# 方法二：
def bubble_sort(list): # 函数解决的问题：对列表进行冒泡排序  #输入：列表  输出：排好序的列表
    for i in range(0, len(list)-1): # 冒泡次数：需要排序的列表的长度减一
        # 外层循环：range函数创建的整数列表的长度：代表需要冒泡的次数
        for j in range(0, len(list)-1-i):  # 整数列表中的元素：代表着每次内层循环需要比较的次数
            # 冒玩一次泡后（就是外循环一次）：内层循环需要比较的次数就要 - 1
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

if __name__ == '__main__': # 1.作为脚本直接执行 2.import到其他的python脚本中被调用
    list = [111,879,223,987,225,333]
    list1=bubblesort(list)
    list2=bubble_sort(list)
    print(list1,list2)