import numpy as np


def step_function(x):
    y = x > 0
    return y.astype(int)


x = np.array([-0.1, 1.0, -2.0])
print(x)
