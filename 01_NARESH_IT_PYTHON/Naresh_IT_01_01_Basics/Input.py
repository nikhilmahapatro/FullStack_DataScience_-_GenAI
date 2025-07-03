import math
from idlelib.autocomplete import TRY_A

# INPUT

# integer as input from the user
A= int(input("Integer Input:- "))
print("Integer= "+str(A))

# float as input from the user
B= float(input("Float Input:- "))
print("Float= "+str(B))

# taking multiple space-separated values as input
C=input("Values:- ").split()
print("multiple space-separated values:- "+ str(C))

# check if a number entered by the user is positive, negative, or zero
D=int(input("Check +ve/-ve:- "))
if D>0:
    d='positive'
elif D<0:
    d='negative'
else:
    d='zero'
print("Check +ve/-ve:- "+ str(D) +" is "+d)


# Convert user input to a list of integers
E= [int(x) for x in input("Enter Numbers:- ")]
print(E)

#  How do you accept a string input and print it in uppercase?
F= input("Up_Str input:- ")
print("UpperCase String:- "+ F.upper())

# Eval input
G= eval(input("Enter expression:- "))
print(G)


# program that accepts a string and prints the number of vowels in it.
# H

# Check if integer input is even or odd
I=int(input("Enter Even/Odd Number:- "))
if I%2==0:
    print(str(I)+" is Even")
else:
    print(str(I) + " is Odd")

# Check if a String is Palindrome or not
J= input("Enter Check Palindrome:- ")
if J==J[::-1]:
    print(J+" is a Palindrome")
else:
    print(J+" is not a Palindrome")

# Square of the Input
K= int(input("Enter number to square:- "))
print(str(K**2)+ " is the square of "+str(K))

# Check if divisible by 3
L= int(input("Divisibility check by 3:- "))
if L%3==0:
    print(str(L)+" is Divisible by 3")
else:
    print(str(L) + " is not Divisible by 3")

# Check if divisible by both 3 and 7
M=int(input("Divisibility check by both 3 and 7:- "))
if M%3==0 and M%7==0:
    print(str(M)+" is Divisible by both 3 and 7")
else:
    print(str(M) + " is not Divisible by both 3 and 7")

#  Accept a list of comma-separated values as input
N=input("Enter coma separated values:- ").split(',')
print(N)

# Take two numbers as input and print their product.
O1=int(input("1st Number:- "))
O2=int(input("2nd Number:- "))
print("Product= "+str(O1*O2))

# Check if input is prime number
P=int(input("Check Prime:- "))
if P>1:
    for i in range(2,P):
        if P%i==0:
            print(str(P)+" is Not a Prime")
            break
        else:
            print(str(P)+" is a Prime")
else:
    print(str(P) + " is Not a Prime")

#  Accept a boolean value from the user
Q=input("Enter True or False: ").lower() == "true"
print("Bool input:- "+str(Q))

# Calculate factorial of input number
R=int(input("Find factorial of:- "))
fact=1
for j in range(1,R+1):
    fact *= j
print("Factorial of "+str(R)+" is "+str(fact))

# Check if input is perfect square
S=int(input("Check perfect square:- "))
if math.sqrt(S)**2==S:
    print(str(S)+" is Perfect Square")
else:
    print(str(S) + " is Not Perfect Square")

# Check Leap Year
T=int(input("Check Leap year:- "))
if (T%4==0 and T%100!=0) or T%400==0:
    print(str(T)+" is a Leap year")
else:
    print(str(T) + " is Not a Leap year")

# Remove leading and trailing spaces from a string input?
U=input("Enter String:- ").strip()
print(U)

#  Handling incorrect inputs when you expect an integer using `input()`?
# Try-Except
try:
    V=int(input("Enter Integer:- "))
except ValueError:
    print("Invalid Input. Enter a valid integer.")

# Accept a string and counts the occurrence of a particular character.
# W

# Convert user input to lowercase using input()
X=input("Enter String:- ").lower()
print(X)

# Check if the input string contains only Alphabets
Y=input("Check only Alphabet string:- ")
if Y.isalpha():
    print("String contains only Alphabets")
else:
    print("String contains other characters")

# Count no of words in the sentence
Z=input("Count No of words:- ").split(" ")
print(Z)
print(len(Z))

# Accept date input from the user
# AA

# Take input from user and print without spaces
BB=input("Enter the string:- ")
print(BB.replace(" ",""))


