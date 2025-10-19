while True:
    n=int(input("n x n = "))
    if n<=20:
        break
A=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input(f"{i+1} рядок {j+1} елемент: ")))
    A.append(row)

def sum_of_row(row):
    summa=0
    for i in range(len(row)):
        summa+=row[i]
    return summa

for i in range(n-2):
        if(sum_of_row(A[i+2])==sum_of_row(A[i+1])+sum_of_row(A[i])):
            print(sum_of_row(A[i+2]),"=",sum_of_row(A[i+1]),'+',sum_of_row(A[i]))
            print(i+3, "рядок = ", i+2, "рядок + ", i+1, "рядок")

for i in range(n):
    print(A[i])