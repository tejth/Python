NumPy
NumPy (or Numpy) is a Linear Algebra Library for Python, the reason it is so important for Data Science with Python is that almost all of the libraries in the PyData Ecosystem rely on NumPy as one of their main building blocks.

Why NumPy?
NumPy is designed for efficiency on large arrays of data and includes a variety of functions for working in domain of linear algebra, Fourier transform, and matrices. Its main purpose is to provide a fast array processing functionality, where arrays are the core of nearly all mathematical computation in Python.

Installation Instructions
It is highly recommended you install Python using the Anaconda distribution to ensure compatibility with other libraries in the PyData ecosystem. If you have Anaconda, install NumPy by opening your terminal or command prompt and typing:

bash
Copy code
conda install numpy
If you do not have Anaconda, refer to NumPy's official documentation for various installation instructions.

Using NumPy
Once installed, NumPy can be imported in Python as:

python
Copy code
import numpy as np
NumPy Arrays
NumPy arrays are essential for working with numerical data in Python. They come in two main flavors: vectors (1-dimensional) and matrices (2-dimensional).

Creating NumPy Arrays
You can create NumPy arrays from Python lists using np.array():

python
Copy code
my_list = [1, 2, 3]
my_array = np.array(my_list)
Built-in Methods
NumPy provides several built-in methods for array generation:

np.arange(): Return evenly spaced values within a given interval.
np.zeros(), np.ones(): Generate arrays of zeros or ones.
np.linspace(): Return evenly spaced numbers over a specified interval.
np.eye(): Creates an identity matrix.
Random
NumPy also offers methods to create arrays filled with random numbers:

np.random.rand(): Create an array of the given shape with random samples from a uniform distribution.
np.random.randn(): Return a sample from the "standard normal" distribution.
np.random.randint(): Return random integers from a low (inclusive) to high (exclusive) range.
Reshape and Attributes
Other useful methods and attributes include reshaping arrays (np.reshape()), finding maximum and minimum values (np.max(), np.min()), and obtaining array shape (array.shape) and data type (array.dtype).

---

---

---

---

NumPy Indexing and Selection

Bracket Indexing and Selection
The simplest way to pick one or some elements of an array looks very similar to python lists:

#Get a value at an index
arr[8]

Broadcasting
Numpy arrays differ from a normal Python list because of their ability to broadcast:
arr[0:5]=100

Indexing a 2D array (matrices)
The general format is arr_2d[row][col] or arr_2d[row,col]. I recommend usually using the comma notation for clarity.

Fancy Indexing
Fancy indexing allows you to select entire rows or columns out of order,to show this, let's quickly build out a numpy array:

Selection
Let's briefly go over how to use brackets for selection based off of comparison operators.

arr = np.arange(1,11)
arr
array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr > 4

---

---

---

NumPy Operations

1. Array with Array
2. Array with Scalars
3. Universal Array Function
