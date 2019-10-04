#Inheritance
class Person:
    def __init__(self,Fname,Lname):
        self.Fname=Fname
        self.Lname=Lname
    def info(self):
        print(  self.Fname,
        self.Lname)
#super() inherinte all function
class Student(Person):
    def __init__(self,Fname,Lname,year):
     super().__init__(Fname,Lname)
     self.graduationyear =year

    def welcome(self):
        print("Welcome ",self.Fname, self.Lname,"to the class of",self.graduationyear) 

obj=Student("Ali","Omar",2019)
obj.info()
print(obj.graduationyear)
obj.welcome()


