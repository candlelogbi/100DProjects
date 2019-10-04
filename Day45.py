#iterator 
mytuple=("apple","banana","orange")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
mystring="Ali"
myit=iter(mystring)
print(next(myit))
print(next(myit))
print(next(myit))
#for  actually creates an iterator 
for x in mytuple:
    print(x)
#To create an object/class as an iterator    __iter__() __next()__ 
class Myumber():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
     if self.a <=4:  
        x = self.a
        self.a +=1
        return x
     else:
           raise StopIteration  
obj=Myumber()
myit=iter(obj)
for x in myit:
    print(x)