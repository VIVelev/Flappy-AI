import numpy as np
from .activations import relu, sigmoid

__all__ = [
    "Layer",
    "NeuralNetwork",
]

"""
My Layer Class
(layer for Neural Network)
"""
class Layer(object):
    def __init__(self, n_inputs, n_nodes):
        self.weights = np.random.randn(n_nodes, n_inputs)
        self.bias = np.random.randn(n_nodes)

"""
My Neural Network Class
"""
class NeuralNetwork(object):
    def __init__(self, n_hidden_layers=1, n_nodes=[6], n_inputs=2, n_classes=2):
        self.n_hidden_layers = n_hidden_layers
        self.n_nodes = n_nodes
        self.n_inputs = n_inputs
        self.n_classes = n_classes        

        self.hidden_layers = []
        if n_classes == 2:
            self.output_layer = Layer(n_nodes[-1], 1)
        else:
            self.output_layer = Layer(n_nodes[-1], n_classes)

        for i in range(n_hidden_layers):
            if i == 0:
                self.hidden_layers.append(Layer(n_inputs, n_nodes[i]))
            else:
                self.hidden_layers.append(Layer(n_nodes[i-1], n_nodes[i]))

    """
    Forward Propagation
    """
    def predict(self, x):
        output = np.matmul(self.hidden_layers[0].weights, np.transpose(x))
        output = np.add(np.transpose(output), self.hidden_layers[0].bias)
        output = relu(output)

        for layer in self.hidden_layers[1:]:
            output = np.matmul(layer.weights, np.transpose(output))
            output = np.add(np.transpose(output), layer.bias)
            output = relu(output)

        output = np.matmul(self.output_layer.weights, np.transpose(output))
        output = np.add(np.transpose(output), self.output_layer.bias)
        output = sigmoid(output)                    

        return output
