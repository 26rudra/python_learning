def sum_of_ascii(input_string):
    sum = 0
    for i in input_string:
       var = ord(i)
       sum = sum + var
    return sum
total = sum_of_ascii('rudraksh')
print(total)    
      