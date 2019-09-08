fSet={"Ali","apple","Ali",9,56,8.9,10.7,"banana"}
print("lenght:",len(fSet))
#Error if it not found
#fSet.remove(3)
#no Error if it not found
fSet.discard(7)
print("Discard(7):",fSet)
#remove random
x=fSet.pop()
print("Remove:",x,fSet)
fSet.clear()
print("Clear:",fSet)
#Constructor 
thisSet=set(("Ahmed","Shamaah",2,6))
del thisSet
#Error
#print(thisSet)