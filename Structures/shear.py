from geometry import make_geometry
from sectionproperties.analysis import Section


def stress_analysis(poly: Section, mode: str="shear", *args):
    """
    Perform stress analysis on the section.

    Parameters:
        poly (Section): The section to perform the stress analysis on.
        mode (str): The type of stress analysis to perform.
        *args: Additional arguments to pass to the stress analysis function.

    Returns:
        None
    
    """
    section = poly
    s = section.calculate_stress(vx=10e3, vy=10e3)
    s.plot_stress(stress=mode, cmap='viridis', normalize=True)

poly = make_geometry(display=True)
stress_analysis(poly, mode="zxy")