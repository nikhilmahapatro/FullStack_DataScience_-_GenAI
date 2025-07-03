
#----------------------------LOOPS-----------------------------#

# WHILE LOOP

# Incremental
a = 1
while a<=5:
    print("Data Science", a)
    a+=1

# Decremental
b = 5
while b>=1:
    print("Data Science", b)
    b-=1

# Nested While loop
c1 = 1

while c1<=5:
    print("Data Science",c1)
    c2 = 1
    while c2<=4:
        print("Gen AI",c2)
        c2+=1
    c1+=1

d1 = 1

while d1<=5:
    print("Data Science ", end=" ")
    d2 = 1
    while d2<=4:
        print("Gen AI ", end=" ")
        d2+=1
    d1+=1
    print()

e1 = 1

while e1<=2:
    e2 = 0
    while e2<=2:
        print(e1*e2, end=" ")
        e2+=1
    e1+=1
    print()

f1 = 1

while f1<=4:
    f2 = 0
    while f2<=3:
        print(f1*f2, end=" ")
        f2+=1
    f1+=1
    print()

#___________________________________________________________________________________________________________________

# FOR LOOP

G = 'nit'
for g in G:
    print(g)

H = [5,9.2,'Auf Wiedersehen']
for h in H:
    print(h)

for i in range(2,8):
    print(i)

for j in range(0,20,3):
    print(j)

for k in range(1,51):
    if k%5==0:
        print(k)

#__________________________________________________________________________________________________________________

# BREAK, CONTINUE, PASS

for l in range(1,11):
    print(l)

for m in range(1,11):
    if m==7:
        break
    print(m)

for n in range(1,11):
    if n==7:
        continue
    print(n)

for o in range(1,11):
        pass