import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

data = loadmat('ex3data1.mat')
# data format
# x = image in size 400, fold into 20x20 to get the image
# y = label

weights = loadmat('ex3weights.mat')

y = data['y']
x  = np.c_[np.ones((data['X'].shape[0], 1)), data['X']]     #add 1 to the front of each row
theta1, theta2 = weights['Theta1'], weights['Theta2']

# print('x: {} (with intercept)'.format(x.shape))
# print('y: {}'.format(y.shape))
# print('theta1: {}'.format(theta1.shape))
# print('theta2: {}'.format(theta2.shape))

# sample = np.random.choice(x.shape[0], 20)
# plt.imshow(x[sample,1:].reshape(-1,20).T)
# plt.axis('off');
# plt.show()

#the logistic function of Logistic Regression
def sigmoid(z):
    return (1 / (1 + np.exp(-z)))

# Cost function of Logistic Regression
def lr_cost(theta, reg, x, y):
    m = y.size
    h = sigmoid(x.dot(theta))

    J = (-1/m)*(np.log(h).T.dot(y) + np.log(1-h).T.dot(1-y)) + (reg/(2*m))*np.sum(np.square(theta[1:]))

    if np.isnan(J[0]): return np.inf
    else: return J[0]

# Gradient Regression
def lr_gradientReg(theta, reg, x, y):
    m = y.size
    h = sigmoid(x.dot(theta.reshape(-1, 1)))

    Gradient = (1/m)*x.T.dot(h-y) - (reg/m)*np.r_[[[0]],theta[1:].reshape(-1,1)]

    return Gradient.flatten()

from scipy.optimize import minimize
# one vs all classification
def oneVsAll(features, classes, n_labels, reg):
    initial_theta = np.zeros((features.shape[1],1))  # 401x1
    all_theta = np.zeros((n_labels, features.shape[1])) #10x401

    i = 1
    for c in np.arange(1, n_labels+1):
        print(i)
        res = minimize(lr_cost, initial_theta, args=(reg, features, (classes == c)*1), method=None,
                       jac=lr_gradientReg, options={'maxiter':50})
        all_theta[c-1] = res.x
        i+=1
    return all_theta

def predictOneVsAll(all_theta, features):
    probs = sigmoid(features.dot(all_theta.T))

    # Adding one because Python uses zero based indexing for the 10 columns (0-9),
    # while the 10 classes are numbered from 1 to 10.
    return np.argmax(probs, axis=1)+1

# one vs all
theta = oneVsAll(x, y, 10, 0.1)
pred = predictOneVsAll(theta, x)
print('Training set accuracy: {} %'.format(np.mean(pred == y.ravel())*100))

# from sklearn.linear_model import LogisticRegression
# clf = LogisticRegression(C=10, penalty='l2', solver='liblinear')
# # Scikit-learn fits intercept automatically, so we exclude first column with 'ones' from X when fitting.
# clf.fit(x[:,1:],y.ravel())
# pred2 = clf.predict(x[:,1:])
# print('Training set accuracy: {} %'.format(np.mean(pred2 == y.ravel())*100))
