import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from time import time

# data format
# x = image in size 400, fold into 20x20 to get the image
# y = label
data = loadmat('ex3data1.mat')

y = data['y']
#add 1 (the intercept term) to the front of each row
x  = np.c_[np.ones((data['X'].shape[0], 1)), data['X']]

# weights of the neural network
# weights = loadmat('ex3weights.mat')
# theta1, theta2 = weights['Theta1'], weights['Theta2']

# print('x: {} (with intercept)'.format(x.shape))
# print('y: {}'.format(y.shape))
# print('theta1: {}'.format(theta1.shape))
# print('theta2: {}'.format(theta2.shape))

# _, axarr = plt.subplots(10,10, figsize=(5, 5))
# for i in range(10):
#     for j in range(10):
#         sample = np.random.choice(x.shape[0], 1)
#         axarr[i,j].imshow(x[sample,1:].reshape(-1,20).T)
#         axarr[i,j].axis('off')
# plt.show()

#the logistic function of Logistic Regression
def sigmoid(z):
    return (1 / (1 + np.exp(-z)))

# Cost function of Logistic Regression
def lr_cost(theta, reg, x, y):
    m = y.size
    h = sigmoid(x.dot(theta))
    J = (-1/m)*(np.log(h).T.dot(y) + np.log(1-h).T.dot(1-y)) + (reg/(2*m))*np.sum(np.square(theta[1:]))
    return J

# Gradient Regularization
def lr_gradientReg(theta, reg, x, y):
    m = y.size
    h = sigmoid(x.dot(theta.reshape(-1, 1)))
    Gradient = (1/m)*x.T.dot(h-y) - (reg/m)*np.r_[[[0]],theta[1:].reshape(-1,1)]
    return Gradient.flatten()

from scipy.optimize import minimize
# one vs all classification
def one_vs_all(features, classes, n_labels, reg, method=None, iter=100):
    initial_theta = np.zeros((features.shape[1],1))  # 401x1
    all_theta = np.zeros((n_labels, features.shape[1])) #10x401
    for c in np.arange(1, n_labels+1):
        res = minimize(lr_cost, initial_theta, args=(reg, features, (classes == c)*1), method=method,
                       jac=lr_gradientReg, options={'maxiter':iter})
        all_theta[c-1] = res.x
    return all_theta

def predict(all_theta, features):
    probs = sigmoid(features.dot(all_theta.T))
    return np.argmax(probs, axis=1)+1

def pred(x, y, classes, lmbda, method=None, iter=100):
    s = time()
    theta = one_vs_all(x, y, classes, lmbda, method, iter=iter)     #trained model
    pred = predict(theta, x)
    t = time()
    print('Training set accuracy: {} %'.format(np.mean(pred == y.ravel())*100))
    print('Time taken: {}'.format(t-s))

# one vs all
classes = 10
lambda_ = 0.1
iter = 100
solver = 'newton-cg'

print("Coded: ")
pred(x, y, classes, lambda_, solver, iter)
print()

from sklearn.linear_model import LogisticRegression
s = time()
clf = LogisticRegression(multi_class='auto', solver=solver, max_iter=iter)
# Scikit-learn fits intercept automatically, so we exclude first column with 'ones' from X when fitting.
clf.fit(x[:,1:],y.ravel())
pred2 = clf.predict(x[:,1:])
t = time()
print('Using external lib: ')
print('Training set accuracy: {} %'.format(np.mean(pred2 == y.ravel())*100))
print('Time taken: {}'.format(t-s))
