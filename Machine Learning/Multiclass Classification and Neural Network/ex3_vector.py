import numpy as np
from time import time
a = np.random.rand(1000000)
b = np.random.rand(1000000)
c = 0

s = time()
for i in range(a.size):
  c += a[i] * b[i]
t = time()
print("value of c {0:.5f}".format(c))
print("time taken using for-loop " + str(1000*(t-s)) + " ms")

c = 0

s = time()
c = np.dot(a,b) # no for-loops in vectorized version
t = time()
print("value of c {0:.5f}".format(c))
print("time taken using vectorized operation " + str(1000*(t-s)) + " ms")
