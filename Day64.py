try:
   print(x)
except NameError:
   print("Variable x is not defined ")
except:
   print("An Exception occurred")
#else will excute if try has no error
try:
   print("Hi")
except:
   print("An Exception occurred")
else:
  print("Nothing went wrong")
#finally will excute if try has error or not   
try:
   print(x)
except:
   print("An Exception occurred")
finally:
  print("The 'try except' is finished")