#Tuple Unchangeable , Cannot add item, Cannot  remove item
thistuple=(2,5,8,8.9,"banana","بايثون")
print(thistuple)
tuple2=(3,)
print(tuple2)
print(thistuple[2])
print(thistuple[2:4])
for x in thistuple:
  print(x)
tuple3=(2,5,8.9,"orange")
#remove all the tuple
del tuple3
#print(tuple3)
