# Bias Variance Trade Off
<ul>
  <li>
    Bias:

Definition: Bias refers to the error introduced by approximating a real-world problem with a simplified model. It's the difference between the average prediction of our model and the true value we are trying to predict.
Example: Imagine we have a dataset of houses with their sizes and prices. We use a simple linear regression model to predict house prices based only on size. If the model assumes a straight-line relationship (e.g., Price = m * Size + b), but in reality, house prices are influenced by factors like location, age, and amenities, then our model might consistently underpredict or overpredict prices (even on average).
Variance:
</li>
<li>
Definition: Variance refers to the model's sensitivity to small fluctuations in the training data. It measures how much the predictions for a given point vary between different realizations of the model.
Example: Continuing with our house price prediction example, if we use a very complex model (e.g., a deep neural network) with many parameters relative to the amount of data we have, the model might "memorize" the training data instead of generalizing from it. As a result, it could perform well on the training data but poorly on new, unseen data. This high sensitivity to the specific data points in the training set indicates high variance.
</li>
</ul>

# Relation 
1.High Bias:
Example: Imagine you have a toy car that always moves in a straight line, no matter what obstacle is in its path. If you use this toy car to navigate a maze with curves
and turns, it will consistently fail to reach the goal because it's too simple to adapt to the maze's complexity. This is like a model with high bias—it's too basic to capture the nuances in the data.

2. High Variance:
Example: Now, picture a robot with arms and legs that can bend in any direction. It's so flexible that it can perfectly replicate any dance move it sees.
However, when it tries to walk straight ahead, it wobbles and falls because it's too sensitive to small changes in its environment. This is like a model with high variance—it's
too complex and reacts too much to the specific details of the training data, so it doesn't perform well on new tasks.

3.Low Bias:
Example: Think of a robot designed specifically for cleaning floors. It's equipped with sensors to detect dirt and can efficiently move around furniture. 
It's tailored to its task, so it cleans floors effectively every time. This is like a model with low bias—it accurately represents the relationship between features (like dirt location) and the target (clean floor).

4.Low Variance:
Example: Now, imagine a simple robot that always follows the same set of instructions to clean floors. It doesn't have fancy sensors or advanced algorithms, 
but it reliably cleans every room it enters without making mistakes. This is like a model with low variance—it's consistent in its performance and doesn't change its behavior drastically based on small variations in the environment.

# Logistic Regression
Logistic regression is a type of statistical model used to predict the probability of a binary outcome (e.g., yes/no, true/false) based on one or more predictor variables.
Despite its name, it's used for classification rather than regression tasks. Logistic regression is suitable when you have a dependent variable that can 
take only two values (e.g., yes/no, pass/fail).
Logistic regression is for predicting probabilities of discrete outcomes.
Linear regression is for predicting continuous numeric values.

## Example:

Imagine you want to predict whether a student passes or fails an exam based on the number of hours they studied. Here, the outcome (pass or fail) is binary.

->You collect data from past students, noting how many hours each student studied and whether they passed (1) or failed (0).
->Logistic regression analyzes this data to find the relationship between study hours and the probability of passing.
->The model outputs a probability score for each student, indicating the likelihood of passing based on their study hours.
