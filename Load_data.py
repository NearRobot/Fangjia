# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 22:28
# @Author  : Nghoman
# @Software: PyCharm Community Edition

'''
fangjia   加载并处理数据
'''
import pandas as pd
import numpy as np
import re

column_name = ['Survived','Pclass', 'Age', 'SibSp', 'Parch', 'Sex','Fare', 'Embarked']


def getRequire_data(data):
    '根据取出对应数据'
    Y = data.iloc[:,0]
    data = data.drop(['Survived'], axis=1)
    return data, Y



##1、加载训练数据
filename = 'boston_corrected.txt'

#Data = pd.read_csv(filename);
#Data = Data.drop(['OBS.'], axis=1)
#print Data

#Data = open(filename, "r")
#lines = Data.readlines()
#print lines

Data = open(filename, "r")
odom = 0
for line in Data:
    odom  = line.split()
    print odom
    