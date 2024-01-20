import numpy as np

F_ax = 9.81 * 800 * 6 * 3
F_lat = 9.81 * 800 * 2 * 3

angles = np.arange(0, 61) * np.pi / 180

R_o = 0.035
t = 0.003
R_in = R_o - t

sigma_y = 276 * 10 ** 6
tau_y = 207 * 10 ** 6

candidates = []

for theta in angles:
    T = F_ax / 2 * np.sin(theta) + F_lat / 2 * np.cos(theta)
    V = F_ax / 2 * np.cos(theta) + F_lat / 2 * np.sin(theta)

    sigma_max = T / (np.pi * R_o ** 2 - np.pi * R_in ** 2)
    tau_max = V * (R_o ** 3 * (2 / 3) - R_in ** 3 * (2 / 3)) / (
                (2 * R_o - 2 * R_in) * (R_o ** 4 * np.pi / 4 - R_in ** 4 * np.pi / 4))
    # tau_max2 = ( (4/3)*V*(R_o**3-R_in**3) ) / (np.pi*(R_o**4-R_in**4)*(R_o-R_in))
    # print(sigma_max, tau_max)

    if sigma_max < sigma_y and tau_max < tau_y:
        s_ratio = sigma_y / sigma_max
        t_ratio = tau_y / tau_max

        if s_ratio > 1 and t_ratio > 1:
            candidates.append([theta * 180 / np.pi, s_ratio, t_ratio])

print(candidates)

import numpy as np

d_o = 0.075
t = 0.003
d_in = d_o-2*t

W = 800 * 9.81 * 2 * 3

L = 0.131


E = 210*10**9
I = (np.pi/64) * (d_o**4 - d_in**4)


v = (W/4)*L**3/(3*E*I)

print(v*1000)