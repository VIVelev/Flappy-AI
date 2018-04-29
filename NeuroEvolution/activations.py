from math import exp

__all__ = [
    "sigmoid",
    "relu",
]

def sigmoid(x):
    for i in range(len(x)):
        try:
            x[i] = 1 / (1 + exp(-x[i]))
        except OverflowError:
            x[i] = 1.00

    return x

def relu(x):
    for i in range(len(x)):
        x[i] = max(0, x[i])

    return x
