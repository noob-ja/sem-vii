import numpy as np

def relation_prop(x_name, x):
    print(x_name)
    print(reflexivity(x))
    print(symmetry(x))
    print(transitive(x))
    print()

def max_min(name, x, *y):
    print(name)
    z = y[0]
    for i in range(1,len(y)):
        z = maxmin(z, y[i])
    print(maxmin(x, z))
    print()

def max_prod(name, x, *y):
    print(name)
    z = y[0]
    for i in range(1,len(y)):
        z = maxproduct(z, y[i])
    print(maxproduct(x, z))
    print()

def reflexivity(x):
    z = []
    for i in range(x.shape[0]):
        bool = False
        if x[i][i] == 1: bool = True
        z.append(bool)
    z = np.array(z)
    if np.all(z):   return "Reflexive"
    elif np.any(z): return "Irreflexive"
    else:           return "Antireflexive"

def symmetry(x):
    t = np.equal(x, x.T)
    if np.all(t):   return "Symmetric"
    z = np.logical_and(np.greater(x, 0), np.greater(x.T, 0))
    for i in range(t.shape[0]):
        t[i][i] = False
        z[i][i] = False
    t = np.logical_or(t, z)
    if np.any(t):   return "Asymmetric"
    else:           return "Antisymmetric"

def transitive(x):
    y = maxmin(x, x)
    t = np.greater_equal(x, y)
    if np.all(t):   return "Transitive"
    elif np.any(t): return "Nontransitive"
    else:           return "Antitransitive"

def maxmin(x, y):
    return sup_i(x, y, max, np.minimum)

def maxproduct(x, y):
    return sup_i(x, y, max, np.multiply)

def sup_i(x , y, sup, i):
    z = []
    for x_ in x:
        for y_ in y.T:
            z.append(sup(i(x_,y_)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))

# m1 = np.array([[1,0,.7],[.3,.2,0],[0,.5,1]])
# m2 = np.array([[.6,.6,0],[0,.6,.1],[0,.1,0]])
# m3 = np.array([[1,0,.7],[0,1,0],[.7,0,1]])
# m4 = np.array([[1, .2, 0, 0],[0, 0, .4, .3],[1, .2, 0, 0],[0, 0, .4, .3]])
# m5 = np.array([[.3,.6,0,1],[.7,0,1,.5],[.5,0,0,.2],[0,0,1,0]])
# m6 = np.array([[.7,.4,0,1],[.7,0,.6,.2],[.5,.2,0,.2],[0,0,.6,.3]])
# m7 = np.array([[0,.5,.5,.4],[.3,0,.8,0],[1,0,.5,0],[0,.3,0,.1]])
#
# mi = {"m4": m4,"m5": m5,"m6": m6,"m7": m7}
# mj = {"m1": m1,"m2": m2,"m3": m3}

# # Q2
# for name,m in mj.items():
#     relation_prop(name,m)
# for name,m in mi.items():
#     relation_prop(name,m)
#
# # Q3
# max_min("M1 o M2", m1,m2)
# max_min("M2 o M3",m2,m3)
# max_min("M4 o M5",m4,m5)
# max_min("M6 o M7",m6,m7)
# max_min("M1 o M2 o M3", m1,m2,m3)
#
# max_prod("M1 o M2", m1,m2)
# max_prod("M2 o M3",m2,m3)
# max_prod("M4 o M5",m4,m5)
# max_prod("M6 o M7",m6,m7)
# max_prod("M1 o M2 o M3", m1,m2,m3)
