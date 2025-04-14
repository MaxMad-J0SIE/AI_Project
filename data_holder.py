import numpy as np
from custom_functions import CustomMethodes
cm = CustomMethodes()

class DataHolder:

    def __init__(self):

        self.table1 = np.array([
                1, 0, 0,
                1, 1, 1,
                0, 1, 1
            ])

        self.answer_key1 = np.array([0, 1, 1])

        self.table2 = np.array([
            1, 1, 0,
            1, 0, 1,
            0, 1, 1
            ])

        self.answer_key2 = np.array([0, 0, 0])

        self.weights1 = cm.fill_weights(3)
        self.weights2 = cm.fill_weights(3)
        self.weights3 = cm.fill_weights(3)
        self.output_weights = cm.fill_weights(3)
        self.output_weights2 = cm.fill_weights(3)

        self.bias = 0.5