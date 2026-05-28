def min_max(lst):
    mini = min(lst)
    maxi = max(lst)

    return mini, maxi


ans = min_max([1, 2, 3, 4, 5, 6])
small, big = ans
print(f"smallet number is {small}")
print(f" biggets number is : {big} ")
