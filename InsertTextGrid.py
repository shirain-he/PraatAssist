# -*- coding:utf-8 -*-
"""
作者：shay
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
    try:
        if tg.tiers[i].name == 'word':
            if len(tg.tiers[i]) != 2*len(savehz_l) + 1:
                print('word列表所需格子%d个，textgrid文件划分格子%d个，请检查！' % ((2*len(savehz_l) + 1, len(tg.tiers[i]))))
            for j in range(len(tg.tiers[i])):
                if j % 2:
                    tg.tiers[i][j].mark = savehz_l[hz_i]
                    hz_i += 1
                else:
                    tg.tiers[i][j].mark = SilenceString
        elif tg.tiers[i].name == 'pinyin':
            if len(tg.tiers[i]) != 2*len(savepy_l) + 1:
                print('pinyin列表所需格子%d个，textgrid文件划分格子%d个，请检查！' % ((2*len(savepy_l) + 1, len(tg.tiers[i]))))
            for j in range(len(tg.tiers[i])):
                if j % 2:
                    tg.tiers[i][j].mark = savepy_l[py_i]
                    py_i += 1
                else:
                    tg.tiers[i][j].mark = SilenceString
        elif tg.tiers[i].name == 'phone':
            if len(tg.tiers[i]) != len(savelast_l):
                print('除yw与无声母拼音外，phone列表所需格子%d个，textgrid文件划分格子%d个，请注意！' % ((len(savelast_l), len(tg.tiers[i]))))
            for j in range(len(tg.tiers[i])):
                if tg.tiers[i][j].mark == SilenceString:
                    tg.tiers[i][j].mark = SilenceString
                    # print(tg.tiers[i][j].minTime)
                    # print(SilenceString)
                    # print("* ")
                    ll_i += 1
                else:
                    tg.tiers[i][j].mark = savelast_l[ll_i]
                    # print(tg.tiers[i][j].minTime)
                    # print(savelast_l[ll_i])
                    # print("* ")
                    ll_i += 1
        else:
            print("UNKNOWN ERROR！\n")
    except Exception:
        print("请根据报错信息所示列表，在已写入的textgrid中观察列表所在层-格子标注错误-的-具体位置！")
        continue

tg.write('YourTextGrid.TextGrid')
