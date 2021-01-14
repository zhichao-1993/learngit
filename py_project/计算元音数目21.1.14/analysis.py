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
