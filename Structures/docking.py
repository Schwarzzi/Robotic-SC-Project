import numpy as np
import matplotlib.pyplot as plt


def separation(mass, dx1, dx2, max_k):
    """
    Calculate the range of impulses based on a range of velocities for a given range of spring constants,
    considering the factor of 5 from the original equation and the ratio of delta x2 to delta x1.
    
    Parameters:
        mass (float): The mass of the chaser in kg.
        dx1 (float): The initial separation between the chaser and target in m.
        dx2 (float): The final separation between the chaser and target in m.
        max_k (float): The maximum spring constant in N/m.
    Returns:
        tuple: A tuple containing the spring constants, impulses, and velocities.
    """
    k_values = np.linspace(0, max_k, 500)
    impulses = []
    velocities = []
    
    for k in k_values:
        v1 = np.sqrt(5 * k / mass * (dx2 ** 2 - dx1 ** 2))
        v2 = np.sqrt(5 * k / mass * dx2 ** 2)
        
        dv = v2 - v1
        velocities.append(v1)
        impulses.append(mass * dv)

    return k_values, impulses, velocities


def plot(results):
    k, impulses, velocities = results
    # fig, ax1 = plt.subplots()

    # # Plot the first line with impulses
    # color = 'tab:red'
    # ax1.set_xlabel('Spring Constant (k)')
    # ax1.set_ylabel('Impulse (Ns)', color=color)
    # ax1.plot(k, impulses, color=color)
    # ax1.tick_params(axis='y', labelcolor=color)
    # ax1.set_ylim(0, 1.1 * max(impulses))  # Ensure impulses are within the frame

    # # Create a twin Axes sharing the xaxis
    # ax2 = ax1.twinx()  
    
    # # Plot the second line with velocities
    # color = 'tab:blue'
    # ax2.set_ylabel('Velocity (m/s)', color=color)
    # ax2.plot(k, velocities, color=color)
    # ax2.tick_params(axis='y', labelcolor=color)
    # ax2.set_ylim(0, 1.1 * max(velocities))  # Ensure velocities are within the frame

    # fig.tight_layout()  # To ensure the right y-label is not clipped
    # plt.show()


    plt.figure(figsize=(10, 6))
    plt.plot(k, impulses, label='Impulses')
    plt.plot(k, velocities, label='Velocities')
    plt.xlabel('Spring stiffness (N/m)')
    plt.ylabel('Velocities (m/s) | Impulses (Ns)')
    plt.legend()
    plt.grid(True)
    plt.show()


imp = separation(50, 1e-2, 1.7e-2, 13000)

#print(imp[1])
plot(imp)