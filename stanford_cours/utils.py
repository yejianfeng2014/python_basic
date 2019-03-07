import  tensorflow as tf

import  os
import  gzip

import  urllib

import  numpy as np

def huber_loss (labels,predictions,delata = 14.0):
    residual = tf.abs(labels - predictions)
    def f1 ():
        return  0.5 * tf.square(residual)

    def f2():
        return  delata * residual -0.5 *tf.square(delata)

    return  tf.cond(residual < delata,f1,f2)

def save_mkdir(path):
    '''create a dirctory if there is not one already '''
    try:
        os.mkdir(path)

    except:
        pass

def read_birth_life_data(file_name):
    '''Read in birth_life_2010.txt and return:
    data in the form of NumPy array
    n_samples: number of samples'''

    text = open(file_name,'r').readlines()[1:]
    data = [line[:-1].split('\t') for line in text]

    births = [float(line[1]) for line in data]
    lifes = [float(line[2]) for line in data]

    data_zip = list(zip(births,lifes))
    n_sample = len(data_zip)

    data_array = np.asarray(data_zip,dtype= np.float32)

    return  data_array,n_sample




    data = text
