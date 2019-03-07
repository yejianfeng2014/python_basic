# coding :utf-8

import  numpy as np

import  tensorflow as tf

TRAIN_DATA ='ptb.train' # 训练数据的路径

EVAL_DATA= 'ptb_valid' # 验证数据

TEST_DATA = 'ptb_test' # 测试集数据

HIDDEN_SIZE = 300 # 隐藏层规模

NUM_LAYERS = 2  # 深层循环网络中lstm结构的层数

VOCAB_SIZE = 10000 # 词典大小

TRAIN_BATCH_SIZE = 20 # 训练数据batch_size

TRAIN_NUM_STEP = 35 # 训练数据阶段长度



