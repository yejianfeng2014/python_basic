import  tensorflow as tf

import collections
import  codecs
from  operator import  itemgetter

RAW_FILE = 'path/data/ptb.train.txt'

VOCAB_OUTPUT = 'ptb.vocab' # 输出的词汇标文件

counter = collections.Counter() # 统计单词出现的频率


with codecs.open(RAW_FILE,'r',encoding='utf-8') as f:
    for line in f:
        for word in line.strip().split():
            counter[word] += 1
# 按照词频对单词进行排序

sorted_word_to_count = sorted(counter.items(),
                              key= itemgetter(1),
                              reverse= True)


sorted_words = [x[0] for x in sorted_word_to_count]

sorted_words = ["<eos>"] + sorted_words

with codecs.open(VOCAB_OUTPUT,'w','utf-8') as file_output:
    for word in sorted_words:
        file_output.write(word +"\n")






