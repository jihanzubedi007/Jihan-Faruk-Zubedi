import math
from numpy import sign
def ridder(f, a, b, tol=1.0e-9):
 fa = f(a)
 if fa == 0.0:
    return a
 fb = f(b)
 if fb == 0.0:
    return b
 if fa*fb > 0.0:
    error.err('Root is not bracketed')
 for i in range(30):
    c = 0.5*(a+b)
    fc = f(c)
    s = math.sqrt(fc**2 - fa*fb)
    if s == 0.0:
        return None
    dx = (c - a)*fc/s
    if (fa-fb) < 0.0:
        dx = -dx
    x = c + dx
    fx = f(x)
    if i > 0:
        if abs(x - xOld) < tol*max(abs(x), 1.0):
            return x
    xOld = x
    if fc*fx > 0.0:
        if fa*fx < 0.0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
    else:
        a = c
        b = x
        fa = fc
        fb = fx
 return None
 print('Too many iterations')
def f(x):
 a = (x - 0.3)**2 + 0.01
 b = (x - 0.8)**2 + 0.04
 return 1.0/a - 1.0/b
root = ridder(f, 0.0, 1.0)
print(root)