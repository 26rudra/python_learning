# x = 5
# y = 6
# total = x + y
# print(total)
# first_name = 'rudr aksh'
# last_name = 'bohra'
# print(first_name.islower())
# print(first_name.upper())
# print(first_name.rsplit())
# print(first_name.isalpha())
# sentence = f'{first_name} {last_name} is a coder'
# print(sentence)
# lst = [1,2,3,4,5,'hello',['a','b','c']]
# print(lst[0])
# print(lst[-1])
# print(lst[-2][0])
# lst[0] = 100
# print(lst)
# random_number_list = [10,32,20,45,42,41,69]
# random_number_list.sort()
# print(random_number_list)
# random_number_list.sort( reverse = True)
# print(random_number_list)
# random_number_list.append('hello world')
# print(random_number_list)
# s = 'Rudraksh'
# ls = list(s)
# print(ls)
# ls.sort()
# print(ls)
# a = [1,2,3]
# b = [3,4,5]
# c = a + b
# print(c)
# a.append(b)
# print(a)
# a.extend(b)
# print(a)
#aaj set aur dictionary krvaya(7/16/22) [print:reserved in python,print_:not reserved in py]
# map_ = {
#     'first_name': 'Rudraksh',
#     'second_name': 'Bohra',
#     'company':'regex'
# }
#print(map_['first_name'])
#print(map_.get('age','not found'))
#print(map_.get('company','not found'))
# company = map_.pop('company')
# print(company)
# print(map_)
# looping syntax
#lst = [1,2,3,4,5,6,6,7,8,4,10]
# for i in lst[2:]:
#for i in 'Rudraksh':
# for i in range(1, 10):
#     print(i)
# for i in range(0,len(lst),2):
#print(lst[i])
# for i in[1,2,3]:
#  for j in ['a','b','c']:
#   print(i,j)
# lst = [1,3,7,24,16,27,19]
              #prime no in python assignment
# fname = 'rudraksh'
# lname = 'bohra'
# if fname == 'rudraksh' and lname == 'bohra':
#     print('yes first name is rudraksh')
# else:
#     print('yes last name is bohra')
# if fname == 'rudraksh' or lname == 'bohra':
#     print('yes first name is rudraksh')
# else:
#     print('no first name is not rudraksh')
# if 'rudraksh' in ['a','b','c']:
#     print('rudraksh is in list')
# elif 'p' in 'rudraksh':
#     print('p is in rudraksh')
# elif 'k' in 'rudraksh':
#     print('k is in rudraksh')
# else:
#     print('kuch nahi mila')
# take an input from an user and print the users whose ascii value is even
# s = input('enter a string:')
# for i in s:
#     if ord(i) % 2 == 0:
#       print(i)
  #/take 5 inputs from the users and append all those inputs in the list
# s = int(input('enter any integer value'))
# lst=[]
# for i in range(s):
#     num = input()
#     lst.append(num)
# print(lst)
#/ take n*2 input from user in 2,2 sets
no_of_elem = int(input())
map_={
  'int':[],
  'str':[],
  'float':[],
  
}

for i in range(no_of_elem):
  dt = input('enter data type: ')
  value=input('enter value for above data type: ')
  if dt =='str':
    map_['str'].append(value)
  elif dt == 'int':
    map_['int'].append(int(value))
  elif dt == 'float':
    map_['float'].append(float(value))
  else:
    print('please initialize a empty list for {dt}'.format(dt))
print(map_)


    
 








