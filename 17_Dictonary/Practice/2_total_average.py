marks = {
    "science" : 98,
    "english": 50,
    "hindi": 62,
    "marathi": 52,
    "math": 32
}

def percentage(students):
    total = 0
    no_of_sub = 0

    for subject, score in students.items():
        total = total + score
        no_of_sub += 1

    average = total / no_of_sub
    

    return average


ans = percentage(marks)

print(ans)    

