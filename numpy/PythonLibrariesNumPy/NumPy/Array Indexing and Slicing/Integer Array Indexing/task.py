import numpy as np

x = np.arange(35)
y = x.reshape(5, 7)

a = x[np.array([7, 13, 28, 33])]
b = np.array([0, 1, 2, 10, 11, 12, 28, 29, 30]).reshape(3, 3)

c = y[np.array([0, 2, 4])]  # TODO: use a 1-D numpy array for indexing
d = y[np.array([0, 2, 4]), np.array([0, 1, 2])]  # TODO: use two 1-D arrays for indexing
e = y[np.array([1,2,4]), 6]  # TODO: use a 1-D numpy array and a scalar for indexing


if __name__ == '__main__':
    print(y)
    print('\n', a.shape)
    print('\n', b.shape)
    print('\n', c.shape)
    print('\n', d.shape)
    print('\n', e.shape)
