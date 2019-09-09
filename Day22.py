#unordered, changeable and indexed,Key and value, {key:value}
fDictionary={
"name":"Shamaah",
"age":24,
"gender":"femele"
}
print(fDictionary)
#Get value using key. 
x=fDictionary["age"]
#get value using get()
#x=fDictionary.get("age")
print(x)
fDictionary["age"]=25
print(fDictionary)
for x in fDictionary:
    #keys
    print(x)
    #values
    print(fDictionary[x])
print("--------")    
for x in fDictionary.values():
    print(x) 
print(fDictionary.values())  
for x in fDictionary.items():
    print(x)   
print(fDictionary.items())          