import numpy as np
from thermalmodel_v4 import ThermalModel
from viewer import plot_3d
from nodes import construct_nodes


def main():
    """
    Main function.
    """

    nodes = construct_nodes()
    tm = ThermalModel(nodes)

    beta_range = np.linspace(0, 90, 2)
    h_range = np.linspace(200, 2000, 1)
    time_range = np.linspace(0, 50000, 100)

    plot_3d(tm, beta_range, h_range, time_range)


if __name__ == "__main__":
    main()