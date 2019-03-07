'''

借助百度语音合成API
神经百度的语音合成API，编写一个简洁的代码，
实现百度API读取一本45W字的小说，以每句话作为一个训练样本。
'''


import  os
import  re
import time
from random import randint

from aip import AipSpeech


APP_ID = '114788XX'   #你自己申请的API ID
API_KEY = '2m4bO8OV8F21saqe96H8'    #你自己申请的API key
SECRET_KEY = 'IO5faSMp7tPkeIjBwClDFTj'   #你自己申请的secret key


client = AipSpeech(appId=APP_ID,apiKey=API_KEY,secretKey=SECRET_KEY)

txt_path ='xxx.txt' # 让百度训练的api 生成的文本

# with open(txt_path,'r',encoding='utf-8') as f:
#     text = f.read()
#
#     text = re.sub(r'(.{30})', lambda x: '{}\n'.format(x.group(1)), text)
#
# with open(txt_path, 'w', encoding='utf8') as f:
#     f.write(text)

with open(txt_path,'r',encoding='utf8') as f:
    for index ,line in enumerate(f):
        index = '2B%06d' % index
        # if index < 8331:
        #     continue
        line = line.strip()
        try:
            # spd
            # String
            # 语速，取值0 - 9，默认为5中语速
            res = client.synthesis(
                                    line, # 需要处理的文本，必须
                                   'zh', # 语言
                                   1,    # 用户唯一id,
                                   {
                                       'per': '4', # 发音人选择，0为女声，1为男生，3，情感合成-度逍遥 4，情感合成度yy
                                       'spd': '5', # 语速，默认5 取值0-9
                                       'vol': '7', # 音量，取值0-15 ，默认5中音量
                                        'aue': '6'
                                   })
        except Exception:
            # 报异常后暂停2 ~10 秒
            time.sleep(randint(2,10))

        if not isinstance(res,dict):
            # 写返回的音频
            with open('./wav/{}.wav'.format(index),'w') as f:
                f.write(res)
            # 写入文字
            with open('./txt/{}.txt'.format(index),'w') as f:
                f.write(line)

        else:
            print(index,'err')

        print(index)

