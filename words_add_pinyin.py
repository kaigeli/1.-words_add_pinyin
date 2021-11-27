import time
import os

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
#file_path = filedialog.askopenfilename() # open a file
target_dir = filedialog.askdirectory() #open a folder
#print(file_path)

import chardet
# 获取文件编码格式，如GB2812，UTF-8等
def get_file_encoding_format(file_name):
    # 首先二进制方式打开文件
    with open(file_name, 'rb') as frb:
        # 检测编码方式
        cur_encoding = chardet.detect(frb.read())['encoding']
        print(cur_encoding)
    return cur_encoding

#打印时间
def printTime():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
printTime()

#建立字典：dic[ord("汉")] == han4
with open("./dic/pinyin_dict_withtone.txt",'r+', encoding = 'UTF8') as fr: #打开文件pinyin_dict_withtone.txt
    dic = eval(fr.read())   #读取的文件文本并转换为字典

with open("./dic/pinyin_dict_notone.txt",'r+', encoding = 'UTF8') as fr: #打开文件pinyin_dict_notone.txt
    dic_notone = eval(fr.read())   #读取的文件文本并转换为字典

for root, dir, files in os.walk(target_dir):  #遍历目录文件
    print("root is " + root)
    for file in files:
        dir_file = os.path.join(root, file)
        #print(dir_file)
        target_encoding = get_file_encoding_format(dir_file)
        #print(target_encoding)
        # 解决bug： nicodeDecodeError: 'gb2312' codec can't decode byte 0xb3 in position 1836: illegal multibyte sequence
        if target_encoding == "GB2312":
            target_encoding = "GB18030"
        with open(dir_file, 'r+', encoding=target_encoding) as fp:  # 打开要转换的汉字文件han.txt
            # 打开转换后输出的文件out_pinyin.txt
            with open(dir_file.split(".")[0]+"add_pinyin_tone.txt", 'w', encoding=target_encoding) as fw:
                # 打开转换后输出的文件out_pinyin.txt
                with open(dir_file.split(".")[0]+"add_pinyin_notone.txt", 'w', encoding=target_encoding) as fw_no:
                    tmp = 0
                    for line in fp:
                        #以下部分决定生成文件的格式，如你好=ni2hao3
                        if tmp == 0 :
                            fw.writelines(str(line.strip('\n')) + '=')
                            fw_no.writelines(str(line.strip('\n')) + '=')
                            tmp = 1
                        else :
                            fw.writelines('\r'+str(line.strip('\n')) + '=')
                            fw_no.writelines('\r'+str(line.strip('\n')) + '=')
                        for data in line:
                            if ord(data) in dic.keys():
                                fw.writelines(str(dic[ord(data)].split(',')[0]))
                                fw_no.writelines(str(dic_notone[ord(data)].split(',')[0]))
                fw_no.close()
            fw.close()
        fp.close()
