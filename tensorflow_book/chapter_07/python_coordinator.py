import  tensorflow as tf

import  numpy as np

import  threading

import  time

# 在线程中运行程序，这个程序在每隔1秒判断是否需要停止打印自己的id

def Myloop(coord,worker_id):
    # 使用tf.Coordinator 类提供的工具判断当前线程是否需要停止

    while not coord.should_stop():
        if np.random.rand() < 0.1:
            # 调用request_stop 函数来停止其他线程

            coord.request_stop()
        else :
            # 打印当前线程id
            print('work on id ',worker_id)

        # 停止1 s
        time.sleep(1)


# 声明一个tr.train.Coorinator 类来协同多个线程
coord = tf.train.Coordinator()

# 声明创建5个线程

threads  = [

    threading.Thread(target= Myloop(),args=(coord,i,)) for i in range(5)
]


for t in threads:
    t.start()

# 等待所有线程退出

coord.join(threads)