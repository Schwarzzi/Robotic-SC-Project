from geometry import make_geometry, make_square_geometry
from sectionproperties.analysis import Section


def stress_analysis(poly: Section, mode: str="zxy", forces: dict={'n': 100e3}):
    """
    Perform stress analysis on the section.

    Parameters:
        poly (Section): The section to perform the stress analysis on.
        mode (str): The type of stress analysis to perform.
            stress="n_zz" - normal stress 
            resulting from the axial load 

            stress="mxx_zz" - normal stress 
            resulting from the bending moment 

            stress="myy_zz" - normal stress 
            resulting from the bending moment 

            stress="m11_zz" - normal stress 
            resulting from the bending moment 

            stress="m22_zz" - normal stress 
            resulting from the bending moment 

            stress="m_zz" - normal stress 
            resulting from all bending moments 

            stress="mzz_zx" - x component of the shear stress 
            resulting from the torsion moment 

            stress="mzz_zy" - y component of the shear stress 
            resulting from the torsion moment 

            stress="mzz_zxy" - resultant shear stress 
            resulting from the torsion moment 

            stress="vx_zx" - x component of the shear stress 
            resulting from the shear force 

            stress="vx_zy" - y component of the shear stress 
            resulting from the shear force 

            stress="vx_zxy" - resultant shear stress 
            resulting from the shear force 

            stress="vy_zx" - x component of the shear stress 
            resulting from the shear force 

            stress="vy_zy" - y component of the shear stress 
            resulting from the shear force 

            stress="vy_zxy" - resultant shear stress 
            resulting from the shear force 

            stress="v_zx" - x component of the shear stress 
            resulting from the sum of the applied shear forces 
            .

            stress="v_zy" - y component of the shear stress 
            resulting from the sum of the applied shear forces 
            .

            stress="v_zxy" - resultant shear stress 
            resulting from the sum of the applied shear forces 

            stress="zz" - combined normal stress 
            resulting from all actions

            stress="zx" - x component of the shear stress 
            resulting from all actions

            stress="zy" - y component of the shear stress 
            resulting from all actions

            stress="zxy" - resultant shear stress 
            resulting from all actions

            stress="11" - major principal stress 
            resulting from all actions

            stress="33" - minor principal stress 
            resulting from all actions

            stress="vm" - von Mises stress 
            resulting from all actions

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

# poly = make_geometry(display=False)
poly = make_square_geometry()
forces = {'n': 211.896e6 / 6,
          'vx': 70.632e6 / 6,
          'vy': 70.632e6 / 6}


stress_analysis(poly, forces=forces)