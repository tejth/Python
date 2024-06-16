import numpy as np;

#Array with Array
arr = np.arange(0,10)
print(arr +arr)
print(arr-arr)
print(arr/arr) #will give you warning for 0/0

#Array with Scalars
print(arr**3)

#Universal Array Functions
print(np.sqrt(arr)) #square root
print(np.exp(arr)) #exponential
print(np.log(arr)) #natural logarithm
print(np.sin(arr)) #sine
print(np.cos(arr)) #cosine
print(np.tan(arr)) #tangent
print(np.pi) #pi constant
print(np.e) #e constant
