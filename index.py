while True:
    n=int(input("n x n = "))
    if n<=20:
        break
A=[]
print("Введіть елементи матриці A:")
for i in range(n):
    A.append(list(map(int, input().split())))

rows = []

for i in range(2, n):
    ok = True
    for j in range(n):
        if A[i][j] != A[i-1][j] + A[i-2][j]:
            ok = False
            break
    if ok:
        rows.append(i + 1)

if rows:
    print("Номери рядків, елементи яких є сумою двох попередніх:")
    for i in range(len(rows)):
        print(rows[i])
else:
    print("Таких рядків немає.")
