marks = {
    "math" : 48,
    "science": 89,
    "hindi" : 67,
    "english": 35,
    "geo": 98,
    "social": 69,
    "sanskrit": 78
}

ans = sorted(
        marks.items(),
        key= lambda x: x[1],
        reverse= True
    )

top = ans[:3]

for i in range(0,len(top)):
    print(f'{top[i][0]} = {top[i][1]}')