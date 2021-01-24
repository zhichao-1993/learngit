"""

"""
def Lyrics_recognition(file,lyric):
    with open(file,'r',encoding='utf-8') as f:
        list1=f.readlines()
        list2=[]
        for i in list1:
            i=i.split('\n')
            list2.append(i[0].strip())
        if lyric in list2:
            print(list2[0])
        else:
            print(False)
file = r'小小的新娘花.txt'
lyric = '风儿吹来了童年的一幅画'
Lyrics_recognition(file,lyric)