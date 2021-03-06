import tensorflow as tf
import os
os.chdir('/media/vsppraneeth/01D3522569C0B1A0/WSDM')
import pandas as pd
import numpy as np
import random as rd

data = pd.read_csv('ML_Dataset.csv', index_col = 0)

from sklearn.model_selection import train_test_split
train_data, test_data = train_test_split(data, test_size = 0.2) 

del data

# Start basic Neural Network
sess = tf.InteractiveSession()


x = tf.placeholder(tf.float32,[None, 102])

W = tf.Variable(tf.zeros([102,1]))
b = tf.Variable(tf.zeros([1]))

init = tf.global_variables_initializer()
sess.run(init)

y = tf.matmul(x,W) + b

y_ = tf.placeholder(tf.float32, [None, 1])

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

train_data_churn = train_data[train_data.is_churn == 1]
train_data_normal = train_data[train_data.is_churn == 0]

for _ in range(1000):
    batch = train_data_churn.sample(500).append(train_data_normal.sample(500))
    ex = batch.drop('is_churn', axis = 1).values
    why = np.reshape(batch.is_churn.values,(-1,1))
    train_step.run(feed_dict={x: ex, y_: why})
    
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
sess.run(accuracy, feed_dict={x: test_data.drop('is_churn', axis = 1).values, y_: np.reshape(test_data.is_churn.values,(-1,1))})

prediction=tf.argmax(y,1)
check = prediction.eval(feed_dict={x: test_data.drop('is_churn', axis = 1).values})
