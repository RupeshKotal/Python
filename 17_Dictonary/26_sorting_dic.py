'''
marks = {
    "math": 85,
    "scienc": 92,
    "english": 69,
    "hindi": 65
}

# print(sorted(marks.values()))

ans = sorted(marks.items(), key= lambda x: x[1])
print(dict(ans))

ans = dict(sorted(marks.items(), key= lambda x: x[1]))

'''

marks = {
    "rajesh" : [34,56,23,65,78],
    "nuresh": [98,45,23,54,32],
    "jayesh": [43,56,78,34,46],
    "jiteh" : [67,43,56,78,43]
}

ans = dict(sorted(marks.items(), key= lambda x: x[1][1]))

ans2 = dict(sorted(marks.items(), key= lambda x: sum(x[1]), reverse= True))
print(ans2)