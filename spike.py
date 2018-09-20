import matplotlib.pyplot as plt
import time
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
            net = network.Netowrk(i)
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
    nn = network.Netowrk()
    timesteps = [0.0]
    activations = [0.0]
    for t in range(0, 1000):
        activation = 2.0 if 0.1 * math.sin(t / 5) > 0.099 else 0.0
        nn.step(activation)
        activations.append(activation)
        timesteps.append(t)
    input_layer = nn.history
    plt.subplot(2, 1, 1)
    plt.plot(timesteps, input_layer)
    plt.xlabel('time step')
    plt.ylabel('activation')
    plt.title('Input Layer Stimulus')
    plt.plot(timesteps, activations)
    plt.grid()
    plt.show()
