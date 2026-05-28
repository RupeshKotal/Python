ph_no = "+91-9876545678"

def clean_ph(ph):
    phone = ph.replace("-","")
    phone = phone.replace("+91", "")
    return phone

print(clean_ph(ph_no))