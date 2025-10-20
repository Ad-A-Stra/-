import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
feiyi = pd.read_csv('C:\\KS\\feiyi.csv',encoding='utf-8-sig')
year = feiyi.year
jilu = feiyi.jilu
while True:
    xx=input("请选择折线图线型，输入“直”是直线，输入“虚”是虚线：")
    if xx=='直':
        lstyle= '-' 
        break
    elif xx=='虚':
        _________                                                              #【1】赋值线型，对应的值为'--'
        break
    else:
        print("输入信息有误，请重新选择线型")
plt.rcParams['lines.marker'] = 'o'  
_________(year, jilu, 'b',linestyle=lstyle,label='非遗数据库数据量')              #【2】绘制折线图
plt.title('2021年至2025年我国非遗数据库数据量增长情况')                  
_________                                                                      #【3】设置图表的x坐标轴标签为'年份'
plt.ylabel('数据量（万条记录）')
plt.xticks(year)
_________                                                                      #【4】设置y坐标轴范围为(0, 400)
plt.legend(loc='upper left')
_________                                                                      #【5】显示网格
plt.show()                                                              