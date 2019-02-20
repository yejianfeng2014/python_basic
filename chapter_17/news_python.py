import  requests

from operator import  itemgetter


#执行请求，并且存储

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
get = requests.get(url)

print(get.status_code)

submisions_ids = get.json()

submission_dicts = []

for submission in submisions_ids[:30]:
    #对于每一篇文章，都执行一次api调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission) + '.json')


    submisions_r = requests.get(url)
    print(submisions_r.status_code)

    response_dic = submisions_r.json()

    submission_dic ={

        'title': response_dic['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission),
        'commment':''
    }

    submission_dicts.append(submission_dic)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                              reverse=True)
    for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])


