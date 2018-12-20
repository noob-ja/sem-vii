from scipy.integrate import quad

c1 = lambda x: 0.5*x - 2
c2 = lambda x: 0.33
c3 = lambda x: -0.5*x + 5
c4 = lambda x: 0.25
c5 = lambda x: -0.5*x + 6
cx = quad(c1, 4, 4.67)[0] + quad(c2, 4.67, 9.33)[0] + quad(c3, 9.33, 9.5)[0] + quad(c4, 9.5, 11.5)[0] + quad(c5, 11.5, 12)[0]

c1_x = lambda x: 0.5*x**2 - 2*x
c2_x = lambda x: 0.33*x
c3_x = lambda x: -0.5*x**2 + 5*x
c4_x = lambda x: 0.25*x
c5_x = lambda x: -0.5*x**2 + 6*x
cx_x = quad(c1_x, 4, 4.67)[0] + quad(c2_x, 4.67, 9.33)[0] + quad(c3_x, 9.33, 9.5)[0] + quad(c4_x, 9.5, 11.5)[0] + quad(c5_x, 11.5, 12)[0]

print(cx_x / cx)
print(cx)

from sympy import Symbol as symb
from sympy import integrate as intg
x = symb('x')
c1 = 0.5*x -2
c2 = 0.33
c3 = -0.5*x + 5
c4 = 0.25
c5 = -0.5*x + 6

cx_x = intg(c1*x, (x,4,4.67)) + intg(c2*x, (x,4.67,9.33)) + intg(c3*x, (x,9.33,9.5)) + intg(c4*x, (x,9.5,11.5)) + intg(c5*x, (x,11.5,12))
cx = intg(c1, (x,4,4.67)) + intg(c2, (x,4.67,9.33)) + intg(c3, (x,9.33,9.5)) + intg(c4, (x,9.5,11.5)) + intg(c5, (x,11.5,12))
print(cx_x / cx)
