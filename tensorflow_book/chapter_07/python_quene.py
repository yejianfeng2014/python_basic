import  tensorflow as tf
#创建一个先进先出的队列，队列中最多可以存储2个，并且指定了数据类型
q = tf.FIFOQueue(2,'int32')

 #使用 enqueue_many 来初始化队列中的元素，和变量初始化类似，
# 在队列使用前，需要明确的调用者个初始化过程
init = q.enqueue_many(([0,10],))

# 使用dequeue 函数将队列中的第一个元素出队列，这个变量将被保存在变量x 中

x = q.dequeue()

# 将得到的值加 1

y = x +1

# 将加1 后的值重新加入队列

q_inc = q.enqueue([y])

with tf.Session() as sess:
    # 初始化队列的操作

    init.run()

    for _ in range(10):

        v,_ = sess.run([x,q_inc])

        #打印出队列的元素

        print(v)