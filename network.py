import numpy as np
import random
import math


class Network:

    # @todo Redesign with Na/K pump and membrane potentials using cell size
    # @todo Design a function to build a network of any size with the proper connections
    def __init__(self, input_neurons=1, hidden_neurons=1, output_neurons=1, axon_density=0.2):
        np.random.seed(0)

        # Simulation Settings
        self.time_since_clean = 0.0
        self.timeStepSize = 0.1

        # Neuron Properties
        self.t = 0.0
        self.clean_time = 25.0
        self.membrane_potential = 0.0
        self.external_charge = 100.0
        self.flow = 0.0
        self.resting_potential = -60.0
        self.threshold_potential = -50.0
        self.return_rate = 0.0
        self.graded_potential = 2.0
        self.rest_proximity = 0.0

    def calculate_mp(self, input):
        # Model the flow of ions into or out of the neuron
        # A factor of how far below the resting potential the current membrane potential is
        self.rest_proximity = 2 / (1 + math.exp(-(self.membrane_potential - (self.resting_potential - 10)))) - 1

        # The natural return rate of the neuron
        self.return_rate = -(2 / (1 + math.exp(-(self.membrane_potential - self.resting_potential))) - 1)
        # self.return_rate = 1 - math.exp((-(self.membrane_potential - self.resting_potential) ** 2) / 10)

        # model the graded potentials affecting the neuron
        # Should be a number that slowly degrades back to zero but with a delay
        self.graded_potential = 0.5 * self.graded_potential + input

        self.flow = math.exp(-self.graded_potential / 20)
        self.membrane_potential += self.return_rate + self.rest_proximity * self.flow * self.graded_potential
        # print(self.membrane_potential)

    def step(self, input):
        # Increment Time step
        self.t += self.timeStepSize
        self.time_since_clean += self.timeStepSize

        # Model the ion levels
        self.calculate_mp(input)
