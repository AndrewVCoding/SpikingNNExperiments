import numpy as np
import random
import math


class Network:

    # @todo Redesign with Na/K pump and membrane potentials using cell size
    # @todo Design a function to build a network of any size with the proper connections
    def __init__(self, input_neurons=1, hidden_neurons=1, output_neurons=1, axon_density=0.2):
        np.random.seed(0)

        self.t = 0
        self.Na = 50
        self.NaGates = 0.0
        self.K = 50
        self.KGates = 0.0
        self.resting_potential = -60.0
        self.graded_potentials = [[0, 0, 0]]
        self.neuron = 0

    def graded_potential(self, magnitude, width, position, x):
        p = (magnitude / (math.pow(2*math.pi, 0.5))) * math.exp(-(1 / 2) * math.pow((x - position) / width, 2))
        return p

    def pump(self):
        voltage = (self.Na + self.K)

    def state(self):
        return self.t, self.neuron, self.Na, self.NaGates, self.K, self.KGates, self.resting_potential

    def step(self, input, t):
        self.t = t
        self.graded_potentials[:, 2] += t
        self.graded_potentials.append(input)

        return self.state()

