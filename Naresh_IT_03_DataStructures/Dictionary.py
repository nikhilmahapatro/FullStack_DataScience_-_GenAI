# DICTIONARY

D={}                                           # Empty Dictionary

# Collection of Key-value pairs
# Keys- No duplicates allowed, Values- duplicates allowed
# Mutable
# can store multiple datatypes

D1={
    1:'one',
    2:'two',
    3:'three',
    4:'Four',
    5:'Five'
}
print(len(D1))
print(D1)

for i in enumerate(D1):
    print(i)                                   # Prints (index,Key)

#______________________________________________________________________________________________________________

# Dict Membership (only for keys)

# Checks if key in Dict
print(200 in D1)                                 # False
print(1 in D1)                                   # True
print('one' in D1)                               # False

#_____________________________________________________________________________________________________________

# Nested Dictionary

# Storing another group in Dict

d={'Maverick':'TopGun',
   'EthanHunt':'MissionImpossible',
   ('Wade Wilson','Steve Rogers'):['Deadpool','Captain America']}

print(d['EthanHunt'])
print(d[('Wade Wilson','Steve Rogers')])
print(d[('Wade Wilson','Steve Rogers')][0])
print(d[('Wade Wilson','Steve Rogers')][1])

D2= {7:'sieben',
     8:'akht',
     'S':["Superman", "Sentry", "Spiderman"],
     'G':("Gambit", "Green Lantern"),
     'Dune':{'Lisan-Al-Gaib':'Voice from the outer world',
             'Kwisatz Haderach':'The Chosen One'
             }}
print(D2)

#_____________________________________________________________________________________________________________

# Creating a Dict from a sequence of keys

K4={'W','X','Y','Z'}
D4=dict.fromkeys(K4)
print(D4)                                 # D4= {'X': None, 'Y': None, 'W': None, 'Z': None}

K5={'P','Q','R'}
V5=69
D5=dict.fromkeys(K5,V5)
print(D5)                                 # D5= {'R': 69, 'Q': 69, 'P': 69}

K6={'AA','BB','CC','DD'}
V6=[10,20,30]
D6=dict.fromkeys(K6,V6)
print(D6)                                 # D6= {'BB': {10, 20, 30}, 'AA': {10, 20, 30}, 'DD': {10, 20, 30}, 'CC': {10, 20, 30}}
V6.append(40)
print(D6)                                 # {'CC': [10, 20, 30, 40], 'BB': [10, 20, 30, 40], 'AA': [10, 20, 30, 40], 'DD': [10, 20, 30, 40]}

#_____________________________________________________________________________________________________________

# Dictionary Methods

D3_1= dict({1:'eins', 2:'zwei', 3:'drei', 4:'vier', 5:'funf', 6:'secks'})
D3_2= dict({'uno':1, 'dos':2, 'tres':3, 'cuatro':4, 'cinco':5})

# the dict() constructor to convert an existing dictionary into a new dictionary,  essentially creating a copy
print(D3_1)
print(D3_2)

print(D3_1.keys())                          # dict_keys([1, 2, 3, 4, 5, 6])

print(D3_1.values())                        # dict_values(['eins', 'zwei', 'drei', 'vier', 'funf', 'secks'])

print(D3_1.items())                         # dict_items([(1, 'eins'), (2, 'zwei'), (3, 'drei'), (4, 'vier'), (5, 'funf'), (6, 'secks')])

print(D3_2['cuatro'])                       # Accessing a Dictionary using key
                                            # If key exists then returns corresponding value. If not then Error

print(D3_2.get('tres'))                     # If key exists then returns corresponding value. If not then NO ERROR

print(D3_1[1])                              # Accessing a Dictionary using index
                                            # If key exists then returns corresponding value. If not then Error

print(D3_1.get(2))                          # If key exists then returns corresponding value. If not then NO ERROR

# Add, Remove & Change Items in Dict

# Changing items in the dict
D7={'Name':'Cristiano','YOB': 1985, 'jersey':9, 'Goals':458, 'Address':'Lisbon'}
D7['jersey']=7
print(D7)
small_D7= {'Name':'Cristiano Ronaldo'}
D7.update(small_D7)
print(D7)

# Adding items to the end of the Dict
D7['Team']= 'Real Madrid'
print(D7)

# Removing items from the Dict
D7.pop('Goals')                              # Removes particular item from the Dict
print(D7)

D1.popitem()                                 # removes a random item from the Dict
print(D1)

del[D7['YOB']]                               # Removing item using del method
print(D7)

D1.clear()                                   # Delete all items of the dictionary using clear method
print(D1)

# Copy a Dictionary
D8={'Student':'John Doe', 'Id':4624, 'Batch':'Phy-Che-Math'}
D9=D8                                        # Create a new reference D9
print(id(D8)), print(id(D9))                 # The address of both mydict & mydict1 will be the same
D10=D9.copy()
print(id(D10))                               # Address of D10 if different from D8 & D9

#____________________________________________________________________________________________________________

for i in D3_1:
    print(i)                                 # prints Keys

for i in D3_1:
    print(D3_1[i])                           # prints values

for i in D3_1:
    print(i , ':' , D3_1[i])                 # prints Key & value pair