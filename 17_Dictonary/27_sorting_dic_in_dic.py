student = {
    "rupesh": {"math": 87, "science": 98, "hindi": 78, "egnilsh": 76},
    "jitesh": {"math": 37, "science": 78, "hindi": 65, "egnilsh": 67},
    "riesh": {"math": 67, "science": 56, "hindi": 89, "egnilsh": 57},
}

ans = dict(sorted(student.items(), key=lambda x: x[1]["math"], reverse=True ))

ans_1 = dict(sorted(student.items(), key=lambda x: x[1]["math"] + x[1]["hindi"]+ x[1]["science"], reverse=True ))

ans_2 = dict(
    sorted(
        student.items(),
        key= lambda x : sum(x[1].values()),
        reverse=True
    )
)


print(ans_1)
print("#######################")
print()
print(ans_2)