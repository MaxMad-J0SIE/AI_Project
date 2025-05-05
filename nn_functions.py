# from data_holder import  DataHolder
import random as rng
# dh = DataHolder()
# custom functions file with functions that I wrote for the project
class NN_functions:
    def __init__(self):
        self.output = 0

    # neuron function that is used to create neurons
    def neuron(self, inputs, weights, bias):
        self.output = 0
        for i in range(len(inputs)):
            self.output += inputs[i] * weights[i]
        return self.output + bias

    # function that is used to check if the output of the neural network is within the acceptable error
    def check_correction(self, output, answer_key, acceptable_error):
        if output - acceptable_error < answer_key < output + acceptable_error:
            return True
        else:
            return False

    # correction algorithm that is used to correct the weights and bias of the neural network
    def correction(self, output, answer_key, acceptable_error):
        pass