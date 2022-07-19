lst = []
while True :
    commands = input()
    commands = commands.split()
    if commands[0] == 'stop':
        break
    elif commands[0] == 'push':
        lst.append(commands[1])
    elif commands[0] == 'pop':
        index_of_value = lst.index(commands[1])
        lst.pop(index_of_value)
    else:
        print('invalid command')
    
    print(lst)