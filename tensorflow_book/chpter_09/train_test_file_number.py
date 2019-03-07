
# 按照字典表把训练集合测试集里面的单词全部转成数字

import  codecs

import  sys

RAW_DATA = "path/data/ptb.train.txt" # 原始训练数据

VOCAB = 'ptb.vocab' # 上面的生成的单词序号

OUTPUT_DATA = 'ptb.train' # 将单词替换为单词编号后的输出文件

#建立词汇标，并把词汇单词编号映射

with codecs.open(VOCAB,'r','utf-8') as f_vocab:
    vocab = [w.strip() for w in f_vocab.readline()]

word_to_id = {k:v for (k,v) in zip(vocab,range(len(vocab)))}


# 如果出现低频词汇，替换为"<unk>"

def get_id(word):
    return  word_to_id[word] if word in word_to_id else word_to_id['<unk>']


fin = codecs.open(RAW_DATA,'r','utf-8')
fout = codecs.open(OUTPUT_DATA,'w','utf-8')

for line in fin:
    words = line.strip().split() +["<eos>"]

    # 读取单词并添加<eos> 结束符

    # 将每一个单词替换为词汇表中的编号

    out_line = ' '.join([str(get_id(w)) for w in words]) +'\n'
    fout.write(out_line)


fin.close()
fout.close()


