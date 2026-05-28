student = {
    101 : {"name" : "rahul",
    "age": 26,
    "subject": ["math", "hindi", "english"],
    "marks": [87,56,57]},
    102 : {
        "name" : "rajesh",
    "age": 26,
    "subject": ["math", "hindi", "english"],
    "marks": [87,56,57]
    },
    103 : {"name" : "rahul",
    "age": 26,
    "subject": ["math", "hindi", "english"],
    "marks": [87,56,57]}
}


for k, v in student.items():
    print(f"Roll no = {k} and name = {v["name"]} and age = {v["age"]}")

    subject_detail = v["subject"]
    marks_detail = v["marks"]

    for i in range(len(subject_detail)):
        print(f"marks in {subject_detail[i]} = {marks_detail[i]}")
        
    print("########################")
    print()

    