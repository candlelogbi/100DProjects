import os
f=open("test.txt","r")
print(f.read(2))
f=open("test.txt","r")
for x in f:
    print(x)
f=open("test.txt","r")
print(f.readline())
f.close()    
f=open("test.txt","a")
f.write(" ,add information")
f.close()
f=open("test.txt","r")
print(f.read())
f.close()
#new file
b=open("newFile.txt","x")
b=open("newFile.txt","w")
b.write("Delete all text,and write new one")
b.close()
b=open("newFile.txt","r")
print(b.read())
b.close()
if os.path.exists("newFile.txt"):
      os.remove("newFile.txt")
      print("delete file")      
else:
    print("the file not found")  
#delete folder        
os.rmdir("myfolder")    