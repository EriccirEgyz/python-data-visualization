import requests

#执行API调用并存储响应
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")
#将API响应赋给一个变量
response_dict=r.json() #将JSON对象转变为字典?
#print(response_dict.keys())
print(f"Total repositories:{response_dict['total_count']}")

#探索有关仓库的信息
repo_dicts=response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")

'''
#研究第一个仓库
repo_dict=repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
'''

print('\nSelected information about each repository:')

