#1
print("Enter first and last letter in your name:")
print("First Letter:")
x=input()
print("Last Letter:")
y=input()
info="Your first letter in your name {} and the last letter {} "
print(info.format(x,y))
#2
txt="Dear {fname} {lname}, Your current balance is {balance} $ "
print(txt.format(fname="Ahmad",lname="Ali",balance=53.44))
#3
arr=[]
number=int(input("Enter the length of array: "))
for i in range(number):
  x=int(input("Enter the next value: "))
  arr.append(x)

print(arr)    