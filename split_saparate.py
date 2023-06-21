# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 21:55:28 2023

@author: a
"""

import jieba
from pandas import DataFrame
import re
import os
import numpy as np

folder_path = '2007'  # 替换为你的文件夹路径
file_list = os.listdir(folder_path)  # 获取文件夹中的所有文件名

names = ["2007/"+ x for x in file_list]
list1_summary=[]
final_count={} 

l=open("function_word_list.txt","r",encoding="utf-8")
L=l.read()
link=jieba.lcut(L,cut_all=False)
link = [word for word in link if word.isalpha()]
###构建虚词表

n=926
for i in names[n:]:
    a=open(i,"r",encoding="utf-8",errors='ignore')
    A=a.read()
###读取全部内容

    b=jieba.cut(A,cut_all=False)
    b=list(b)
    b1 = [word for word in b if word.isalpha()]
###去除标点符号

    b2 = [word for word in b1 if word not in link]
###剔除文本中虚词 

    b3 =[item for item in b2 if not re.search('[a-zA-Z]', item)]
###剔除英文

    b4 = [word for word in b3 if len(word) >= 2]       
###只报告两个汉字以上的内容


    list1_summary.append(b4)    
### 按文本列表套列表

example_dict=np.load("compare1.npy",allow_pickle=True)
example_dict = example_dict.item()
###调用对照字典

number=n
for item in list1_summary:
    number=number+1
    count=example_dict.copy()
    for x in item:
        count[x]+=1                
    df=DataFrame(count,index=[file_list[number]])
    number1=file_list[number]
    number1=number1[:-4]
    df.to_csv("tmp/"+number1+".csv")

   
    
