email = 'info@ac' \
'cen.in'
email_2= 'rupeshgmail.com'

def email_valid(email):
    if email.count('@') == 1 and "." in email:
        return True
    else:
        return False
    
print(email_valid(email_2))
