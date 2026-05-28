allowed_user= {"ritesh", "rupesh", "parth"}

user = input("ENter a name : ")

if user in allowed_user:
    print(f"{user} allowed in user")
else:
    print(f"{user} not allowed to access")