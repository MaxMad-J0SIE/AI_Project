from custom_functions import CustomMethodes
from data_holder import DataHolder

dh = DataHolder()
cm = CustomMethodes()


class Main:
    def __init__(self):
        self.inputs = dh.table1

        self.weights1 = dh.weights1
        self.weights2 = dh.weights2
        self.weights3 = dh.weights3
        self.weights4 = dh.weights4
        self.weights5 = dh.weights5
        self.weights6 = dh.weights6
        self.output_weights = dh.output_weights

        self.bias = dh.bias

        self.Training = True
        self.i = 1
        while self.Training:
            print(f"\n\nIteration {self.i}\n\n")
            outputs = self.neural_network()
            if cm.check_correct(outputs, dh.answer_key1, dh.acceptable_error):
                print("Training complete")
                self.Training = False
            else:
                cm.correction_algorithm(outputs, dh.answer_key1)
                self.i += 1

    def neural_network(self):
        print("Function call")

        # Hidden layer
        neuron1 = cm.neuron(self.inputs, self.weights1)
        print(f"Neuron 1 {neuron1}")
        neuron2 = cm.neuron(self.inputs, self.weights2)
        print(f"Neuron 2 {neuron2}")
        neuron3 = cm.neuron(self.inputs, self.weights3)
        print(f"Neuron 3 {neuron3}")
        neuron4 = cm.neuron(self.inputs, self.weights4)
        print(f"Neuron 4 {neuron4}")
        neuron5 = cm.neuron(self.inputs, self.weights5)
        print(f"Neuron 5 {neuron5}")
        neuron6 = cm.neuron(self.inputs, self.weights6)
        print(f"Neuron 6 {neuron6}")

        # Output layer
        output_neuron = cm.neuron([neuron1, neuron2, neuron3, neuron4, neuron5, neuron6], self.output_weights)
        print(f"Output Neuron {output_neuron}")
        return output_neuron


main = Main()