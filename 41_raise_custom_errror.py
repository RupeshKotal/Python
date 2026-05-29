a = int(input("ENter value between 6 and 10 : "))

if a<5 or a >10:
    raise ValueError("Entered value is not btween 6 and 10")

else:
    print(a)  