# 题目
获取任何给定文本中每个字符的数目
## 一、分析代码
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
## 二、代码及思路
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
        file = input("请输入文件名：")
        try:
            with open(file, 'r') as fp:
                a = fp.read().lower()
                count = collections.Counter(a)
        except FileNotFoundError:
            print("没有找到指定文件")
            main()
    
        value = pprint.pformat(count)
        print(value)
        exit()
    
    if __name__ == "__main__":
        main()
## 三、提出问题
 1.
 
## 四、强化薄弱的基础知识
 1.try-except
 2.with open
 3.collections.Counter 计数器
 4.pprint 
 5.if __name__ == "__main__":
 
## 五、重复以上步骤
 1.记录每一次，重复写代码的时间和感悟<br>
 
| 次数 | 时间 | 感悟 |
| :---          |     :---:      |          ---: |
|   1  |  2min    |     |
|       |        |       |

