import json
x={"name":"Shamaah","age":24,"fruits":("apple","banana"),"pets":None,
"child":[{"name":"Ali","age":4,"gender":"M"},{"name":"Naya","age":2,"gender":"F"}]}
y=json.dumps(x,indent=4, separators=(".","="),sort_keys=True)
print(y)