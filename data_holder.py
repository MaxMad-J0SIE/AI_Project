import numpy as np
from custom_functions import CustomMethodes
arr = [10, 5, 2, 3, 1, 4, 6, 7, 8, 9]
cm = CustomMethodes()

class DataHolder:

    def __init__(self):

        self.table1 = np.array([
            [1, 0, 0],
            [1, 1, 1],
            [0, 1, 1]
            ])

        self.table2 = np.array([
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]
            ])

        self.weights1 = cm.fill_weights(3)
        self.weights2 = cm.fill_weights(3)
        self.weights3 = cm.fill_weights(3)
        self.output_weights = cm.fill_weights(3)
        self.output_weights2 = cm.fill_weights(3)

        self.bias = 0.5

    def prepare_values(self):
        self.weights1 = cm.fill_weights(3)
        self.weights2 = cm.fill_weights(3)
        self.weights3 = cm.fill_weights(3)
        self.output_weights = cm.fill_weights(3)
        self.output_weights2 = cm.fill_weights(3)

        return self.weights1, self.weights2, self.weights3, self.output_weights, self.output_weights2