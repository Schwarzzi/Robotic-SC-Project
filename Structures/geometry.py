from sectionproperties.pre import Material, Geometry
from sectionproperties.analysis import Section
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, LinearRing
from shapely.ops import unary_union


def plot_geometry(geoms: Polygon, ax: plt.Axes) -> None:
    """
    Plot the geometry.

    Parameters:
        geoms (list): A list of shapely.geometry.Polygon objects.
        ax (matplotlib.axes.Axes): The axes to plot the geometry on.
    """
    for geom in geoms:
        if geom.geom_type == 'Polygon':
            ax.plot(*geom.exterior.xy)
            for interior in geom.interiors:
                ax.plot(*interior.xy)
        elif geom.geom_type == 'MultiPolygon':
            for poly in geom:
                ax.plot(*poly.exterior.xy)
                for interior in poly.interiors:
                    ax.plot(*interior.xy)

def create_hollow_square(center: float, side: float, thickness: float) -> Polygon:
    """
    Create a hollow square with the specified center, side length and thickness.

    Parameters:
        center (tuple): The center of the square.
        side (float): The side length of the square.
        thickness (float): The thickness of the square.

    Returns:
        shapely.geometry.Polygon: The hollow square.
    """
    half_side = side / 2.0
    outer_square = Polygon([(center[0]-half_side, center[1]-half_side), 
                            (center[0]+half_side, center[1]-half_side), 
                            (center[0]+half_side, center[1]+half_side), 
                            (center[0]-half_side, center[1]+half_side)])
    inner_square = Polygon([(center[0]-half_side+thickness, center[1]-half_side+thickness), 
                            (center[0]+half_side-thickness, center[1]-half_side+thickness), 
                            (center[0]+half_side-thickness, center[1]+half_side-thickness), 
                            (center[0]-half_side+thickness, center[1]+half_side-thickness)])
    # Create a hollow square by subtracting the inner square from the outer square
    hollow_square = outer_square.difference(inner_square)
    return hollow_square

def create_hollow_hexagon(inner_radius: float, thickness: float, square_side: float, square_thickness: float) -> Polygon:
    """
    Create a hollow hexagon with inner squares.

    Parameters:
        inner_radius (float): The radius of the inner hexagon.
        thickness (float): The thickness of the hexagon.
        square_side (float): The side length of the inner squares.
        square_thickness (float): The thickness of the inner squares.

    Returns:
        shapely.geometry.Polygon: The hollow hexagon with inner squares.
    """
    outer_radius = inner_radius + thickness

    angles_inner = np.linspace(0, 2*np.pi, 7)[:-1]
    angles_outer = np.linspace(0, 2*np.pi, 7)[:-1]

    inner_hex = LinearRing(np.column_stack([inner_radius*np.cos(angles_inner), inner_radius*np.sin(angles_inner)]))
    outer_hex = Polygon(np.column_stack([outer_radius*np.cos(angles_outer), outer_radius*np.sin(angles_outer)]), holes=[inner_hex])

    vertices = outer_hex.exterior.coords[:-1]  # Get the vertices of the hexagon
    squares = [create_hollow_square(vertex, square_side, square_thickness) for vertex in vertices]

    inner_squares = []
    # Create a hole in the hexagon at the position of each square
    for square in squares:
        # Shrink the square slightly to avoid overlaps
        square = square.buffer(-0.001)
        inner_hex = LinearRing(square.exterior.coords[:])
        outer_hex = Polygon(outer_hex.exterior, holes=list(outer_hex.interiors) + [inner_hex])

        # Create the inner part of the square
        inner_square = Polygon(inner_hex)
        inner_squares.append(inner_square)

    # Subtract all the inner squares from the hexagon at once
    for inner_square in inner_squares:
        # Use buffer(0) to correct the geometry before subtracting
        outer_hex = outer_hex.buffer(0).difference(inner_square.buffer(0))

    all_geometries = [outer_hex] + squares

    return unary_union(all_geometries)

def make_geometry(inner_radius: float=1600, thickness: float=1, square_side: float=75, square_thickness: float=2, display: bool=False) -> Polygon:
    """
    Creates a geometry by calling the create_hollow_hexagon function with the specified parameters.

    Parameters:
        inner_radius (float): The inner radius of the hollow hexagon.
        thickness (float): The thickness of the hollow hexagon.
        square_side (float): The side length of the square.
        square_thickness (float): The thickness of the square.

    Returns:
        shapely.geometry.Polygon: The hollow hexagon with inner squares.
    """

    steel = Material(name="Steel",
                    elastic_modulus=200e3,  # N/mm^2 (MPa)
                    poissons_ratio=0.3,  # unitless
                    density=7.85e-6,  # kg/mm^3
                    yield_strength=500,  # N/mm^2 (MPa)
                    color="grey",
                )
    poly = create_hollow_hexagon(inner_radius=inner_radius, thickness=thickness, square_side=square_side, square_thickness=square_thickness)
    geom = Geometry(geom=poly, material=steel)
    geom.create_mesh(mesh_sizes=1)
    sec = Section(geometry=geom)
    if display:
        sec.plot_mesh()

    sec.calculate_geometric_properties() # MPa
    sec.calculate_warping_properties()
    sec.calculate_plastic_properties()
    return sec

def make_square_geometry(side=70, thickness=2):
    steel = Material(name="Steel",
                    elastic_modulus=200e3,  # N/mm^2 (MPa)
                    poissons_ratio=0.3,  # unitless
                    density=7.85e-6,  # kg/mm^3
                    yield_strength=500,  # N/mm^2 (MPa)
                    color="grey",
                )
    
    poly = create_hollow_square(center=(0,0), side=side, thickness=thickness)
    geom = Geometry(geom=poly, material=steel)
    geom.create_mesh(mesh_sizes=0.1)
    sec = Section(geometry=geom)
    sec.plot_mesh()
    sec.calculate_geometric_properties()
    sec.calculate_warping_properties()
    sec.calculate_plastic_properties()
    return sec