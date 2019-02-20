import  requests


# 执行api 并且响应

url ='https://api.github.com/search/repositories?q=language:python&sort=stars'\

r = requests.get(url)

print(r.status_code)

response_dic = r.json()

#处理


print(response_dic.keys())


#演技第一个仓库

repo_items = response_dic['items']

print("repo size :",len(repo_items))

#研究第一个库的信息
repo_dict_first = repo_items[0]

print('key',repo_dict_first)

for key in repo_dict_first.keys():
    print(key)


for repo_dict_first in repo_items:
    print(">>>>>>>>>>>>>>>>>>>>>>>")
    print('name',repo_dict_first['name'])
    print('ower',repo_dict_first['owner']['login'])
    print('stars',repo_dict_first['stargazers_count'])
    print('Repository:', repo_dict_first['html_url'])


# 搜索api 的速率限制
url = 'https://api.github.com/rate_limit'

get_response = requests.get(url)

json = get_response.json()

print(json)
#
# "search": {
#  "limit": 10, 每分钟10个请求
#  "remaining": 8,当前分钟内还可以执行8个请求
#  "reset": 1426078803




