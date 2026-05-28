name = "potohon"
count = 0
for char in name:
    if char == "o":
        count+=1
# print(count)


for ind, char in enumerate(name, start=6):
    print(ind, char)
