fDictionary={
"name":"Shamaah",
"age":24,
"gender":"femele"
}
if "age" in fDictionary:
 print("Yes")
print(len(fDictionary)) 
#new index key -- value
fDictionary["Year"]=2019
print(fDictionary)
#pop() show error if it is empty or not found
fDictionary.pop("Year")
print(fDictionary)
#last item
fDictionary.popitem()
print(fDictionary)
del fDictionary["age"]
#delete all dictionary
#del fDictionary
fDictionary.clear()
#print(fDictionary)  #Error