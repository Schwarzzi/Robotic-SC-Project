import numpy as np

d = 0.130
t = 0.001
d2 = d- 2*t

#uses the weird definition of hexagon
#https://calcdevice.com/hexagon-moment-of-inertia-id204.html
#https://www.engineersedge.com/calculators/section_square_case_15.htm

theta30 = 30*np.pi/180

A = 1.5*d**2*np.tan(theta30)

I = (A/12)*(d**2 *(1+2*np.cos(theta30)**2)) / (4*np.cos(theta30)**2)

I = I*10**12


A2 = 1.5*d2**2*np.tan(theta30)

I2 = (A2/12)*(d2**2 *(1+2*np.cos(theta30)**2)) / (4*np.cos(theta30)**2)

I2 = I2*10**12

I_final = I-I2

print(I, I2)
print(I_final)


I_req = 176966.9745

print(I_final > I_req )

