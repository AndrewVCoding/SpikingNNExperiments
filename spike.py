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
# nc_subplot = fig.add_subplot(3, 1, 2)
# pc_subplot = fig.add_subplot(3, 1, 3)
mp_subplot = fig.add_subplot(1, 1, 1)
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


def graph(plot, y_label='', x_label='', window=100, x=None, y=None, z=None, max=20, min=-60):
    if x is not None and y is not None:
        xs = x[-window:]
        ys = y[-window:]
        plot.clear()
        plot.plot(xs, ys)
        if z is not None:
            zs = z[-window:]
            plot.plot(xs, zs)
        plot.set_ylabel(y_label)
        plot.set_xlabel(x_label)
        plot.set_ylim(min, max)
    else:
        print('Can not plot, insufficient data given')


def animate(i):
    for x in range(0, 1):
        simulate(i)

    graph(mp_subplot, '', 'mp', 100, nn.t, nn.mp, nn.activation_history, max(nn.mp) + 5, min(nn.mp) - 5)


if __name__ == '__main__':
    np.set_printoptions(precision=2)

    print(nn.t, nn.activation_history)

    fig.canvas.mpl_connect('button_press_event', onClick)
    ani = animation.FuncAnimation(fig, animate, interval=1)

    plt.show()
