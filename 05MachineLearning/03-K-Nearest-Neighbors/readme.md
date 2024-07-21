# K-nearest Neigbour Algo
The K-Nearest Neighbors (KNN) algorithm is a simple and intuitive machine learning algorithm used for classification and regression tasks. It works based on the principle
that data points with similar attributes tend to fall into similar categories or have similar numeric values.

## Simple Example:

Let's illustrate KNN with a classification example:

->Scenario: Suppose you have a dataset of fruits categorized as either "apple" or "orange" based on their weight and sweetness level.

->Problem: Given a new fruit with a weight of 135 grams and sweetness level of 7, predict whether it's an apple or an orange.

## Using KNN:

1. Choose K: Decide on the number of nearest neighbors, K. For instance, let's set K = 3.

2. Calculate Distance: Calculate the Euclidean distance (or other distance metrics) between the new fruit and all existing fruits in your dataset.
![2](https://github.com/user-attachments/assets/fcc8faac-fe37-436b-bfa3-ff0ac5489fbe)

3. Find K Nearest Neighbors: Select the K nearest neighbors based on the smallest distances. In this case, K = 3, so we choose the three closest fruits:

   Closest: Apple (130 grams, sweetness 7) </br>
   Second closest: Orange (140 grams, sweetness 8)</br>
   Third closest: Apple (120 grams, sweetness 8)</br>
