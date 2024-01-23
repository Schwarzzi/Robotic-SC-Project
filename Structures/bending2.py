
L = 4.45

sf = 1.25*1.1
DL = 2*9.81*4700
DL_sf = DL*sf

w =  DL_sf / L
E = 210*10**9
#I = 0.0010930373*4
#I = 0.008678310387
I = 0.0114674596

d = w*L**4 / (8*E*I)

print(d*1000)

#thickness needed to prevent bending problems