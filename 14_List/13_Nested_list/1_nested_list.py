matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(matrix[0][1])

rows = len(matrix)
column = len(matrix[0])
for i in range(0, rows):
    for j in range(0, column):
        print(matrix[i][j], end=" ")

    print()
