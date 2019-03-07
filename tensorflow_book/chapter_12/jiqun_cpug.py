#coding=utf-8
import  tensorflow as tf

cluster = tf.train.ClusterSpec({

    "worker"  : [
        "A_IP:2222",  # 格式 IP地址：端口号，第一台机器A的IP地址 ,在代码中需要用这台机器计算的时候，就要定义：/job:worker/task:0
        "B_IP:1234"  # 第二台机器的IP地址 /job:worker/task:1
        "C_IP:2222"  # 第三台机器的IP地址 /job:worker/task:2

    ],
    "ps": [
        "D_IP:2222",  # 第四台机器的IP地址 对应到代码块：/job:ps/task:0

]
})


server=tf.train.Server(cluster,job_name='worker',task_index=0)#找到‘worker’名字下的，task0，也就是机器A
