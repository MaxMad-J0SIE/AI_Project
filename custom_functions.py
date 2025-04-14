import numpy as np


class CustomMethodes:

    def __init__(self):
        self.left = []
        self.right = []
        self.pivot = None

    def sorter(self, arr):
        if len(arr) <= 1:
            return arr
        self.pivot = arr[len(arr) // 2]
        self.left = [x for x in arr if x < self.pivot]
        self.right = [x for x in arr if x > self.pivot]
        return self.sorter(self.left) + [self.pivot] + self.sorter(self.right)

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

        return output_weights, output_weights2