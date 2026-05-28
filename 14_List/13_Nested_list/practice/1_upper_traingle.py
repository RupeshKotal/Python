'''
1 * *
4 5 *
7 8 9
'''

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

r = len(matrix)
c = len(matrix[0])
#upper traingle
'''
for i in range(0,r):
    for j in range(0,c):
        if i >= j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")

    print()
'''

# lower traingle

'''
for i in range(0,r):
    for j in range(0,c):
        if i <= j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")

    print()
'''


#Diagonal

'''
for i in range(0,r):
    for j in range(0,c):
        if i == j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")

    print()
'''

# reverse- digonal


for i in range(0,r):
    for j in range(0,c):
        if i + j == r-1:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")

    print()

