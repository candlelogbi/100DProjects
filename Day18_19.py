#1
fList=[2,6,"shamaah","ali",5.7,6]
print("List:",fList)
number=fList.count(6)
print("Count number 6:",number)
add=fList.extend([6,7])
print("Extend (6,7):",fList)
fList.reverse()
print("Reverse:",fList)
fList.remove(6)
print("Remove number 6:",fList)
#2
fTuple = ("java", "python", "swift") 
if "python" in fTuple:
    print("Yes,python found")
else:
    print("No,not found")    