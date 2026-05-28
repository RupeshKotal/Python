# loop on dic
info = {"name": "Rupesh", "age": 18, "city": "hyd", "phone": 98765}
# Keys
"""
for sub in info.keys():
    print(f"Student {sub} is {student[sub]}")
"""
student = {"science": 98, "math": 67, "hindi": 56, "english": 89}

# values
"""
total = 0
for marks in student.values():
    total = total + marks

print(total)
"""

# items

student = {"science": 98, "math": 67, "hindi": 56, "english": 89}

for k,v in student.items():
    print(f"marks in subject {k} is {v}")
