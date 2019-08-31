#Please, I want {} sandwishes and {} donutes 
x="Please, I want {} sandwishes and {} donutes"
#1.Please, we want {} sandwishes and {} donutes 
x1=x.replace("I","we")
print(x1)
#2.Please, we want 5 sandwishes and 7 donutes 
a,b=5,7
x2=x1.format(a,b)
print(x2)
#3.PleAse, we wAnt 5 sAndwishes And 7 donutes 
#print(x2.replace("a","A"))
x3=x2.translate(str.maketrans("a","A"))
print(x3)
