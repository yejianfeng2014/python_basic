import requests

import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def create_faverate_top(url, language):
    # 执行API调用并存储响应
    # URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
    URL = url

    r = requests.get(URL)
    print("Status code:", r.status_code)
    response_dict = r.json()
    print('total repos :', response_dict['total_count'])
    # 研究有关仓库的信息
    repo_dicts = response_dict['items']
    names, stars = [], []
    for repo in repo_dicts:
        names.append(repo['name'])
        stars.append(repo['stargazers_count'])
    print(len(names))
    # 可视化
    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart.title = 'Most-Starred '+  lanuage +' Projects on GitHub'
    chart.x_labels = names
    chart.add('', stars)
    save_name = language + '_repos.svg'
    chart.render_to_file(save_name)


# python language

url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
lanuage = 'python'
create_faverate_top(url, lanuage)
# chart.render_to_file('python_repos.svg')

url = 'https://api.github.com/search/repositories?q=language:java&sort=star'
lanuage = 'java'

create_faverate_top(url,lanuage)

url = 'https://api.github.com/search/repositories?q=language:scala&sort=star'
lanuage = 'scala'
create_faverate_top(url,lanuage)


url = 'https://api.github.com/search/repositories?q=language:javascript&sort=star'
lanuage = 'javascript'
create_faverate_top(url,lanuage)


# scala 的项目
