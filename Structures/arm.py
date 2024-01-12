import numpy as np
import matplotlib.pyplot as plt

def shear_tear_out(F, A: list):
    """
    Calculates the shear tear out failure of a bolt.

    Parameters:
        F (float): The bearing load on the bolt in N.
        A (float): The shear area of the bolt in mm^2.

    Returns:
        float: The shear tear out stress in MPa.
    """
    shear_tear_out_stress = [F / A[i] for i in range(len(A))]
    return np.array(shear_tear_out_stress)

def bearing(nf, Fx, Fz, My, D, t, A: list, r: list):
    """
    Calculates the bearing failure of a bolt.

    Parameters:
        nf (float): The number of fasteners.
        Fx (float): The axial load on the bolt in N.
        Fz (float): The shear load on the bolt in N.
        My (float): The bending moment in N-mm.
        D (float): The distance between applied force and NA in mm.
        t (float): The thickness of the material in mm.
        A (list): The area of the bolt in mm^2.
        r (list): The distance of the bolt from the neutral axis in mm.
    Returns:
        np.array: The bearing stress in MPa.
    """
    return (np.array(Fx / nf) + np.array(Fz / nf) + [My * A[i] * r[i] / np.sum(np.multiply(A, np.square(r))) for i in range(nf)]) / D / t
    

def pull_through(Fy, nf, Mz, D_fo, D_fi, r: list, A: list):
    """
    Calculates the pull/push through failure of a bolt.

    Parameters:
        Fy (float): The axial load on the bolt in N.
        nf (float): The number of fasteners.
        Mz (float): The bending moment in N-mm.
        D_fo (float): The diameter of the bolt head/nut in mm.
        D_fi (float): The diameter of the bolt in mm.
        r (list): The distance of the bolt from the neutral axis in mm.
        A (list): The area of the bolt in mm^2.

    Returns:
        np.array: The pull/push through stress in MPa.
    """
    return (np.array(Fy / nf) + [Mz * A[i] * r[i] / np.sum(np.multiply(A, np.square(r))) for i in range(nf)]) / (D_fo - D_fi) * np.pi ** 2 / 4


def net_section(Fsu, w, nf, D_fi, t):
    """
    Calculates the net section stres of a bolt.

    Parameters:
        Fsu (float): The allowable ultimate tensile strength of the bolt in MPa.
        w (float): The width of the plate in mm.
        nf (float): The number of fasteners.
        df (float): The diameter of the bolt hole in mm.
        t (float): The thickness of the material in mm.

    Returns:
        float: The net section of the bolt in mm^2.
    """
    net_section_stress = [Fsu / (w - nf * D_fi) / t] * nf
    return np.array(net_section_stress)
    

def end_pad_shear(nf, Fy, D_fo, t, Fsu):
    """
    Calculates the end pad shear failure of a bolt.

    Parameters:
        Fy (float): The tensile load on the bolt in N.
        D_fo (float): The diameter of the washer in mm.
        t (float): The thickness of the end-pad in mm.
        Fsu (float): The allowable ultimate shear strength of the bolt in MPa.

    Returns:
        tuple: The end pad shear stress in MPa and the allowable bolt tension in N.
    """
    end_pad_shear_stress = [Fy / np.pi / D_fo / t] * nf
    allowable_bolt_tension = Fsu * np.pi * D_fo * t
    return np.array(end_pad_shear_stress)


def plot():
    # max_stress = mat.sigma_max

    nf = 29
    Fx = 100000 # N
    Fz = 520000 # N
    Fy = 3200000 # N
    My = 34000 # N-mm
    Mz = 28000 # N-mm
    Distance = 404.44 # mm
    radial_distances = np.array([431.45, 328.12, 357.66, 408.94, 407.71, 356.14, 330.95, 326.47, 358.27, 410.25,
                         362.63, 338.83, 427.14, 338.74, 425.07, 360.76, 401.27, 396.65, 354.46, 326.96,
                           406.09, 408.31, 322.22, 349.67, 391.25, 395.72, 353.31, 329.46, 425.70]) * np.array(0.612) # mm
    D_fi = 22 * 0.612 # mm
    D_fo = 37 * 0.612 # mm
    Areas = np.array([(22/2) ** 2 * np.pi ] * 29) * np.array(0.612) # mm
    Fsu = 500 # MPa
    w = 550 # mm

    sto_x_var = []
    sto_z_var = []
    bearing_var = []
    pt_var = []
    net_var = []
    eps_var = []
    ts = np.linspace(0.01, 3, 1000)
    for t in ts: # mm
        sto_x_var.append(shear_tear_out(Fx, Areas))
        sto_z_var.append(shear_tear_out(Fz, Areas))
        bearing_var.append(bearing(nf, Fx, Fz, My, Distance, t, Areas, radial_distances))
        pt_var.append(pull_through(Fy, nf, Mz, D_fo, D_fi, radial_distances, Areas))
        net_var.append(net_section(Fsu, w, nf, D_fi, t))
        eps_var.append(end_pad_shear(nf, Fy, D_fo, t, Fsu))
    
    i = 1
    titles = ['Shear tear out x', 'Shear tear out z', 'Bearing', 'Pull through', 'Net section', 'End pad shear']

    for var in [sto_x_var, sto_z_var, bearing_var, pt_var, net_var, eps_var]:
        var = np.array(var).T
        plt.figure(i)
        for j in var:
            plt.plot(ts, j, label=f'Fastener {i}')
            
        plt.xlabel('Thickness (mm)')
        plt.ylabel('Stress (MPa)')
        plt.legend(labels = [f'Fastener {i}' for i in range(1, 30)], ncol=3, loc='best')
        plt.axhline(Fsu, color='red', linestyle='--', label='Max Allowable Stress')
        plt.grid(True)
        plt.title(titles[i-1])
        i += 1

    plt.show()

    return np.max(np.array([sto_x_var, sto_z_var, bearing_var, pt_var, net_var, eps_var]).flatten()) # fix


    # Find intersections
    # intersections = {'Shear tear out': [], 'Bearing': [], 'Pull through': [], 'Net section': [], 'End pad shear': []}

    # # Helper function to find intersections
    # def find_intersections(stress, label):
    #     for i in range(1, len(t)):
    #         if (stress[i-1] - max_stress) * (stress[i] - max_stress) < 0:
    #             # Linear interpolation for more accurate intersection point
    #             x_intersect = t[i-1] + (t[i] - t[i-1]) * (max_stress - stress[i-1]) / (stress[i] - stress[i-1])
    #             intersections[label].append((x_intersect, max_stress))

    # # find_intersections(fl, 'Longitudinal Stress')
    # # find_intersections(fh, 'Hoop Stress')

    # # Plotting
    # plt.figure(figsize=(10, 6))
    # plt.plot(t, fl, label='Longitudinal Stress')
    # plt.plot(t, fh, label='Hoop Stress')
    # plt.axhline(max_stress, color='red', linestyle='--', label='Max Allowable Stress')
    # plt.xlabel('Thickness (mm)')
    # plt.ylabel('Stress (Pa)')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    # # Printing intersections
    # for stress_type, points in intersections.items():
    #     for point in points:
    #         print(f"Intersection at {stress_type}: Thickness = {point[0]:.2f} mm")

    # minimum_thickness = max(intersections['Longitudinal Stress'][0][0], intersections['Hoop Stress'][0][0])

    # print(f"Minimum thickness required with safety factor of 1.2: {1.2 * minimum_thickness:.2f} mm")

a = plot()
print(a)

def stress_concentration(d, w, t, F, M):
    kt_axial = 3 - 3.13 * (d / w) + 3.66 * (d / w) ** 2 - 1.53 * (d / w) ** 3
    sigma_max_axial = kt_axial * F / (w - d) / t
    kt_moment = (1.79 + 0.25 / (0.39 + d / t) + 0.81 / (1 + d ** 2 / t ** 2) - 0.26 / (1 + d ** 3 / t ** 3)) * (1 - 1.04 * d / w + 1.22 * d ** 2 / w ** 2)
    sigma_max_moment = kt_moment * 6 * M / ( w - d) / t ** 2