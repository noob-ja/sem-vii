import numpy as np
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getData():
    f = open('iris.txt','r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    data = []
    label = []
    for row in lines:
        data.append([float(d) for d in row.split(',')[:4]])
        lab = row.split(',')[-1]
        if lab == 'Iris-setosa':
            label.append(10)
        elif lab == 'Iris-versicolor':
            label.append(20)
        else:
            label.append(30)
    return np.array(data), np.array(label)

x, label = getData()
u = []
m = 2
C = 3
N = len(x)
D = len(x[0])

c = np.random.randint(12, size=(C,D))

def cost_function():
    sum = 0
    for i in range(N):
        sum_ = 0
        for j in range(C):
            u_ijm = math.pow(u[i][j],m)
            sum_ += u_ijm * norm(x[i],c[j])
        sum += sum_
    return sum

def membership_deg():
    u = np.zeros((N,C))
    for i in range(N):
        x_i = x[i]
        for j in range(C):
            c_j = c[j]
            top = norm(x_i, c_j)
            sum = 0
            for k in range(C):
                btm = norm(x_i, c[k])
                res = top/btm
                res = math.pow(res, 2/(m-1))
                sum += res
            u[i][j] = math.pow(sum, -1)
    return u

def norm(x_i, c_j):
    val = 0
    for i in range(len(x_i)):
        val += math.pow(x_i[i]-c_j[i],2)
    return math.sqrt(val)

def update_cluster():
    c = np.zeros((C,D))
    for j in range(C):
        top = 0
        btm = 0
        for i in range(N):
            top += math.pow(u[i][j],m) * x[i]
            btm += math.pow(u[i][j],m)
        c[j] = top/btm
    return c

for I in range(24):
    u = membership_deg()
    c = update_cluster()
    cost = cost_function()
    print("Iteration: ", I, ", Cost: ", cost)

print(c)

def getMax():
    label = []
    for i in range(len(u)):
        u_ = u[i]
        ind = np.unravel_index(np.argmax(u_, axis=None), u_.shape)
        if ind[0] ==  0:
            label.append(10)
        elif ind[0] == 1:
            label.append(20)
        else:
            label.append(30)
    return label

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [x_[0] for x_ in x] + [c_[0] for c_ in c]
Y = [x_[1] for x_ in x] + [c_[1] for c_ in c]
Z = [x_[2] for x_ in x] + [c_[2] for c_ in c]
S = [x_[3]*10 for x_ in x] + [c_[3]*10 for c_ in c]
# color =  [l for l in label] + [50,50,50]
color = getMax() + [50,50,50]

ax.scatter(X, Y, Z, s=S, c=color)
plt.show()
