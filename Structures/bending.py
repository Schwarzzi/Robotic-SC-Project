#before coach told us this doesnt make sense , we should just use bending of the total structure

import numpy as np

a = 2*9.81
m = 4700
F_DL = m*a
sf = 1.25*1.1
F_DL = F_DL*sf
l = 4.45

E = 210*10**9 #E modulus of material of crossbeam
max_d = 2 *10**(-3) #Maximum deflection of material

P = 0*F_DL
w = F_DL/l

C1 = (1/l) * (-P/6*l**3 + w*l**4/24)

z = np.arange(0, l, 0.01)
z_max = -99
EIV_max = -99999

EIv = (P*z**3/6 - w*z**4 /24 + C1*z)

EIV_max = np.abs(max(EIv.min(), EIv.max(), key=abs))

print(EIV_max)
Ireq = EIV_max / (E*max_d)
print(f"required moment of inertia: {Ireq*10**12}")

#less than Imm of whole structure, so verified