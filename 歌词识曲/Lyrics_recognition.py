# 模糊匹配，process模块，字符串与列表中元素的匹配
# fuzzywuzzy  process,fuzz模块,process模块比较字符串和列表的，fuzz模块是比较两个字符串的
# process.extractOne(字符串,列表)，生成一个元组，返回的第一个是列表中最匹配的元素，第二个是分数
import os
from fuzzywuzzy import process
from fuzzywuzzy import fuzz


def Get_song_keywords(path):
#遍历path下所有文件
    files = os.listdir(path)  # 返回指定目录下的所有文件
    songs = []  # 一个三层嵌套列表，把文件夹下所有的数据存入列表中
    for file in files:  # 遍历文件
        file_name = os.path.join(path, file)  # 路径拼接：路径+文件名=绝对路径
        son = []  # son存的是一个文件的数据，第一个元素是个名字，第二个元素是歌词（歌词是一个列表）
        with open(file_name, 'r', encoding='utf-8')as f:  # 打开文件
            song = f.readline()  # 读取第一行，歌名
            lyric = f.readlines()  # 读取所有的行，歌词列表
            son.append(song)  # 歌名存入son列表中
            son.append(lyric)  # 歌词存入son列表中
            songs.append(son)  # 将son文件存入songs中
    return songs  # 返回songs列表，列表总包含文件夹下所有文件的数据

# 遍历模糊匹配
# process.extractOne(字符串,列表)，生成一个元组，返回的第一个是列表中最匹配的元素，第二个是分数
def search(songs):  # 输入歌词，输出歌名
    ly = input("请输入歌词：")  # 手动输入歌词
    match = process.extractOne(ly, songs)
# 生成一个元组两个元素，第一个元素是列表中最匹配的元素，第二个是对它的打分
    """
    (['世界这么大还是遇见你 - 程响', 
    ['背包塞满青涩的回忆 \n', '就要踏上成长的旅程 \n', '就到 这个路口 \n', '你就不要送我 你快回去 \n', 
    '相逢又告别一句再见 \n', '过去的一切不会重现 \n', '失落的时候 \n', '请像我一样相信你自己 \n', '世界这么大还是遇见你 \n', 
    '多少次疯狂 多少天真 \n', '一起做过梦 \n', '有一天我们会重逢故里 \n', '世界这么大还是遇见你 \n', '一起走过许多个四季 \n', 
    '天南地北 \n', '别忘记我们之间的情谊 \n', '背包塞满青涩的回忆 \n', '就要踏上成长的旅程 \n', '就到 这个路口 \n', '你就不要送我 你快回去 \n', 
    '相逢又告别一句再见 \n', '过去的一切不会重现 \n', '失落的时候 \n', '请像我一样相信你自己 \n', '世界这么大还是遇见你 \n', '多少次疯狂 多少天真 \n', 
    '一起做过梦 \n', '有一天我们会重逢故里 \n', '世界这么大还是遇见你 \n', '一起走过许多个四季 \n', '天南地北 \n', '别忘记我们之间的情谊 \n', 
    '世界这么大还是遇见你 \n', '多少次疯狂 多少天真 \n', '一起做过梦 \n', '有一天我们会重逢故里 \n', '世界这么大还是遇见你 \n',
     '一起走过许多个四季 \n', '天南地北 \n', '别忘记我们之间的情谊 \n', '世界这么大还是遇见你 \n', '多少次疯狂 多少天真 \n', '一起做过梦 \n',
      '有一天我们会重逢故里 \n', '世界这么大还是遇见你 \n', '一起走过许多个四季 \n', '天南地北 \n', '别忘记我们之间的情谊 ']], 60)
    """

    if match[1] >= 50:  # 如果大于50分
        print(match[0][0])  # 就打印歌名
    else:  # 否则就打印没有
        print('没有匹配的歌词')


if __name__ == "__main__":
    path = 'lyric'  # 歌词文件夹
    songs = Get_song_keywords(path)  # 将文件夹下的所有文件的数据存入列表
    search(songs)  # 遍历模糊匹配，输入歌词，输出歌名
