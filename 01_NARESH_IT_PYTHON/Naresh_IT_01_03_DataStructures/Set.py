# SET

S0={}                               # empty Dictionary
print(type(S0))

S={}                                # empty set
S=set()
print(type(S))

# Duplicates not allowed
# Set is bot mutable & immutable (items can be added/removed but cannot be manipulated)
# Can store multiple datatypes, but no nested sets,etc not allowed
# Indexing/Slicing not allowed
      # print(S[0]) ----> Error
# Set is not duplicable

S1={7,6,2,4,9,5,8,3,1,2,45,9}
print(S1)
print(len(S1))

S2={4, 'style', 96, 7.21, 2+3j, False}
print(type(S2))
print(len(S2))
print(S2)

print(max(S1))
print(min(S1))
print(sum(S1))

for i in enumerate(S2):
    print(i)

#__________________________________________________________________________________________________________________

# Set Membership

print('style' in S2)                                 # False
print(1 in S2)                                       # True

#__________________________________________________________________________________________________________________

# Basic Set Methods

S1.add(27)                                           # Adds element to the end of the set
print(S1)

S3=S1.copy()                                         # copies 1 set into another
print(S3)

S3.clear()                                           # removes all the elements from the set
print(S3)

S1.pop()                                             # removes random elements from the set
print(S1)                                            # S1.pop(5) ---> Error

S1.update([69,52,36])                                # S1.update(74) ---> Error
print(S1)

S1.remove(9)                                         # If element in the set then removes it. If not then Error
print(S1)                                            # S1.remove(11) ---> Error

S1.discard(11)                                       # If element in the set then removes it. If not then NO ERROR
print(S1)

#__________________________________________________________________________________________________________________

# Superset, Subset, Disjoint = Dad, Son, Neighbour

X={1,2,3,4,5,6,7,8,9}
Y={3,4,5,6,7,8}
Z={23,49,77}
W={7,8,9,10,11,12}

print(X.issuperset(Y))                               # True
print(Y.issubset(X))                                 # True
print(X.isdisjoint(Z))                               # True
print(Z.isdisjoint(X))                               # True
print(W.issubset(X))                                 # False

#__________________________________________________________________________________________________________________

# Set operations

A={1,2,3,4,5}
B={4,5,6,7,8}
C={8,9,10}

# Union
print(A|B)                                            # {1,2,3,4,5,6,7,8}
print(A.union(B))                                     # {1,2,3,4,5,6,7,8}

# Intersection
print(A&B)                                            # {4,5}
print(A.intersection(B))                              # {4,5}

# Difference
print(A-B)                                            # {1,2,3}
print(A.difference(B))                                # {1,2,3}
print(B-A)                                            # {8,6,7}
print(B.difference(A))                                # {8,6,7}

# Symmetric Difference
print(A^B)                                            # {1,2,3,6,7,8}
print(A.symmetric_difference(B))                      # {1,2,3,6,7,8}
print(B^A)                                            # {1,2,3,6,7,8}
print(B.symmetric_difference(A))                      # {1,2,3,6,7,8}

# Symmetric Difference Update
A.symmetric_difference_update(B)                      # A= {1,2,3,6,7,8}
print(A)
B.symmetric_difference_update(C)                      # B= {4,5,6,7,9,10}
print(B)

#__________________________________________________________________________________________________________________

S6= {3,9,2,'trdhs', 6+2j, 3,True, 7.5, False}
S7= {0, False, 0+0j, 0.0}
S8= {4, 8, 3, 4, 8.2, 'yoyo', True}

print(any(S6))                           # Checks if any one element in the list is True/non-zero
print(any(S7))
print(any(S8))

print(all(S6))                           # Checks if all the elements in the list are True/non-zero
print(all(S7))
print(all(S8))



