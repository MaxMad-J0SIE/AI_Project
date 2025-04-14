from custom_functions import CustomMethodes
from data_holder import DataHolder

dh = DataHolder()
cm = CustomMethodes()


class Main:
    def __init__(self):
        self.inputs = dh.table1

        self.output_weights = None
        self.output_weights2 = None

        self.bias = dh.bias

        self.answer_key = dh.answer_key1
        self.Training = True
        self.i = 1
        while self.Training:
            print(f"\n\nIteration {self.i}\n\n")
            outputs = self.neural_network()
            if cm.check_correct(outputs, self.answer_key, dh.acceptable_error):
                print("Training complete")
                self.Training = False
            else:
                self.i += 1

    def neural_network(self):
        print("Function call")
        holder = cm.prepare_values()
        self.output_weights = holder[0]
        self.output_weights2 = holder[1]

        # Hidden layer
        neuron1 = cm.neuron(self.inputs, cm.fill_weights(9))
        print(f"Neuron 1 {neuron1}")
        neuron2 = cm.neuron(self.inputs, cm.fill_weights(9))
        print(f"Neuron 2 {neuron2}")
        neuron3 = cm.neuron(self.inputs, cm.fill_weights(9))
        print(f"Neuron 3 {neuron3}")
        neuron4 = cm.neuron(self.inputs, cm.fill_weights(9))
        print(f"Neuron 4 {neuron4}")
        neuron5 = cm.neuron(self.inputs, cm.fill_weights(9))
        print(f"Neuron 5 {neuron5}")
        neuron6 = cm.neuron(self.inputs, cm.fill_weights(9))
        print(f"Neuron 6 {neuron6}")

        # Output layer
        vertical_output = cm.neuron([neuron1, neuron2, neuron3, neuron4, neuron5, neuron6], self.output_weights)
        print(f"Vertical output {vertical_output}")
        horizontal_output = cm.neuron([neuron1, neuron2, neuron3, neuron4, neuron5, neuron6], self.output_weights2)
        print(f"Horizontal output {horizontal_output}")
        diagonal_output = cm.neuron([neuron1, neuron2, neuron3, neuron4, neuron5, neuron6], self.output_weights2)
        print(f"Diagonal output {diagonal_output}")
        return vertical_output, horizontal_output, diagonal_output


main = Main()