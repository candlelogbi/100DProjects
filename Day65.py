price=50
txt="The price is {} dollars"
txt2="The price is {:.2f} dollars"
print(txt.format(price))
print(txt2.format(price))
quantity=3
item=300
myorder="I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity,item,price))