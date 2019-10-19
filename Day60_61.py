import json
import re
#1
fTuple=("Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday")
print(type(fTuple))
#convert from python to json
y=json.dumps(fTuple)
print(y)
print(type(y))
#2
s="data is the new oil"
e=re.search("data",s)
print(e)
#3
PL={
    "name":"python",
    "year":1991,
    "designer":"Guido van Rossum",
    "paradigm":("object-oriented","functional","imperative")
}

y=json.dumps(PL)
print(y)