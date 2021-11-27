# 概述 
汉语字词添加pinyin

1. 双击执行words_add_pinyin.py文件
   （注：要按照python3，及chardet模块：pip install chardet）
2. 弹出文件夹选择：选择要将中文添加pinyin的文件夹。
3. 执行结果：
如：文件夹下有：地名.txt，执行后结果如下：
    地名add_pinyin_tone.txt  //带音调
    地名add_pinyin_notone.txt  //不带音调
4. v1.0 已实现：
	指定目录下所有文件都会添加pinyin(带音调和不带音调)
	编码格式自适应
    选择的目录下文件及其子目录文件都会生成添加pinyin后的文件
5. 其他：
	目前只实现中文添加拼音，多音字取第一个音。这个也是问题，后需要完善
