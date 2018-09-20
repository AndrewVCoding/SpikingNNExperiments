import numpy as np
import random
import math


class Netowrk:
    def __init__(self, input_neurons=10, hidden_neurons=20, output_neurons=10, axon_density=0.2):
        self.input_neurons = input_neurons
        self.hidden_neurons = hidden_neurons
        self.output_neurons = output_neurons
        self.neuron = np.zeros(input_neurons + hidden_neurons + output_neurons) - 2.0
        self.threshold = 20.0
        self.resting_potential = 0.0
        self.activation = self.neuron.copy()
        self.state = np.array([self.neuron, self.threshold, self.resting_potential, self.activation])
        self.history = [0.0]
        self.return_rates = 1.1

    def activate(self, activation):
        self.neuron[0, :] = activation

    def step(self, activation):
        x = self.neuron
        # decay
        # The decay term to bring the potential back towards 0.0
        # Need to only use this rapid decay rate following an action potential, otherwise use a slower one.
        #@todo
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
        self.neuron = s + (n + r) * activation
        self.state = np.array([self.neuron, self.threshold, self.resting_potential, self.activation])
        self.history.append(self.neuron[0])
