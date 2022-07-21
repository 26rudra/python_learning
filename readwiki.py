def readin():
     val=open("wiki.txt","r")
     val=val.read()
    #  print(val.split())
     return val.split()
val=readin()

dics={}
for i in  (val):
    if i in dics:
        dics[i]+=1
    else:
        dics[i]=1    
print(dics)