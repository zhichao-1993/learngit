"""
fuzz.ratio(s1,s2)直接计算s2和s2之间的相似度，返回值为0-100，100表示完全相同；

fuzz.partial_ratio(S1,S2)部分匹配，如果S1是S2的子串依然返回100；

fuzz.token_sort_ratio(S1,S2)只比较S1，S2单词是否相同，不考虑词语之间的顺序；

fuzz.token_set_ratio(S1，S2)相比fuzz.token_sort_ratio不考虑词语出现的次数；

process.extract(S1, ListS,limit=n)，表示从列表ListS中找出Top n与S1最相似的句子;

process.extractOne(S1,ListS)，返回最相似的一个
"""
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
S1='我的天空'
S2='我的妈呀'

a=fuzz.token_set_ratio(S1,S2)
print(a.get)



