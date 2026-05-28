lst = [1,2,3,4,5,6,88,7,8,9,10,12,23,46,67,78]

def even_odd(lst):

    even = []
    odd = []
    n= len(lst)

    for i in range(0,n):
        if lst[i]%2==0:
            even.append(lst[i])
        else:
          odd.append(lst[i])

    print(even)
    print(odd)

ans = even_odd(lst)

print(ans)