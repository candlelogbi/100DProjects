import camelcase

c=camelcase.CamelCase()
txt="date: sunday , 26 october"
#capitalizefirst letter of each word
print(c.hump(txt))