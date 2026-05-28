text = "helLo World"


#case conversion
'''
capital = text.upper()
print(capital)

print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

'''


#checkin content

# print(text.isalpha())  #false, beacuse it content space
# print(text.isdigit()) #false
# print(text.isalnum()) #either num or alpabhet
# print(text.isspace())


# print(text.startswith("h"))
# print(text.endswith('d'))


age = input("Enter your age : ")

if age.isdigit():
    if int(age) > 18:
        print("you are eligible")

    else:
        print("not elible")
else:
    print("enter validate age")

