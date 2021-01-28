# 输入要查询的歌词和处理好的字典，输出歌名
# dgbug:
#       1.songs={}变量放到了for循环里面，每次循环都被清空了，放到循环外面就解决了
import os

def Get_song_keywords(path):
#遍历path下所有文件，将数据存入字典
    files = os.listdir(path)  # 返回指定目录下的所有文件
    songs = {}  # 空字符串
    for file in files:  # 对指定目录下的文件进行遍历
        file_name = os.path.join(path, file)  # 路径拼接：目录名字+文件名字=绝对路径
        with open(file_name,'r',encoding='utf-8')as f:  # 对文件的读写
            song = f.readline()  # 读取第一行，歌名
            lyric = f.read()  # 读取第二行到最后，歌词
            songs[lyric] = song  # 歌词未key，歌名为value，存入字典
    return songs  # 返回字典

# 遍历匹配
def search(songs):  # 输入存有歌词的列表，输出歌名
    ly = input("请输入歌词：")  # 手动输入歌词
    count = 0  # count计数，如果等于字典的长度，就说明没有匹配的歌词
    for lyrics in songs.keys():  # 对于字典的key进行遍历，key存有歌词
        count += 1  # 遍历一首歌曲，就加一
        if ly in lyrics:  # 如果歌词在key里面
            print(songs[lyrics])  # 就输出value，并且break
            break
        elif count == len(songs):  # 如果等于字典的长度，就说明没有匹配的歌词
            print('没有匹配的歌词')


if __name__ == "__main__":
    path = 'lyric'  # 目录
    songs = Get_song_keywords(path)  # 将目录中的数据存入字典
    search(songs)  # 输入歌词，进行匹配
