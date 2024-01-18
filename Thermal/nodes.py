"""
A module that contains constructors for nodes.
"""

from constants import Constants as C
from materials import Material as Mat
from materials import Component as Comp
from thermalmodel_v4 import Node

# Structures
Aluminium = Mat("Aluminium", 237, 897, 0.9, 0.3)
Steel = Mat("Steel", 50, 500, 0.9, 0.3)

# ADCS
Cmg = Comp("Control Moment Gyroscope", 640, Aluminium, 0.1)
Gnss = Comp("GNSS", 4.4, Aluminium, 0.1)
Accelerometer = Comp("Accelerometer", 1.12, Aluminium, 0.1)
Stim210 = Comp('Gyroscope', 3, Aluminium, 0.1)
Mag3 = Comp('Magnetometer', 1.7, Aluminium, 0.1)
St400 = Comp('Star Tracker', 2, Aluminium, 0.1)

# EPS
GalliumArsenide = Mat("Gallium Arsenide", 40, 340, 0.8, 0.8)
Vl51es = Comp("Batteries", 1958, Aluminium, 0.01) # Check efficiency
EvoPCDU = Comp("Power Control and Distribution Unit", 30, Aluminium, 0.1)
Smrt2805D = Comp("DC-DC Converter", 30, Aluminium, 0.1)	
Mw1000DD24L = Comp("DC-DC Converter", 1000, Aluminium, 0.12)

# CDH
Leon4FT = Comp("Onboard Computer", 4, Aluminium, 0.1)
StOBC = Comp("Onboard Computer", 4.8, Aluminium, 0.1)

# Docking
AmsV5618LA10P = Comp("Docking System", 67.2, Aluminium, 0.1)
AmsV4118CA01 = Comp("Docking System", 48, Aluminium, 0.1)

# Robotics
Vispa = Comp("Robotic Arm", 350, Aluminium, 0.1)


node_data = [
            {
                'key': 1,
                'name': 'Nadir-North',
                'area': C.A_panel,
                'mass': C.m_panel,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 30,
                'rb': 'earth',
                'position': [[1.8, 0.0, 2.5], [54.25, 90, 35.75]],
            },
            {
                'key': 2,
                'name': 'Nadir-South',
                'area': C.A_panel,
                'mass': C.m_panel,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 30,
                'rb': 'earth',
                'position': [[0.9, 1.5588, 2.5], [73.01, 59.60, 35.75]],
            },
            {
                'key': 3,
                'name': 'South',
                'area': C.A_panel,
                'mass': C.m_panel,
                'material': Aluminium,
                'temperature': 350.15,
                'gamma': 90,
                'rb': 'sun',
                'position': [[-0.9, 1.5588, 2.5], [106.99, 59.60, 35.75]],
            },
            {
                'key': 4,
                'name': 'Zenith-South',
                'area': C.A_panel,
                'mass': C.m_panel,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 30,
                'rb': 'earth',
                'position': [[-1.8, 0.0, 2.5], [125.75, 90, 35.75]],

            },
            {
                'key': 5,
                'name': 'Zenith-North',
                'area': C.A_panel,
                'mass': C.m_panel,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 30,
                'rb': 'sun',
                'position': [[-0.9, -1.5588, 2.5], [106.99, 120.40, 35.75]],
            },
            {
                'key': 6,
                'name': 'North',
                'area': C.A_panel,
                'mass': C.m_panel,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 90,
                'rb': 'earth',
                'position': [[0.9, -1.5588, 2.5], [73.01, 120.40, 35.75]],
            },
            {
                'key': 7,
                'name': 'Velocity',
                'area': C.A_top,
                'mass': C.m_top,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 90,
                'rb': 'earth',
                'position': [[0, 0, 5.0], [90, 90, 0]],
            },
            {
                'key': 8,
                'name': 'Negative-Velocity',
                'area': C.A_top,
                'mass': C.m_top,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 90,
                'rb': 'sun',
                'position': [[0, 0, 0], [90, 90, 180]],
            },
            {
                'key': 9,
                'name': 'North-Solar-Array',
                'area': C.A_solar,
                'mass': C.m_array,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[6, 0, 2.5], [54.25, 90, 35.75]],
            },
            {
                'key': 10,
                'name': 'South-Solar-Array',
                'area': C.A_solar,
                'mass': 50,
                'material': Aluminium,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]],
            },
            # From here on, area, mass, gamma, and position are incorrect
            {   
                'key': 11,
                'name': 'Vispa Nadir',
                'area': 4, # ??
                'mass': 50,
                'material': Vispa,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'earth',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 12,
                'name': 'Vispa Zenith',
                'area': 4, # ??
                'mass': 50,
                'material': Vispa,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 13,
                'name': 'CMG 75-75s by Airbus 1',
                'area': 1.81,
                'mass': 69,
                'material': Cmg,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 14,
                'name': 'CMG 75-75s by Airbus 2',
                'area': 1.81,
                'mass': 69,
                'material': Cmg,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 15,
                'name': 'CMG 75-75s by Airbus 3',
                'area': 1.81,
                'mass': 69,
                'material': Cmg,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 16,
                'name': 'CMG 75-75s by Airbus 4',
                'area': 1.81,
                'mass': 69,
                'material': Cmg,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            
            },
            {   
                'key': 17,
                'name': 'GNSS-701 by AAC Clyde Space 1',
                'area': 0.2, # ?
                'mass': 0.32,
                'material': Gnss,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 18,
                'name': 'GNSS-701 by AAC Clyde Space 2',
                'area': 0.2, # ?
                'mass': 0.32,
                'material': Gnss,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 19,
                'name': '3313 Series by Dytran Instruments 1',
                'area': 0.1, # ?
                'mass': 0.008,
                'material': Accelerometer,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 20,
                'name': '3313 Series by Dytran Instruments 2',
                'area': 0.1, # ?
                'mass': 0.008,
                'material': Accelerometer,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 21,
                'name': 'STIM210 by Sensonor AS 1',
                'area': 0.2,
                'mass': 0.104,
                'material': Stim210,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 22,
                'name': 'STIM210 by Sensonor AS 2',
                'area': 0.2,
                'mass': 0.104,
                'material': Stim210,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 23,
                'name': 'Mag-3 by AAC Clyde Space 1',
                'area': 0.4,
                'mass': 0.2,
                'material': Mag3,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 24,
                'name': 'Mag-3 by AAC Clyde Space 2',
                'area': 0.4,
                'mass': 0.2,
                'material': Mag3,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 25,
                'name': 'ST400 Startracker by AAC Clyde Space 1',
                'area': 0.4,
                'mass': 0.560,
                'material': St400,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'earth',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 26,
                'name': 'ST400 Startracker by AAC Clyde Space 2',
                'area': 0.4,
                'mass': 0.560,
                'material': St400,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 27,
                'name': 'ThalesAlenia Space COSMO-SkyMed solar panels North',
                'area': C.A_solar,
                'mass': 25.8,
                'material': GalliumArsenide, # fix
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 28,
                'name': 'ThalesAlenia Space COSMO-SkyMed solar panels South',
                'area': C.A_solar,
                'mass': 25.8,
                'material': GalliumArsenide, # fix
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 29,
                'name': 'Saft VL51ES 8S2P battery packs 1',
                'area': 0.67,
                'mass': 22.3,
                'material': Vl51es, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 30,
                'name': 'Saft VL51ES 8S2P battery packs 2',
                'area': 0.67,
                'mass': 22.3,
                'material': Vl51es, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 31,
                'name': 'Saft VL51ES 8S2P battery packs 3',
                'area': 0.67,
                'mass': 22.3,
                'material': Vl51es, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 32,
                'name': 'Airbus EVO PCDU 1',
                'area': C.A_solar,
                'mass': 23.5,
                'material': EvoPCDU,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 33,
                'name': 'Airbus EVO PCDU 2',
                'area': C.A_solar,
                'mass': 23.5,
                'material': EvoPCDU, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 34,
                'name': 'AMS V5718L-A10P 1',
                'area': C.A_solar,
                'mass': C.m_array,
                'material': AmsV5618LA10P, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 35,
                'name': 'AMS V5718L-A10P',
                'area': C.A_solar,
                'mass': C.m_array,
                'material': AmsV5618LA10P, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 36,
                'name': 'AMS V4118C-A01',
                'area': C.A_solar,
                'mass': C.m_array,
                'material': AmsV4118CA01, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            }
]

# Define neighbor relationships
neighbor_mapping = {
    0: [(1, C.A_contact_side), (5, C.A_contact_side), (6, C.A_contact_top), (7, C.A_contact_boom), (8, C.A_contact_support)],
    1: [(2, C.A_contact_side), (6, C.A_contact_top), (7, C.A_contact_top), (8, C.A_contact_support)],
    2: [(3, C.A_contact_side), (6, C.A_contact_top), (7, C.A_contact_top), (10, C.A_contact_boom), (8, C.A_contact_support)],
    3: [(4, C.A_contact_side), (6, C.A_contact_top), (7, C.A_contact_top), (8, C.A_contact_support)],
    4: [(5, C.A_contact_side), (6, C.A_contact_top), (7, C.A_contact_top), (8, C.A_contact_support)],
    5: [(6, C.A_contact_top), (7, C.A_contact_top), (9, C.A_contact_boom), (8, C.A_contact_support)],
    6: [(7, C.A_contact_top), (6, C.A_contact_top)],
    8: [(0, C.A_contact_side), (1, C.A_contact_side), (2, C.A_contact_side), (3, C.A_contact_side), (4, C.A_contact_side), (5, C.A_contact_side), (6, C.A_contact_top)],
    # Continue for other nodes if needed
}


def construct_nodes(node_data=node_data, neighbor_mapping=neighbor_mapping):
    """
    Constructs nodes and sets up their neighbor relationships.

    Parameters:
        node_data (list): A list of dictionaries, each containing data for initializing a Node.
        neighbor_mapping (dict): A dictionary mapping node indices to lists of tuples (neighbor index, contact area).

    Returns:
        A list of constructed Node instances with neighbor relationships set.
    """
    # Construct nodes
    nodes = [Node(**data) for data in node_data]

    # Add neighbors based on mapping
    for node_index, neighbors in neighbor_mapping.items():
        for neighbor_index, contact_area in neighbors:
            nodes[node_index].add_neighbor(nodes[neighbor_index], contact_area)

    return nodes
