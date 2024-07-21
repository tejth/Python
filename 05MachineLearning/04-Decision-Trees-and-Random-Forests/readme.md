# Decision Tree
## Definition:
A Decision Tree is a flowchart-like structure where each internal node represents a "test" on an attribute (e.g., whether a feature is greater than a certain value), 
each branch represents the outcome of the test, and each leaf node represents a class label or a numeric value (in regression problems).

## Example:

->Scenario: Suppose you want to decide whether to play tennis based on weather conditions (Outlook, Temperature, Humidity, Wind).

->Data:

Outlook: Sunny, Overcast, Rainy </br>
Temperature: Hot, Mild, Cool </br>
Humidity: High, Normal </br>
Wind: Weak, Strong </br>
Play Tennis: Yes or No </br>

->Decision Tree:
A decision tree might split based on Outlook first (e.g., if Outlook is Sunny, go to the next node), then Temperature, and so on, until a 
decision (play tennis or not) is reached at the leaf nodes.

## Use Case:

Decision trees are used in various fields for classification and regression tasks where understanding the decision-making process is important.
Example applications include customer churn prediction, medical diagnosis, and credit risk assessment.

# Random Forest
## Definition:
Random Forest is an ensemble learning method that constructs multiple decision trees during training and outputs the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.

## Example:

->Scenario: Continuing with the tennis example, a random forest would create multiple decision trees based on subsets of the data and features.

->Process:

Random Forest builds multiple decision trees by: </br>
Bootstrapping: Randomly selecting subsets of data (with replacement) to train each tree.</br>
Random Feature Selection: Randomly selecting subsets of features for each split in each tree.
Voting: For classification tasks, the final prediction is the mode of the predictions of all individual trees. For regression tasks, it's the average prediction.</br>
->Use Case:
Random Forests are robust and widely used for tasks where accuracy and interpretability are crucial.
They excel in handling large datasets with many features, dealing with missing values, and maintaining performance without overfitting.
