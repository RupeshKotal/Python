lst = [1,2,3,2,3,3,4,4,6,6,4,4,6,7,7,8,8,5,5]

def remove_duplicate(lst):

    new_list = []
    
    n = len(lst)

    for i in range(0,n):
        if lst[i] not in new_list:
            new_list.append(lst[i])

    return new_list

ans = remove_duplicate(lst)

print(ans)