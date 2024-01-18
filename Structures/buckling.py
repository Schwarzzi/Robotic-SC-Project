import numpy as np
m = 3000
a_l = 6*9.81
sf = 1.2*1.15
P_cr = m*a_l*sf/6

E = 210*10**9
l = 4.45
k = 1

I = P_cr*l**2*k**2 / (np.pi**2 *E)
print(I*10**12)

a = 75
t = 2

I_outer = a**4/12
I_inner = (a-2*t)**4/12
print(I_outer-I_inner)


#75x75 with a thickness of 2mm suffices 5.19079 x10^5 mm^4



