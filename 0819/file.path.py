import os.path

if os.path.isfile('hi.txt'):
    print('存在')
    file = open('hi.txt', 'a')
    file.write('這是新的檔案')
    
    
else:
    print('不存在')
    file = open('hi.txt','w')
    file.write('這是新的檔案')
    