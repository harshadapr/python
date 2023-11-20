import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

plt.plot(x_values, y_values, marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
