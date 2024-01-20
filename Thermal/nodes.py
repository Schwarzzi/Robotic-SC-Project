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
SwOBC = Comp("SpaceWire", 3, Aluminium, 0.1)

# Docking
AmsV5618LA10P = Comp("Docking System", 67.2, Aluminium, 0.1)
AmsV4118CA01 = Comp("Docking System", 48, Aluminium, 0.1)

# Robotics
Vispa = Comp("Robotic Arm", 350, Aluminium, 0.1)

# Communications
Victs = Comp("Antenna", 75, Aluminium, 0.1)
Swift = Comp("Transmitter", 50, Aluminium, 0.1)
Para = Comp('Paradigm', 51, Aluminium, 0.1)
Erz = Comp('ERZ', 120, Aluminium, 0.1)

# Thermal
Rad = Comp("Radiators", -200, Aluminium, 1)
Heatpipe = Mat("Heatpipe", 10000, C.cp_al, 0.9, 0.3)

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
                'position': [[0, 0, 3], [0, 45, 45]], # Corret Center panel
            },
            # {   
            #     'key': 14,
            #     'name': 'CMG 75-75s by Airbus 2',
            #     'area': 1.81,
            #     'mass': 69,
            #     'material': Cmg,
            #     'temperature': 293.15,
            #     'gamma': 0,
            #     'rb': 'internal',
            #     'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            # },
            # {   
            #     'key': 15,
            #     'name': 'CMG 75-75s by Airbus 3',
            #     'area': 1.81,
            #     'mass': 69,
            #     'material': Cmg,
            #     'temperature': 293.15,
            #     'gamma': 0,
            #     'rb': 'internal',
            #     'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            # },
            # {   
            #     'key': 16,
            #     'name': 'CMG 75-75s by Airbus 4',
            #     'area': 1.81,
            #     'mass': 69,
            #     'material': Cmg,
            #     'temperature': 293.15,
            #     'gamma': 0,
            #     'rb': 'internal',
            #     'position': [[-6, 0, 2.5], [125.75, 90, 35.75]], 
            
            # },
            {   
                'key': 17,
                'name': 'GNSS-701 by AAC Clyde Space 1',
                'area': 0.2, # ?
                'mass': 0.32,
                'material': Gnss,
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[1.08, 0, 2.64], [45, 0, 45]], # correct North panel
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
                'position': [[-1.08, 0, 2.64], [45, 0, 45]], # correct South panel
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
                'position': [[1.08, -0.05, 2.64], [45, 0, 45]], # correct North panel
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
                'position': [[-1.08, 0.05, 2.64], [45, 0, 45]], # correct South panel
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
                'position': [[1.08, 0.15, 2.64], [45, 0, 45]], # correct North panel
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
                'position': [[-1.08, -0.15, 2.64], [45, 0, 45]], # correct South panel
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
                'position': [[1.08, 0.25, 2.65], [45, 0, 45]], # correct North panel
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
                'position': [[-1.08, -0.25, 2.65], [45, 0, 45]], # correct South panel
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
                'position': [[1.12, 0, 4.2], [45, 0, 45]], # correct North panel
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
                'position': [[-1.12, 0, 4.2], [45, 0, 45]], # correct South panel
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
                'position': [[-0.3, 1.168, 2.71], [45, 45, 0]], # correct Nadir center
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
                'position': [[-0.3, 1.168, 2.87], [45, 45, 0]], # correct Nadir center
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
                'position': [[-0.3, 1.168, 3.03], [45, 45, 0]], # correct Nadir center
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
                'position': [[0.4, -1.168, 2.77], [45, 45, 0]], # correct Zenith center
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
                'position': [[0.4, -1.168, 2.98], [45, 45, 0]], # correct Zenith center
            },
            {   
                'key': 34,
                'name': 'AMS V5718L-A10P 1',
                'area': 0.2,
                'mass': 1.066,
                'material': AmsV5618LA10P, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[0.1, 0, 4.45], [0, 45, 45]], # correct top panel
            },
            {   
                'key': 35,
                'name': 'AMS V5718L-A10P',
                'area': 0.2,
                'mass': 1.066,
                'material': AmsV5618LA10P, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-0.1, 0, 4.45], [0, 45, 45]], # correct top panel
            },
            {   
                'key': 36,
                'name': 'AMS V4118C-A01',
                'area': 0.1,
                'mass': 0.409,
                'material': AmsV4118CA01, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[0, 0, 4.45], [0, 45, 45]], # correct top panel
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
                'position': [[0.54, 0.87, 2.66], [75, 37.76, 20.71]], # correct Nadir-north panel
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
                'position': [[-0.54, 0.87, 2.66], [15, 37.76, 20.71]], # correct Nadir-south panel
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
                'position': [[-1.08, 0, 2.7], [45, 0, 45]], # correct South panel
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
                'position': [[-0.54, -0.87, 2.66], [75, 37.76, 20.71]], # correct Zenith-south panel
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
                'position': [[0.54, -0.87, 2.66], [15, 37.76, 20.71]], # correct Zenith-north panel
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
                'position': [[1.08, 0, 2.7], [45, 0, 45]], # correct North panel
            },
            {   
                'key': 43,
                'name': 'De Wit MW1000-DD24-L 1',
                'area': 0.11,
                'mass': 1.9,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[0, 0, 3.6], [0, 45, 45]], # correct Pressurised compartment
            },
            {   
                'key': 44,
                'name': 'De Wit MW1000-DD24-L 2',
                'area': 0.11,
                'mass': 1.9,
                'material': Smrt2805D, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[0, 0, 3.9], [0, 0, 45]], # correct Pressurised compartment
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
                'position': [[1.15, 0, 2.5], [45, 45, 0]], # correct North panel
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
                'position': [[-1.15, 0, 2.5], [45, 45, 0]], # correct South panel
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
            {   
                'key': 51,
                'name': 'VICTS Patent Array antenna 1',
                'area': 0.29,
                'mass': 20,
                'material': Victs, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'earth',
                'position': [[0.57, 0.9, 1.5], [75, 37.76, 20.71]], # correct Nadir-north panel
            },
            {   
                'key': 52,
                'name': 'VICTS Patent Array antenna 2',
                'area': 0.29,
                'mass': 20,
                'material': Victs, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'earth',
                'position': [[-0.57, 0.9, 1.5], [15, 37.76, 20.71]], # correct Nadir-south panel
            },
            {   
                'key': 53,
                'name': 'VICTS Patent Array antenna 3',
                'area': 0.29,
                'mass': 20,
                'material': Victs, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'none',
                'position': [[-1.2, 0, 1.5], [45, 0, 45]], # correct South panel
            },
            {   
                'key': 54,
                'name': 'VICTS Patent Array antenna 4',
                'area': 0.29,
                'mass': 20,
                'material': Victs, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[-0.57, -0.9, 1.5], [75, 37.76, 20.71]], # correct Zenith-south panel
            },
            {   
                'key': 55,
                'name': 'VICTS Patent Array antenna 5',
                'area': 0.29,
                'mass': 20,
                'material': Victs, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'sun',
                'position': [[0.57, -0.9, 1.5], [15, 37.76, 20.71]], # correct Zenith-north panel
            },
            {   
                'key': 56,
                'name': 'VICTS Patent Array antenna 6',
                'area': 0.29,
                'mass': 20,
                'material': Victs, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'none',
                'position': [[1.2, 0, 1.5], [45, 0, 45]], # correct North panel
            },
            {   
                'key': 57,
                'name': 'Swift X KTRX 1',
                'area': 0.29,
                'mass': 0.062,
                'material': Swift, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[0.54, 0.87, 2.8], [75, 37.76, 20.71]], # correct Nadir-north panel
            },
            {   
                'key': 58,
                'name': 'Swift X KTRX 2',
                'area': 0.29,
                'mass': 0.062,
                'material': Swift, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-0.54, 0.87, 2.8], [15, 37.76, 20.71]], # correct Nadir-south panel
            },
            {   
                'key': 59,
                'name': 'Swift X KTRX 3',
                'area': 0.29,
                'mass': 0.062,
                'material': Swift, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-0.54, -0.87, 2.8], [75, 37.76, 20.71]], # correct Zenith-south panel
            },
            {   
                'key': 60,
                'name': 'Swift X KTRX 4',
                'area': 0.29,
                'mass': 0.062,
                'material': Swift, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[0.54, -0.87, 2.8], [15, 37.76, 20.71]], # correct Zenith-north panel
            },
            {   
                'key': 62,
                'name': 'Paradigma Ka Band Transponder 1',
                'area': 0.24,
                'mass': 1.6,
                'material': Para, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[1.08, 0, 3], [45, 0, 45]], # correct North panel
            },
            {   
                'key': 63,
                'name': 'Paradigma Ka Band Transponder 2',
                'area': 0.24,
                'mass': 1.6,
                'material': Para, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-1.08, 0, 3], [45, 0, 45]], # correct South panel
            },
            {   
                'key': 64,
                'name': 'ERZ-HPA-2700-3100-43-C',
                'area': 0.029,
                'mass': 1,
                'material': Para, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[1.08, -0.2, 3], [45, 0, 45]], # correct North panel
            },
            {   
                'key': 65,
                'name': 'SIRIUS QUADCORE LEON4FT "stacked"',
                'area': 0.035,
                'mass': 0.1,
                'material': Para, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[1.08, 0.2, 3], [45, 0, 45]], # correct North panel
            },
            {   
                'key': 66,
                'name': 'SIRIUS OBC "stacked"',
                'area': 0.02,
                'mass': 0.25,
                'material': StOBC, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-1.08, 0.2, 3], [45, 0, 45]], # correct South panel
            },
            {   
                'key': 67,
                'name': 'GR718B Radiation-Tolerant 18x SpaceWire Router',
                'area': 0.035,
                'mass': 0.1,
                'material': SwOBC, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[-1.08, -0.2, 3], [45, 0, 45]], # correct South panel
            },
            {   
                'key': 68,
                'name': 'Center panel',
                'area': 0.035,
                'mass': 0.1,
                'material': Aluminium, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[0, 0, 2.63], [0, 45, 45]], # correct Center panel supporting components
            },
            {   
                'key': 69,
                'name': 'Pressurised compartement',
                'area': 1.8,
                'mass': 40,
                'material': Aluminium, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[0, 0, 3], [0, 45, 45]], # correct Center panel supporting components
            },
            {   
                'key': 70,
                'name': 'Radiator North panel',
                'area': 9,
                'mass': 10,
                'material': Rad, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[4.287, 0.3, 2.225], [45, 45, 0]], # correct Center panel supporting components
            },
            {   
                'key': 71,
                'name': 'Radiator South panel',
                'area': 9,
                'mass': 10,
                'material': Rad, 
                'temperature': 293.15,
                'gamma': 0,
                'rb': 'internal',
                'position': [[4.287, -0.3, 2.225], [45, 45, 0]], # correct Center panel supporting components
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
    13: [(68, 0.314)], # CMG 75-75s by Airbus 1
    17: [(6, 0.01)], # GNSS-701 by AAC Clyde Space 1
    18: [(3, 0.01)], # GNSS-701 by AAC Clyde Space 2
    19: [(6, 0.01)], # 3313 Series by Dytran Instruments 1
    20: [(3, 0.01)], # 3313 Series by Dytran Instruments 2
    21: [(6, 0.01)], # STIM210 by Sensonor AS 1
    22: [(3, 0.01)], # STIM210 by Sensonor AS 2
    23: [(6, 0.01)], # Mag-3 by AAC Clyde Space 1
    24: [(3, 0.01)], # Mag-3 by AAC Clyde Space 2
    25: [(6, 0.01)], # ST400 Startracker by AAC Clyde Space 1
    26: [(3, 0.01)], # ST400 Startracker by AAC Clyde Space 2
    # EPS Contacts
    29: [(1, 0.02), (2, 0.02), (68, 0.14)], # Saft VL51ES 8S2P battery packs 1
    30: [(1, 0.02), (2, 0.02), (29, 0.14)], # Saft VL51ES 8S2P battery packs 2
    31: [(1, 0.02), (2, 0.02), (30, 0.14)], # Saft VL51ES 8S2P battery packs 3
    32: [(4, 0.04), (5, 0.04), (68, 0.23)], # Airbus EVO PCDU 1
    33: [(4, 0.04), (5, 0.04), (32, 0.23)], # Airbus EVO PCDU 2
    37: [(1, 0.004)], # Interpoint SMRT2805D 1
    38: [(2, 0.004)], # Interpoint SMRT2805D 2
    39: [(3, 0.004)], # Interpoint SMRT2805D 3
    40: [(4, 0.004)], # Interpoint SMRT2805D 4
    41: [(5, 0.004)], # Interpoint SMRT2805D 5
    42: [(6, 0.004)], # Interpoint SMRT2805D 6
    43: [(69, 0.04)], # De Wit MW1000-DD24-L 1
    44: [(69, 0.04)], # De Wit MW1000-DD24-L 2
    # Docking Contacts
    34: [(7, 0.01)], # AMS V5718L-A10P 1
    35: [(7, 0.01)], # AMS V5718L-A10P 2
    36: [(7, 0.01)], # AMS V4118C-A01
    # Communication Contacts
    51: [(1, 0.3)], # VICTS Patent Array antenna 1
    52: [(2, 0.3)], # VICTS Patent Array antenna 2
    53: [(3, 0.3)], # VICTS Patent Array antenna 3
    54: [(4, 0.3)], # VICTS Patent Array antenna 4
    55: [(5, 0.3)], # VICTS Patent Array antenna 5
    56: [(6, 0.3)], # VICTS Patent Array antenna 6
    57: [(1, 0.1)], # Swift X KTRX 1
    58: [(2, 0.1)], # Swift X KTRX 2
    59: [(4, 0.1)], # Swift X KTRX 3
    60: [(5, 0.1)], # Swift X KTRX 4
    62: [(6, 0.1)], # Paradigma Ka Band Transponder 1
    63: [(3, 0.1)], # Paradigma Ka Band Transponder 2
    64: [(6, 0.1)], # ERZ-HPA-2700-3100-43-C
    65: [(6, 0.1)], # SIRIUS QUADCORE LEON4FT "stacked"
    66: [(3, 0.1)], # SIRIUS OBC "stacked"
    67: [(3, 0.1)], # GR718B Radiation-Tolerant 18x SpaceWire Router
    # Miscellaneous Contacts
    68: [(1, 0.0024), (2, 0.0024), (3, 0.0024), (4, 0.0024), (5, 0.0024), (6, 0.0024)], # Center panel
    69: [(1, 0.0004), (2, 0.0004), (3, 0.0004), (4, 0.0004), (5, 0.0004), (6, 0.0004), (7, 0.28), (8, 0.28)], # Pressurised compartment

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
    # print(neighbor_mapping.items())
    # Add neighbors based on mapping
    # for node_index, neighbors in neighbor_mapping.items():
    #     for neighbor_index, contact_area in neighbors:
    #         print(f'Node: {nodes[node_index-1] }')
    #         print(f'Neighbor index: {neighbor_index - 1}')
    #         print(f'Neighbor: {nodes[neighbor_index - 1]}')
    #         nodes[node_index-1].add_neighbor(nodes[neighbor_index-1], contact_area)

    # return nodes
    nodes_dict = {node.key: node for node in nodes}
    for node_key, neighbors in neighbor_mapping.items():
        current_node = nodes_dict[node_key]
    
        for neighbor_info in neighbors:
            neighbor_key, contact_area = neighbor_info
            neighbor_node = nodes_dict[neighbor_key]
            current_node.add_neighbor(neighbor_node, contact_area)

    return nodes

