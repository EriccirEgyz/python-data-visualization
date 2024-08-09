#练习用
import matplotlib.pyplot as plt

x_values=range(1,5001)
y_values=[x**3 for x in x_values]

plt.style.use('fast')

fig,ax=plt.subplots()
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.magma, s=2)

#设置图标标题并给坐标轴加上标签
ax.set_title('cube number', fontsize=24)
ax.set_xlabel("number", fontsize=14)
ax.set_ylabel("cube of the number", fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
ax.axis([0,5500,0,550000000000]) #设置x坐标轴的范围为0到1100，y坐标轴的取值范围为0到1100000

plt.savefig('cubes_plot.png')