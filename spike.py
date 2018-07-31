import random
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

import network
import numpy as np

simulation_speed = 2

fig = plt.figure()
fig.subplots_adjust(wspace=1.0, hspace=1.0)
oa_subplot = fig.add_subplot(2, 2, 2)
mp_subplot = fig.add_subplot(2, 2, 1)
na_subplot = fig.add_subplot(2, 2, 3)
k_subplot = fig.add_subplot(2, 2, 4)
nn = network.Network()

window = 200

t = []
oa = []
mp = []
na = []
k = []
inputs = []


def simulate():
    # Retrieve the relevant information
    t.append(nn.t)
    if len(t) >= window:
        t.pop(0)
    oa.append(nn.OA)
    if len(oa) >= window:
        oa.pop(0)
    mp.append(nn.mp)
    if len(mp) >= window:
        mp.pop(0)
    na.append(nn.NA)
    if len(na) >= window:
        na.pop(0)
    k.append(nn.K)
    if len(k) >= window:
        k.pop(0)

    input = 20.0 * math.sin(nn.t / 1) if math.sin(nn.t / 1) > 0.999 else 0.0
    inputs.append(input)
    if len(inputs) >= window:
        inputs.pop(0)

    nn.step(input)


def mp_graph():
    xs = t
    ys = mp
    mp_subplot.clear()
    mp_subplot.plot(xs, ys)
    mp_subplot.plot(xs, inputs)
    mp_subplot.set_ylabel('membrane potential (mV)')
    mp_subplot.set_ylim(-80, 50)


def oa_graph():
    xs = t
    ys = oa
    oa_subplot.clear()
    oa_subplot.plot(xs, ys)
    oa_subplot.set_ylabel('OA')
    oa_subplot.set_xlabel('time')
    # oa_subplot.set_ylim(-70, 20)


def na_graph():
    xs = t
    ys = na
    na_subplot.clear()
    na_subplot.plot(xs, ys)
    na_subplot.set_ylabel('Na')
    na_subplot.set_xlabel('time')
    # na_subplot.set_ylim(-70, 20)


def k_graph():
    xs = t
    ys = k
    k_subplot.clear()
    k_subplot.plot(xs, ys)
    k_subplot.set_ylabel('K')
    k_subplot.set_xlabel('time')
    # k_subplot.set_ylim(-70, 20)


def animate(i):
    for x in range(0, simulation_speed):
        simulate()
    mp_graph()
    # oa_graph()
    na_graph()
    k_graph()


if __name__ == '__main__':
    np.set_printoptions(precision=2)
    # style.use('fivethirtyeight')

    ani = animation.FuncAnimation(fig, animate, interval=1)

    plt.show()
