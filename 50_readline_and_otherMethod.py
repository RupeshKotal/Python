'''
###### Reading a file line by line ########
f = open("demo.txt", "r")

while True:
    line = f.readline()
    if not line:
        break

    m1 = line.split(",")
    lst = ['sci', 'math', 'eng']
    for i in range(0, len(m1)):
        print(f'Marks in {lst[i]} is {m1[i]}')
'''

f = open('demo.txt', 'w')
lines = ["Hello RUoesh \n", "hello jitesh \n", "hello kakesh \n"]
f.writelines(lines)
f.close()



