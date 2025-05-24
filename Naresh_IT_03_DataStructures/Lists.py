# LISTS

L=[]                                              # Empty List

# Duplicates allowed
# Mutable
# Can store multiple datatypes and nested lists,etc

L1=[5,4,6,8,9,4,6,8,7,1,4,5,9]

print(len(L1))

print(max(L1))
print(min(L1))
print(sum(L1))

for i in enumerate(L1):
    print(i)

#_______________________________________________________________________________________________________________

# List Membership

print(200 in L1)                                 # False
print(1 in L1)                                   # True

#_______________________________________________________________________________________________________________

# Nested List Indexing

l = ['str', 4, 6.7, [9,4,7,6,5,2,8], 5+8j]
print(l[3])
print(l[3][0])
print(l[3][1])
print(l[3][2])
print(l[3][3])

#_______________________________________________________________________________________________________________

L2= [3,9,2,'trdhs', 6+2j, 3,True, 7.5, False]
L3= [4,6,8,9,8,956,7,56,5,62,5,1]
L4= [5,6,8,4,6,4,6,2,5,8,1,9,6,3,5,3,1]
L5= [4,7,8,9,8,5,4,9,5,4,8,5,3,5,5,1,8,2,9,1]

# List Methods

temp_L2=L2.copy()                        # copies 1 list into another
print('temp_L2= ' + str(temp_L2))

L2.append(7)                             # adds element to the end of the list
print(L2)

print(L2.count(3))                       # counts the no of occurances of element

print(L2.index(7.5))                     # prints the index of first occurance of element

L4.reverse()                             # reverses a list
print(L4)

L3.extend(L4)                            # concatenates 2 lists
print(L3)

L3.pop()                                 # removes last element from the list by default
print(L3)
L3.pop(5)                                # removes element at index 'i'
print(L3)

L4.remove(2)                             # removes the element from the list
print(L4)

L4.sort()                                # sorts in Ascending order
print(L4)

L3.sort(reverse=False)                   # sorts in Ascending order
print(L3)

L5.sort(reverse=True)                    # sorts in Descending order
print(L5)

L4.clear()                               # removes all elements from the list
print(L4)

del L5                                   # Deletes the List

#___________________________________________________________________________________________________________________

L6= [3,9,2,'trdhs', 6+2j, 3,True, 7.5, False]
L7= [0, False, 0+0j, 0.0]
L8= [4, 8, 3, 4, 8.2, 'yoyo', True]

print(any(L6))                           # Checks if any one element in the list is True/non-zero
print(any(L7))
print(any(L8))

print(all(L6))                           # Checks if all the elements in the list are True/non-zero
print(all(L7))
print(all(L8))

# List is duplicable
L9=[5,7,9,2,8,25,6,43,2,1,4,7]
L10=L9*2
print(L10)                               # [5, 7, 9, 2, 8, 25, 6, 43, 2, 1, 4, 7, 5, 7, 9, 2, 8, 25, 6, 43, 2, 1, 4, 7]

L9[5]='jit'
print(L9)