import numpy as np
m = 3000
a_l = 6*9.81
sf = 1.2
P_cr = m*a_l*sf/6

E = 210*10**9
l = 5
k = 1

t = 0.04

I = P_cr*l**2*k**2 / (np.pi**2 *E)

a = np.sqrt(I*3/t**3)

print(a)




