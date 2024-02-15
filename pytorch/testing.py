import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# Sample data
x = np.linspace(0, 5, 100)
y = 2 * x + 1 + np.random.normal(0, 1, size=len(x))  # Adding some noise to the data

# Convert data to PyTorch tensors
x_tensor = torch.FloatTensor(x.reshape(-1, 1))
y_tensor = torch.FloatTensor(y.reshape(-1, 1))

# Define a simple linear regression model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

# Instantiate the model
model = LinearRegressionModel()

# Check if the model has parameters
if list(model.parameters()):
    # Define the loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Training the model
    num_epochs = 1000
    for epoch in range(num_epochs):
        # Forward pass
        y_pred = model(x_tensor)

        # Compute the loss
        loss = criterion(y_pred, y_tensor)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Make predictions using the trained model
    with torch.no_grad():
        predicted_tensor = model(x_tensor)

    # Convert the predicted values back to NumPy array
    predicted = predicted_tensor.numpy()

    # Create a linear plot with the original and predicted data
    plt.plot(x, y, label='Original Data', color='blue', marker='o', linestyle='', markersize=5)
    plt.plot(x, predicted, label='Predicted Data', color='red', linewidth=2)

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Linear Regression Example')

    # Add a legend
    plt.legend()

    # Customize the appearance
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xticks(np.arange(0, 6, 1))
    plt.yticks(np.arange(0, 15, 1))



    # Show the plot
    plt.show()
else:
    print("Model has no parameters.")