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
flow_subplot = fig.add_subplot(2, 1, 2)
mp_subplot = fig.add_subplot(2, 1, 1)
nn = network.Network()

window = 200

mp = []
rr = []
t = []
inputs = []


def simulate():
    # Retrieve the relevant information
    t.append(nn.t)
    if len(t) >= window:
        t.pop(0)
    mp.append(nn.membrane_potential)
    if len(mp) >= window:
        mp.pop(0)
    rr.append(nn.rest_proximity)
    if len(rr) >= window:
        rr.pop(0)

    input = 1.0 * math.sin(nn.t / 1) if math.sin(nn.t / 5) > 0.9 else 0.0
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


def flow_graph():
    xs = t
    ys = rr
    flow_subplot.clear()
    flow_subplot.plot(xs, ys)
    flow_subplot.set_ylabel('return rate')
    flow_subplot.set_xlabel('time')
    # oa_subplot.set_ylim(-70, 20)


def animate(i):
    for x in range(0, simulation_speed):
        simulate()
    mp_graph()
    flow_graph()


if __name__ == '__main__':
    np.set_printoptions(precision=2)
    # style.use('fivethirtyeight')

    ani = animation.FuncAnimation(fig, animate, interval=1)

    plt.show()
