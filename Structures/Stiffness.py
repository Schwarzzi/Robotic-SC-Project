import numpy as np

A = (584 + 465*2 + 930*2)*4/(1000**2)
E = 210*10**9
m = 3000
L = 5
Imm = (75**4/12 - 71**4/12) + 584*805.4**2 + (465*2**3)/12 + 465*2*806.4**2 + (2*930**3*np.sin(60)**2)/12 + 930*2*(0.5*np.sin(60)*930)**2
I = Imm*10**(-12)

f_nat_ax = 0.25*np.sqrt(A*E/(m*L))

f_nat_lat = 0.56*np.sqrt(E*I/(m*L**3))

print(f"lateral = {f_nat_lat}")
print(f"axial = {f_nat_ax}")