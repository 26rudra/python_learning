file = open('twentyonedemo.txt','r')
#data = file.read()
data = file.readlines()
file.close()
print(data)