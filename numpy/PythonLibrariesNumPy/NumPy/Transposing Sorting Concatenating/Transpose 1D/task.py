import numpy as np


def reshape_transpose(start, stop, step=1):
    # Create a 1D array using arange function
    # Reshape the 1D array so that you can transpose it
    array = np.arange(start, stop, step)
    return array.reshape(1, array.shape[0]).transpose()
# return np.array(start,stop,step).reshape(-1,1)


if __name__ == '__main__':
    print(reshape_transpose(1, 100, 10))
    print(reshape_transpose(0, 5))
