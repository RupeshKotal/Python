a = input("Enter number for table : ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(f"entered value '{a}' is not valid number")
    print(e)


print("some important line of code")