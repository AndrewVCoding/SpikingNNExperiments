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
        self.neuron = -10.0

        # Generate the threshold for each neuron
        # self.threshold = np.zeros(size, dtype=np.double) + 20.0
        self.threshold_potential = 20

        # Generate the resting potential of each neuron
        # self.resting_potential = np.zeros(size, dtype=np.double)
        self.resting_potential = -20.0

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

        # Leakage of voltage into the cell brings the voltage to zero
        leak = -0.01 * (x + 5)

        # Absolute proximity of membrane potential to the resting potential
        prox_abs = 1 - np.exp(-0.01 * (x-self.resting_potential) ** 4)

        # distance of membrane potential from the resting potential as a sigmoid function
        dist = 2 / (1 + np.exp(-0.1 * (x - self.resting_potential))) - 1

        # rate of ion channels opening based on membrane potential
        n_open = -1 / (1 + np.exp(-1 * (x - self.resting_potential)))

        self.n += n_open
        # n = -1 / (1 + np.exp(-1 * self.n)) + 0.5

        # self.p += 0.5 * (-1 / (1 + np.exp(-0.1 * (x - self.resting_potential))))
        p = -0.0 * (x - self.resting_potential)
        self.n += p


        # Test values
        # n = 0.0
        # p = 0.0

        a = input / (1 + np.exp(-(x - self.resting_potential)))

        # print('n: ', self.n, '\np: ', self.p, '\na: ', a, '\n')

        self.neuron += n_open + leak + a

        self.mp.append(self.neuron)
        self.np.append(self.n)
        self.pp.append(n_open)
        self.t.append(self.t[-1] + self.time_step)

        return self.neuron
