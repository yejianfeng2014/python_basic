from  tensorflow.python.platform import  gfile

import tensorflow as tf

with tf.Session() as sess:

    model_file = 'Saved_model/combined_model.pb'

    with gfile.FastGFile(model_file,'rb') as f:

        graph_def = tf.GraphDef()

        graph_def.ParseFromString(f.read())

    result = tf.import_graph_def(graph_def, return_elements=["add:0"])
    print(sess.run(result))