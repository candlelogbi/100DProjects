import re
s="The rain in Spain"
e=re.findall("in",s)
print(e)
if(e):
    print("Yes there is match")
else:
     print("No match") 
     
#first white space   
b=re.search("\s",s)
print("the first white space locate in:", b.start())     
e=re.search("se",s)
print(e)
e=re.split("\s",s)
print(e)