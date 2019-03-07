import  tensorflow as tf

input_data = [1,2,3,5,8]

dataset = tf.data.Dataset.from_tensor_slices(input_data)


#定义一个迭代器来遍历数据集，因为上面的数据集没有用到placeholder

interator = dataset.make_one_shot_iterator()
# get_next() 代表返回数据的一个张量

x = interator.get_next()

y = x *x

with tf.Session() as sess:
    for i in range(len(input_data)):
        print(sess.run(y))

