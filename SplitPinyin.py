# -*- coding:utf-8 -*-
"""
作者：Hsy_Xju
日期：2022年11月17日
"""


def ShengMu(strs):
    smlist = 'bpmfdtnlgkhjqxrzcsyw'
    nosm = ['eR', 'aN', 'eN', 'iN', 'uN', 'vN', 'nG', 'NG']
    # rep = {'ZH': 'Zh', 'CH': 'Ch', 'SH': 'Sh'}

    for s in smlist:
        strs = strs.replace(s, s.upper())

    for s in nosm:
        strs = strs.replace(s, s.lower())

    return strs


# 切分声母韵母
def SplitPinyin(strs):
    upper_strs = ''
    lower_strs = ''
    # yd_char = ''
    for char in strs:
        if char.isupper():
            upper_strs += char
        # elif char.isdigit():
        #     yd_char += char
        else:
            lower_strs += char
    # 求声母+韵母+音调
    # return upper_strs.lower(), lower_strs, yd_char
    return upper_strs.lower(), lower_strs


# objPinyin = 'chang1'
# pinyin_convert = ShengMu(objPinyin)
# upperp, lowerp = SplitPinyin(pinyin_convert)
# print(pinyin_convert)
# print(upperp, lowerp)
