import tensorflow as tf

with tf.variable_scope('test1'):
    get_var1 = tf.get_variable(name='firstvar',shape=[1],dtype=tf.float32)

    with tf.variable_scope('test2',):
        get_var2 = tf.get_variable(name='firstvar',shape=[2],dtype=tf.float32)



print('get_var1:',get_var1.name)

print('get_var2: ',get_var2.name)

# 此时就不会报错，tf.AUTO_REUSE可以实现第一次调用variable_scope时，
# 传入的reuse值为False,再次调用时，传入reuse的值就会自动变为True
with tf.variable_scope('test1',reuse=tf.AUTO_REUSE):
    get_var3 = tf.get_variable(name='firstvar', shape=[2], dtype=tf.float32)
    with tf.variable_scope('test2', ):
        get_var4 = tf.get_variable(name='firstvar', shape=[2], dtype=tf.float32)

print('get_var3:',get_var3.name)
print('get_var4:',get_var4.name)