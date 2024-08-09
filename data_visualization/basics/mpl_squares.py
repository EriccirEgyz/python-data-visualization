import matplotlib.pyplot as plt

#print(plt.style.available)
#matplotlib提供了很多已经定义好的样式，上面的命令可以查看

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]

plt.style.use('seaborn-v0_8-notebook') #使用内置样式
fig, ax=plt.subplots()
#fig表示整张图片
#ax表示图片中的各个图表
ax.plot(input_values, squares, linewidth=3)
#这里如果不指定input_values的话，默认第一个数据点对应的x坐标是0!!!

#设置图标标题并给坐标轴加上标签
ax.set_title("square number", fontsize=24)
ax.set_xlabel("number", fontsize=14)
ax.set_ylabel("square of the number", fontsize=14)
#中文默认字体似乎不支持

#设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()