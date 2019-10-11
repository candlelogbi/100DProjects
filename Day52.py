import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
y=datetime.datetime(2020,11,7)
print(y)
#strftime("%Letter")
#A day, B month, year
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%Y"))
