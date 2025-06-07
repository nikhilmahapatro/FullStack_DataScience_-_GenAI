
#------------------------------CONDITIONAL STATEMENTS-------------------------------#

# IF

if True:
    print("If True")

if False:
    print("If False")

# Python program to check even number
a1 = 4
a2 = a1 % 2
if a2==0:
    print("Even Number")
if a2==1:
    print("Odd Number")
# Writing multiple 'ifs' increases space complexity

#________________________________________________________________________________________________________________

# IF ELSE

if True:
    print("Data Science")
else:
    print("See you later")

# Python program to check even number
b1 = 4
b2 = a1 % 2
if b2==0:
    print("Even Number")
else:
    print("Odd Number")

#_________________________________________________________________________________________________________________

# NESTED IFs

c1 = 8
c2 = a1 % 2
if c2==0:
    print("Even Number")
    if c1>5:
        print("Greater than 5")
    else:
        print("Smaller than 5")
else:
    print("Odd Number")

#__________________________________________________________________________________________________________________

# IF ELIF ELSE

# Python program to check even number
d1 = 4
d2 = a1 % 2
if d2==0:
    print("Even Number")
elif d2==1:
    print("Odd Number")

e = 3
if e==1:
    print('one')
elif e==2:
    print('two')
elif e==3:
    print('three')
elif e==4:
    print('four')
else:
    print('not in range')