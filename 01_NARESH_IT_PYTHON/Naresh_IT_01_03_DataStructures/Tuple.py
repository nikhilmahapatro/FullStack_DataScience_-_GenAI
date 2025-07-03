# TUPLE

T=()                                          # empty Tuple

# Duplicates allowed
# Immutable
# Can store multiple datatypes and nested tuple,etc
# Bank data is stored in Tuple format so that data can't be added or deleted, but can be duplicated

T1= (4,6,8,3,6,7,2,1,6,4,8,7,5,6,4)

print(len(T1))

print(max(T1))
print(min(T1))
print(sum(T1))

for i in enumerate(T1):
    print (i)

#____________________________________________________________________________________________________________________

# Tuple Membership

print(45 in T1)                                 # False
print(3 in T1)                                  # True

#_______________________________________________________________________________________________________________

# Nested Tuple Indexing

t = ('str', 4, 6.7, (9,4,7,6,5,2,8), 5+8j)
print(t[3])
print(t[3][0])
print(t[3][1])
print(t[3][2])
print(t[3][3])

#_______________________________________________________________________________________________________________

# Tuple Methods

print(T1.count(6))                               # counts the no of occurances of the element

print(T1.index(7))                               # prints the index of first occurance of the element

#_______________________________________________________________________________________________________________

T2= (3,9,2,'trdhs', 6+2j, 3,True, 7.5, False)
T3= (0, False, 0+0j, 0.0)
T4= (4, 8, 3, 4, 8.2, 'yoyo', True)

print(any(T2))                           # Checks if any one element in the tuple is True/non-zero
print(any(T3))
print(any(T4))

print(all(T2))                           # Checks if all the elements in the tuple are True/non-zero
print(all(T3))
print(all(T4))

# Tuple is duplicable
t1=(4, 3.5, 'cygfyu', 49+92j, False)
t2=t1*3
print(t2)    # (4, 3.5, 'cygfyu', (49+92j), False, 4, 3.5, 'cygfyu', (49+92j), False, 4, 3.5, 'cygfyu', (49+92j), False)