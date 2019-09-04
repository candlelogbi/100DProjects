fruit=["orange","apple","banana"]
print(len(fruit))
fruit.append("pineapple")
print(fruit)
fruit.insert(3,"strawberries")
print(fruit)
fruit.remove("orange")
print(fruit)
fruitList=fruit.copy()
fruit.pop()
print(fruit)
print(fruitList)
flist=list(fruit)
print(flist)
#remove with index or last item
fruit.pop(1)
print(fruit)
fruit.pop()
print(fruit)
#clear all item
fruit.clear()
print(fruit)
numberList=list((1,2,4,6,7,8,12))
print(numberList)




