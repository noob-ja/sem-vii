import numpy as np
import random
import math
import matplotlib.pyplot as plt

x = np.array([[5,5],[6,8],[8,10],[9,12]])
u = np.array([[1,0],[1,0],[0,1],[0,1]])
m = 2
C = 2
N = len(x)
D = len(x[0])

X = [x_[0] for x_ in x]
Y = [x_[1] for x_ in x]

plt.scatter(X, Y)
plt.show()

c = np.random.randint(12, size=(C,D))
# c = [[0, 0], [0, 0]]
print(c)

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

for I in range(100):
    cost = cost_function()
    print("Iteration: ", I, ", Cost: ", cost)
    u = membership_deg()
    c = update_cluster()

print(c)

X += [c_[0] for c_ in c]
Y += [c_[1] for c_ in c]

plt.scatter(X,Y)
plt.show()
