n=int(input("Вивести всі прості числа до: "))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
for i in range(n):
    if is_prime(i):
        print(i)