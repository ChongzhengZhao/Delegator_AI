#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/26 15:23
#@Author: wangyuyang
#@File  : delegator.py

import pymysql
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, request, render_template
import os
import re
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
import itertools
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords,wordnet
from nltk.stem.porter import PorterStemmer
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.tree import DecisionTreeClassifier
import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score, accuracy_score
import time

def processing_file(des):
    df = pd.read_csv('all_tickets_new.csv')
    Employee_Number = {0:'Smith',1:'Jacobs',2:'David',3:'Ricky',4:'Alex',5:'Marcus',6:'Glenn',7:'Adam',8:'Josh'}
    label_encoder = preprocessing.LabelEncoder()
    df['Employee Skills']= label_encoder.fit_transform(df['Employee Skills'])
    df['Employee Workload']= label_encoder.fit_transform(df['Employee Workload'])
    df['Business Impact']= label_encoder.fit_transform(df['Business Impact'])
    df['Priority']= label_encoder.fit_transform(df['Priority'])
    df['Employee Name']= label_encoder.fit_transform(df['Employee Name'])
    df['Category']= label_encoder.fit_transform(df['Category'])
    df = df.dropna(axis=0)
    Y = pd.DataFrame(df['Employee Name'])
    X = df.drop(columns=['Subject',"Employee Name"])
    cv = CountVectorizer()
    X_train_tf = cv.fit_transform(X['Description'])
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf= tfidf_transformer.fit_transform(X_train_tf)
    mnb = MultinomialNB()
    mnb.fit(X_train_tfidf, Y)
    X_test=[des]   ##. INPUT SENTENCE HERE
    X_test_tf = cv.transform(X_test)
    X_test_tfidf = tfidf_transformer.transform(X_test_tf)
    pred = mnb.predict(X_test_tfidf)
    return Employee_Number[pred[0]]


# 建立模型
model = pickle.load(open('model.pkl', 'rb'))
# 打开数据库连接

# SQL 查询语句
query_sql = "SELECT * FROM tickets \
       WHERE assign_to_who = 'Pending'";

while(True):
    # try:
        # 执行SQL语句
    # 使用cursor()方法获取操作游标
    db = pymysql.connect(******)
    cursor = db.cursor()
    print("开始新一轮处理")
    cursor.execute(query_sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        description = row[7]
        assign_to_who = row[9]
        output = processing_file(description)
        print(output)
        try:
            cursor.execute("UPDATE tickets SET assign_to_who='%s' WHERE id ='%s' " %(output,id))
            print("更新完成")
            db.commit()
        except:
            db.rollback()
    cursor.close()
    # except:
    #     print("Error: unable to fetch data")
    db.close()
    time.sleep(10)

# 关闭数据库连接


