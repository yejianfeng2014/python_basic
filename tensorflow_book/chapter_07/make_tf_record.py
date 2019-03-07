import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

import numpy as np


# 生成整数型的属性

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


mnist = input_data.read_data_sets("/path/to/minst", dtype=tf.uint8, one_hot=True)

images = mnist.train.images

labels = mnist.train.labels

# print(len(images))
# 训练数据的图像分辨率可以作为Example 中的一个属性
pixels = images.shape[1]

num_exaples = mnist.train.num_examples

# 输出record 地址

fileName = "path/to/output.tfrecords"

writer = tf.python_io.TFRecordWriter(fileName)

for index in range(num_exaples):
    # 将图像数据转为字符串

    image_raw = images[index].tostring()

    example = tf.train.Example(features=tf.train.Feature(feature={

        'pixels': _int64_feature(pixels),
        'label': _int64_feature(np.argmax(labels[index])),
        'image_raw': _bytes_feature(image_raw)
    }))

    # 将example 写入tfrecord
    writer.write(example.SerializeToString())

writer.close()

# t
