# -*- coding:utf-8 -*-
"""
作者：shay
日期：2022年11月16日
"""
# import json
# import jsonpath
import os
from GetAllPinyin import GetAllPinyin, GetPinyin


# 导入json文件并提取拼音
# obj = json.load(open('F:\SeienceResearch\Marktasks\jsons\pinyin.json', 'r', encoding='utf-8'))
# pinyin_l = jsonpath.jsonpath(obj, '$..text')  # 文件对象jsonpath语法
# while '' in pinyin_l:
#     pinyin_l.remove('')
# while 'sil' in pinyin_l:
#     pinyin_l.remove('sil')


def ExtractAndGenerate():
    # 导入text文件中的汉字
    f = open('YourMp3ToText.txt', 'r+', encoding='utf-8')
    wordList = f.read()
    ChineseWordList = [0 for i in range(len(wordList))]  # 拿来放从文件每行找到的汉字
    f.seek(0)  # 注意将读文件指针回到开头

    word = f.read(1)
    i = 0
    while word:
        if word == '，' or word == '。' or word == ' ':
            word = ''
        ChineseWordList[i] = word
        i = i + 1
        word = f.read(1)
    f.close

    while '' in ChineseWordList:
        ChineseWordList.remove('')

    SaveHZList = []
    SaveLastList = []
    SavePYList = []

    # 获得对应的全拼 声调 声母 韵母等
    pinyin_l = GetAllPinyin(ChineseWordList)
    ShengmuList, YunmuList1, YunmuList2 = GetPinyin(ChineseWordList, pinyin_l)

    # 输出保存到文件中
    z_c_s_r = ['z', 'c', 's']
    zh_ch_sh = ['zh', 'ch', 'sh']
    i_1_2_3_4 = ['i1', 'i2', 'i3', 'i4']
    f_word = open("HistoryLog.txt", "a", encoding="utf-8")

    for h in ChineseWordList:
        SaveHZList.append(str(h))
        f_word.write("%8s" % (str(h)))
    f_word.write("\n\n")

    for p in pinyin_l:
        SavePYList.append(str(p))
        if len(p) > 5:
            f_word.write("%7s" % (str(p)))
        else:
            f_word.write("%-9s" % (str(p)))
    f_word.write("\n\n")

    SaveLastList.append("sil")
    for sm, ym, ym1 in zip(ShengmuList, YunmuList2, YunmuList1):
        # 如果最后一个音调不一样，肯定是多音字，我们选取切分的非转写韵母,#号标注多音字
        # print(ym, ym1)
        # if ym1[-1] != ym[-1]:
        #     f_word.write("%3s#%-5s" % (str(sm), str(ym1)))
        #     continue
        # 韵母不一样，要么多音字要么转写韵母
        # if ym1 != ym:
        #     f_word.write("%3s*%5s " % (str(sm), str(ym)))
        #     continue

        if sm in z_c_s_r and ym1 in i_1_2_3_4:
            SaveLastList.append(str(sm))
            SaveLastList.append("iy" + str(ym1[-1]))
            SaveLastList.append("sil")
            f_word.write("%3s*iy%-5s" % (str(sm), str(ym1[-1])))
            continue
        if sm in zh_ch_sh and ym1 in i_1_2_3_4:
            SaveLastList.append(str(sm))
            SaveLastList.append(("ix" + str(ym1[-1])))
            SaveLastList.append("sil")
            f_word.write("%3s*ix%-5s" % (str(sm), str(ym1[-1])))
            continue
        if sm == 'r' and ym1 in i_1_2_3_4:
            SaveLastList.append(str(sm))
            SaveLastList.append(("iz" + str(ym1[-1])))
            SaveLastList.append("sil")
            f_word.write("%3s*iz%-5s" % (str(sm), str(ym1[-1])))
            continue
        if sm != '' and sm != 'w' and sm != 'y':
            SaveLastList.append(str(sm))
        SaveLastList.append(str(ym))
        SaveLastList.append("sil")
        f_word.write("%3s%5s " % (str(sm), str(ym)))
    f_word.write("\n\n")

    f_word.close()
    print(SaveHZList, SavePYList, SaveLastList)
    return SaveHZList, SavePYList, SaveLastList
