fTuple=(3,4.5,"orange",3,23,31.55,3)
if 3 in fTuple:
 print("yes, it's in tuple")
else:
  print("no,  it's not in tuple")
sTuple=("apple",)*2
x=(3,4,5,6)
x=x+(1,2,3)
print(x)
print(len(sTuple))
fList=[3,4,5,6]
thTuple=tuple(fList)
print(thTuple)
y=fTuple.index("orange")
z=fTuple.count(3)
print(y)
print(z)