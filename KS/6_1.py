#导入库
import tensorflow as tf                                                                #【_1_】
import matplotlib.pyplot as plt
print('\n开始程序运行...\n')
 
print('正在载入和预处理数据集...\n')
#载入mnist数据集
mnist = tf.keras.datasets.mnist                                 
(X_train, y_train), (X_test, y_test) = mnist.load_data()  

#利用reshape函数转换数字图像
X_train_reshape = X_train.reshape(X_train.shape[0], 28*28) 
X_test_reshape = X_test.reshape(X_test.shape[0], 28*28)  

#归一化数字图像
X_train_norm, X_test_norm = X_train_reshape / 255.0, X_test_reshape / 255.0 
print('载入和预处理数据集结束\n')

#显示测试集第1幅图像及其内容
plt.figure() 
plt.imshow(X_test[0], cmap='gray')  
plt.show()

#构建Sequential模型
model = tf.keras.models.Sequential()                                     
model.add(tf.keras.layers.Dense(50,input_dim=28*28,activation='relu', name='Hidden1')) #【_2_】
model.add(tf.keras.layers.Dense(50, activation='relu', name='Hidden2'))
model.add(tf.keras.layers.Dense(50, activation='relu', name='Hidden3'))
model.add(tf.keras.layers.Dense(10,activation='softmax',name='Output'))  

#打印模型的概况
print(model.summary())

#模型编译
print('正在编译...\n')
model.compile(optimizer='Adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
print('编译结束\n')	

#模型训练
print('正在训练...\n')	
model.fit(X_train_norm, y_train, epochs=4,  verbose=2,  validation_split=0.3)          #【_3_】  
print('训练结束\n')

print('正在评估...\n')	
model.evaluate(X_test_norm, y_test)                                                    #【_4_】                                                                         
print('评估结束\n')	

#保存和加载训练好的模型
print("正在保存和读取训练好的模型...\n")	
model.save('model2025.h5')                                                          
model = tf.keras.models.load_model('model2025.h5')                                    #【_5_】 
print('模型保存和读取结束\n')  

print('程序运行结束。\n') 