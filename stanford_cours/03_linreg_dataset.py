import  tensorflow as tf

import  os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = 2

import  time
import utils
import  matplotlib.pyplot as plt

DATA_FILE = 'data/birthday_life_2010.txt'

# 第一步读取数据

data, n_samples = utils.read_birth_life_data(DATA_FILE)

print(data)

print(n_samples)