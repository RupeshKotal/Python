marks = {"science": 98, "english": 50, "hindi": 62, "marathi": 52, "math": 32}

print(len(marks))

print(sum(marks.values()))

print("######### minumum values ###########")
print(min(marks.values()))

print("######### maxium values ###########")
print(max(marks.values()))

print()
print("######### sorted by key ###########")
print(sorted(marks))

print()
print("################ sorted by item #########")
print(sorted(marks.items()))
