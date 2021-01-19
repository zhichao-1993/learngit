"""
1.输入元素数量n
2.在输入n个数字
3.将排列好的数字，放到列表里

问题：
1.看不懂counting_sort函数
 1.不知道计数列表是什么？
 2.[0] * (k + 1)不知道它有什么用处？
"""
# python program for counting sort (updated)
#python程序用于计数排序(更新)
n = int(input("请给出元素的数量\n"))  # 手动输入元素的数量n
print("好的，现在请输入n个由空格分隔的数字")
tlist = list(map(int, input().split()))
# map(function,iterable) function函数；iterable一个或多个序列。序列中的每一个元素调用function函数，返回迭代器（里面的值都调用了function函数）
# split(str,num)  str分隔符，默认是所有的空字符，包括空格、换行符和制表符；num分割次数.将分隔的元素放在列表里。
k = max(tlist)  # max() 获取列表的最大值
n = len(tlist)  # len() 获取列表的长度


def counting_sort(tlist, k, n):  # 输入列表，最大值，列表长度；输出排好序的列表
    """
        数数排序，排序就位。
        Args：
            Tlist：要排序的目标列表
            K：假设已知的最大值
            N：给定列表的长度
            将信息映射到计数列表的索引。
        ADV：
            计数(和和之后)将按排序顺序保存元素的实际位置。
            利用上面这些，
    """

    # 创建一个计数列表，并使用索引映射到tlist中的整数。
    count_list = [0] * (k + 1)  # 1.不知道计数列表是什么？ 2.[0] * (k + 1)不知道它有什么用处？

    # 迭代tgt_list以放入计数列表中
    for i in range(0, n):
        count_list[tlist[i]] += 1

    # 修改计数列表，使计数列表的每个索引都是以前计数的总和。
    # 每个索引都表示输出序列中的实际位置(或序列)。
    for i in range(1, k + 1):
        count_list[i] = count_list[i] + count_list[i - 1]

    flist = [0] * (n)
    for i in range(n - 1, -1, -1):
        count_list[tlist[i]] = count_list[tlist[i]] - 1
        flist[count_list[tlist[i]]] = (tlist[i])

    return flist


flist = counting_sort(tlist, k, n)
print(flist)