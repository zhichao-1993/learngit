"""
获取任何给定文本中每个字符的数目
1.写一个main函数:输入文件名字，输出字典
    1.输入文件名
        1.Counter计数器直接将文本里，每个字符的数目存到字典里
        2.try-except
            文件找不到，重新输入
        3.打印输出 pprint
"""
import collections
import pprint


def main():
    file_input = input('File Name: ')
    try:
        with open(file_input, 'r') as info:
            count = collections.Counter(info.read().upper())  # 获取任何给定文本中每个字符的数目,并存在字典里
    except FileNotFoundError:
        print("Please enter a valid file name.")
        main()

    value = pprint.pformat(count)  # 将字典漂亮的输入
    print(value)
    exit()


if __name__ == "__main__":
    main()