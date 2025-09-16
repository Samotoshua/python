
def sum(number):
    sum = 0
    for i in range(0,number):
        sum += ((-1)**i) / (2*i+1)
    return sum  
n=int(input("Кількість членів суми: "))
print(sum(n))