import numpy as np
import random
import math


class Network:

    def __init__(self, input_neurons=2, hidden_neurons=1, output_neurons=1, axon_density=0.2):
        self.input_neurons = input_neurons
        self.hidden_neurons = hidden_neurons
        self.output_neurons = output_neurons

        size = input_neurons + hidden_neurons + output_neurons

        self.neuron = np.zeros(size, dtype=np.double)

        self.threshold = np.zeros(size, dtype=np.double) + 20.0

        self.resting_potential = np.zeros(size, dtype=np.double)

        self.axon = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0]])

        self.activation = np.zeros(size, dtype=np.double)

        self.state = np.array([self.neuron, self.threshold, self.resting_potential, self.activation])

        self.history = [0.0]

        self.return_rates = 1.1

    def activate(self, input):
        self.activation[:] = np.sum(self.axon * self.neuron, axis=1) + input
        print(self.activation)

    def step(self, input):
        self.activate(input)

        x = self.neuron

        # decay
        # The decay term to bring the potential back towards 0.0
        d = 0.5 / np.exp(10 * np.power(x - self.resting_potential, 2) / 1000)

        # The action potential fire term to reduce the potential back towards rest
        f = 1.1 / (np.exp(50 * (x - self.threshold - 1.0)) + 1.0) - 0.6

        # Apply the decay rate to the network potential
        s = (f + d) * x

        # Calculate the effect of the action potential based on the current potential
        # The resting term 1/(1+e^(-10x))
        r = 1.0 / (1.0 + np.exp(-10.0 * (s + 0.0)))

        # The threshold term 2/(1+e^(-10x + 190))
        n = 1.0 / (1.0 + np.exp(-1.0 * (s - 22.0)))

        self.neuron = s + (n + r) * self.activation
        self.state = np.array([self.neuron, self.threshold, self.resting_potential, self.activation])
        self.history.append(self.neuron[-1])
