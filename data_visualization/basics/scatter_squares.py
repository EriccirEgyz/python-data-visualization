import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values=[x**2 for x in x_values] #列表推导式用上了

plt.style.use('fast')
fig, ax = plt.subplots()
#scatter散点图：要花一个点的话就分别传x和y坐标，要画一系列点就分别传x和y坐标的列表

#ax.scatter(x_values, y_values, c=(0,0.8,0) ,s=10) #参数s设置绘制图形时使用的点的尺寸
#这里的颜色表示挺有意思，不同于RGB，三个数值是红绿蓝的分量，但是范围为0到1

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#采用了颜色映射，根据每个点的y值来设置其颜色，使用cmap告诉pyplot使用了哪个颜色映射


#设置图标标题并给坐标轴加上标签
ax.set_title('square number', fontsize=24)
ax.set_xlabel("number", fontsize=14)
ax.set_ylabel("square of the number", fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
ax.axis([0,1100,0,1100000]) #设置x坐标轴的范围为0到1100，y坐标轴的取值范围为0到1100000

#plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
#保存图标，第一个参数是图片的名字，第二个参数这里指定将图标多余的空白区域裁剪掉
#这个文件保存到当前所在的目录下！！！（所以要用好终端的cd