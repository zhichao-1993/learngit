"""
# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# 生成 0 ~ 9 之间的随机数

# 导入 random(随机数) 模块
"""
import random
a =random.randint(1, 3)
if a in range(1, 6):
    print("选择恶臭")
elif a in range(6, 11):
    print("选择假酒法")
elif a in range(11, 16):
    print("选择6野兽2娜迦")
elif a in range(16, 21):
    print("选择6骑士2术2亡")
elif a in range(21, 26):
    print("选择4骑士6亡")
elif a in range(26, 30):
    print("选择9战士")
