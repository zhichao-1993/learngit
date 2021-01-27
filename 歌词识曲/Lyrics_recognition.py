# 输入要查询的歌词和处理好的字典，输出歌名
# dgbug:
#       1.songs={}变量放到了for循环里面，每次循环都被清空了，放到循环外面就解决了
import os
def Get_song_keywords(path):
#遍历path下所有文件，将数据存入字典
    files = os.listdir(path)# 返回指定目录下的所有文件和目录名
    songs = {}
    for file in files:
        file_name=os.path.join(path,file) # 路径拼接
        with open(file_name,'r',encoding='utf-8')as f:
            song = f.readline()
            lyric = f.read()
            songs[lyric] = song
    return songs

# 遍历搜索
def search(songs):
    ly = input("请输入歌词：")
    count = 0
    for lyrics in songs.keys():
        count += 1
        if ly in lyrics:
            print(songs[lyrics])
            break
        elif count == len(songs):
            print('没有匹配的歌词')


if __name__ == "__main__":
    #递归遍历目录下所有文件
    path = 'lyric'
    songs = Get_song_keywords(path)
    search(songs)
