#!/usr/bin/python
#----------------------------------
#---Arithmetic Serie---------------
h=lambda n : -31-7*(n-1)
def h_r(n):
    if n==1:
        return -31
    else:
        return h_r(n-1)-7
#---------------------------------
g=lambda n : 9.6-0.1*(n-1)
def g_r(n):
    if n==1:
        return 9.6
    else:
        return g(n-1)-0.1
#---------------------------------
#---Geometric series--------------
x=lambda n :  168.0*((1.0/2.0)**(n-1))
def x_r(n):
    if n==1:
        return 168.0
    else:
        return (1.0/2.0)*x(n-1)
#---------------------------------
w=lambda n : 9*(8**(n-1))
def w_r(n):
    if n==1:
        return 9
    else:
        return 8*w_r(n-1)
for i in range(1,10):
    print("{},{}".format(w(i),w_r(i)))
