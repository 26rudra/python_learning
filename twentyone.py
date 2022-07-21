file = open('twentyonedemo.txt','w')
file.write('This is a demo file 1')
file.writelines(['this is a demo file',
'this is a demo file'])
file.close()
