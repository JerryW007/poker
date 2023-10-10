# -*- coding: utf-8 -*-

from collections import OrderedDict
from re import X
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
examDict = {
    '学习时间': [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5,3.75, 4.0, 4.25, 4.5, 4.75,5.00,5.50],
    '分数': [10, 22, 13, 43, 20, 22, 33, 50, 62, 48, 55, 75, 62, 73, 81, 76, 64, 82, 90, 93]
}

def add(a, b):
    return a+b
    
if __name__ == '__main__':
    examOrderedDict = OrderedDict(examDict)
    examDf = pd.DataFrame(examOrderedDict)
    # print(examDf.head())
    # 提取特征值features
    exam_X = examDf.loc[:,'学习时间']
    exam_Y = examDf.loc[:,'分数']
    # 作图
    plt.scatter(exam_X,exam_Y,color='r',label='exam data')
    # 添加横纵坐标标名
    plt.xlabel('leaning hours')
    plt.ylabel('score')
    # plt.show()
    
    # 建立训练集和测试集
    X_train,X_test,Y_train,Y_test = train_test_split(exam_X, exam_Y, train_size = .8)
    print('原始数据特征：',exam_X.shape,
     '训练集数据特征：',X_train.shape,
     '测试集数据特征：',X_test.shape)
    rdf = examDf.corr()
    
    X_train=X_train.reshape(-1,1)
    print(X_train)
    
