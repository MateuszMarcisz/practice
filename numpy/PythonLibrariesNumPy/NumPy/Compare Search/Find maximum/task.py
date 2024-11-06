import numpy as np

data = np.loadtxt('data.csv', delimiter=',', dtype=np.int64)
maxima = np.argmax(data, axis=1)  # Find indices of maximum values in each row
# result = data[np.arange(data.shape[0]), maxima]  # Extract the maximum elements from each row
result = np.take_along_axis(data, maxima.reshape(-1, 1), axis=1)

if __name__ == '__main__':
    print(f'{data}\n')
    print(f'{maxima}\n')
    print(result)
