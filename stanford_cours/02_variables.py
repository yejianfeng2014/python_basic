import os
import tensorflow as tf

# create variables

s = tf.Variable(2, name='scalar')

m = tf.Variable([[1, 2], [3, 4]], name='matrix')

w = tf.Variable(tf.zeros(784, 10), name='big_matrix')
v = tf.Variable(tf.truncated_normal([784, 10]), name='normal_matrix')

s = tf.get_variable('scalar', initializer=tf.constant(2))
m = tf.get_variable('matrix', initializer=tf.constant([[0, 1], [2, 3]]))
W = tf.get_variable('big_matrix', shape=(784, 10), initializer=tf.zeros_initializer())
V = tf.get_variable('normal_matrix', shape=(784, 10), initializer=tf.truncated_normal_initializer())

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print(sess.run(V))

# 给变量赋值

m1 = tf.Variable(10, name="fuzhi")
m1.assign(100)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(m1))  # 数据结果是10

m2 = tf.Variable(11, name='fuzhi2')

ass_op = m2.assign(12)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    sess.run(ass_op)
    print(sess.run(m2))  # >>输出12

# 创建一个原始值，是2

a = tf.get_variable(name='scalar1', initializer=tf.constant(2))

a_times_two = a.assign(a * 2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print('one: ', sess.run(a_times_two))

    print('two: ', sess.run(a_times_two))
    print('three: ', sess.run(a_times_two))
    print('four: ', sess.run(a_times_two))

w = tf.Variable(20, name='w1')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print(sess.run(w.assign_add(10)))  # >> 30

    print(sess.run(w.assign_sub(2)))  # >> 28

# Example 3: Each session has its own copy of variable

W = tf.Variable(20)

sess1 = tf.Session()

sess2 = tf.Session()

sess1.run(W.initializer)

sess2.run(W.initializer)

print('1', sess1.run(W.assign_add(10)))  # 30

print('2', sess2.run(W.assign_add(20)))  # 40

sess1.close()
sess2.close()
