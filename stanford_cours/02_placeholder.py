import  os

import  tensorflow as tf

# Example 1: feed_dict with placeholder

a = tf.placeholder(dtype= tf.float32,shape=[3],name='a')

b = tf.constant([5,5,5],tf.float32,name='b')

c = a + b # short for the tf.add(a, b)

writer = tf.summary.FileWriter('graphs/placeholders',tf.get_default_graph())

with tf.Session() as sess:

    print(sess.run(c,{a:[1,2,3]}))


writer.close()



