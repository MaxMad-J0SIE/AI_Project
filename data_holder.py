import numpy as np
from custom_functions import CustomMethodes
cm = CustomMethodes()

class DataHolder:

    def __init__(self):

        self.table1 = np.array([
                0, 0, 0, 1, 0,
                0, 0, 1, 1, 0,
                0, 0, 0, 1, 0,
                0, 0, 0, 1, 0,
                0, 0, 0, 0, 0,
            ])

        self.answer_key1 = 1

        self.table2 = np.array([
                0, 1, 1, 0, 0,
                0, 0, 0, 1, 0,
                0, 0, 1, 0, 0,
                0, 1, 1, 1, 0,
                0, 0, 0, 0, 0,
            ])

        self.answer_key2 = 2

        self.weights1 = cm.fill_weights(len(self.table1))
        self.weights2 = cm.fill_weights(len(self.table1))
        self.weights3 = cm.fill_weights(len(self.table1))
        self.weights4 = cm.fill_weights(len(self.table1))
        self.weights5 = cm.fill_weights(len(self.table1))
        self.weights6 = cm.fill_weights(len(self.table1))
        self.output_weights = cm.fill_weights(6)

        self.bias = 0.5

        self.acceptable_error = 0.4