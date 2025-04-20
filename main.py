from custom_functions import CustomMethodes
from data_holder import DataHolder

dh = DataHolder()
cm = CustomMethodes()


class Main:
    def __init__(self):
        self.inputs = dh.table1

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
        neuron1 = cm.neuron(self.inputs, dh.weights1)
        print(f"Neuron 1 {neuron1}")
        neuron2 = cm.neuron(self.inputs, dh.weights2)
        print(f"Neuron 2 {neuron2}")
        neuron3 = cm.neuron(self.inputs, dh.weights3)
        print(f"Neuron 3 {neuron3}")
        neuron4 = cm.neuron(self.inputs, dh.weights4)
        print(f"Neuron 4 {neuron4}")
        neuron5 = cm.neuron(self.inputs, dh.weights5)
        print(f"Neuron 5 {neuron5}")
        neuron6 = cm.neuron(self.inputs, dh.weights6)
        print(f"Neuron 6 {neuron6}")

        # Output layer
        vertical_output = cm.neuron([neuron1, neuron2, neuron3, neuron4, neuron5, neuron6], dh.output_weights)
        print(f"Vertical output {vertical_output}")
        horizontal_output = cm.neuron([neuron1, neuron2, neuron3, neuron4, neuron5, neuron6], dh.output_weights2)
        print(f"Horizontal output {horizontal_output}")
        diagonal_output = cm.neuron([neuron1, neuron2, neuron3, neuron4, neuron5, neuron6], dh.output_weights3)
        print(f"Diagonal output {diagonal_output}")
        return vertical_output, horizontal_output, diagonal_output


main = Main()