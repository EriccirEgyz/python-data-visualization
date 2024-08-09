from plotly.graph_objs import Bar, Layout
from plotly import offline

#看来一般是先导入下载的包，再导入其它py文件中的类
from die import Die

die=Die()

#掷几次骰子并将结果存储在一个列表里
results=[]
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies=[] #这里我的第一直觉是用字典，但种类有序且比较少？就不需要了
for value in range(1, die.num_sides+1):
    frequency = results.count(value) #列表还有计数的功能呀，都忘记了
    frequencies.append(frequency)

#对结果进行可视化
x_values=list(range(1,die.num_sides+1))
#我注意到区别了，不同于matplotlib, plotly不能直接接受range生成的结果（迭代器？）
data=[Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'outcome'}
y_axis_config = {'title': 'frequency of the outcome'}
my_layout=Layout(title='the outcome of rolling the dice for a thousand times',
                 xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')