import  tensorflow as tf

print(tf.__version__)

# 在上下文管理器“foo”中创建变量“v”

with tf.variable_scope("foo"):
    v = tf.get_variable("v",shape=[1],initializer=tf.constant_initializer(1.0))

with tf.variable_scope('foo',reuse=True):

    v1 = tf.get_variable('v',shape=[1])

print(v == v1)


# 嵌套上下文管理器中的reuse参数的使用


with tf.variable_scope('root'):
    print(tf.get_variable_scope().reuse)

    with tf.variable_scope('foo',reuse=True):
        print(tf.get_variable_scope().reuse)

        with tf.variable_scope('bar'):
            print(tf.get_variable_scope().reuse)
    # 内层的reuse 传递不到外层
    print(tf.get_variable_scope().reuse)


# 3. 通过variable_scope来管理变量

v1 = tf.get_variable("v", [1])
print(v1.name)


with tf.variable_scope("foo", reuse=True):
    v2 = tf.get_variable("v", [1])
print(v2.name)

with tf.variable_scope("foo"):
    with tf.variable_scope("bar"):
        v3 = tf.get_variable("v", [1])
        print(v3.name)

v4 = tf.get_variable("v1", [1])
print(v4.name)


with tf.variable_scope("",reuse=True):
    v5 = tf.get_variable("foo/bar/v", [1])
    print (v5 == v3)
    v6 = tf.get_variable("v1", [1])
    print (v6 == v4)