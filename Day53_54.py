import moduleMath 
import datetime

moduleMath.sum(1,8)
moduleMath.subtract(4,2)
moduleMath.multiple(6,6)
moduleMath.division(8,2)

x=datetime.datetime.now()
print(x.strftime("%Y"))
print(x.strftime("%c"))
print(x.strftime("%B"))
print(x.strftime("%A"))
y=datetime.timedelta(1)
z=(x - y).strftime('%Y-%m-%d')
print(z)
j=(x + y).strftime('%Y-%m-%d')
print(j)


