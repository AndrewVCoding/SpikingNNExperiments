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
        self.threshold_potential = 60.0

        # Generate the resting potential of each neuron
        # self.resting_potential = np.zeros(size, dtype=np.double)
        self.resting_potential = 5

        # Set the decay rate of each neuron
        self.decay = 0.5

        # self.axon = np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]])

        self.activation = 0.0
        # for x in range(0, 100):
        #     self.activation.append(np.zeros(size, dtype=np.double))

        self.history = [0.0]

        self.activation_history = [0.0]
        self.mp = [0.0]
        self.t = [0.0]

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

        # decay
        # The decay term to bring the potential back towards resting potential
        d = self.decay / (np.exp(0.1 * (x - (self.resting_potential))) + 1) - 0 / (
                np.exp(-1 * (x - (self.resting_potential))) + 1) - (self.decay / 2) - 40 / (
                    1 + np.exp(-10 * (x - self.threshold_potential)))

        # Apply the decay rate to the network potential
        s = x + d

        # Calculate the effect of the action potential based on the current potential
        # The resting term 1/(1+e^(-10x))
        p = 1 / (1 + np.exp(-10 * (x - self.resting_potential))) + 3 / (1 + np.exp(-10 * (x - self.threshold_potential))) - (
                    4 / (1 + np.exp(-10 * (x - self.threshold_potential * 1.05))))

        # Calculate the final potential of each neuron at this time step
        self.neuron = s + p * self.activation

        self.mp.append(s + p * self.activation)
        self.t.append(self.t[-1] + self.time_step)

        return self.neuron
