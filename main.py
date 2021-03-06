import tensorflow as tf
import numpy as np
import pandas as pd
#加一层神经元
def add_layer(inputs,in_size,out_size,activation_function=None):
    #该层神经元的权值  tf.random_normal(shape,mean=0.0,stddev=1.0,dtype=tf.float32,seed=None,name=None)正太分布随机数，均值mean,标准差stddev
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    #偏置
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)
    wx_plus_b=tf.matmul(inputs,Weights)+biases
    #激活函数
    if activation_function is None:
        outputs=wx_plus_b
    else:
        outputs=activation_function(wx_plus_b)
    return outputs

#随机梯度下降时每一次处理多少数据
batch_size=10
#批量
# 梯度下降时存储的数据
xs=tf.placeholder(tf.float32)
ys=tf.placeholder(tf.float32)

#第一层神经元，100代表权值的数量，10为输出的数量，激活函数是relu函数
l1=add_layer(xs,100,10,activation_function=tf.nn.relu)
#输出层，10为上一层的输入个数，1个输出，没有激活函数
prediction=add_layer(l1,10,1,activation_function=None)
#损失函数为最小二乘   tf.square(ys-prediction先平方    tf.reduce_sum(tf.square(ys-prediction)对数据的loss求和,   tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction)对loss的和进行平均
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
#最小化loss，用的方法是梯度下降
train_step=tf.train.GradientDescentOptimizer(0.0001).minimize(loss)

init=tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)

#读取数据


train_x=pd.read_csv("5000_100_X.csv",header=None,dtype=np.float32,delim_whitespace=True).values
train_y=np.mat(pd.read_csv("AT_120_Y.csv",header=None,nrows=5000,dtype=np.float32,delim_whitespace=True).values)
'''
lists = [[] for i in range(5000)]
for m in range(5000):
    for n in range(100):
        lists[m].append(train_x[m][n])
        if n==99:
            lists[m].append(m%5)
train_x=np.mat(lists)
'''

"""

#随机生成数据，数据形状为5000*100
train_x=np.random.random(size=(5000,100))
true_w=np.mat(np.linspace(-1,1,100)).transpose()
train_y=train_x*true_w+0.3
"""

#迭代10000次
for i in range(30000):
    #offset为随机梯度下降每次迭代train_x开始的下标
    offset=(i*batch_size)%(train_x.shape[0]-batch_size)
    #随机梯度下降每一次迭代所需要的数据
    batch_data=train_x[offset:offset+batch_size,:]
    batch_labels=train_y[offset:offset+batch_size,:]
    #更新参数以及计算loss
    step_length,accuracy=sess.run([train_step,loss],feed_dict={xs:batch_data,ys:batch_labels})
    if i%100==0:
        print(accuracy)
sess.close()



