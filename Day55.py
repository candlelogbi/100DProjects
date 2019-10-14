import json
#json
x='{"name":"Shamaah","age":24}'
#prase x convert from JSON to Python
y=json.loads(x)
print(y["age"])

#convert from Python to JSON  
x={"name":"Shamaah","age":24}
#prase x convert from JSON to Python
y=json.dumps(x)
print(y)

print(json.dumps("hi"))
print(json.dumps(["apple","banana"]))
print(json.dumps(False))
x={"name":"Shamaah","age":24,"fruits":("apple","banana"),"pets":None,
"child":[{"name":"Ali","age":4},{"name":"Ahmed","age":2}]}
y=json.dumps(x)
print(y)