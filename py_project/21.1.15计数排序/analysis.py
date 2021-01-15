"""

"""
# python program for counting sort (updated)
#python程序用于计数排序(更新)
n = int(input("请给出元素的数量\n"))
print("好的，现在请输入n个由空格分隔的数字")
tlist = list(map(int, input().split()))
k = max(tlist)
n = len(tlist)


def counting_sort(tlist, k, n):
    """ Counting sort algo with sort in place.
        Args:
            tlist: target list to sort
            k: max value assume known before hand
            n: the length of the given list
            map info to index of the count list.
        Adv:
            The count (after cum sum) will hold the actual position of the element in sorted order
            Using the above,

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

    # Create a count list and using the index to map to the integer in tlist.
    # 创建一个计数列表，并使用索引映射到tlist中的整数。
    count_list = [0] * (k + 1)

    # iterate the tgt_list to put into count list
    # 迭代tgt_list以放入计数列表中
    for i in range(0, n):
        count_list[tlist[i]] += 1

    # Modify count list such that each index of count list is the combined sum of the previous counts
    # 修改计数列表，使计数列表的每个索引都是以前计数的总和。
    # each index indicate the actual position (or sequence) in the output sequence.
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