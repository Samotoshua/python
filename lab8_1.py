def is_column_descending(matrix, col_idx, n):
    for i in range(n - 1):
        if matrix[i][col_idx] <= matrix[i+1][col_idx]:
            return False
    return True

def build_vector(matrix, n):
    B = []
    for j in range(n):
        if is_column_descending(matrix, j, n):
            B.append(j + 1)
    return B

n = 12
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(100 - i)
    A.append(row)

B = build_vector(A, n)

for el in A:
    print(el)

print(f"Знайдено стовпців: {len(B)}")
print("Результат (по 10 у рядку):")

counter = 0
for number in B:
    print(number, end='\t')
    counter += 1
    if counter == 10:
        print()
        counter = 0