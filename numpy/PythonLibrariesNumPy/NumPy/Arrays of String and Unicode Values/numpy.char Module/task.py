import numpy as np


def read_data(file):
    text = np.genfromtxt(file, delimiter='\n', dtype=np.bytes_)
    return np.char.decode(text, encoding='utf-8')


if __name__ == '__main__':
    X = read_data('text.txt')
    print(X)
    # This should NOT be a numpy.ndarray:
    print(type(X[0]))
