import  tensorflow as tf

from  __future__ import  print_function


import  argparse

from datetime import  datetime

import  json

import  os
import  time

from wavenet import WaveNetModel, AudioReader, optimizer_factory


BATCH_SIZE = 1

DATA_DIRECTION = './VCTK-Corpus'

LOG_ROOT = './logdir'

CHECKPINT_EVENT = 50



