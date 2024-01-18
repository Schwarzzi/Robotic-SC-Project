import numpy as np


#Bus structure frequency mdof

A = (584 + 584*2 + 1087*2)*4/(1000**2)
E = 210*10**9
m = 3000
L = 4.45
#Imm = (75**4/12 - 71**4/12) + 584*805.4**2 + (465*2**3)/12 + 465*2*806.4**2 + (2*930**3*np.sin(60)**2)/12 + 930*2*(0.5*np.sin(60)*930)**2
Imm = (75**4/12 - 71**4/12) + 584*1087**2 + (584*2**3)/12 + 584*2*1087**2 + (2*1169**3*np.sin(60)**2)/12 + 1169*2*(0.5*np.sin(60)*1169)**2
I = 4*Imm*10**(-12)

#simple pillar approximation
f_nat_ax_b = 0.16*np.sqrt(A*E/(m*L))
f_nat_lat_b = 0.276*np.sqrt(E*I/(m*L**3))

f_nat_ax_un = 0.25*np.sqrt(A*E/(m*L))
f_nat_lat_un = 0.56*np.sqrt(E*I/(m*L**3))

f_nat_sdof = 1/(2*np.pi) * np.sqrt(3*E*I/ (m*L**3))

print(f"lateral simple = {f_nat_lat_b}")
print(f"axial simple = {f_nat_ax_b}")
print(f"lateral uniform = {f_nat_lat_un}")
print(f"axial uniform = {f_nat_ax_un}")
print(f"sdof = {f_nat_sdof}")

#rms frequencies
psd = 0.0044
damping = 0.02
sf_rms = 5

x_rms = np.sqrt(np.pi * f_nat_sdof*psd/(4*damping))

print(f"peak RMS g = {sf_rms*x_rms}")

###########
#solar array frequency

#assume CoM is at center of array
#Solar array boom made of Al 6061, 6x1 on each side
#Solar array mass gotten from midterm report gives initial sizing mass of 49kg

#Boom moment of inertia

d_o = 0.05
d_i = 0.048

I_boom = 2*np.pi * (d_o**4 - d_i**4)/64

#Solar array fundamental frequency
E = 68.2*10**9
mass_sa = 49/2 #mass of a single solar array
L = 3.5

f_n_sa = (1/(2*np.pi) ) * np.sqrt(3*E*I_boom/(mass_sa*L**3))

print(f"solar array frequency = {f_n_sa}")

#############
#robotic arm simulation

E = 70*10**9 #https://www.carpenteradditive.com/hubfs/Resources/Data%20Sheets/Scalmalloy_Datasheet.pdf
D_out = 0.13756
thickness = 0.006878
D_in = D_out-thickness
I = np.pi * (D_out**4-D_in**4) / 64
A = np.pi * (D_out**2-D_in**2) / 4
m_payload = 2500
m_arm = 20
L_arm = 1.8

f_nat_ax_arm = 0.16*np.sqrt(A*E/(m_payload*L_arm + 0.333*m_arm*L_arm))
f_nat_lat_arm = 0.276*np.sqrt(E*I/(m_payload*L_arm**3 + 0.236*m_arm*L_arm**3))

print(f"lateral robotic arm = {f_nat_lat_arm}")
print(f"axial robotic arm = {f_nat_ax_arm}")