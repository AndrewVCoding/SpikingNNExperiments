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
        self.neuron = -20.0

        # Generate the resting potential of each neuron
        # self.resting_potential = np.zeros(size, dtype=np.double)
        self.resting_potential = -20.0

        self.history = [0.0]

        self.activation_history = [0.0]
        self.mp = [self.neuron]
        self.np = [0.0]
        self.pp = [0.0]
        self.t = [0.0]
        self.ap = 9.0

        # The percentage of negative and positive ion channels open
        self.n = 31.0
        self.p = 0.0
        self.p_open = 0.0

        self.time_step = 0.1

    def step(self, input):
        # Threshold equations
        # tp is 1 when neuron potential is close to zero
        tp = 5 * np.exp(-0.5 * self.neuron ** 2)
        # rr is 1 when neuron potential is above threshold
        rr = 1 / (1 + np.exp(-1000 * self.neuron))

        # Scale the input voltage down if the neuron's voltage is below the neuron's resting potential to simulate a
        # refractory period
        input = (1 - rr) * input / (1 + np.exp(-100 * (self.neuron - self.resting_potential)))
        self.activation_history.append(input)

        x = self.neuron

        # rate of positive ion channels opening or closing goes down when there is an input signal
        # Starts at 1, approaches 0 when an input is applied
        # Is also given a boost when threshold potential is reached
        p_rate = 1 - (2 / (1 + np.exp(-1 * input)) - 1)
        # The number of positive ions added is the input - the rate of p_ion channels closing
        self.p += input - 0.2 * p_rate * self.p

        # Suppression of negative ion channels opening due to input
        s = np.exp(-50 * self.p ** 2)

        # rate of ion channels opening based on membrane potential
        n_open = 2 / (1 + np.exp(-1 * (x - self.resting_potential))) - 1.0 + 60 * rr

        self.n += s * n_open

        self.neuron = -s * self.n + tp * self.ap

        self.mp.append(self.neuron)
        self.np.append(n_open)
        self.pp.append(self.n)
        self.t.append(self.t[-1] + self.time_step)

        return self.neuron
