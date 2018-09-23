import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

import network
import numpy as np
import math


simulation_speed = 10
pause = False

fig = plt.figure()
fig.subplots_adjust(wspace=2.0, hspace=1.0)
# oa_subplot = fig.add_subplot(2, 2, 2)
mp_subplot = fig.add_subplot(3, 1, 1)
nc_subplot = fig.add_subplot(3, 1, 2)
pc_subplot = fig.add_subplot(3, 1, 3)
nn = network.Network()

window = 200

oa = []
mp = []
na = []
k = []
inputs = []


def onClick(event):
    global pause
    pause ^= True


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
                activation = 10.0 if math.sin(t / 20) > 0.099 else 0.0
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

    # if 20 < i < 50:
    #     input = 0.2 * math.sin(1 * i) if math.sin(1 * i) > 0.5 else 0.05
    # if 70 < i < 100:
    #     input = 0.1 if math.sin(1 * i) > 0.5 else 0.0
    # if 130 < i < 140:
    #     input = 0.1
    # if not pause:
    #     nn.step(input)

    if pause:
        input = 0.05

    nn.step(input)

    # if not pause:
    #     nn.step(input)


def get_window(x):
    return x[-window:window]


def mp_graph():
    xs = nn.t
    ys = nn.mp
    mp_subplot.clear()
    mp_subplot.plot(xs, ys)
    mp_subplot.plot(xs, nn.activation_history)
    mp_subplot.set_ylabel('(mV)')
    mp_subplot.set_ylim(-50, 50)


def n_channel_graph():
    xs = nn.t
    ys = nn.np
    nc_subplot.clear()
    nc_subplot.plot(xs, ys)
    nc_subplot.set_ylabel('n_ions')
    # nc_subplot.set_ylim(-80, 50)


def p_channel_graph():
    xs = nn.t
    ys = nn.pp
    pc_subplot.clear()
    pc_subplot.plot(xs, ys)
    pc_subplot.set_ylabel('d(n_ion)/d(t)')
    # pc_subplot.set_ylim(-5, 5)


def animate(i):
    for x in range(0, 1):
        simulate(i)
    mp_graph()
    n_channel_graph()
    p_channel_graph()


if __name__ == '__main__':
    np.set_printoptions(precision=2)

    print(nn.t, nn.activation_history)

    fig.canvas.mpl_connect('button_press_event', onClick)
    ani = animation.FuncAnimation(fig, animate, interval=1)

    plt.show()
