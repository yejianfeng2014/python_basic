import tensorflow as tf
var1 = tf.Variable(1.0,name='firstvar')
print('var1:',var1.name)
var1 = tf.Variable(2.0,name='firstvar')
print('var1:',var1.name)
var2 = tf.Variable(3.0)
print('var2:',var2.name)
var2 = tf.Variable(4.0)
print('var2:',var2.name)
get_var1 = tf.get_variable(name='firstvar',shape=[1],dtype=tf.float32,initializer=tf.constant_initializer(0.3))
print('get_var1:',get_var1.name)
get_var1 = tf.get_variable(name='firstvar1',shape=[1],dtype=tf.float32,initializer=tf.constant_initializer(0.4))
print('get_var1:',get_var1.name)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print('var1=',var1.eval())
    print('var2=',var2.eval())
    print('get_var1=',get_var1.eval())



# 这个方式给名称赋值同样的名称会报错的
# get_var1 = tf.get_variable(name='a',shape=[1],dtype=tf.float32,initializer=tf.constant_initializer(0.3))
# print('get_var1:',get_var1.name)
# get_var2 = tf.get_variable(name='a',shape=[1],dtype=tf.float32,initializer=tf.constant_initializer(0.4))
# print('get_var1:',get_var1.name)

# 使用variabel_scope 可以把变量分开
import tensorflow as tf
with tf.variable_scope('test1'):
    get_var1 = tf.get_variable(name='firstvar',shape=[2],dtype=tf.float32)
with tf.variable_scope('test2'):
    get_var2 = tf.get_variable(name='firstvar',shape=[2],dtype=tf.float32)
print('get_var1:',get_var1.name)
print('get_var2:',get_var2.name)