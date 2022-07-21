file = open ('demon.txt','r')
  data = file.readlines()
  print(data)
  def read_file(file_path):
      file = open(file_path, 'r')
      data =file.readlines ()
      map_={}
      for elem in data:
          sub, name = elem.split()
          lst = sub.split()  ['Maths', 'Shivank']
      if sub in map_:
             map_[sub].add(name)
      else:
              map_[sub] = {name}
      file.close()
      return map_
  map_ = read_file('../demo.txt')
  print(map_)
  def read_file_and_return_map(file_path):
      file = open(file_path, 'r')
      data = file.read()
      map_ = {}
      lst=[]
      count = 0
      for i in data:
          count = count + 1
          lst= i.split()
          if i in map_:
              map_[i].add(count)
          else:
              map_[i] = {count}
      file.close()
      return map_
  map_ = read_file_and_return_map('../demon.txt')
  print(map_)