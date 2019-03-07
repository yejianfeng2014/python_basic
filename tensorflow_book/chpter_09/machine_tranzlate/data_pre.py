import  tensorflow as tf
MAX_LEN =50 # 限定最大句子长度

SOS_ID = 1 # 目标语言中<sos> 的id

# 使用dataset api 从文件中读取一个语言的数据

# 数据格式是，每一行一句话，单词已经转化为单词编号

def MakeDataset(file_path):
    dataset = tf.data.TextLineDataset(file_path)

    # 根据空格将单词编号切分，并放入一个一维向量
    dataset = dataset.map(lambda string:tf.string_split([string]).values)

    # 将字符串形式的单词编号转为整数

    dataset = dataset.map(lambda string : tf.string_to_number(string,tf.int32))

    # 统计每一个单词的数量，并且与句子一起放入dataset 中

    dataset = dataset.map(lambda x :(x,tf.size(x)))

    return  dataset

# 从源语言和目标语言分别读取数据，并进行填充和batching操作

def MakeSrcTrgDataset(src_path,trg_path,batch_size):
    src_data = MakeDataset(src_path)

    trg_data = MakeDataset(trg_path)

    # 通过zip 操作将两个dataset 合并为一个dataset 现在每一个dataset 由以下
    # 4个张量来表示
    # ds[0][0]  是源句子
    # ds[0][1] 是源句子长度
    # ds[1][0] 是目标句子
    # ds[1][1] 是目标句子长度

    dataset = tf.data.Dataset.zip(src_data,trg_data)


    # 删除内容为空，或者长度过长的句子

    def FilterLength(src_tuple,trg_tuple):
        ((src_input,src_len),(trg_input,trg_len)) = (src_tuple,trg_tuple)

        src_len_ok = tf.logical_and (tf.greater(src_len,1),tf.less_equal(src_len,MAX_LEN))

        trg_len_ok = tf.logical_and(tf.greater(trg_len,1),tf.less_equal(trg_len,MAX_LEN))

        return  tf.logical_and (src_len_ok ,trg_len_ok)

    dataset = dataset.filter(FilterLength)
