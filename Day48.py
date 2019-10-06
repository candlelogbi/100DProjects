#Global scope and loca;
y=50
def myfunction():
    x=300
    def insidefunction():
        print(x+y)
    insidefunction()
myfunction()