import re
s="The rain in Spain"
e=re.sub('\s',"-",s)
print(e)
e=re.sub('\s',"-",s,2)
print(e)
e=re.search("ai",s)
print(e)
e=re.search(r"\bS\w+",s)
print(e.span())
print(e.string)
print(e.group())



