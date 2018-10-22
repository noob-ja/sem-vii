import relation
import numpy as np

def negation(x):
    return 1 - x

def conjunction(x, y):
    return min(x, y)

def disjunction(x ,y):
    return max(x, y)

def implication(x, y, op):
    z = []
    for x_ in x:
        for y_ in y.T:
            z.append(op(x_, y_))
    return np.array(z).reshape([x.shape[0], y.shape[0]])

# Kleene-Dienes
def implication_kd(x, y):
    return np.maximum(y, 1 - x)

# Reichenbach
def implication_rbach(x ,y):
    return 1 - x + np.multiply(x,y)

# Lukasiewicz
def implication_luka(x, y):
    return np.minimum(1, 1 - x + y)

def biconditional(x, y, implication_op=implication_kd):
    x = np.array(x, ndmin=1)
    y = np.array(y, ndmin=1)
    return np.minimum(implication(x, y, implication_op), implication(y, x, implication_op))

def compositional_rule_of_inference(x, y, x_, implication_op=implication_kd):
    r = implication(np.array(x, ndmin=1), np.array(y, ndmin=1), implication_op)
    x_ = np.array(x_, ndmin=1)
    return relation.maxmin(x_.reshape(1, x_.shape[0]), r)

# X = [.5, 1, .6]
# X_ = [.6, .9, .7]
# Y = [1, .4]
# print(compositional_rule_of_inference(X, Y, X_, implication_op=implication_luka))

# Q1
# If class is early or schedule is packed and sleep is less, then sleepiness is high

# Q2
# “If either Andrew or Bob lose and the Carman wins, then David will be disqualified, and I will win"
# If either A OR B lose AND C wins, then D disqualified AND I win
# a) Truth value = min(1, 1 - min(max(A,B), C) + min(D, I))
# b)
A_ = 0.8
B = 0.6
C = 0.7
D = 0.3
Truth = 0.7
# which means that 1 - min(max(A,B),C) + min(D,I) = 0.7
print(min(max(1-A_,B),C))
# 1 - 0.6 + min(0.3,I) = 0.7
# min(0.3, I) = 0.7 - 0.4
# min(0.3, I) = 0.3
# Hence, I >= 0.3

# Q3
# a) t = min(old(x), tall(x))
# b) t = max(more_or_less_old(x), short(x))
# c) t = max(old(father(x)), 1 - min(very_young(x), tall(x)))
# d) t = max(tall(x), 1 - not_very_old(x))

# Q4
A = [.6, 1, .9]
B = [.6, 1]
A_ = [.6, .9, 1]
print(compositional_rule_of_inference(A, B, A_, implication_op=implication_kd))
print(compositional_rule_of_inference(A, B, A_, implication_op=implication_rbach))
print(compositional_rule_of_inference(A, B, A_, implication_op=implication_luka))
