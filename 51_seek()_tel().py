'''
with open('demo.txt', 'r') as f:
    f.seek(10)  #123456789T1112 it will skip upto 10 words

    # tell() returns the current cursor position
    print(f.tell())  
    # data = f.read(5)
    data = f.read()
    print(data)

'''

##### truncate  #####

with open('demo.txt', 'w') as f:
    f.write('Hello world')
    f.truncate(5)   # to size file by bite so file only contain "Hello"


with open('demo.txt', 'r') as f:
    print(f.read())
    
    