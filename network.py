import numpy as np
import random
import math

class Network:

    def __init__(self, history):
        np.random.seed(2)

        self.history = history

        self.time = 0.0
        self.resting_potential = -70.0
        self.membrane_potential = 0.0
        self.positive_ions = 0.0
        self.negative_ions = 0.0
        self.positive_channels_in = 0.0
        self.positive_channels_out = 0.0
        self.negative_channels_in = 0.0
        self.negative_channels_out = 0.0
        self.positive_rate_in = 1 - (1 / (1 + np.exp(-0.1 * (self.positive_channels_in - 30))))
        self.positive_rate_out = 1 - (1 / (1 + np.exp(-0.1 * (self.positive_channels_out - 30))))
        self.negative_rate_in = 1 - (1 / (1 + np.exp(-0.1 * (self.negative_channels_in - 30))))
        self.negative_rate_out = 1 - (1 / (1 + np.exp(-0.1 * (self.negative_channels_out - 30))))

        # Passive ion channels
        self.positive_channels = 1 - 2 / (1 + np.exp(-0.1 * self.membrane_potential))
        self.negative_channels = 2 - 4 / (1 + np.exp(0.1 * self.membrane_potential))

        # Exchange channels
        self.exchange = -2.0 * (1 - 2 / (1 + np.exp(-0.1 * (self.membrane_potential - self.resting_potential)))) * (
                1 / (1 + np.exp(-100 * (self.membrane_potential - self.resting_potential))))

        self.record()

    def step(self, input):
        self.time += 1.0

        if 200 < self.time < 220:
            self.positive_ions += 1.0

        # account for electrostatic pressure inside the neuron
        self.positive_channels = 1 - 2 / (1 + np.exp(-0.005 * self.membrane_potential))
        self.negative_channels = 1 - 2 / (1 + np.exp(0.005 * self.membrane_potential))

        # set the strength of the positive-negative ion exchange pump
        self.exchange = -(1 - 2 / (1 + np.exp(-0.1 * (self.membrane_potential - self.resting_potential)))) * (
                1 / (1 + np.exp(-100 * (self.membrane_potential - self.resting_potential))))

        self.positive_ions += self.positive_channels + self.exchange * (0.99 - 2/(1 + np.exp(-1 * self.positive_ions)))

        self.negative_ions += self.negative_channels - self.exchange * (0.99 - 2/(1 + np.exp(-1 * self.negative_ions)))

        self.membrane_potential = self.positive_ions - self.negative_ions

        self.record()

    def record(self):
        self.history.time.append(self.time)
        self.history.membrane_potential.append(self.membrane_potential)
        self.history.positive_ions.append(self.positive_ions)
        self.history.positive_rate_in.append(self.positive_rate_in)
        self.history.positive_rate_out.append(self.positive_rate_out)
        self.history.positive_in.append(self.positive_channels_in)
        self.history.positive_out.append(self.positive_channels_out)
        self.history.negative_ions.append(self.negative_ions)
        self.history.negative_rate_in.append(self.negative_rate_in)
        self.history.negative_rate_out.append(self.negative_rate_out)
        self.history.negative_in.append(self.negative_channels_in)
        self.history.negative_out.append(self.negative_channels_out)
        self.history.positive_channels.append(self.positive_channels)
        self.history.negative_channels.append(self.negative_channels)
        self.history.exchange.append(self.exchange)


class History:

    def __init__(self):
        self.time = []
        self.membrane_potential = []
        self.positive_ions = []
        self.negative_ions = []
        self.positive_rate_in = []
        self.positive_rate_out = []
        self.negative_rate_in = []
        self.negative_rate_out = []
        self.positive_in = []
        self.positive_out = []
        self.negative_in = []
        self.negative_out = []
        self.positive_channels = []
        self.negative_channels = []
        self.exchange = []
