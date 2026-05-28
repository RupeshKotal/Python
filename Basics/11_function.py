# def greet(name):
#     print(f"Hello {name}")

# greet("rupesh")


def factor():
    num = int(input("Enter your number : "))
    for i in range(1, num+1):
        if num%i==0:
            print(i, end=" ")

factor()