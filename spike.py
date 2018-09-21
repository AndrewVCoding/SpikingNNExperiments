import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

import network
import numpy as np
import math


simulation_speed = 10

fig = plt.figure()
fig.subplots_adjust(wspace=1.0, hspace=1.0)
# oa_subplot = fig.add_subplot(2, 2, 2)
mp_subplot = fig.add_subplot(1, 1, 1)
# na_subplot = fig.add_subplot(2, 2, 3)
# k_subplot = fig.add_subplot(2, 2, 4)
nn = network.Network()

window = 200

oa = []
mp = []
na = []
k = []
inputs = []


def time_trial():
    """
    Run the simulation and measure the amount of time it takes to run each step
    :return:
    """
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


def simulate(i):
    input = 0.0

    if 50 < i < 60:
        input = 0.0

    inputs.append(input)
    if len(inputs) >= window:
        inputs.pop(0)

    nn.step(input)


def get_window(x):
    return x[-window:window]


def mp_graph():
    xs = nn.t
    ys = nn.mp
    mp_subplot.clear()
    mp_subplot.plot(xs, ys)
    mp_subplot.plot(xs, nn.activation_history)
    mp_subplot.set_ylabel('membrane potential (mV)')
    mp_subplot.set_ylim(-80, 50)


def animate(i):
    for x in range(0, 1):
        simulate(i)
    mp_graph()


if __name__ == '__main__':
    np.set_printoptions(precision=2)

    print(nn.t, nn.activation_history)

    ani = animation.FuncAnimation(fig, animate, interval=1)

    plt.show()
