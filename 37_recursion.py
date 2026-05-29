# factorial(7) = 7*6*5*4*3*1
# factorial(6) = 6*5*4*3*1

# factrial(n) = n * factorial(n-1)

'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))

'''


def fibonnaci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    

print(fibonnaci(6))

