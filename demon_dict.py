def read_file_and_return_map(file_path):
    file = open(file_path, 'r')
    data = file.readlines()
    map_ = {}
    """
    ["Maths Shivank\n", "Maths Nootan\n"]
    """
    for elem in data:
        """
        "Maths Shivank\n"
        """
        sub, name = elem.split()
        # lst = sub.split() # ['Maths', 'Shivank']
        if sub in map_:
            map_[sub].add(name)
        else:
            map_[sub] = {name}
    file.close()
    return map_

map_ = read_file_and_return_map('demo.txt')
print(map_)