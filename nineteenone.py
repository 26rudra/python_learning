input_string = input('enter a string : ')
string_ = input_string.lower()
frequency = {}
for i in string_:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)        

    