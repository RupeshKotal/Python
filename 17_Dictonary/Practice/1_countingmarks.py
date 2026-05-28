marks = {
    "science" : 98,
    "english": 50,
    "hindi": 62,
    "marathi": 52,
    "math": 32
}

for subject, score in marks.items():
    if score >= 80:
        print(f"excellent marks in {subject} you got {score}")
    elif score >= 60 and score <= 80:
        print(f"good work in {subject} you got {score} ")
    else:
        print(f"need to work on {subject} you got {score}")


passed_subject=0
failed_subject=0

for subject, score in marks.items():
    if score > 35:
        passed_subject+=1
    else:
        failed_subject+=1

print(f"you failed in {failed_subject} subject")
print(f"you passed in {passed_subject} subject")

    