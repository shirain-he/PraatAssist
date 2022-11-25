# -*- coding:utf-8 -*-
"""
作者：Hsy_Xju
日期：2022年11月25日
"""
import textgrid
from ExtractAndGet import ExtractAndGenerate

# 导入textgrid
tg = textgrid.TextGrid()
tg.read('YourTextGrid.TextGrid')
# 先清空mark内容
for i in range(len(tg.tiers)):
    for j in range(len(tg.tiers[i])):
        tg.tiers[i][j].mark = ''
tg.write('YourTextGrid.TextGrid')

savehz_l, savepy_l, savelast_l = ExtractAndGenerate()
hz_i = 0
py_i = 0
ll_i = 0
SilenceString = 'sil'
for i in range(len(tg.tiers)):
    if tg.tiers[i].name == 'word':
        for j in range(len(tg.tiers[i])):
            if j % 2:
                tg.tiers[i][j].mark = savehz_l[hz_i]
                hz_i += 1
            else:
                tg.tiers[i][j].mark = SilenceString
    elif tg.tiers[i].name == 'pinyin':
        for j in range(len(tg.tiers[i])):
            if j % 2:
                tg.tiers[i][j].mark = savepy_l[py_i]
                py_i += 1
            else:
                tg.tiers[i][j].mark = SilenceString
    elif tg.tiers[i].name == 'phone':
        for j in range(len(tg.tiers[i])):
            if tg.tiers[i][j].mark == SilenceString:
                tg.tiers[i][j].mark = SilenceString
                ll_i += 1
            else:
                tg.tiers[i][j].mark = savelast_l[ll_i]
                ll_i += 1
    else:
        print("ERROR！\n")
        break

tg.write('YourTextGrid.TextGrid')
