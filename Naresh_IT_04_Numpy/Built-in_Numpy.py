import numpy as np
from numpy.ma.core import reshape

#____________________________________________________________________________________________________________________
# ARRAY CREATION FUNCTIONS

# Create an array from a list
A = np.array([1,5,3,8,7,6])
print("Array A:-\n", A)

# Create an array with evenly spaced values
B = np.arange(0,10,2)
print("Array B:-\n",B)                                        # Values from 0 to 10 with step 2

# Create an array with linearly spaced values
C1 = np.linspace(0,20,5,)                                     # 5 values evenly spaced between 0 and 20
print("Array C1:-\n",C1)
C2 = np.linspace(10,30,5,dtype=int)                           # 5 values evenly spaced between 10 and 30 (integer)
print("Array C2:-\n",C2)

# Create an array filled with zeros
D1 = np.zeros((2, 3))                                         # 2x3 array of zeros
print("Array D1:-\n", D1)
D2 = np.zeros((2, 3),dtype=int)                               # 2x3 array of zeros (integer)
print("Array D2:-\n", D2)

# Create an array filled with ones
E1 = np.ones((3, 2))                                          # 3x2 array of ones
print("Array E1:-\n", E1)
E2 = np.ones((3, 2),dtype=int)                                # 3x2 array of ones (integers)
print("Array E2:-\n", E2)

# Create an identity matrix
F = np.eye(4,dtype=int)                                       # 4*4 identity matrix
print("Identity Matrix:-\n",F)

#______________________________________________________________________________________________________________________

# ARRAY MANIPULATION FUNCTIONS

# Reshape an array
G = np.array([1,5,9,7])
g = np.reshape(G,(1,4))                                       # Reshape into 1*4 array
print("Reshaped Array:-\n",g)

# Flatten an array
H = np.array([[1,7],[2,3]])
h = np.ravel(H)                                               # Flattens into 1D array
print("Flattened Array:-\n",h)

# Transpose an array
I = np.array([[1,2,3],[4,5,6],[7,8,9]])
i = np.transpose(I)
print("Transpose Array:-\n",i)

# Stack arrays vertically
J1 = np.array([1,2,3])
J2 = np.array([4,5,6])            
j = np.vstack([J1,J2])                                        # Stacks J1 vertically upon J2
print("Stacked Array:-\n",j)

#______________________________________________________________________________________________________________________

# MATHEMATICAL FUNCTIONS

