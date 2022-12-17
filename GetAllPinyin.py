# from xpinyin import Pinyin
from pypinyin import pinyin, Style
from SplitPinyin import ShengMu, SplitPinyin


# 从汉字获取拼音
def GetAllPinyin(chineseword_l):
    llen = len(chineseword_l)
    pinyin_list = [0 for i in range(llen)]  # 拿来放从每个汉字找到的拼音
    for i in range(llen):
        pinyin_list[i] = pinyin(str(chineseword_l[i]), Style.TONE3, heteronym=False, errors='default', strict=True)[0][0]
    return pinyin_list


# 汉字转拼音
def GetPinyin(chineseword_l, pinyin_list):
    llen = len(pinyin_list)
    # ChineseWordList = getChineseWord(pinyin_list)
    shengmu_l = [0 for i in range(llen)]  # 拿来放我们自己分割的声母
    yunmu_l1 = [0 for i in range(llen)]  # 拿来放我们自己分割的韵母
    yunmu_l2 = [0 for i in range(llen)]  # 拿来放我们自己分割的韵母
    for x in range(llen):
        shengmu_l[x], yunmu_l1[x] = SplitPinyin(ShengMu(str(pinyin_list[x])))
        yunmu_l2[x] = pinyin(str(chineseword_l[x]), style=Style.FINALS_TONE3, heteronym=False, errors='default', strict=True)[0][0]

    return shengmu_l, yunmu_l1, yunmu_l2

# # 从拼音获取汉字
# def getChineseWord(pinyin_list):
#     """
#     根据拼音获取汉字
#     param: 拼音和声调
#     return: 生成拼音列表
#     """
#     llen = len(pinyin_list)
#     p = Pinyin()
#     ChineseWord = [0 for i in range(llen)]  # 拿来放从每个拼音找到的汉字

#     j = 0
#     for x in pinyin_list:
#         # if x == '':
#         #     ChineseWord[j] = ''
#         #     j += 1
#         #     continue
#         for i in range(0x4e00, 0x9fa6):
#             word = chr(i)
#             ret = p.get_pinyin(word, tone_marks='numbers', splitter=' ')
#             if ret == x:
#                 ChineseWord[j] = word
#                 break
#         j += 1

#     # print(ChineseWord)
#     return ChineseWord
