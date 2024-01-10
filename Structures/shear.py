from geometry import make_geometry
from sectionproperties.analysis import Section


def stress_analysis(poly: Section, mode: str="zxy", forces: dict={'n': 100e3}):
    """
    Perform stress analysis on the section.

    Parameters:
        poly (Section): The section to perform the stress analysis on.
        mode (str): The type of stress analysis to perform.
        Forces: Additional arguments to pass to the stress analysis function.
            n (float)  Axial force
            vx (float)  Shear force acting in the x-direction
            vy (float) Shear force acting in the y-direction
            mxx (float) Bending moment about the centroidal xx-axis
            myy (float) Bending moment about the centroidal yy-axis
            m11 (float) Bending moment about the centroidal 11-axis
            m22 (float) Bending moment about the centroidal 22-axis
            mzz (float) Torsion moment about the centroidal zz-axis

    Returns:
        None
    
    """
    section = poly
    s = section.calculate_stress(**forces)
    s.plot_stress(stress=mode, cmap='viridis', normalize=True)

poly = make_geometry(display=False)
stress_analysis(poly)