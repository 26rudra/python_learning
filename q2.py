from collections import Counter
x=input()
l1=[]
for i in range(int(x)):
 
        l1.add[i]
d = Counter(l1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)    