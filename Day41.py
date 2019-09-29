class myFirstClass:
    #constructor
    #def name(parameter)
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def func(self):
        print("My name is: "+ self.name)

sObject= myFirstClass("Shamaah",24)
print(sObject.name)
print(sObject.age)
sObject.func()
