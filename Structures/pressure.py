import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class Material:
    """
    Represents a material with its properties.
    
    Parameters:
        name (str): The name of the material.
        density (float): The density of the material.
        young (float): Young's modulus of the material.
        poisson (float): Poisson's ratio of the material.
        allowable_stress (float): The allowable stress of the material.
    Returns:
        None
    """
    def __init__(self, name, density, young, poisson, allowable_stress):
        self.name = name
        self.den = density
        self.young = young
        self.poisson = poisson
        self.sigma_max = allowable_stress

def pressure_sphere(r: float, p: float, t = np.linspace(0.5, 3, 1000)) -> tuple:
    """
    Calculates the stress due to pressure inside a cylinder.

    Parameters:
        r (float): The radius of the cylinder in mm.
        p (float): The pressure inside the cylinder in Pa.
        t (np.ndarray): The thickenss range of the simulation in mm.
    """
    f1 = np.array(p * r / 2 / t)

    return f1, f1, p, t, r
    

def pressure_cylinder(r: float, p: float, t=np.linspace(0.5, 3, 1000)) -> tuple:
    """
    Calculates the stress due to pressure inside a sphere.

    Parameters:
        r (float): The radius of the sphere in mm.
        p (float): The pressure inside the sphere in Pa.
        t (np.ndarray): The thickenss range of the simulation in mm.
    """
    fl = p * r / 2 / t
    fh = p * r / t
    return fl, fh, p, t, r


def compatibility_mat(shape='sphere', *args, **kwargs):

    if shape == 'sphere' or shape == 'cylinder':
        return 0, 0, 0, 0

    elif shape != 'sphere' or shape != 'cylinder':
        # Unpack remaining variables from args
        (M21_delta, M22_delta, MS_delta, M11_delta, MC_delta, M12_delta,
         Q21_delta, Q22_delta, QS_delta, Q11_delta, QC_delta, Q12_delta,
         delta_2t, delta_s, delta_1t, delta_c,
         beta_2t, beta_s, beta_1t, beta_c,
         M21_beta, M22_beta, MS_beta, M11_beta, MC_beta, M12_beta,
         Q21_beta, Q22_beta, QS_beta, Q11_beta, QC_beta, Q12_beta) = args
        

    mat = np.array([[M21_delta, M22_delta - MS_delta, Q21_delta, Q22_delta - QS_delta],
                    [M11_delta - MC_delta, M12_delta, Q11_delta - QC_delta, Q12_delta],
                    [M21_beta, M22_beta - MS_beta, Q21_beta, Q22_beta - QS_beta],
                    [M11_beta - MC_beta, M12_beta, Q11_beta - QC_beta, Q12_beta]])

    rem = np.array([delta_2t - delta_s, delta_1t - delta_c, beta_2t - beta_s, beta_1t - beta_c]).T

    return np.linalg.solve(mat, rem)

def plot(func, mat):
    fl, fh, p, t, r = func
    max_stress = mat.sigma_max
    plt.figure(figsize=(10, 6))
    plt.plot(t, fl, label='Longitudinal Stress')
    plt.plot(t, fh, label='Hoop Stress')
    plt.axhline(max_stress, color='red', linestyle='--', label='Max Allowable Stress')
    plt.xlabel('Thickness (mm)')
    plt.ylabel('Stress (Pa)')
    plt.legend()
    plt.grid(True)
    plt.show()
    

aluminium = Material('Aluminium', 2700, 70e9, 0.33, 100e6)
steel = Material('Steel', 7850, 210e9, 0.3, 200e6)
titanium = Material('Titanium', 4500, 110e9, 0.34, 100e6)

cylinder = pressure_cylinder(500, 200e6)
sphere = pressure_sphere(500, 200e6)

plot(cylinder, aluminium)