import numpy as np
from numpy.ma.core import reshape
from numpy.matrixlib.defmatrix import matrix

#____________________________________________________________________________________________________________________
# ARRAY CREATION FUNCTIONS

# Create an array from a list
A = np.array([1,5,3,8,7,6])
print("Array A:-\n", A)

# Create an array with evenly spaced values
B = np.arange(0,10,2)
print("Array B:-\n",B)                                        # Values from 0 to 10 with step 2

# Create an array with linearly spaced values
C1 = np.linspace(0,20,5,)                    # 5 values evenly spaced between 0 and 20
print("Array C1:-\n",C1)
C2 = np.linspace(10,30,5,dtype=int)          # 5 values evenly spaced between 10 and 30 (integer)
print("Array C2:-\n",C2)

# Create an array filled with zeros
D1 = np.zeros((2, 3))                                         # 2x3 array of zeros
print("Array D1:-\n", D1)
D2 = np.zeros((2, 3),dtype=int)                        # 2x3 array of zeros (integer)
print("Array D2:-\n", D2)

# Create an array filled with ones
E1 = np.ones((3, 2))                                          # 3x2 array of ones
print("Array E1:-\n", E1)
E2 = np.ones((3, 2),dtype=int)                                # 3x2 array of ones (integers)
print("Array E2:-\n", E2)

# Create an identity matrix
F = np.eye(4,dtype=int)                                    # 4*4 identity matrix
print("Identity Matrix:-\n",F)

#______________________________________________________________________________________________________________________

# ARRAY MANIPULATION FUNCTIONS

# Reshape an array
G = np.array([1,5,9,7])
g = np.reshape(G,(1,4))                                 # Reshape into 1*4 array
print("Reshaped Array:-\n",g)

# Flatten an array
H = np.array([[1,7],[2,3]])
h = np.ravel(H)                                                # Flattens into 1D array
print("Flattened Array:-\n",h)

# Transpose an array
I = np.array([[1,2,3],[4,5,6],[7,8,9]])
i = np.transpose(I)
print("Transpose Array:-\n",i)

# Stack arrays vertically
J1 = np.array([1,2,3])
J2 = np.array([4,5,6])                                         # Stacks J1 vertically upon J2
j = np.vstack([J1,J2])
print("Stacked Array:-\n",j)

#______________________________________________________________________________________________________________________

# MATHEMATICAL FUNCTIONS

# Add 2 to each element of an array
K = np.array([1,2,3,4])
k = np.add(K,2)
print("Added 2 to Array:-",k)

# Square each element of an array
M = np.array([1,2,3])
m = np.pow(M,2)
print("Square of Array:- ",m)

# Cube each element of an array
N = np.array([0,1,2])
n = np.pow(N,3)
print("Cube of Array:- ",n)

# Root each element of an array
O = np.array([4,9,16,25,36])
o = np.sqrt(O)
print("Square root of Array:- ",o)

# Dot product of 2 arrays
P1 = np.array([3,4,5])
P2 = np.array([6,7,8])
P3 = np.array([1,2,3,9])
p = np.dot(P1,P2)
# np.dot(P1,P3) --> Error
# np.dot(P2,P3) --> Error
print("Dot product of P1 & P2:- ",p)

#_____________________________________________________________________________________________________________________

# STATISTICAL FUNCTIONS

# Mean of an array
Q = np.array([2,5,6,9])
q = np.mean(Q)
print("Mean of array:- ",q)

# Standard deviation of an array
R = np.array([4,6,8,5])
r = np.std(R)
print("Standard Deviation of  Array:- ",r)

# Minimum element of an array
S = np.array([5,4,9,6,3])
s = np.min(S)
print("Min of s:- ", s)

# Maximum element of an array
T = np.array([4,7,5,2,1,3,6])
t = np.max(T)
print("Max of T:-", t)

#____________________________________________________________________________________________________________________

# LINEAR ALGEBRA FUNCTIONS

# Create a Matrix
matrix = np.array([[9,2,3],[4,8,6],[7,1,9]])

# Determinant of a matrix
determinant = np.linalg.det(matrix)
print("Determinant of matrix:- ",determinant)

# Inverse of a matrix
inverse = np.linalg.inv(matrix)
print("Inverse of matrix:-\n",inverse)

#_____________________________________________________________________________________________________________________

# RANDOM SAMPLING FUNCTIONS

# # Generate random values between 0 and 1
U = np.random.rand(3)
print("Randon values:- ",U)                                     # Array of 3 random values between 0 and 1

np.random.seed(0)                                               # Setting seed for reproducibility
                                                                # Always prints the same 3 numbers
V = np.random.rand(3)
print("Randon values seed:- ",V)

# Generate random integers
W = np.random.randint(0, 10, 5 )                 # Random integers between 0 and 10
print("Random integers:", W)

np.random.seed(0)                                               # Setting seed for reproducibility
X = np.random.randint(0, 10, 5 )                 # Random integers between 0 and 10
print("Random integers:", X)

#____________________________________________________________________________________________________________________

# BOOLEAN & LOGICAL FUNCTIONS

logical_test = np.array([True, False, True])

# Check if all elements are True
all_true = np.all(logical_test)
print("All elements True:", all_true)

# Check if any elements are True
any_true = np.any(logical_test)
print("Any elements True:", any_true)

#___________________________________________________________________________________________________________________

# SET OPERATIONS

# Intersection of two arrays
set_a = np.array([1, 2, 3, 4])
set_b = np.array([3, 4, 5, 6])
intersection = np.intersect1d(set_a, set_b)
print("Intersection of a and b:", intersection)

# Union of two arrays
union = np.union1d(set_a, set_b)
print("Union of a and b:", union)

#_________________________________________________________________________________________________________________

# ARRAY ATTRIBUTES FUNCTIONS

# Array attributes
Y= np.array([1, 2, 3])
shape = Y.shape                                     # Shape of the array
size = Y.size                                       # Number of elements
dimensions = Y.ndim                                 # Number of dimensions
dtype = Y.dtype                                     # Data type of the array

print("Shape of a:", shape)
print("Size of a:", size)
print("Number of dimensions of a:", dimensions)
print("Data type of a:", dtype)

#____________________________________________________________________________________________________________________

# OTHER FUNCTIONS

# Create a copy of an array
Z = np.array([1, 2, 3])
copied_array = np.copy(Z)                           # Create a copy of array a
print("Copied array:", copied_array)

# Size in bytes of an array
array_size_in_bytes = Z.nbytes                      # Size in bytes
print("Size of Z in bytes:", array_size_in_bytes)

# Check if two arrays share memory
shared = np.shares_memory(Z, copied_array)
print("Do a and copied_array share memory?", shared)
