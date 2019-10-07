x=200
z=100
def myfunc():
    global y
    global z
    y=4
    x=300
    z=40
    print("x=",x)

myfunc()
print("x=",x,", y=",y)
print("z=",z)

