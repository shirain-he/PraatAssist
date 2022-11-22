这个项目的任务是用来辅助Praat进行标注
 一般流程如下：
 一、 将mp3等语音转化为文本
        有很多现成的模型，本人是借助https://jianwai.youdao.com/
        YourMp3ToText.txt：该文件用来存放你用上述方法所导出的文本。
 二、 逐行逐个读取YourMp3ToText.txt文本的汉字。
 三、 将读取到每个汉字借助pypinyin库函数pinyin()获得全拼+声母+韵母。
        GetAllPinyin.py: 获取全拼，声母，韵母等
 四、 将结果保存到GetAllYin.txt文件中，方便我们复制到Praat中画好的格子上。
        ExtractAndPinyin.py:主函数，只需运行该函数即可获得汉字对应的全拼以及全拼分解后的各部分。
 五、 区分被与常识不太相符的转写韵母。输出时附上'*'
 六、 关于多音字问题，未完待续...

 【注意】 请务必在python脚本所在的外创建你路径创建你的汉字文本