import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

INTPU_NODE = 784

OUTPUT_NODE = 10

LAYER1_NODE = 500

BATCH_SIZE = 100

# 模型相关参数

LEARNING_RATE_BASE = 0.8

LEARNING_RATE_DECAY = 0.99

REGULARAZTION_RATE = 0.0001

TRAINING_STEPS = 5000

MOVING_AVERAGE_DECAY = 0.99


# 定义辅助函数来计算前向传播结果，使用ReLU做为激活函数

def inference(input_tensor, avg_class, weights1, bia1, weights2, bia2):
    # 不使用平均类
    if avg_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + bia1)

        return tf.matmul(layer1, weights2) + bia2

    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) + avg_class.average(bia1))

        return tf.nn.relu(tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(bia2))


# 定义训练过程

def train(mnist):
    x = tf.placeholder(dtype=tf.float32, shape=[None, INTPU_NODE], name='x-input')
    y_ = tf.placeholder(dtype=tf.float32, shape=[None, OUTPUT_NODE], name='y-input')

    # 生成隐藏层的参数

    weights1 = tf.Variable(tf.truncated_normal([INTPU_NODE, LAYER1_NODE], stddev=0.1))

    bia1 = tf.Variable(tf.truncated_normal(shape=[LAYER1_NODE], stddev=0.1))

    # 第二层

    weights2 = tf.Variable(tf.truncated_normal(shape=[LAYER1_NODE, OUTPUT_NODE], stddev=0.1), name='weights_2')

    bia2 = tf.Variable(tf.truncated_normal(shape=[OUTPUT_NODE], stddev=0.1), name='bia_2')

    # 计算不含滑动平均类的前向传播结果
    y = inference(x, None, weights1, bia1, weights2, bia2)

    # 定义训练轮数及相关的滑动平均类

    global_step = tf.Variable(0, trainable=False)

    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)

    variables_averages_op = variable_averages.apply(tf.trainable_variables())

    average_y = inference(x, variable_averages, weights1, bia1, weights2, bia2)

    # 计算交叉熵以及均值

    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))

    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    # 损失函数的计算

    regularizer = tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)

    regularaztion = regularizer(weights1) + regularizer(weights2)

    loss = cross_entropy_mean + regularaztion

    # 设置指数衰减的学习率

    # 设置指数衰减的学习率。
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        mnist.train.num_examples / BATCH_SIZE,
        LEARNING_RATE_DECAY,
        staircase=True)

    # 优化损失函数

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    # 反向传播更新参数和更新每一个参数的滑动平均值
    with tf.control_dependencies([train_step, variables_averages_op]):

        train_op = tf.no_op(name='train')

    # 计算正确率

    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))

    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 初始化会话，并开始训练

    with tf.Session() as sess:

        initializer = tf.global_variables_initializer()

        sess.run(initializer)

        validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}
        test_feed = {x: mnist.test.images, y_: mnist.test.labels}

        # 循环的训练神经网络。

        for i in range(TRAINING_STEPS):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)

                print("After %d training step(s), validation accuracy using average model is %g " % (i, validate_acc))

            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x: xs, y_: ys})

        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print(("After %d training step(s), test accuracy using average model is %g" % (TRAINING_STEPS, test_acc)))


# 程序入口

def main(argv=None):
    mnist = input_data.read_data_sets("../../../datasets/MNIST_data", one_hot=True)

    print( mnist.train.num_examples)

    train(mnist)


if __name__ == '__main__':
    main()
