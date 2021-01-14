# 计算字符串中每一个元音的数量
## 一、解题思路
    """
    计算字符串中每一个元音的数量
    """
    vowels = 'aeiou'  # 元音字母
    
    ip_str = 'Hello, have you tried our tutorial section yet?'
    
    ip_str = ip_str.casefold()  # casefold()方法，大写转小写；lower()方法也可以
    
    count = {}.fromkeys(vowels, 0)  # 字典的fromkeys(seq,value)方法，以seq中的元素作为字典的键值；value默认未None，也可以自己设置
    
    for char in ip_str:  # 遍历字符串的元素，判断是否在字典中
       if char in count:
           count[char] += 1
    
    print(count)
 
## 二、代码及解答
    """
    计算字符串中每一个元音的数量
    1.用变量存元音字母的字符串
    2.用变量存一段话的字符串
        str不是python关键字，可以作为变量名
    3.将字符串的大写变成小写
        str.lower()
        str.caseflod()
    4.创建一个计数的字典，将元音作为字典的key，value值默认为0
        {}.fromkeys()
    5.判断字符串中的元素是否在字典里，在的话，value值加1
        for循环遍历
        if
    6.打印字典
        print
    """
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    str = 'Hello, have you tried our tutorial section yet?'
    str = str.lower()
    count = {}.fromkeys(vowels, 0)
    for i in str:
        if i in count:
            count[i] += 1
    print(count)

    
## 三、提出问题
 1.
 
## 四、强化薄弱的基础知识
 1.str.lower()
 2.str.caseflod()
 3.{}.fromkeys()
 
## 五、重复以上步骤
 1.记录每一次，重复写代码的时间和感悟<br>
 
| 次数 | 时间 | 感悟 |
| :---          |     :---:      |          ---: |
|   1  |  2min    |     |
|       |        |       |

