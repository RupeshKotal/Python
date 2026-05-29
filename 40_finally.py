'''
a = input("enter a index value: ")
lst = [2,32,4,5]

try:
    print(lst[int(a)])
except IndexError:
    print("index error")
finally:
    print("this line is always run")

'''

def func(a):
    lst= [3,4,5,6,]
    try:
        print(lst[int(a)])
        return 1
    except IndexError:
        print("index error")
        return 0
    finally:
        print("this line is always run")

ans = func(6)
print(ans)