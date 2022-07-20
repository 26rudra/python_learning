def alpha_freq(my_string):
    flag = 0
    for i in range(len(my_string)-1):
        if ord(my_string[i]) + 1 == ord(my_string[i+1]):
            flag += 1
    return flag
my_value = alpha_freq('abcade')
print(my_value)
