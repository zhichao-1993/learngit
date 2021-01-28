#7. 数据存入csv
import os
import json
import csv
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
def Get_song_keywords(path):
#遍历filepath下所有文件，包括子目录
    files = os.listdir(path)# 返回指定目录下的所有文件和目录名
    songs=[]
    for file in files:
        file_name=os.path.join(path,file) # 路径拼接
        son=[]
        with open(file_name,'r',encoding='utf-8')as f:
            song = f.readline()
            lyric = f.readlines()
            son.append(song)
            son.append(lyric)
            songs.append(son)
    return songs

def csv_save(new_file,songs): # 传入songs列表，输出csv文件
    with open(new_file,'w',newline='',encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerows(songs)
    return new_file

def csv_read(c): # 输入csv文件，输出list
    son=[]
    with open(c,'r',encoding='utf-8') as fp:
        reader = csv.reader(fp)
        for i in reader:
            son.append(i)
    return son

# 遍历匹配
# process.extractOne(字符串,列表)，生成一个元组，返回的第一个是列表中最匹配的元素，第二个是分数
# AttributeError: ‘str’ object has no attribute ‘load’;解决办法不应将变量名命名为 json。
def search(songs):
    ly=input("请输入歌词：")
    match=process.extractOne(ly,songs)
    if match[1]>=50:
        print(match[0][0])
    else:
        print('没有匹配的歌词')
if __name__ == "__main__":
    #递归遍历目录下所有文件
    path=r'C:\Users\java\Desktop\python\lyric'
    songs=Get_song_keywords(path)
    file=csv_save('songs.csv',songs)
    son=csv_read(file)
    search(son)