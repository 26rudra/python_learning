#only add and subtract input dikhega(add 4 5 100 20   )
user_input = int(input('how many numbers : '))
sum = 0
mul = 1
for i in range(user_input):
    operation = input('please enter operation string')
    operation_list = operation.split()
    print(operation_list)
    if operation_list[0] == 'add':
        for j in range(1,len(operation_list)):
            sum = int(sum) + int(operation_list[j])
        print(sum)   
    if operation_list[0] == 'mul':
        for j in range(1,len(operation_list)):
            mul = int(mul) * int(operation_list[j])
        print(mul)      
