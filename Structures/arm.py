import numpy as np

def shear_tear_out(pbr, As):
    """
    Calculates the shear tear out failure of a bolt.

    Parameters:
        pbr (float): The bearing load on the bolt in N.
        As (float): The shear area of the bolt in mm^2.

    Returns:
        float: The shear tear out stress in MPa.
    """
    shear_tear_out_stress = pbr / As
    return shear_tear_out_stress

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
        float: The bearing stress in MPa.
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
    """
    return (np.array(Fy / nf) + [Mz * A[i] * r[i] / np.sum(np.multiply(A, np.square(r))) for i in range(nf)]) / (D_fo - D_fi) * np.pi ** 2 / 4


def net_section(Fsu, w, nf, df, t):
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
    net_section_stress = Fsu / (w - nf * df) / t
    return net_section_stress
    

def end_pad_shear(pt, dw, te, Fsu):
    """
    Calculates the end pad shear failure of a bolt.

    Parameters:
        pt (float): The tensile load on the bolt in N.
        dw (float): The diameter of the washer in mm.
        te (float): The thickness of the end-pad in mm.
        Fsu (float): The allowable ultimate shear strength of the bolt in MPa.

    Returns:
        tuple: The end pad shear stress in MPa and the allowable bolt tension in N.
    """
    end_pad_shear_stress = pt / np.pi / dw / te
    allowable_bolt_tension = Fsu * np.pi * dw * te
    return end_pad_shear_stress, allowable_bolt_tension


nf = 5
Fx = 1000
Fz = 1000
Fy = 1000
My = 100
D = 50
t = 5
A = [1, 2, 1, 4, 3]
r = [2, 2, 3, 4, 5]
D_fo = 6
D_fi = 4

print(pull_through(Fy, nf, My, D_fo, D_fi, r, A))