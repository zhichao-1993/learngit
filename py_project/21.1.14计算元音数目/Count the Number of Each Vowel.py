"""
计算字符串中每一个元音的数量
1.用变量存元音字母的字符串
2.用变量存一段话的字符串
    str不是python关键字，可以作为变量名
3.将字符串的大写变成小写
    str.lower()
    str.caseflod()
4.创建一个计数的字典，将元音作为字典的key，value值默认为0
    {}.fromkeys(keys,value)
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



