#print factorial of n
n = int(input('enter a number to find its factorial'))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)    

