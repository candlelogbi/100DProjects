class myFirstClass:
    #constructor
    #def name(parameter)
    def __init__(self,name,age,gender):
       self.name=name
       self.age=age
       self.gender=gender
    def func(self):
        print("My name is: "+ self.name)

obj= myFirstClass("Shamaah",24,"F")
obj.age=40
print(obj.age)
#produce error
#del obj.gender
print(obj.gender)
#produce error
#del obj
obj.func()




