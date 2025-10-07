"""
    ## 🧠 DeepTSE AI Model – Step-by-Step LSTM RNN Construction
    
    This notebook contains the core implementation of DeepTSE’s predictive AI model, built using a multi-layered LSTM RNN architecture.  
    It is designed to forecast short-term price movements in high-volume traded symbols on the Tehran Stock Exchange (TSE), using both technical and external variables.
    
    Key features of this notebook include:
    - TensorFlow 2.x setup with optional TPU acceleration  
    - Integration of Persian calendar and timezone for localized timestamping  
    - Data loading from preprocessed `.pkl` and `.csv` sources  
    - Feature scaling, encoding, and preparation for time-series modeling  
    - Construction of LSTM layers with Keras Sequential API  
    - Evaluation metrics including RMSE, accuracy, precision, recall, F1, ROC AUC, and confusion matrix  
    - Model checkpointing, early stopping, and learning rate scheduling  
    - Compatibility with both Theano and TensorFlow backends (legacy support)
    
    This notebook is part of the model creation pipeline, and works in tandem with simulation, threshold optimization, and deployment subsystems.
"""

#CREATE MODEL Step by Step 5 - LSTM RNN
%tensorflow_version 2.x
#!pip install tensorflow==2.4
import tensorflow as tf
print("Tensorflow version " + tf.__version__)
"""
try:!!
  tpu = tf.distribute.cluster_resolver.TPUClusterResolver()  # TPU detection
  print('Running on TPU ', tpu.cluster_spec().as_dict()['worker'])
except ValueError:
  raise BaseException('ERROR: Not connected to a TPU runtime; please see the previous cell in this notebook for instructions!')
 
tf.config.experimental_connect_to_cluster(tpu)
tf.tpu.experimental.initialize_tpu_system(tpu)
tpu_strategy = tf.distribute.experimental.TPUStrategy(tpu)
"""
!pip install persiantools
import os,time,datetime;from persiantools.jdatetime import JalaliDate;os.environ['TZ']='Asia/Tehran';time.tzset();
x=datetime.datetime.now();print(x,JalaliDate(x));

import re
import theano
import os; 
#os.environ['KERAS_BACKEND'] = 'theano'
import theano
import numpy
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import load_model
import datetime
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import sys
#print(sys.path);
import pandas
#import tk as plt
import matplotlib.pyplot as plt
import pathlib
import fnmatch
import keras.utils
import matplotlib.image as mpimg
import pdb
from sklearn.preprocessing import LabelEncoder
from dateutil.parser import parse
from numpy import concatenate
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.datasets import make_circles
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from keras.optimizers import SGD

import os.path
import pickle
base_path1='/content/drive/My Drive/';
address_external_variables_file=base_path1+"Metadata/external_variables.pkl";
if os.path.isfile(address_external_variables_file):
  with open(address_external_variables_file, 'rb') as f:
      symbol_id_table = pickle.load(f);
address_local_variables_file=base_path1+"Metadata/local_variables.pkl";
if os.path.isfile(address_local_variables_file):
  with open(address_local_variables_file, 'rb') as f:
      minute_data_array, all_dataset_size, all_train_size, all_test_size = pickle.load(f);

dataset_address='/content/drive/My Drive/Metadata/SymbolTable 5-6-2020.csv';
dataset = pandas.read_csv(dataset_address, engine='python', names=["symbol","id","title"], dtype={'symbol': str, 'id': str, 'title': str});

# 📌 The full code spans over 2,000 lines, covering architecture, training, evaluation, and integration logic.
