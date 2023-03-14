from random import randint
class Casino:
    print("Casino")
    balance=100
    print("Можливі кості - 2,3,4,5,6")
    while(balance>0):
        print("Ваш баланс: ", balance)
        cost=int(input("Введіть вашу ставку: "))

        guessNumber=list(map(int,input("Введіть 2 числа які вважаєте що випадуть: ").split()))
        coupone=[0,0]
        playersCoupone=[0,0]
        for i in range(len(coupone)):
            coupone[i]=randint(2,6)
            i+=1
        if coupone==guessNumber:
            balance+=cost*2
            print("Ваша ставка зайшла!")
        else:
            balance-=cost
            print("Невдача")
        print(coupone,"\n",guessNumber)
    else:
        print("Ви все програли!")