def factorial(number):
    for i in range(1,number):
        number*=i
    return number     
def sum(number):
    sum = 0
    for i in range(1,number+1):
        sum += 1/factorial(i)
    return sum+1  
n=int(input("Кількість членів суми: "))
print(sum(n))