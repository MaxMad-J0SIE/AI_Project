# from data_holder import  DataHolder
import random as rng
# dh = DataHolder()

class NN_functions:
    def __init__(self):
        self.output = 0

    def neuron(self, inputs, weights, bias):
        self.output = 0
        for i in range(len(inputs)):
            self.output += inputs[i] * weights[i]
        return self.output + bias

    def check_correction(self, output, answer_key, acceptable_error):
        if output - acceptable_error < answer_key < output + acceptable_error:
            return True
        else:
            return False

    def correction(self, output, answer_key, acceptable_error):
