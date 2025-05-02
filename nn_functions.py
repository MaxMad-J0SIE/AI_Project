from data_holder import  DataHolder
import random as rng
dh = DataHolder()

class NN_functions:
    def __init__(self):
        self.output = 0

    def neuron(self, inputs, weights):
        self.output = 0
        for i in range(len(inputs)):
            self.output += inputs[i] * weights[i]