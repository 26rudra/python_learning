# print("Enter the number")
# l=[]
# lr=[]
# n = int(input())
# for i in range(0 ,n):
#     dabba = int(input())
#     l.append(dabba)
# print(l)
# for j in range(0,n):
#     dabalit=l[-1]
#     lr.append(dabalit)
#     l.pop(-1)
# print(lr)
# print(l)
# pehlanumberdaal = int(input())   #print greater number
# dusranumberdaal = int(input())
# if pehlanumberdaal>dusranumberdaal:
#     print("pehlanumbe rdaalis greater")
# else:
#     print("dusranumberdaal is greater") 
 
# print("Enter element in list:")
# lst=[]
# count = 0
# n = int(input())
# for i in range(0, n):
#     x = int(input())
#     lst.append(x)
# print("enter the target whose frequency is to be found")  
# target = int(input())
# for j in range(0,n):
#     if target == lst[j]:
#         count += 1 
# print(count)      
# print("enter the element")   #sum and average of array
# l=[]
# sum = 0
# n = int(input())
# for i in range(0,n):
#     x = int(input())
#     l.append(x)
# for j in range(n):
#     sum += l[j]
# print("sum is equal to : ",sum)
# avg=sum//n
# print("Average is equak to : ",avg)
    
# print("enter the elements : ")
# n = int(input())                                   #multiply all numbers in the list
# multiply = 1
# l = []
# for i in range(0 ,n):
#     x = int(input())
#     l.append(x)
# print(l)    
# for j in range(0 ,n):
#     multiply *= l[j]
# print("multiplication of all numbers in list is : ",multiply)

# print("enter the elements : ")
# n = int(input())
# smallest=1000000000
# l = []
# for i in range(0 ,n):
#     x = int(input())
#     l.append(x)
# for j in range(0 ,n):
#     if l[j]<smallest:
#         smallest = l[j]
# print("the smallest number is : ",smallest)
 


# print("enter the elements : ")
# n = int(input())
# l = []
# le=[]
# for i in range(0 ,n):     #j loop mein fas rhah hu bahut zyaada 
#     x = int(input())      #samajh nahii aa rha kya aise ho rha h plz help:)
#     l.append(x)
# for j in range(0 ,n):
#     if l[j]%2==0:
#         le.append(l[j])
# print(le)


# print("size of list : ")
# l =[]
# ln=[]
# n = int(input())
# for i in range(-n ,n):
#     x = int(input())
#     l.append(x)
# for j in range(-n ,n):    
#     if l[j]>=0:
#        ln.append(l[j])
# print(ln)       
# print("enter the size : ")
# l = []
# count = 0
# n = int(input())
# for i in range(0 ,n):
#     x = int(input())
#     l.append(x)
# print(l)
# l.sort()    
# print(l)
# for j in range(n-1,0,-1):
#     if l[j]!=l[j-1]:
#         print(l[j-1])
#         break

# print("enter the size : ")                     # remove multiple elements from list 
# l = []
# k=1
# n = int(input())
# for i in range(0 ,n):
#     x = int(input())
#     l.append(x)  
# print(l)          
# z = int(input("enter the number of elements you want to remove : "))    
# while k<=z:
#     r = int(input("enter the numbers you want to remove : "))
#     for j in range(len(l)-1):
#         if l[j] == r:
#             l.remove(r)
#     k = k+1        
# print("new list is : ",l)            

# n = int(input("enter the number of commands you want to enter : "))
# l = []
# nl = []
# for i in range(0 ,n):
#     x = input("enter command you want to execute : ")       # i should use insert instead
#     y =  x.split()
#     print(y)
#     for z in range(0 ,n):
#         l.append(y)
#     print(l[i])
#     if l[0] == 'append':
#         nl.append(l[1])
# print(nl)

#hackerrank question strings mutations
main_input = input("Enter a string : ")
l = list(main_input)
print(l)
index2chnge = int(input("Enter the index where you want to replace the character : "))
character2change = input("Enter the character you want to replace at particular index : ")
l[index2chnge] = character2change
string = ''.join(l)
print(string)


#second method for above question
# main_input = input("Enter a string : ")
# index2chnge = int(input("Enter the index where you want to replace the character : "))
# character2change = input("Enter the character you want to replace at particular index : ")
# string = main_input[:index2chnge] + character2change + main_input[index2chnge+1:]
# print(main_input)
# print(string)



    

    
                       