import numpy as np
#some shit didn't work
# old custom functions to throw out

class CustomMethodes:

    def __init__(self):
        self.left = []
        self.right = []
        self.pivot = None
        self.hidden_layer_outputs = []

    def sorter(self, arr):
        if len(arr) <= 1:
            return arr
        self.pivot = arr[len(arr) // 2]
        self.left = [x for x in arr if x < self.pivot]
        self.right = [x for x in arr if x > self.pivot]
        return self.sorter(self.left) + [self.pivot] + self.sorter(self.right)

    def neural_network(self, layers_in_hidden, number_of_neurons_in_hidden, number_of_neurons_in_output):
        #hidden layer
        for i in range(layers_in_hidden):
            for j in range(number_of_neurons_in_hidden):
                pass

    def neuron(self, inputs, weights):
        output = 0
        for i in range(len(inputs)):
            print(f"Weight: {weights[i]}")
            output += inputs[i] * weights[i]
        bias = np.random.uniform(-1, 1)
        print(f"Bias: {bias}")
        return output + bias

    def fill_weights(self, length):
        weights = np.zeros(length)
        for i in range(length):
            weights[i] = np.random.uniform(-1, 1)
        return weights

    def prepare_values(self):
        output_weights = self.fill_weights(6)
        output_weights2 = self.fill_weights(6)
        output_weights3 = self.fill_weights(6)

        return output_weights, output_weights2, output_weights3

    def correction_algorithm(self, output, answer_key):
        from data_holder import DataHolder
        dh = DataHolder()

        # What the dog doing
        #Dog:

        if output[0] > answer_key[0]:
            for i in range(len(dh.output_weights)):
                dh.output_weights[i] += (output[0] - answer_key[0]) / 100
        if output[1] > answer_key[1]:
            for i in range(len(dh.output_weights2)):
                dh.output_weights2[i] += (output[1] - answer_key[1]) / 100
        if output[2] > answer_key[2]:
            for i in range(len(dh.output_weights3)):
                dh.output_weights3[i] += (output[2] - answer_key[2]) / 100

        modulator = ((output[0] - answer_key[0]) / 100 + (output[1] - answer_key[1]) / 100 + (
                    output[2] - answer_key[2]) / 100) / 3

        # This part needs to be corrected
        # Random values are shit
        # THey need to be calculated
        for i in range(len(dh.weights1)):
            dh.weights1 += modulator
            dh.weights2 += modulator
            dh.weights3 += modulator
            dh.weights4 + modulator
            dh.weights5 += modulator
            dh.weights6 += modulator

    def check_correct(self, output, answer_key, acceptable_error):
        if output - acceptable_error < answer_key < output + acceptable_error:
            return True
        else:
            return False
