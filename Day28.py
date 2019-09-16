#while
i=1
while i<7:
    print(i)
    #stop
    if i==4:
     break
    i+=1
    
i=0
while i<7:
    i+=1    
    #skip this and continue
    if i==4:
     continue
    print(i)
else:
    print("i is no longer less than 7")    


