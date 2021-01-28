# 6. 数据存入json,读取json
# fuzzywuzzy  process,fuzz模块,process模块比较字符串和列表的，fuzz模块是比较两个字符串的
# 1.将目录中的内容放到列表中去
import os
import json
from fuzzywuzzy import process
from fuzzywuzzy import fuzz


def Get_song_keywords(path):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(path)  # 返回指定目录下的所有文件和目录名
    songs = []
    for file in files:
        file_name = os.path.join(path, file)  # 路径拼接
        son = []
        with open(file_name, 'r', encoding='utf-8')as f:
            song = f.readline()
            lyric = f.readlines()
            son.append(song)
            son.append(lyric)
            songs.append(son)
    return songs


# 生成一个三层列表，第一层元素是歌，第二层元素是歌名+歌词列表，第三层元素是每一句歌词


def json_save(new_file, songs):  # 传入songs列表，输出json文件
    with open(new_file, 'w', encoding='utf-8') as fp:
        json.dump(songs, fp, ensure_ascii=False)
    return new_file


def json_read(j):  # 输入json文件，输出
    with open(j, 'r', encoding='utf8') as fp:
        json_str = json.load(fp)
    return json_str


# 遍历匹配
# process.extractOne(字符串,列表)，生成一个元组，返回的第一个是列表中最匹配的元素，第二个是分数
# AttributeError: ‘str’ object has no attribute ‘load’;解决办法不应将变量名命名为 json。
def search(songs):
    ly = input("请输入歌词：")
    match = process.extractOne(ly, songs)
    if match[1] >= 50:
        print(match[0][0])
    else:
        print('没有匹配的歌词')


if __name__ == "__main__":
    # 递归遍历目录下所有文件
    path = r'C:\Users\java\Desktop\python\lyric'
    songs = Get_song_keywords(path)
    j = json_save('songs.json', songs)
    m = json_read(j)
    search(m)
