'''
num = 1

while num <= 5:
    print(num)
    num+=1
'''

'''
start = int(input("enter start num : "))
end = int(input("enter end num : "))

i= start
total = 0

while i <= end:
    total = total + i
    i+=1

print(f" sum of {start} to {end} is {total}")
'''

'''
start = int(input("enter start num : "))
end = int(input("enter end num : "))

i= start
total = 0


while i <= end:
    if i%2==0 and i%7==0:
      total = total + i
      print(i)
    i+=1

print(f" sum of {start} to {end} is {total}")
'''

num = int(input("enter a num : "))

i = 1

while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i+=1
