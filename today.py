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