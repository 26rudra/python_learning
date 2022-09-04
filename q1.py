

import math
 

def digSum( n):
    sum = 0
     
    while(n > 0 or sum > 9):
     
        if(n == 0):
            n = sum
            sum = 0
         
        sum += n % 10
        n /= 10
     
    return sum
 
# Driver method
n = input("enter number: ")
x=n.split(" ")
q=x[0]
w=x[1]
if  ((int(digSum(int(q))))== (int(digSum(int(w))))):
    print(True)
else:
    print(False)    
    
