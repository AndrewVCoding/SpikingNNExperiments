import numpy as np
import random
import math


class Network:

    # @todo Redesign with Na/K pump and membrane potentials using cell size
    # @todo Design a function to build a network of any size with the proper connections
    def __init__(self, input_neurons=1, hidden_neurons=1, output_neurons=1, axon_density=0.2):
        np.random.seed(0)

        self.t = 0
        self.graded_potentials = []
        self.length = np.linspace(0, 100, 1000)

        self.Na = 50
        self.NaGates = 0.0
        self.K = 50
        self.KGates = 0.0
        self.resting_potential = -60.0
        self.neuron = 0
        self.timeStepSize = 1.0

    def graded_potential(self, magnitude=1.0, width=1.0, position=0.0, x=0.0):
        gp = (2.5 * magnitude / (math.pow(2*math.pi, 0.5))) * math.exp(-(1 / 2) * math.pow((x - position) / width, 2))
        return gp

    def graded_sum(self, p):
        s = 0.0
        for gp in self.graded_potentials:
            s += self.graded_potential(magnitude=gp[0], position=gp[1], x=p)

        return s

    def graph(self):
        graph = []

        for p in self.length:
            graph.append(self.graded_sum(p=p))

        return graph

    def pump(self):
        voltage = 0.1 * (self.Na + self.K)

    def state(self):
        return self.t, self.neuron, self.Na, self.NaGates, self.K, self.KGates, self.resting_potential

    def step(self):
        self.t += self.timeStepSize
        for gp in self.graded_potentials:
            gp[0] = gp[0] * 0.95
            gp[1] += self.timeStepSize

