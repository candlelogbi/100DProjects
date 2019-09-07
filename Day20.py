#unordered , unindexed and unique 
fSet={"Ali","apple","Ali",9,56,8.9,"banana"}
print(fSet)
# cannot access items using index
print("-------")
for x in fSet:
    print(x)
print("-------")
print("Ali" in fSet)    
# cannot change its items
#add one item
fSet.add(8)
print(fSet)
#add more than one item
fSet.update([8,"Ahmed"])
print(fSet)