user_input = int(input('hpw many test cases : '))
for i in range(user_input):
    operation = input('please enter operation string')
    operation_list = operation.split()
    print(operation_list)
    if operation_list[0] == 'add':
       first_number = int(operation_list[1])
       second_number = int(operation_list[2])
       print(first_number + second_number)
    elif operation_list[0] == 'sub':
         first_number = int(operation_list[1])
         second_number = int(operation_list[2])
         print(first_number - second_number)
    elif operation_list[0] == 'mul':
         first_number = int(operation_list[1])
         second_number = int(operation_list[2])
         print(first_number * second_number)   
    elif operation_list[0] == 'div': 
         first_number = int(operation_list[1])
         second_number = int(operation_list[2])
         print(first_number / second_number)      
             

        
