x=3
y=7
print(x>6 and y>5)
print(x>6 or y>5)
print(not(x>6 and y>5))
#compare same object, with the same memory location
x=["apple","orange"]
y=["apple","orange"]
z=x
print(x is y)
print(x is not y)
print(x is z)
print(x == y)
# if a value is presented in an object.
print("apple" in x)
print("apple" not in x)
#bitwise
b=34 #0001 0001  
c= b << 2 
d= b >> 2
print(c) #0100 0100
print(d) #0000 0100
