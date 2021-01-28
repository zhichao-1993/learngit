import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
# 歌词url
url = "https://music.163.com/weapi/song/lyric"

# 请求参数
data = {
    "params": "AeD2ElKiKl4q6I30ReDnsEifoCslqY + fVw1UG3LaNiGyWpUhMkVzVEaqTQtIGLiJ",
    "encSecKey": "c16c0ce1651c5385cc1aed22cb452621d3d4d4da92a06d05591b0f88e0a0f0070af8db1fd3b330a6e8106cd291ecb7b314f92056f7154bbcc4925e696f0ee85bc673824a07b10de1ee4dc4d25c603b0f0fce52985b4c4361adab30a1e346fae29730e9443ca472e92bbfa1fb7ed4f232fde519f1efd6c23567662681a3e1d831"

}
response = requests.post(url=url, data=data, headers=headers)

json_str = response.content.decode('utf-8')

dic_str = json.loads(json_str)['tlyric']["lyric"]
with open('wangyiyun.txt','w',encoding='utf-8') as f:
    f.write(dic_str)
print(dic_str)

# https://music.163.com/weapi/song/lyric
"""
params: AeD2ElKiKl4q6I30ReDnsEifoCslqY+fVw1UG3LaNiGyWpUhMkVzVEaqTQtIGLiJ
encSecKey: c16c0ce1651c5385cc1aed22cb452621d3d4d4da92a06d05591b0f88e0a0f0070af8db1fd3b330a6e8106cd291ecb7b314f92056f7154bbcc4925e696f0ee85bc673824a07b10de1ee4dc4d25c603b0f0fce52985b4c4361adab30a1e346fae29730e9443ca472e92bbfa1fb7ed4f232fde519f1efd6c23567662681a3e1d831

"""