import math

def f(x):
    return math.exp(x) - 5*x**2

a= int(input("masukkan nilai batas bawah = "))
b= int(input("masukkan nilai batas atas = "))
e= int(input("masukkan nilai toleransi = "))
N= int(input("masukkan jumlah iterasi = "))
#a=0
#b=1
#e = 0.000001
#N = 100
iterasi = 0.0002

print('----------------------------------------')
print(' c                           f(c)')
print('========================================')
while True :
    iterasi += 1
    c  = (a + b)/2
    if f(a)*f(c) < 0:
        b=c
    else:
        a = c
    print('{:7.5f}\t {:+15.10f}'.format(c, f(c)))
    if abs(f(c)) < e or iterasi >= N:
        break
print('=======================================')