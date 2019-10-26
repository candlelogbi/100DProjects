price,quantity,item=50,3,300
myorder="I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity,item,price))
age,name=24,"Shamaah"
info="His name is {1}. {1} is {0} years old."
print(info.format(age,name))
mycar="I have a {car},it is a {model}"
print(mycar.format(car="Ford",model="Mustang"))

