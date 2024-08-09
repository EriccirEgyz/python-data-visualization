import requests
from plotly.graph_objs import Bar
from plotly import offline

#执行API调用并存储响应
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")
#将API响应赋给一个变量
response_dict=r.json() #将JSON对象转变为字典?
repo_dicts=response_dict['items']
repo_links, stars, labels=[],[],[]
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    #这个是用了html标记，不太懂
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    label=f"{owner}<br />{description}"
    #回忆一下f字符串的用法，不只是在print中才可以用
    #这里的<br>跟jupyter notebook中的markdown有些像啊!都是换行？
    labels.append(label)

#可视化
data=[{
    'type':'bar',
    'x':repo_links,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5, 'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]
#marker设置影响条形设计。这里给条形制定了一种自定义的蓝色，加上了宽1.5像素的深灰色轮廓
#opacity将不透明度设置为0.6
#pyplot的一大特点可以说是hovertext,就是在网页中用户点到时显示的信息，这里也做了设置
my_layout={
    'title':'the most welcome python projects on Github',
    'titlefont':{'size':28},
    'xaxis':{'title':'repository',
             'titlefont':{'size':24},
             'tickfont':{'size':14},
             },
    'yaxis':{'title':'stars',
             'titlefont':{'size':24},
             'tickfont':{'size':14},
             },
    #这里的tickfont是刻度标签字号的设置
}
fig={'data':data, 'layout':my_layout}
offline.plot(fig,filename='python_repos.html')


