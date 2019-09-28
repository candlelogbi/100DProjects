#1
def myFunction(num,power): 
   if(power!=0):
    return num * myFunction(num,power-1)
   else:
    return 1  
print(myFunction(5,3))

#2
numbers=[-4,-6,-5,-1,2,3,7,9,88]
#filter(condtion,list)
y=filter(lambda x: (x>=0),numbers)
print(*y)



