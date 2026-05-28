lst = ["Hello", "World", 56, 89.5, "Rahul"]

n = len(lst) -1

for i in range(n,0,-1):
    print(lst[i], end=" ")
    i+=1

for i in lst:
    print(i, end=" ")