from random import randint
class Casino:
    print("Casino")
    balance=100
    print('\x1b[6;30;42m' + "Можливі кості - 2,3,4,5,6"+'\x1b[0m')
    print('\x1b[6;30;42m' + "Якшо вказати більше чисел ніж 2, вони не будуть враховуватись\n"+'\x1b[0m')
    while(balance>0):
        print("Ваш баланс: ", balance)

        try:
            cost=int(input("Введіть вашу ставку: "))
        except(ValueError):
            print('\x1b[0;30;41m' + 'Введіть корректне число!' + '\x1b[0m')
            continue

        while(True):
            if(cost<=balance):
                break
            else:
                print('\x1b[0;30;41m' + "Ви вказали ставку більшу ніж ваш баланс!" + '\x1b[0m')
                cost=int(input("Введіть вашу ставку: "))
                continue
            
        guessNumber=list(map(int,input("Введіть 2 числа які вважаєте що випадуть: ").split()))
        coupone=[0,0]
        playersCoupone=[0,0]

        for i in range(len(coupone)):
            coupone[i]=randint(2,6)
            i+=1

        try:
            print('\x1b[0;30;43m' + "Переможні числа: ",coupone,"\n", "Ваші числа: ",guessNumber," "+ '\x1b[0m')
            if coupone==guessNumber:
                balance+=cost*2
                print("Ваша ставка зайшла!\n\n")
            elif coupone[0]==guessNumber[0]:
                balance+=cost/2
                print("Ваше перше число випало!\n\n")
            elif  coupone[1]==guessNumber[1]:
                balance+=cost/2
                print("Ваше друге число співпало!\n\n")
            else:
                balance-=cost
                print("Невдача")
        except(IndexError):
            print('\x1b[0;30;41m' + "Ви ввели лише 1 число!" + '\x1b[0m')
    else:
        print("Ви все програли!")
