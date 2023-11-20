from sklearn.linear_model import LinearRegression
import numpy as np

# Generate random data for demonstration
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
new_data_point = np.array([[2.5]])
predicted_value = model.predict(new_data_point)
print(f"Predicted value for {new_data_point[0][0]} is: {predicted_value[0][0]}")
