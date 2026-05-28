# i = 1

# while i <= 10:
#    print(i)
#    if i == 5:
#       break
#    i += 1


#Continue

i = 1

'''
while i <= 10:
   print(i)
   if i == 5:
      continue  #Infinity loop
   i += 1
'''

'''
while i <= 10:
   print(i)
   i += 1
   if i == 5:
      continue 
   print(i)

'''


total = 0

while True:
    num = int(input("Enter your nnumber positive number will be added and negitive will be ignored : "))
    if num == 0:
        break
    if num <=0:
        continue
    total = total + num

print(total)



   