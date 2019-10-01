#Inheritance
class Person:
    def __init__(self,Fname,Lname):
        self.Fname=Fname
        self.Lname=Lname
    def info(self):
        print(  self.Fname,
        self.Lname)    
class Student(Person):
    pass
    def __init__(self,Fname,Lname):
     Person.__init__(self,Fname,Lname)

obj=Person("khaled","Ahmed")
obj2=Student("Ali","Omar")
obj.info()
obj2.info()

