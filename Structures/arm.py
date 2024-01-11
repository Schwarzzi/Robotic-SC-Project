import numpy as np

def shear_tear_out_failure(pbr, As):
    """
    Calculates the shear tear out failure of a bolt.

    Parameters:
        pbr (float): The bearing load on the bolt in N.
        As (float): The shear area of the bolt in mm^2.

    Returns:
        float: The shear tear out stress in MPa.
    """
    shear_tear_out_stress = pbr / As

def bearing_faliure(pbr, D, t):
    """
    Calculates the bearing failure of a bolt.

    Parameters:
        pbr (float): The bearing load on the bolt in N.
        D (float): The diameter of the bolt in mm.
        t (float): The thickness of the material in mm.

    Returns:
        float: The bearing stress in MPa.
    """
    bearing_stress = pbr / D / t
    

def pull_push_through(Fy, nf, Mz, At, ri, Ai):
    """
    Calculates the pull/push through failure of a bolt.

    Parameters:
        Fy (float): The tensile load on the bolt in N.
        nf (float): The number of fasteners.
        Mz (float): The bending moment in N-mm.
        At (float): The tensile area of the bolt in mm^2.
        ri (np.ndarray): The distance of the bolt from the neutral axis in mm.
        Ai (float): The tensile area of the bolt in mm^2.
    """
    f_pt = Fy / nf
    f_pmz = Mz * At * np.sum(ri) / Ai / np.sum(ri ** 2) 
    shear_stress = Fy / At

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
    

def end_pad_shear_failure(pt, dw, te, Fsu):
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


