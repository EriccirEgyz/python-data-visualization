import csv
#讲个热知识，csv的全称是comma sperated values(以逗号分隔的值
from datetime import datetime

import matplotlib.pyplot as plt

filename='D:\code\python\python编程从入门到实践项目\data_visualization\data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader) #调用next()并传入阅读器对象,它将返回文件中的下一行（因此这里返回第一行
    
    '''
    for index, column_reader in enumerate(header_row):
        print(index, column_reader)
        #还记得enumerate的用法吧,对有序对象使用.可以返回索引
        #得知日期和最高温分别存储再第三列和第六列
    '''

    #从文件中获取最高温度
    dates, highs, lows=[], [], []
    for row in reader:
        current_date=datetime.strptime(row[2], '%Y-%m-%d')
        #datatime包用于将日期字符串转化成表示相应日期的对象
        #第一个参数是所需日期的字符串
        #第二个参数说明设置日期的格式 
        # %Y-让python将字符串第一个连字符前面的部分视为四位的年份，%m和%d则分别是月份和日期
        high=int(row[5])
        low=int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    #有点奇怪啊，这些操作都要再缩进情况下才能完成吗

#根据最高温度绘制图形
plt.style.use('fast')
fig, ax=plt.subplots(figsize=(15,9))
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#fill_between接受一个x值和两个y值系列，填充之间的空白
#alpha制定颜色的透明度, 0表示完全透明，1表示完全不透明

#设置图形的格式
ax.set_title('the highest and lowest temperature on every day of 2018', fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
#用来绘制倾斜的日期标签，以免彼此重叠
ax.set_ylabel('temperature(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

#设置y轴的范围
plt.ylim(20,120)

plt.savefig('stika temp.png')
