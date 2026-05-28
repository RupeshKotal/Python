#Union ( | or .union() ) and intersection ( & or .interesction() )

math_student = {"pratik", "sidhant", "tunner", "utkarsh", "hemu"}
scinec_student = {"tunner", "utkarsh", "rushi", "shubham"}

#Student in both math and science
print(math_student & scinec_student)
# print(math_student.intersection(scinec_student))

#All student
print(math_student | scinec_student)
# print(math_student.union(scinec_student))