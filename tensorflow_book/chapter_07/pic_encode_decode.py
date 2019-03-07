import tensorflow as tf

import matplotlib.pyplot as plt

# 读取原始图像

file_path = 'to/picture/cat.jpeg'
image_raw_data = tf.gfile.FastGFile(file_path, 'rb').read()

with tf.Session() as sess:
    # 对图像进行jpeg格式的解码，从而得到图像的三维矩阵，
    # tensorflow同时提供了其他图像的解析方法

    image_data = tf.image.decode_jpeg(image_raw_data)

    print(sess.run(image_data))

    print(">>>>>>>>>>>")
    print(image_data.eval())

    # 可视化

    plt.imshow(image_data.eval())

    plt.show()

    #将三维数据按照jpeg 格式写入文件
    encode_image = tf.image.encode_jpeg(image_data)

    with tf.gfile.GFile('to/picture/output.jpeg','wb') as f:
        f.write(encode_image.eval())
