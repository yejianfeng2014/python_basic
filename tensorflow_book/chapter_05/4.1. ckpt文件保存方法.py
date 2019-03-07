import tensorflow as tf

v1 = tf.Variable(tf.random_normal([1], stddev=1, seed=1))
v2 = tf.Variable(tf.random_normal([1], stddev=1, seed=1))

result = v1 + v2

init_op = tf.global_variables_initializer()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init_op)

    saver.save(sess, 'Saved_model/model.ckpt')


# 加载模型

with tf.Session() as sess:
    saver.restore(sess,'Saved_model/model.ckpt')
    print(sess.run(result))
    print(sess.run(v1))
    print(sess.run(v2))


    