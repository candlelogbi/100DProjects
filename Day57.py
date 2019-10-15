import re
def check(x):
  if(x):
    print("We have match")
  else:
    print("There is no matcing") 
txt="The rain in the Spain"
a=re.search("^The.*Spain$",txt)
b=re.search("rain|is",txt)
#contain white space
c=re.findall("\s",txt)
#contain no digit
d=re.findall('\D',txt)
e=re.search("[arn]",txt)
f=re.search("[0-5][0-9]",txt)
check(a)
check(b)
print(c)
check(d)
check(e)
check(f)



