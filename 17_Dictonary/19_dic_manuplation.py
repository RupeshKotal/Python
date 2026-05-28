student = {"name": "Rupesh", "age": 18, }

#update
student["name"] = "Anirudh"

#add
student["gender"] = "male"

#add multiple value
student.update({"city": "Hyd", "phone": 98765 })


#remove
student.pop("age")

#remove all
# student.clear()
del student

print(student)