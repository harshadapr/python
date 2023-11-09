import numpy as np

data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print(f"Data: {data}")
print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev:.2f}")
