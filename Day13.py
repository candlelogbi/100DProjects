fruit=["orange","apple","banana"]
numbers=[1.2,3.6,11.5]
print("Numbers list:") 
print(numbers)
print("Numbers list:") 
for x in numbers:
    print(x)

print("Item in index[1]:"+fruit[1])
fruit[1]="buerry"
print("Fruit after change item[1]:")
print(fruit)

del fruit[1]
print("Fruit after delete item[1]:")
print(fruit)
print("Max number is :")
print( max(numbers))


y=[5,"A",8,"B","C"]
del y
#print(y) 