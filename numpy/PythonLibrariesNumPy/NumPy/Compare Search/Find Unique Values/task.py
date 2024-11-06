import numpy as np
from numpy.ma.core import argmax

csv = np.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=np.int64)
data, labels =  csv[:, 1:], csv[:, 0]

classes = np.unique(labels)
unique_measurements, unique_data_counts = np.unique(data, return_counts=True)

most_frequent_index = argmax(unique_data_counts)
most_frequent_measurement = unique_measurements[most_frequent_index]

if __name__ == "__main__":
    print(data, '\n')
    print(labels, '\n')
    print(classes, '\n')
    print(unique_measurements, '\n')
    print(unique_data_counts, '\n')
    print(most_frequent_index, '\n')
    print(most_frequent_measurement)
