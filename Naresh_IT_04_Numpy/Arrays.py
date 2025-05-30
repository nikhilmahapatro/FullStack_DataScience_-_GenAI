from wsgiref.simple_server import sys_version

import numpy as np
import sys

print(np.__version__)
print((sys_version))

myList=[1,2,5,4,8,4,6,5,3]
print(type(myList))

arr=np.array(myList)                             # Converting a list into an array
print(type(myList))
print(type(arr))

# Array Methods

print(np.arange(10))                             # [0 1 2 3 4 5 6 7 8 9]
print(np.arange(5.0))                            # [0. 1. 2. 3. 4.]
print(np.arange(10,20))                          # [10 11 12 13 14 15 16 17 18 19]
print(np.arange(20,10))                          # [] ----> Always 1st arg < 2nd arg
print(np.arange(-16,1))                          # [-16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0]
print(np.arange(10,40,3))                        # [10 13 16 19 22 25 28 31 34 37]
print(np.arange(10,40,3))

# Parameter Tuning
print(np.zeros(5))                               # [0. 0. 0. 0. 0.]
# Hyperparameter Tuning
print(np.zeros(10,dtype=int))             # [0 0 0 0 0 0 0 0 0 0]
print(np.zeros((2,2)))                           # 2*2 array--> [[0. 0.][0. 0.]]
print(np.zeros((2,2), dtype=int))         # 2*2 array--> [[0 0][0 0]]
print(np.zeros((3,4), dtype=int))         # 3*4 array--> [[0 0 0 0][0 0 0 0][0 0 0 0]]

print(np.ones(7))                               # [1. 1. 1. 1. 1. 1. 1.]
print(np.ones((3,3)))                           # 3*3 array--> [[1. 1. 1.][1. 1. 1.][1. 1. 1.]]
print(np.ones((3,5),dtype=int))                 # 3*5 array--> [[1 1 1 1 1][1 1 1 1 1][1 1 1 1 1]]

print(np.random.rand(5))                        # [0.93947515 0.40208097 0.2263055  0.51842431 0.01126621]
print(np.random.rand(2,3))                      # 2*3 array--> [[0.12089843 0.79271894 0.45682247][0.50187188 0.7821017  0.13896569]]
print(np.random.randint(5,16))        # Generates 1 random int in range[5,16)
print(np.random.randint(0,21,4)) # Generates 4 random int in range[0,21)
print(np.random.randint(0,1))         # Generates 0 everytime