# Praat批量标注TextGrid文件辅助工具

## 一般流程如下

### 将mp3等语音转化为文本

- 本人是借助[网易ASR]（ <https://jianwai.youdao.com/> ） 来实现声音转文字，将获得的文字保存在一个txt文件，获得的文件命名为YourMp3ToText.txt（要不然你需要回到代码中修改代码）。

### 逐行逐个读取YourMp3ToText.txt文本的汉字

- GetAllPinyin.py: 将读取到每个汉字借助pypinyin库函数pinyin()获得全拼+声母+韵母。

### 使用Praat画格子

- 将你要标注的MP3或wave文件在Praat中打开，并手动给需要标注的声音信号划分格子；
- 画好格子后将得到的只有格子没有文本的该文件保存到该脚本文件路径下，保存名称为YourTextGrid（不建议修改）；
- 等待InsertTextGrid.py使用来批量向其插入我们获取到的全拼+声母+韵母。

### 如何使用该脚本

 1. **ExtractAndPinyin.py:主函数，使用时只需运行该函数即可；**
 2. 【TODO】关于多音字问题，检测到声母不对应，肯定是多音字，输出时附上'*'，其他情况暂时没办法，只能手动检查...

### 注意

- 请务必在python脚本所在路径创建你的汉字文本YourMp3ToText.txt和       praat划分好的格子文件YourTextGrid.TextGrid.
- 运行ExtractAndPinyin.py成功后会生成HistoryLog.txt即为日志
- 而此时的YourTextGrid.TextGrid已插入对应的全拼+声母+韵母！
