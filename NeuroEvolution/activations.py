from math import exp

__all__ = [
    "sigmoid",
    "relu",
]

def sigmoid(x):
    for i in range(len(x)):
       x[i] = 1 / (1 + exp(-x[i]))

    return x

def relu(x):
    for i in range(len(x)):
       x[i] = max(0, x[i])

    return x
