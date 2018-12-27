import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

import network
import numpy as np
import math

simulation_speed = 1
pause = False

fig = plt.figure()
fig.set_size_inches(12, 8)
fig.subplots_adjust(wspace=0.5, hspace=0.5)
mp_subplot = fig.add_subplot(2, 2, 1)
nc_subplot = fig.add_subplot(2, 2, 2)
pc_subplot = fig.add_subplot(2, 2, 3)
exchange_subplot = fig.add_subplot(2, 2, 4)
# nn = network.Network()

window = 100

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
        input = 0.07

    for x in range(1, simulation_speed + 1):
        nn.step(input)

    # if not pause:
    #     nn.step(input)


def get_window(x):
    return x[-window:len(x)]


def mp_graph():
    xs = get_window(hist.time)
    y1 = get_window(hist.membrane_potential)
    mp_subplot.clear()
    mp_subplot.plot(xs, y1)
    mp_subplot.set_ylabel('(mV)')
    mp_subplot.set_ylim(-100, 20)


def negative_ion_graph():
    xs = get_window(hist.time)
    y1 = get_window(hist.negative_ions)
    y2 = get_window(hist.negative_channels)
    y3 = get_window(hist.negative_out)
    nc_subplot.clear()
    nc_subplot.plot(xs, y1)
    nc_subplot.plot(xs, y2)
    nc_subplot.plot(xs, y3)
    nc_subplot.set_ylabel('negative_ions')
    # nc_subplot.set_ylim(-80, 50)


def positive_ion_graph():
    xs = get_window(hist.time)
    y1 = get_window(hist.positive_ions)
    y2 = get_window(hist.positive_channels)
    y3 = get_window(hist.positive_out)
    pc_subplot.clear()
    pc_subplot.plot(xs, y1)
    pc_subplot.plot(xs, y2)
    pc_subplot.plot(xs, y3)
    pc_subplot.set_ylabel('positive_ions')
    # pc_subplot.set_ylim(-5, 5)


def exchange_graph():
    xs = get_window(hist.time)
    y1 = get_window(hist.exchange)
    exchange_subplot.clear()
    exchange_subplot.plot(xs, y1)
    exchange_subplot.set_ylabel('exchange_rate')
    exchange_subplot.set_ylim(-1.1, 1.1)


def animate(i):
    for x in range(0, 1):
        simulate(i)
    mp_graph()
    negative_ion_graph()
    positive_ion_graph()
    exchange_graph()


if __name__ == '__main__':
    np.set_printoptions(precision=2)
    hist = network.History()
    nn = network.Network(hist)

    fig.canvas.mpl_connect('button_press_event', onClick)
    ani = animation.FuncAnimation(fig, animate, interval=1)

    plt.show()
