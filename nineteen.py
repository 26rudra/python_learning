input_string = input('enter a string : ')
frequency = {}
for i in input_string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)        

    