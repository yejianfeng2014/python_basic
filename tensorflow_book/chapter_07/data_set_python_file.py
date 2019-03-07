import  tensorflow as tf

input_file = ['to/file/file1.txt','to/file/file2.txt']

# 每次读取一行作为一个元素
dataset = tf.data.TextLineDataset(input_file)

# 定义迭代器

iter = dataset.make_one_shot_iterator()

# get_next 返回一个字符串类型的张量，代表文件中的一行
x =iter.get_next()
with tf.Session() as sess:
    for i in range(3):
        print(sess.run(x ))
