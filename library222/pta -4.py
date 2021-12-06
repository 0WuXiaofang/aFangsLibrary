# import jieba
# import wordcloud
# import imageio
#
# import os
#
# mask=imageio.imread("guanyu.jpg")#读入图片
# #中文必须定义，否则会乱码，字体模板定义为微软雅黑
# #mask是词云形状模板
# #scale这个是文字显示的清晰度
# wc=wordcloud.WordCloud(width=1000,
#                        height=700,
#                        background_color='white',
#                        font_path='msyh.ttc',
#                        mask=mask,
#                        scale=15)#设定相关的词云参数
#
# text=open("三国演义.txt",encoding='utf_8')#打开文件方便下面的读入文件
# txt=text.read()
# txtlist=jieba.lcut(txt)#将文本字符串格式切割为一个个的词语储存在列表里面
# string=" ".join(txtlist)#将列表转为一个个的词语分隔开的字符串
# wc.generate(string)#传入词云需要用到的字符串
# wc.to_file("三国演义.jpg")

import jieba

import wordcloud

import imageio

import os

# 读取txt文件，获取需要统计词汇的文本

f = open("./ThreeKingdoms.txt", "r", encoding="utf-8")

t = f.read()

f.close()

# 设置图像遮罩

mask = imageio.imread("./guanyu.jpg")

# 请在下列exludes集合中，自行补充其他需要排除的词汇

excludes = {"将军", "却说", "二人", "不可", "荆州", "不能", "如此"

            }

words = jieba.lcut(t)

counts = {}

# 请扩展系列分支结构，转换更多替代词

for word in words:

    if len(word) == 1:

        continue

    elif word == "玄德" or word == "玄德曰":

        rword = "刘备"




    else:

        rword = word

    counts[rword] = counts.get(rword, 0) + 1

# 实现删除干扰词汇功能（此处约2行代码）

# 使用列表和lambda功能实现 词汇的排序 （此处约2行代码）


# 将替代名词转换为正式姓名

items[items.index(("孔明", 1383))] = ("诸葛亮", 1383)

items[items.index(("后主", 217))] = ("刘禅", 217)

# 生成词云函数所需要的文本段（此处约1行代码）
text=open("三国演义.txt",encoding='utf_8')#打开文件方便下面的读入文件
txt=text.read()
txtlist=jieba.lcut(txt)#将文本字符串格式切割为一个个的词语储存在列表里面
string=" ".join(txtlist)#将列表转为一个个的词语分隔开的字符串


# 调用WordCloud函数生成词云（此处约2行代码）
wc=wordcloud.WordCloud(width=1000,
#                        height=700,
#                        background_color='white',
#                        font_path='msyh.ttc',
#                        mask=mask,
#                        scale=15)#设定相关的词云参数
#
wc.generate(string)#传入词云需要用到的字符串
# 判断输出文件夹是否存在，如果不存在则创建

outputFileFolder = "output"

if os.path.exists(outputFileFolder) == False:
    os.mkdir(outputFileFolder)

# 输出打印生成的图片到指定文件夹

w.to_file(outputFileFolder + "/SanGuoWordCloudV1.png")