def myfunction(x):
  return lambda a: a * x
y=myfunction(2)
z=myfunction(3)
print(y(4))
print(z(4))