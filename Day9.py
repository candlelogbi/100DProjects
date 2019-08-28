a,c=45,78
b="My number is {}"
#format() place it in {}
print(b.format(a))
d="My numbers are {} and {}"
print(d.format(a,c))
#use index number 
d="My numbers are {1} and {0}"
print(d.format(a,c))



#person={"name":"shamaah","age":24}
#fruit={"orange","banan","apple"}
#print("My name is {0[name]}, i\'m {0[age]} years I love {1[2]}.".format(person,fruit))