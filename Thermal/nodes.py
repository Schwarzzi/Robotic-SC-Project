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
FrontPanel = Mat("Front Panel", C.k_ga, C.cp_ga, 0.899, 0.92)
BackPanel = Mat("Back Panel", C.k_al, C.cp_al, 0.01, 0.5)

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
                'position': [[0.5435, 0.876, 2.225], [75, 37.76, 20.71]], # correct
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
                'position': [[-0.5435, 0.876, 2.225], [15, 37.76, 20.71]], # correct
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
                'position': [[-1.087, 0, 2.225], [45, 0, 45]], # correct
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
                'position': [[-0.5435, -0.876, 2.225], [75, 37.76, 20.71]], # correct

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
                'position': [[-0.5435, 0.876, 2.225], [15, 20.71, 37.76]], # correct
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
                'position': [[1.087, 0, 2.225], [45, 0, 45]], # correct
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
                'position': [[0, 0, 4.45], [0, 45, 45]], # correct
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
                'position': [[0, 0, 0], [0, 45, 45]], # correct
            },
            {
                'key': 9,
                'name': 'North-Solar-Array Front',
                'area': C.A_solar,
                'mass': C.m_array / 2,
                'material': FrontPanel,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[4.287, -0.02, 2.225], [45, 0, 45]], #correct
            },
            {
                'key': 10,
                'name': 'South-Solar-Array Front',
                'area': C.A_solar,
                'mass': C.m_array / 2,
                'material': FrontPanel,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-4.287, -0.02, 2.225], [45, 0, 45]], #correct
            },
            # From here on, area, mass, gamma, and position are incorrect
            {   
                'key': 11,
                'name': 'Vispa Nadir North',
                'area': 4, # ??
                'mass': 50,
                'material': Vispa,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'earth',
                'position': [[0.55, 0.89, 4], [75, 37.76, 20.71]], # correct
            },
            {   
                'key': 12,
                'name': 'Vispa Zenith South',
                'area': 4, # ??
                'mass': 50,
                'material': Vispa,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-0.55, -0.89, 4], [75, 37.76, 20.71]], # correct 
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
            # {   
            #     'key': 27,
            #     'name': 'ThalesAlenia Space COSMO-SkyMed solar panels North',
            #     'area': C.A_solar,
            #     'mass': 25.8,
            #     'material': GalliumArsenide, # fix
            #     'temperature': 293.15,
            #     'gamma': 0,
            #     'rb': 'sun',
            #     'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            # },
            # {   
            #     'key': 28,
            #     'name': 'ThalesAlenia Space COSMO-SkyMed solar panels South',
            #     'area': C.A_solar,
            #     'mass': 25.8,
            #     'material': GalliumArsenide, # fix
            #     'temperature': 293.15,
            #     'gamma': 0,
            #     'rb': 'sun',
            #     'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            # },
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
                'area': 0.875,
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
                'area': 0.875,
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
            },
            {   
                'key': 37,
                'name': 'Interpoint SMRT2805D 1',
                'area': 0.01,
                'mass': 0.1,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 38,
                'name': 'Interpoint SMRT2805D 2',
                'area': 0.01,
                'mass': 0.1,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 39,
                'name': 'Interpoint SMRT2805D 3',
                'area': 0.01,
                'mass': 0.1,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 40,
                'name': 'Interpoint SMRT2805D 4',
                'area': 0.01,
                'mass': 0.1,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 41,
                'name': 'Interpoint SMRT2805D 5',
                'area': 0.01,
                'mass': 0.1,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 42,
                'name': 'Interpoint SMRT2805D 6',
                'area': 0.01,
                'mass': 0.1,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 43,
                'name': 'De Wit MW1000-DD24-L',
                'area': 0.11,
                'mass': 1.9,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 44,
                'name': 'De Wit MW1000-DD24-L',
                'area': 0.11,
                'mass': 1.9,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 45,
                'name': 'North-Solar-Array Back',
                'area': C.A_solar,
                'mass': C.m_array / 2 ,
                'material': BackPanel, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'earth',
                'position': [[4.287, 0.02, 2.225], [45, 45, 0]], # correct 
            },
            {   
                'key': 46,
                'name': 'South-Solar-Array Back',
                'area': C.A_solar,
                'mass': C.m_array / 2 ,
                'material': BackPanel, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'earth',
                'position': [[-4.287, 0.02, 2.225], [45, 45, 0]], # correct
            },
            {   
                'key': 47,
                'name': 'North-Solar-Array Boom',
                'area': 0.1,
                'mass': 1 ,
                'material': Aluminium, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 48,
                'name': 'South-Solar-Array Boom',
                'area': 0.1,
                'mass': 1 ,
                'material': Aluminium, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            },
            {   
                'key': 49,
                'name': 'South-Solar-Array Sandwhich',
                'area': 0.1,
                'mass': 1 ,
                'material': Aluminium, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-4.287, 0, 2.225], [45, 45, 0]], # correct
            },
            {   
                'key': 50,
                'name': 'North-Solar-Array Sandwhich',
                'area': 0.1,
                'mass': 1 ,
                'material': Aluminium, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[4.287, 0, 2.225], [45, 45, 0]], # correct 
            },
            
            
            

            
]

# Define neighbor relationships
neighbor_mapping = {
    # Structural Panel Contacts
    1: [(2, C.A_contact_side), (6, C.A_contact_side), (7, C.A_contact_top), (8, C.A_contact_top)], # Nadir-North
    2: [(1, C.A_contact_side), (3, C.A_contact_side), (7, C.A_contact_top), (8, C.A_contact_top)], # Nadir-South
    3: [(2, C.A_contact_side), (4, C.A_contact_side), (7, C.A_contact_top), (8, C.A_contact_top), (48, C.A_contact_boom)], # South
    4: [(3, C.A_contact_side), (5, C.A_contact_side), (7, C.A_contact_top), (8, C.A_contact_top)], # Zenith-South
    5: [(4, C.A_contact_side), (6, C.A_contact_side), (7, C.A_contact_top), (8, C.A_contact_top)], # Zenith-North
    6: [(5, C.A_contact_side), (1, C.A_contact_side), (7, C.A_contact_top), (8, C.A_contact_top), (47, C.A_contact_boom)], # North
    7: [(1, C.A_side_top), (2, C.A_side_top), (3, C.A_side_top), (4, C.A_side_top), (5, C.A_side_top), (6, C.A_side_top)], # Velocity
    8: [(1, C.A_side_top), (2, C.A_side_top), (3, C.A_side_top), (4, C.A_side_top), (5, C.A_side_top), (6, C.A_side_top)], # Negative-Velocity
    # Solar Array Contacts 
    9: [(50, 1)], # North Solar Array Front
    10: [(49, 1)], # South Solar Array Front
    45: [(50, 1)], # North Solar Array Back
    46: [(49, 1)], # South Solar Array Back
    47: [(50, C.A_contact_boom), (6, C.A_contact_boom)], # North Solar Array Boom
    48: [(49, C.A_contact_boom), (3, C.A_contact_boom)], # South Solar Array Boom
    49: [(10, 1), (46, 1), (48, C.A_contact_boom)], # South Solar Array Sandwich
    50: [(9, 1), (45, 1), (47, C.A_contact_boom)], # North Solar Array Sandwich
    # Robotics Contacts
    11: [(1, 0.24)], # Vispa Nadir
    12: [(4, 0.24)], # Vispa Zenith
    # ADCS Contacts



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
            nodes[node_index-1].add_neighbor(nodes[neighbor_index-1], contact_area)

    return nodes
