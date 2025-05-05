from data_holder import DataHolder
from nn_functions import NN_functions
dh = DataHolder()
nn = NN_functions()

class Controler:
    def __init__(self):
        self.neuron1_1 = None
        self.neuron1_2 = None
        self.neuron1_3 = None
        self.neuron1_4 = None
        self.neuron1_5 = None
        self.neuron1_6 = None
        self.neuron2_1 = None
        self.neuron2_2 = None
        self.neuron2_3 = None
        self.output_neuron = None
        self.nn_output = self.neural_network_control()
        if(nn.check_correction()):
            print("Correct")
            print(f"w1\\n{dh.weights1_1}\n"
                  f"w2\\n{dh.weights1_2}\n"
                  f"w3\\n{dh.weights1_3}\n"
                  f"w4\\n{dh.weights1_4}\n"
                  f"w5\\n{dh.weights1_5}\n"
                  f"w6\\n{dh.weights1_6}\n"
                  f"w2.1\\n{dh.weights2_1}\n"
                  f"w2.2\\n{dh.weights2_2}\n"
                  f"w2.3\\n{dh.weights2_3}\n"
                  f"wo\\n{dh.output_weights}\n")

    def neural_network_control(self):
        #hidden layer 1
        self.neuron1_1 = nn.neuron(dh.table1, dh.weights1_1, dh.bias)
        self.neuron1_2 = nn.neuron(dh.table1, dh.weights1_2, dh.bias)
        self.neuron1_3 = nn.neuron(dh.table1, dh.weights1_3, dh.bias)
        self.neuron1_4 = nn.neuron(dh.table1, dh.weights1_4, dh.bias)
        self.neuron1_5 = nn.neuron(dh.table1, dh.weights1_5, dh.bias)
        self.neuron1_6 = nn.neuron(dh.table1, dh.weights1_6, dh.bias)
        #hidden layer 2
        self.neuron2_1 = nn.neuron([self.neuron1_1, self.neuron1_2, self.neuron1_3, self.neuron1_4, self.neuron1_5, self.neuron1_6], dh.weights2_1, dh.bias)
        self.neuron2_2 = nn.neuron([self.neuron1_1, self.neuron1_2, self.neuron1_3, self.neuron1_4, self.neuron1_5, self.neuron1_6], dh.weights2_2, dh.bias)
        self.neuron2_3 = nn.neuron([self.neuron1_1, self.neuron1_2, self.neuron1_3, self.neuron1_4, self.neuron1_5, self.neuron1_6], dh.weights2_3, dh.bias)
        #output layer
        self.output_neuron = nn.neuron([self.neuron2_1, self.neuron2_2, self.neuron2_3], dh.output_weights, dh.bias)
        return self.output_neuron