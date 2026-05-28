# without .reverse() and slicing(::-1)

lst = [1,2,3,4,5]
new_list= []

n = len(lst) - 1

for i in range(n,0-1,-1):
    new_list.append(lst[i])
    

print(new_list)
