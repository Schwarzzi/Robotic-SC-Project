from sectionproperties.pre.library import rectangular_section
from sectionproperties.pre.library import rectangular_hollow_section
from sectionproperties.pre import Material
from sectionproperties.analysis import Section


mat3 = Material(
    name="Steel",
    elastic_modulus=200e9,
    poissons_ratio=0.3,
    yield_strength=250e6,
    density=8000,
    color="gray",
)

def create_geometry(side1, side2, t, material):

    p1 = rectangular_section(d=side1, b=side2, material=material).align_center()
    p2 = rectangular_section(d=side1 - t, b= side2 - t, material=material).align_center()
    geom = p1 - p2
    # geom.plot_geometry()
    return geom

def make_mesh(geometry):
    mesh = Section(geometry.create_mesh(mesh_sizes=[10]))
    # mesh.plot_mesh()
    return mesh

def process_mesh(mesh):
    mesh.calculate_geometric_properties()
    mesh.calculate_warping_properties()


def find_stress(mesh):
    stress = mesh.calculate_stress(
            n=100e3,
            mxx=10e6,
            myy=5e6,
            vx=25e3,
            vy=50e3,
            mzz=3e6,
        )

    stress.plot_stress(stress="zxy", cmap="viridis", normalize=False)


def run():
    geom = create_geometry(10, 10, 1, mat3)
    mesh = make_mesh(geom)
    process_mesh(mesh)
    return find_stress(mesh)

run()