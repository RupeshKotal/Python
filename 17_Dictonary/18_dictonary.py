'''
marks = {
    "english": 87,
    "math" : 98,
    87: 100,
    "arry": [1,2,3,4],
    (2,4) : "surat"  #only for example
}

print(marks["english"])

ans = marks.get("mathi", "nahi hai")
print(ans)
'''


marks = {
    "english": 87,
    "math" : 98,
    "hindi": 100,
     "science" : 44
}

inp = input("enter a subject : ")
ans = marks.get(inp)

if ans is None:
    print("SUbject not exist")
else:
    print(f"Marks in subject {inp} is {ans}")