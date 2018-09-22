import numpy as np
import random
import math


class Network:

    # @todo Design the axon functions
    # @todo Design a function to build a network of any size with the proper connections
    def __init__(self, input_neurons=1, hidden_neurons=0, output_neurons=0, axon_density=0.2):
        np.random.seed(2)

        # Record the number of neurons in the three layers
        self.input_neurons = input_neurons
        self.hidden_neurons = hidden_neurons
        self.output_neurons = output_neurons

        size = input_neurons + hidden_neurons + output_neurons

        # Create an ndarray of zeros to represent the potential of each neuron
        self.neuron = 0.0

        # Generate the threshold for each neuron
        # self.threshold = np.zeros(size, dtype=np.double) + 20.0
        self.threshold_potential = 20

        # Generate the resting potential of each neuron
        # self.resting_potential = np.zeros(size, dtype=np.double)
        self.resting_potential = -30.0

        # Set the decay rate of each neuron
        self.decay = 0.5

        # self.axon = np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]])

        self.activation = 0.0
        # for x in range(0, 100):
        #     self.activation.append(np.zeros(size, dtype=np.double))

        self.history = [0.0]

        self.activation_history = [0.0]
        self.mp = [0.0]
        self.np = [0.0]
        self.pp = [0.0]
        self.t = [0.0]

        # The percentage of negative and positive ion channels open
        self.n = 0.0
        self.p = 0.0
        self.p_open = 0.0

        self.time_step = 0.1

    def state(self):
        return [self.t, self.neuron, self.resting_potential, self.threshold_potential, self.decay, self.axon, self.activation]

    def activate(self, input):
        # self.activation = (np.sum(self.axon * self.neuron, axis=0))
        self.activation += input
        self.activation_history.append(input)

    def step(self, input):
        self.activate(input)

        x = self.neuron

        # rate of positive ion channels opening or closing goes down when there is an input signal
        # Starts at 1, approaches 0 when an input is applied
        p_rate = 1 - (2 / (1 + np.exp(-1 * input)) - 1)
        # The number of positive ions added is the input - the rate of p_ion channels closing
        self.p += input - 0.1 * p_rate * self.p

        # Suppression of negative ion channels opening due to input
        s = 1 * np.exp(-0.01 * self.p ** 2)

        # rate of ion channels opening based on membrane potential
        n_open = 2 / (1 + np.exp(-1 * (x - self.resting_potential))) - 0.5

        self.n += s * n_open
        # n = -1 / (1 + np.exp(-1 * self.n)) + 0.5

        # print('n: ', self.n, '\np: ', self.p, '\na: ', a, '\n')

        self.neuron = -s * self.n

        self.mp.append(self.neuron)
        self.np.append(s)
        self.pp.append(self.n)
        self.t.append(self.t[-1] + self.time_step)

        return self.neuron
