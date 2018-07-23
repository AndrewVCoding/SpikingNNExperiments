import matplotlib.pyplot as plt
import time

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors

import network
import numpy as np
import math


def time_trial():
    x = []
    times = []

    start = time.time()
    for i in range(900, 1000):
        trial = []
        x.append(i)
        t1 = time.time()
        for n in range(0, 50):
            trial = []
            net = network.Network(i)
            t1 = time.time()
            for t in range(0, 100):
                activation = 10.0 if 0.1 * math.sin(t / 20) > 0.099 else 0.0
                net.step(activation)
            t2 = time.time()
            trial.append(t2 - t1)
        times.append(np.mean(trial))
        print(i, ' neurons simulated in ', time.time() - t1, ' seconds')
    print('Total Time: ', time.time() - start)

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.scatter(x, times)
    ax.set_xlabel('neurons')
    ax.set_ylabel('avg time (seconds)')
    ax.set_title('Time per 100 Simulation steps averaged across 50 trials')
    plt.grid()

    plt.show()


if __name__ == '__main__':
    np.set_printoptions(precision=2)

    nn = network.Network()

    timesteps = np.linspace(-10, 10, 2000)
    activations = []
    for t in timesteps:
        activations.append(nn.graded_potential(2.5, 10, 10, t))

    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = fig.add_subplot(111)

    # Plot the input signal
    ax.plot(timesteps, activations)
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
