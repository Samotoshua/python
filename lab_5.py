while True:
    n=int(input("Введіть розмірність матриці: "))
    if(n<=20):
        break
matrix=[]

for row_element in range(n):
    row=[]
    for column_element in range(n):
        element=int(input(f"Введіть елемент матриці [{row_element+1}][{column_element+1}]: "))
        row.append(element)
    matrix.append(row)

increasing_rows = []
decreasing_columns = []

for row_element in range(n):
    is_increasing = True
    for column_element in range(n - 1):
        if matrix[row_element][column_element] >= matrix[row_element][column_element+1]:
            is_increasing = False 
            break   
    if is_increasing:
        increasing_rows.append(row_element + 1)

for column_element in range(n):
    is_decreasing = True
    for row_element in range(n - 1):
        if matrix[row_element][column_element] <= matrix[row_element+1][column_element]:
            is_decreasing = False
            break
    if is_decreasing:
        decreasing_columns.append(column_element + 1)

for num in matrix:
    print(num)
print(f"Рядки, елементи яких впорядковані за зростанням: {increasing_rows}")
print(f"Стовпчики, елементи яких впорядковані за спаданням: {decreasing_columns}")
