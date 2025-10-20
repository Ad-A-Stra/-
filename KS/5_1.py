# 导入库
from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

wine = load_wine()                                     
data = wine.data
target = wine.target

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(______________)  #【1】划分数据集，测试集占比25%，随机数种子为12

# 标准化数据
standerd_scaler = StandardScaler()
X_train = ______________                                            #【2】对训练集进行标准化拟合和转换
X_test = standerd_scaler.transform(X_test)          

# 基于KNN算法进行分类
knc = KNeighborsClassifier()
______________                                                     #【3】利用训练集的特征数据和标签数据进行模型拟合
 #对测试集的特征数据进行类别预测
y_predict = knc.predict(X_test)                      

score = ______________                                             #【4】使用模型自带的评估函数进行准确性测评                    
print('The accuracy of K-Nearest Neighbor Classifier is %.2f' % score)
# 显示主要分类指标的文本报告
report = ______________                                            #【5】显示主要分类指标的文本报告
print(report)


'''以下为选项
standerd_scaler.fit_transform(X_train)
data, target, test_size=0.25, random_state=12
knc.fit(X_train, y_train)
standerd_scaler.transform(X_train)
classification_report(y_test, y_predict)
knc.fit(X_test)
X, y, test_size=0.25, random_state=12
knc.score(X_train)
classification_report(x_test, y_test)
knc.score(X_test, y_test)
'''