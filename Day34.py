def myFunction(food):
   for x in food:
    print (x) 

def myFunction1(y):
    return 5 * y
#kwargs 
def myFunction2(Fname,Mname,Lname):
    print("My first name:" + Fname)
#save as tuple
def myFunction3(*letter):
    print("The letter is:" + letter[3])
#Recursion: function calls itself
def recFunction(k):
    if (k>0):
        result=k+recFunction(k-1)
        print(result)
    else:
        result=0 
    return result  

fruits=["orange","banana","apple"]   
myFunction(fruits)
print(myFunction1(5))
myFunction2(Lname="Ahmed",Fname="Shamaah",Mname="Yahya")
myFunction3("A","C","D","E")
print("Recursion:")
recFunction(5)