fDictionary={
"name":"Shamaah",
"age":24,
"gender":"femele"
}
#copy
sDic=fDictionary.copy()
dic4=dict(fDictionary)
print(sDic)
print(dic4)
#nested
info1={
"name":"Maha",
"age":20,
"gender":"femele"
}
info2=dict(
name="Ahmed",
age=24,
gender="male"
)
dic={
    "dic1":fDictionary,
    "dic2":info1,
    "dic3":info2
}
print(dic)