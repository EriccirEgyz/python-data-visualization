import json
import plotly.express as px

#探索数据的结构
filename='D:\code\python\python编程从入门到实践项目\data_visualization\earthquake_scatter\eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)

'''
readable_file='D:\code\python\python编程从入门到实践项目\data_visualization\earthquake_scatter\\readable_eq_data.json'
#这里是创建一个新的文件
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
    #将all_eq_data编码为JSON格式并写入文件
'''

all_eq_dicts=all_eq_data['features'] #先对上面可阅读的JSON数据结构进行分析，找到想要的数据在哪里

mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
'''
fig=px.scatter(
    x=lons,
    y=lats,
    labels={'x':'longtitude', 'y':'latitude'},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title="the scatter plot of the world's earthquakes",
)
'''

fig=px.scatter_geo(
    lat=lats,
    lon=lons,
    width=1600,
    height=1600,
    title="the scatter plot of the world's earthquakes",
)

fig.write_html("global_earthquakes.html")
fig.show()


