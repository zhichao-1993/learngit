"""
1.输入数字的数量n
2.输入n个数字
"""
n = input("请输入元素数量：\n")
print("你好，请输入n个数字以空格分隔")
a = input().split()  # 返回列表
b = map(int, a)  # 返回迭代器
tlist = list(b)  # 返回列表
k = max(tlist)  # 返回列表里的最大值
n = len(tlist)  # 返回列表的长度
