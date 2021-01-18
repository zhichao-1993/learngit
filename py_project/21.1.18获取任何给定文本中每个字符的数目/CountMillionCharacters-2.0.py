"""
获取任何给定文本中每个字符的数目
1.写一个main函数:输入文件名字，输出字典
    1.输入文件名
        1.Counter计数器直接将文本里，每个字符的数目存到字典里
        2.try-except
            文件找不到，重新输入
        3.打印输出 pprint
2.if name == main
"""
import collections
import pprint

def main():
    file_input = input("请输入文件名：")
    try:
        with open(file_input,'r') as fp:
            a = fp.read().lower()
            count = collections.Counter(a)
    except FileNotFoundError:
        print("请输入有效文件名：")
        main()

    value = pprint.pformat(count)
    print(value)
    exit()

if __name__ == "__main__":
    main()


