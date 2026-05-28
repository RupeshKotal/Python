num = [2,3,4,2,1,3,457,43,4,56,67,5,4,654,6]

new_list = sorted(num)

# print(new_list, id(new_list), num)

print("##############")
num.sort()
print(num)

print("##############")
num.sort(reverse=True)
print(num)

print("##############")
num.reverse()
print(num)


num.clear()

print(num)
