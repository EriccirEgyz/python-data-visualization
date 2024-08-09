import matplotlib.pyplot as plt

from random_walk import RandomWalk

#只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw=RandomWalk(50000)
    #到了100000就有些难看了，到500000就变得有些卡顿了
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
               cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    #突出终点和起点
    ax.scatter(0,0,c='green',edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
               edgecolors='none', s=100)
    
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #plt.show()
    plt.savefig('random_walk.png', bbox_inches='tight')

    keep_running=input("make another walk? (y/n): ")
    if keep_running == 'n': #注意这里是str
        break