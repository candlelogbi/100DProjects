import random
x=1 #int all number +,-
y=-2.8 #float all number with , and e power of 10
y2=3e9
z=6j #complex all number with j
print(type(x))
print(type(y))
print(type(y2))
print(type(z))
#convert types
a=complex(x)
b=int(y)
c=float(x)  
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#Random module
print(random.randrange(1,20))