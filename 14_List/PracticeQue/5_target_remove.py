nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 6]
"""
# it will give wrong result
def target_remove(lst,target):
    for num in lst:
        if num == target:
            lst.remove(num)

    return lst


ans = target_remove(nums,1)

print(ans)

"""


# def target_remove(lst, target):
#     new_list = []
#     for num in lst:
#         if num != target:
#             new_list.append(num)

#     return new_list


# ans = target_remove(nums, 1)

# print(ans)



def remove_occ(lst, target):
    while target in lst:
        lst.remove(target)

remove_occ(nums,1)