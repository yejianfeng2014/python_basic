import  tensorflow as tf

#创建一个reader 来读取TFrecord 中的文件

reader = tf.TFRecordReader()

#创建一个队列来维护输入文件列表，

file_name = '/path/to/output.tfrecords'

filename_queue = tf.train.string_input_producer([file_name])

#从文件中读取一个样例，也可以使用read_up_to 函数一次读取多个

_,serialized_example = reader.read(filename_queue)

#解析读取的一个样例，如果是多个样例使用parse_example


features = tf.parse_single_example(
    serialized_example,
    features= {
        'image_raw':tf.FixedLenFeature([],tf.string),
        'pixels':tf.FixedLenFeature([],tf.int64),
        'label':tf.FixedLenFeature([],tf.int64)
    }
)

#使用tf.decode_raw 可以将字符串解析成图像对应的像素

image = tf.decode_raw(features['image_raw'],tf.uint8)


lable = tf.cast(features['lable'],tf.int32)

pixels = tf.cast(features['pixels'],tf.int32)

sess =tf.Session()
#启动多线程处理数据

coord = tf.train.Coordinator()

threads = tf.train.start_queue_runners(sess = sess,coord= coord)

#每次运行可以读取一个实例，当所有的样例都读取完毕

for i in range(10):
    print(sess.run(image,lable,pixels))
