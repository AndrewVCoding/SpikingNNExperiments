import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

import network
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
nn = network.Network()

def animate(i):
    xs = nn.length
    ys = nn.graph()
    ax.clear()
    ax.plot(xs, ys)
    nn.step()


if __name__ == '__main__':
    np.set_printoptions(precision=2)
    style.use('fivethirtyeight')

    timesteps = np.linspace(0, 100, 500)
    graph = []

    animation.FuncAnimation(fig, animate, interval=1000)

    # Plot the input signal
    for t in timesteps:
        animate(1)
        nn.step()

    #
    # N = 0
    # for N in range(0, len(nn.neuron)):
    #     xyz2 = []
    #     for point in xyz:
    #         if point[0] == N:
    #             xyz2.append(point)
    #
    #     xyz2 = np.array(xyz2)
    #     # Voltage
    #     z = xyz2[:, 2]
    #     # Time
    #     y = xyz2[:, 1]
    #     # Neuron
    #     x = xyz2[:, 0]
    #
    #     # ax.plot(x, y, z)
    #     ax.plot(y, z)

    ax.set_xlabel('position')
    ax.set_ylabel('Potential(mV)')
    # ax.set_zlabel('POTENTIAL')
    plt.grid()

    plt.show()
