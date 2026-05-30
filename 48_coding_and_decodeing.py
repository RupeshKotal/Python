password = input("enter your pasword : ")
decode = input("enter 1 to encrypt or 0 for as it is : ")

encrypt = True if decode == "1" else False

print(encrypt)

if encrypt:
    new_pass = []
    lst_pass = password.split()
    for pswd in lst_pass:
        if len(pswd) >= 3:
            r1 = "abc"
            r2= "xyz"
            new_word = r1+ pswd[1:] + pswd[0] + r2
            new_pass.append(new_word)
        else:
            small_word = pswd[::-1]
            new_pass.append(small_word)

    encrypt_pass = " ".join(new_pass)
    print(encrypt_pass)

else:
    print(password)
