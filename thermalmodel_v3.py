"""
Thermal modelling tool for multiple nodes

https://apps.dtic.mil/sti/pdfs/AD1170386.pdf
https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Preliminary_Thermal_Analysis_of_Small_Satellites.pdf
https://core.ac.uk/download/pdf/70405505.pdf
"""


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

r_earth = 6378 # km
r_sun = 147310000 # km
h = 300 # km

A_panel = 4.657 # m^2
A_top = 2.25 # m^2
A_solar = 6 # m^2

A_contact_boom = 0.00149 # m^2 thin walled 5 cm diameter
A_contact_side = 0.025 # m^2 0.005 (t) * 5 (height)
A_contact_top = 0.0279 # m^2 0.005 (t) * 0.93 (width panel) * 6 (sides)

q_sun = 1370 # W / m^2

m_panel = 70 # kg 0.005 (t) * 0.93 (w) * 5 (h) * 2710 (rho)
m_top = 30 # kg
m_array = 60 # kg each

cp_al = 897
cp_ga = 340

# absorptance and emmitance of white paint
alpha_external = 0.3
alpha_internal = 0.4 # absorptance of inside of skin panels
alpha_solar = 0.8
epsilon = 0.9 #external skin panels
epsilon_solar = 0.8
epsilon_compartment = 0.31 # emmitance aluminium

sigma = 5.67 * 10 ** -8

T_0 = 293.15

def period():
    G = 6.674 * (10 ** -11)  # Gravitational constant in m^3 kg^-1 s^-2
    M = 5.972 * (10 ** 24)   # Mass of Earth in kg
    R = 6.371 * (10 ** 6)    # Radius of Earth in meters

    a = R + h * 1000  # Semi-major axis in meters

    T = 2 * np.pi * np.sqrt(a**3 / (G * M))
    return T  # The period is in seconds

def beta_critical():
    # angle at which eclipse will be a factor to consider
    return np.arcsin(r_earth / (r_earth + h)) # in rad

def eclipse_fraction(beta):
    if np.abs(np.deg2rad(beta)) < beta_critical():
        f_e = 1 / np.pi * np.arccos(np.sqrt((h ** 2 + 2 * r_earth * h)) / ((r_earth + h) * np.cos(np.deg2rad(beta))))
    elif np.abs(np.deg2rad(beta)) >= beta_critical():
        f_e = 0

    return f_e

def view_factor(h, gamma, r):
    # gamma = 60 deg for faces non perpendicular to earth/sun
    gamma_rad = np.deg2rad(gamma)
    r_sc = r + h
    H = r_sc / r
    phi_m = np.arcsin(1 / H)
    b = np.sqrt(H ** 2 - 1)

    if gamma_rad <= (np.pi / 2 - phi_m):
        F = np.cos(gamma_rad) / H ** 2
    
    elif gamma_rad > (np.pi / 2 -phi_m) and gamma_rad <= (np.pi / 2 + phi_m):
        t1 = 1/2 * np.arcsin(b/(H * np.sin(gamma_rad)))
        t2 = 1 / (2 * H ** 2) * (np.cos(gamma_rad) * np.arccos(-b * np.arctan(gamma_rad)) -b * np.sqrt(1 - H ** 2 * (np.cos(gamma_rad))**2))
        F = 2 / np.pi * (np.pi / 4 - t1 + t2)
    
    else:
        F = 0

    return F

def albedo(beta):
    if beta < 30:
        return 0.14
    elif beta >= 30:
        return 0.19

def earth_ir(beta):
    if beta < 30:
        return 228
    elif beta >= 30:
        return 218

def q_solar(F, A, alpha):
    return F * A * q_sun * alpha

def q_albedo(beta, A, alpha):
     return albedo(beta) * A * q_sun * alpha

def q_ir(beta, A):
    return earth_ir(beta) * A


class Nodes:

    def Q_1(beta):
        # Nadir-North
        neighbors = ['Q_2', 'Q_6', 'Q_7', 'Q_8']
        gamma = 30 # earth radiating body
        F = view_factor(h, gamma, r_earth)
        return [q_solar(F, A_panel, alpha_external), q_albedo(beta, A_panel, alpha_external), q_ir(beta, A_panel)] # conductance and emmitance missing

    def Q_2(beta):
        # Nadir-South
        neighbors = ['Q_1', 'Q_3', 'Q_7', 'Q_8']
        gamma = 30 # earth radiating body
        F = view_factor(h, gamma, r_earth)
        return [q_solar(F, A_panel, alpha_external),  q_albedo(beta, A_panel, alpha_external), q_ir(beta, A_panel)] # conductance and emmitance missing

    def Q_3(beta):
        # South
        neighbors = ['Q_2', 'Q_4', 'Q_7', 'Q_8']
        gamma = 90 # sun radiating body
        F = view_factor(h, gamma, r_sun)
        return [q_solar(F, A_panel, alpha_external), q_albedo(beta, A_panel, alpha_external), q_ir(beta, A_panel)] # conductance and emmitance missing

    def Q_4():
        # Zenith-South
        neighbors = ['Q_3', 'Q_5', 'Q_7', 'Q_8']
        gamma = 30 # sun radiating body
        F = view_factor(h, gamma, r_sun)
        return [q_solar(F, A_panel, alpha_external), 0, 0]  # conductance and emmitance missing

    def Q_5():
        # Zenith-North
        neighbors = ['Q_4', 'Q_6', 'Q_7', 'Q_8']
        gamma = 30 # sun radiating body
        F = view_factor(h, gamma, r_sun)
        return [q_solar(F, A_panel, alpha_external), 0, 0] # conductance and emmitance missing

    def Q_6(beta):
        # North
        neighbors = ['Q_5', 'Q_1', 'Q_7', 'Q_8']
        gamma = 90 # earth radiating body
        F = view_factor(h, gamma, r_earth)
        return [q_solar(F, A_panel, alpha_external), q_albedo(beta, A_panel, alpha_external), q_ir(beta, A_panel)] # conductance and emmitance missing

    def Q_7():
        # Velocity
        neighbors = ['Q_1', 'Q_2', 'Q_3', 'Q_4', 'Q_5','Q_6']
        gamma = 90 # earth (and sun?) radiating body
        F = view_factor(h, gamma, r_earth)
        return [q_solar(F, A_top, alpha_external), 0, 0] # conductance and emmitance missing

    def Q_8():
        # Negative Velocity
        neighbors = ['Q_1', 'Q_2', 'Q_3', 'Q_4', 'Q_5','Q_6']
        gamma = 90 # sun (and earth?) radiating body
        F = view_factor(h, gamma, r_sun)
        return [q_solar(F, A_top, alpha_external), 0, 0] # conductance and emmitance missing
    
    def Q_9(beta):
        # North Array
        neighbors = ['Q_6']
        gamma = 0
        F = view_factor(h, gamma, r_earth)
        return [q_solar(F, A_solar, alpha_solar), q_albedo(beta, A_solar, alpha_solar), q_ir(beta, A_solar)]

    def Q_10(beta):
        # South Array
        neighbors = ['Q_3']
        gamma = 0
        F = view_factor(h, gamma, r_earth)
        return [q_solar(F, A_solar, alpha_solar), q_albedo(beta, A_solar, alpha_solar), q_ir(beta, A_solar)]


def heat_balance(t, T, beta):
    # from literature https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Preliminary_Thermal_Analysis_of_Small_Satellites.pdf

    k = np.array([[0, 237, 0, 0, 0, 237, 237, 237, 0, 0],
                 [237, 0, 237, 0, 0, 0, 237, 237, 0, 0],
                 [0, 237, 0, 237, 0, 0, 237, 237, 0, 0],
                 [0, 0, 237, 0, 237, 0, 237, 237, 0, 237],
                 [0, 0, 0, 237, 0, 237, 237, 237, 0, 0],
                 [237, 0, 0, 0, 237, 0, 237, 237, 0, 0],
                 [237, 237, 237, 237, 237, 237, 0, 0, 237, 0],
                 [237, 237, 237, 237, 237, 237, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 237, 0, 0, 0, 0],
                 [0, 0, 237, 0, 0, 0, 0, 0, 0, 0]])

    T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9, T_10 = T

    A_contact = [A_contact_side, A_contact_side, A_contact_side, A_contact_side, A_contact_side,
                 A_contact_side, A_contact_top, A_contact_top, A_contact_boom, A_contact_boom]

    Q_cond = np.zeros_like(T)
    for i in range(len(T)):
        for j in range(len(T)):
            if i != j:
                Q_cond[i] += k[i, j] * A_contact[j] * (T[j] - T[i])

    T_component = 293.15 # Assume 20 C fixed temperature for components
    A_compartment = 2.64 # m^2 Surface area of component cylinder r = 0.3 h = 0.8

    Q_internal_radiated = np.array([sigma * epsilon_compartment * A_compartment * T_component ** 4,
                                    sigma * epsilon_compartment * A_compartment * T_component ** 4,
                                    sigma * epsilon_compartment * A_compartment * T_component ** 4,
                                    sigma * epsilon_compartment * A_compartment * T_component ** 4,
                                    sigma * epsilon_compartment * A_compartment * T_component ** 4,
                                    sigma * epsilon_compartment * A_compartment * T_component ** 4,
                                    sigma * epsilon_compartment * A_compartment * T_component ** 4,
                                    0,
                                    0,
                                    0]) # Not in contact with negative velocity panel and solar arrays

    # 6 attachment points for each side panel 
    k_comp = np.array([
                    [237, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 237, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 237, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 237, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 237, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 237, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    A_support = 0.001 # m^2 Assumed support contact area

    Q_internal_conducted = np.zeros_like(T)
    for i in range(len(T)):
        for j in range(len(T)):
            if i != j:
                Q_internal_conducted[i] += k_comp[i, j] * A_support * (T_component - T[i])

    Q_solar_flux = np.array(
                            [Nodes.Q_1(beta)[0],
                            Nodes.Q_2(beta)[0],
                            Nodes.Q_3(beta)[0],
                            Nodes.Q_4()[0],
                            Nodes.Q_5()[0],
                            Nodes.Q_6(beta)[0],
                            Nodes.Q_7()[0],
                            Nodes.Q_8()[0],
                            Nodes.Q_9(beta)[0],
                            Nodes.Q_10(beta)[0]])
    
    Q_albedo = np.array(
                        [Nodes.Q_1(beta)[1],
                        Nodes.Q_2(beta)[1],
                        Nodes.Q_3(beta)[1],
                        Nodes.Q_4()[1],
                        Nodes.Q_5()[1],
                        Nodes.Q_6(beta)[1],
                        Nodes.Q_7()[1],
                        Nodes.Q_8()[1],
                        Nodes.Q_9(beta)[1],
                        Nodes.Q_10(beta)[1],])
    
    Q_ir = np.array(
                    [Nodes.Q_1(beta)[2],
                    Nodes.Q_2(beta)[2],
                    Nodes.Q_3(beta)[2],
                    Nodes.Q_4()[2],
                    Nodes.Q_5()[2],
                    Nodes.Q_6(beta)[2],
                    Nodes.Q_7()[2],
                    Nodes.Q_8()[2],
                    Nodes.Q_9(beta)[2],
                    Nodes.Q_10(beta)[2]])
    
    Q_radiated = np.array([
                        sigma * epsilon * A_panel * T_1 ** 4,
                        sigma * epsilon * A_panel * T_2 ** 4,
                        sigma * epsilon * A_panel * T_3 ** 4,
                        sigma * epsilon * A_panel * T_4 ** 4,
                        sigma * epsilon * A_panel * T_5 ** 4,
                        sigma * epsilon * A_panel * T_6 ** 4,
                        sigma * epsilon * A_panel * T_7 ** 4,
                        sigma * epsilon * A_panel * T_8 ** 4,
                        sigma * epsilon_solar * A_solar * T_9 ** 4,  # north array
                        sigma * epsilon_solar * A_solar * T_10 ** 4]) # south array
    
    tau = period()
    f_e = eclipse_fraction(beta)

    t_eclipse = np.mod(t, tau) # restarts time from orbital period

    if (tau / 2 * (1 - f_e) < t_eclipse < tau / 2 * (1 + f_e)):
        eclipse = True
    else:
        eclipse = False

    if eclipse is True:
        Q_solar_flux = 0 * Q_solar_flux
        Q_albedo = 0.3 * Q_albedo

    thermal_mass = [m_panel * cp_al, m_panel * cp_al, m_panel * cp_al, m_panel * cp_al,
                    m_panel * cp_al, m_panel * cp_al, m_top * cp_al, m_top * cp_al,
                    m_array * cp_ga, m_array * cp_ga]

    Q_total = Q_solar_flux + Q_albedo + Q_ir + Q_cond + Q_internal_radiated + Q_internal_conducted - Q_radiated
    
    # print(f"Solar flux: {Q_solar_flux}", f"Albedo: {Q_albedo}", f"IR: {Q_ir}", f"Cond: {Q_cond}", f"Intenal rad: {Q_internal_radiated}", f"Internal cond: {Q_internal_conducted}", f"Radiated: {Q_radiated}")

    dT_dt = Q_total / thermal_mass # derivatives of temperature (fix)

    return dT_dt


def integrate_heat_balance(beta_range, time_range, initial_T):
    results = np.zeros((len(beta_range), len(time_range), len(initial_T)))
    for i, beta in enumerate(beta_range):
        print(f'{beta} Done!')
        for j, time in enumerate(time_range):
            sol = solve_ivp(heat_balance, [0, time], initial_T, args=(beta,), method='RK45')
            results[i, j, :] = sol.y[:, -1]  # Taking the last value
    return results


def plot_3d():
    # Define ranges for beta and time
    beta_range = np.linspace(0, 90, 31)  # From 0 to 90 degrees
    time_range = np.linspace(0, 60000, 500)  # Example time range
    initial_T = np.full(10, 293.15)  # Initial temperatures

    # Integrate
    temperatures = integrate_heat_balance(beta_range, time_range, initial_T)

    # 3D Plot for each panel
    fig, axs = plt.subplots(2, 5, subplot_kw={'projection': '3d'}, figsize=(20, 10))
    axs = axs.ravel()

    Node_title = ['Nadir-North', 'Nadir-South', 'South', 'Zenith-South', 'Zenith-North', 'North', 'Velocity', 'Negative Velocity', 'North Array', 'South Array']

    for i in range(10):
        X, Y = np.meshgrid(time_range, beta_range)
        Z = temperatures[:, :, i]
        surf = axs[i].plot_surface(X, Y, Z, cmap='viridis', vmin=vmin, vmax=vmax)
        axs[i].plot_surface(X, Y, Z, cmap='viridis')
        axs[i].set_title(Node_title[i])
        axs[i].set_xlabel('Time (s)')
        axs[i].set_ylabel('Beta Angle (deg)')
        axs[i].set_zlabel('Temperature (K)')
        axs[i].set_zlim(250, 450)
    

    fig.colorbar(surf, ax=axs, shrink=0.5, aspect=5)
    plt.tight_layout()
    plt.show()


plot_3d()
