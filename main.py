from custom_functions import CustomMethodes
from data_holder import DataHolder

dh = DataHolder()
cm = CustomMethodes()

class Main:
    def __init__(self):
        self.inputs1 = dh.table1[0, :3]
        self.inputs2 = dh.table1[1, :3]
        self.inputs3 = dh.table1[2, :3]

        self.weights1 = dh.weights1
        self.weights2 = dh.weights2
        self.weights3 = dh.weights3
        self.output_weights = dh.output_weights
        self.output_weights2 = dh.output_weights2

        self.bias = dh.bias
        self.neural_network()
    def neural_network(self):
        print("Function call")
        # Hidden layer
        neuron1 = cm.neuron(self.inputs1, self.weights1, self.bias)
        neuron2 = cm.neuron(self.inputs2, self.weights2, self.bias)
        neuron3 = cm.neuron(self.inputs3, self.weights3, self.bias)

        # Output layer
        output1 = cm.neuron([neuron1, neuron2, neuron3], self.output_weights, self.bias)
        output2 = cm.neuron([neuron1, neuron2, neuron3], self.output_weights2, self.bias)

        print(f"Output 1: {output1}")
        print(f"Output 2: {output2}")

main = Main()