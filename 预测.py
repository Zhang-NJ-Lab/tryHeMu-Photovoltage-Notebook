from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from pandas import DataFrame
from sklearn import preprocessing
import numpy as np

dataset= r'train.xlsx' #训练集
dataset1= r'prediction.xlsx' #预测集

data=pd.DataFrame(pd.read_excel(dataset))
data1=pd.DataFrame(pd.read_excel(dataset1))

X=data.values[:,:-1]  #训练集
predX=data1.values[:,:]  #预测集
#输入数据归一化
for i in range(X.shape[1]):
    X[:,[i]] = preprocessing.MinMaxScaler().fit_transform(X[:,[i]])
y=data.values[:,-1]

for i in range(predX.shape[1]):
    predX[:,[i]] = preprocessing.MinMaxScaler().fit_transform(predX[:,[i]])

lrTool=RandomForestRegressor(random_state=i,n_estimators=j,criterion='squared_error')

lrTool.fit(X,y) #模型训练

predy=lrTool.predict(predX) #预测

print(predy) #输出
