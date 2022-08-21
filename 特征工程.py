import pandas as pd
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

dataset= r'origin.xlsx' #读取原始数据集

data=pd.DataFrame(pd.read_excel(dataset)) #

featureData=data.iloc[:,:]
        
corMat = DataFrame(featureData.corr())  #corr 求相关系数矩阵

print(corMat)

writer = pd.ExcelWriter('output0.xlsx') #写入Excel文件

corMat.to_excel(writer,'Sheet1')

writer.save()

plt.figure(figsize=(20, 30))

sns.heatmap(corMat, annot=False, vmax=1, square=True, cmap="Blues",linewidths=0) #画出热力图

plot.show()
