# Linear Regression
Linear Regression is a fundamental technique in statistics and machine learning used to understand the relationship between a dependent
variable (target) and one or more independent variables (features).

## Use Case
Linear regression is commonly used in various fields for prediction and forecasting tasks. For instance, let's say we want to predict the 
price of a house based on its size (in square feet). Here, the price of the house is the dependent variable, and the size of the house is the independent variable.

## Creating the Model:
To create a linear regression model:

1. Define the Problem: We want to predict house prices (Price) based on house sizes (Size).

2. Split Data: Split the dataset into a training set (used to train the model) and a test set (used to evaluate the model's performance).

3. Choose Model: Select linear regression as the algorithm to model the relationship between Size and Price.

4. Train the Model: Fit the model to the training data. This involves finding the best-fitting line (in this case, a straight line) that minimizes the difference between the predicted prices and the actual prices in the training data.

5. Evaluate the Model: Use the test data to evaluate how well the model predicts house prices. Metrics like Mean Squared Error (MSE) or R-squared can be used to assess the model's accuracy.

6. Prediction: Once trained and evaluated, the model can be used to predict the price of a new house (not seen during training) based on its size.
