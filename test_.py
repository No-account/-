"""
import numpy as np
#b[np.newaxis]可以让b多一个维度
x_data = np.linspace(-1,1,300)[:, np.newaxis]
print(x_data)
"""
import pandas as pd
import numpy as np
'''
train_x=pd.read_csv("5000_100_X.csv",header=None,dtype=np.float32,delim_whitespace=True).values
'''
"""
train_x_temp=[]
print(train_x)
for i in range(5000):
    for j in range(100):
        train_x_temp.append(train_x[i][j])

        if j==99:
            train_x_temp.append(i%2)
train_x_temp=train_x_temp.
"""
"""
mylist=[[None for j in range(101)]for i in range(5000)]

for m in range(5000):
    for n in range(100):
        mylist[m].append(train_x[m][n])
        if n==99:
            mylist.append(m%5)
print(mylist)
"""
'''
lists = [[] for i in range(5000)]
for m in range(5000):
    for n in range(100):
        lists[m].append(train_x[m][n])
        if n==99:
            lists[m].append(m%5)
print(np.mat(lists))
'''
train_x=[[]for m in range(5000)]
train_y=[[]for n in range(5000)]
for i in range(5000):
    for j in range(100):
        train_x[i].append(np.random.random())
        if j==0:
            train_y[i].append(train_x[i][0])
        else:
            train_y[i][0]+=train_x[i][j]
        if j==99:
            train_x[i].append(i%5)
            train_y[i].append(i%5)
print(np.mat(train_x))
print(np.mat(train_y))