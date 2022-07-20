#map function:   map(ord,  lst/str/[])
# def sum_of_ascii(input_string):
#     return sum(map(ord, input_string))

# map(len, [['shiv'], ['ank']])  #1   
def generate_password(username , password):
    username = username[:4]
    password = password[-4:]

    value = username + password
    return value
last_pass = generate_password('rudraksh' , '12345678')    
print(last_pass)
