#Normal way

square = {}

for i in range(1,6):
    square[i] = i*i

# print(square)


#Dicnory Comprehension

square_1 = {i: i*i for i in range(1,6)}
# print(square_1)


#with condition

marks = {
    "math" : 48,
    "science": 89,
    "hindi" : 67,
    "english": 35
}

top = {k: v for k,v in marks.items() if v >= 50}
print(top)
