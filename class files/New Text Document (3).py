a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6],
    [7, 8]
]

c = [
    [0, 0],
    [0, 0]
]

for i in range(2):
    for j in range(2):
        for k in range(2):
            c[i][j] += a[i][k] * b[k][j]

print("Matrix A:", a)
print("Matrix B:", b)
print("Multiplication of A and B:")
for row in c:
    print(row)







a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6],
    [7, 8]
]

# zip(*b) transposes matrix b into columns
c = [[sum(x * y for x, y in zip(row_a, col_b)) for col_b in zip(*b)] for row_a in a]

print("Multiplication of A and B:")
for row in c:
    print(row)
