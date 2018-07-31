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
        self.mp = 0.0

        # Input signals to the neuron
        self.graded_potentials = []

        # Chemical Values
        # Organic Anions are created inside the neuron
        self.OA = 0.0
        self.OA_max = 5.0
        self.K = 0.0
        self.NA = 0.0
        self.CL = 0.0
        self.CA = 0.0

        # Diffusion Force Values
        self.OA_diffuse = -1.0
        self.K_diffuse = 1.0
        self.NA_diffuse = 1.0
        self.CL_diffuse = 1.0
        self.CA_diffuse = 1.0

        # Electrical force values
        self.OA_electric = -1.0
        self.K_electric = -1.0
        self.NA_electric = 1.0
        self.CL_electric = -1.0
        self.CA_electric = 1.0

        # Chemical Gate Values
        self.OA_pass = 0.0
        self.K_leak = 0.2
        self.NA_leak = 0.2
        self.resting_potential = -60.0

    def clean_up(self):
        # Get rid of useless elements
        self.graded_potentials = [gp for gp in self.graded_potentials if gp[1] < 110.0 and abs(gp[0]) > 0.01]

    def generate_oa(self):
        self.OA += -0.1 * (self.OA - 5.0)

    def membrane_potential(self):
        self.mp = -80 + (self.OA + self.K + self.NA)

    def NaK_pump(self):
        """
        3 Na out for 2 K in
        :return:
        """
        strength = 0.1
        # strength = 0.9 * (self.mp - self.resting_potential)
        self.NA -= 3 * strength
        self.K += 2 * strength

    def ClK_pump(self):
        """
        1 Cl out and 1 K out
        :return:
        """
        strength = 0.01
        self.CL -= 1 * strength
        self.K -= 1 * strength

    def CaNa_pump(self):
        """
        1 Ca out for 1 Na in
        :return:
        """
        strength = 0.01
        self.CA -= 1 * strength
        self.NA += 1 * strength

    def model_diffusion_force(self):
        """
        Negative values represent a force pushing ions out of the neuron
        Positive values represent a force pushing ions into the neuron

        OA should be negative
        NA should be positive at rest
        K+ should be positive at rest, and should then match the electrical force
        Cl should be positive at rest
        Ca
        :return:
        """
        self.OA_diffuse = -0.1 * self.OA
        self.NA_diffuse = -0.1 * self.NA
        self.K_diffuse = -0.1 * self.K
        self.CL_diffuse = -0.1 * self.CL
        self.CA_diffuse = -0.1 * self.CA

    def model_electrical_force(self):
        """
        Negative values represent a force pushing ions out of the neuron
        Positive values represent a force pushing ions into the neuron

        :return:
        """
        self.OA_electric = 2 / (1 + math.exp(-0.1 * self.mp))
        self.NA_electric = -2 / (1 + math.exp(-0.1 * self.mp))
        self.K_electric = -0.1 * self.mp
        self.CL_electric = 2 / (1 + math.exp(-0.1 * self.mp))
        self.CA_electric = -2 / (1 + math.exp(-0.1 * self.mp))

    def leak(self):
        rate = 0.1
        self.OA += self.OA_pass * (self.OA_diffuse + self.OA_electric)
        self.K += rate * (self.K_diffuse + self.K_electric)
        self.NA += rate * (self.NA_diffuse + self.NA_electric)
        self.CL += rate * (self.CL_diffuse + self.CL_electric)
        self.CA += rate * (self.CA_diffuse + self.CA_electric)

    def step(self, input):
        # Increment Time step
        self.t += self.timeStepSize
        self.time_since_clean += self.timeStepSize

        # Model the chemical levels
        self.model_diffusion_force()
        self.model_electrical_force()
        self.leak()
        self.generate_oa()
        # self.NaK_pump()
        self.membrane_potential()

        self.mp += input
