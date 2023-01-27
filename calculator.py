numbers = int(input("Количество чисел, участвующих в операции: "))
print("Выберите операцию \n1 - умножить\n2 - поделить\n3 - сложить\n4 - вычесть")
operator = int(input())
if operator > 4:
    print("Вы ввели число больше 4")
    exit()
elif operator < 1:
    print("Вы ввели число меньше 1")
    exit()


counter = 0
pervCount = 0
finalValue = 1
number = 0
a = 0
CheckNumber =0
b = 0



while numbers > counter:
    counter+=1
    CheckNumber = input(f"Введите {counter} число: ")
    if CheckNumber == '':
        print("Вы не ввели число!")
        exit()
    pervCount=int(CheckNumber)
    while pervCount==0:
                print("На ноль делить нельзя!")
                pervCount=int(input(f"Введите {counter} число: "))
                
                
    if operator == 1:
        if (numbers <= counter):
            finalValue *=pervCount
            print(finalValue)
        else:
            counter+=1
            b = input(f"Введите {counter} число: ")
            if b == '':
                print("Вы не ввели число!")
                exit()
            number=int(b)
            finalValue *= pervCount * number
            print(finalValue)
    elif operator == 2:
        if (numbers <= counter):
            if pervCount==0:
                print("На ноль делить нельзя!")
                exit()
            finalValue /=pervCount
            print(finalValue)
        elif a !=0:
            counter+=1
            b = input(f"Введите {counter} число: ")
            if b == '':
                print("Вы не ввели число!")
                exit()
            number=int(b)
            if number==0:
                print("На ноль делить нельзя!")
                exit()
            finalValue = a / (pervCount / number)
            a = finalValue
            print(finalValue)
        else:
            counter+=1
            b = input(f"Введите {counter} число: ")
            if b == '':
                print("Вы не ввели число!")
                exit()
            number=int(b)
            if number==0:
                print("На ноль делить нельзя!")
                exit()
            finalValue = pervCount / number
            a = finalValue
            print(finalValue)
    elif operator == 3:
        if (numbers <= counter):
            finalValue +=pervCount
            print(finalValue)
        else:
            counter+=1
            if finalValue == 1:
                finalValue-=1
            b = input(f"Введите {counter} число: ")
            if b == '':
                print("Вы не ввели число!")
                exit()
            number=int(b)
            finalValue += pervCount + number
            print(finalValue)
    elif operator == 4:
        if (numbers <= counter):
            finalValue -=pervCount
            print(finalValue)
        elif a !=0:
            counter+=1
            b = input(f"Введите {counter} число: ")
            if b == '':
                print("Вы не ввели число!")
                exit()
            number=int(b)
            finalValue = a - pervCount - number
            a = finalValue
            print(finalValue)
        else:
            counter+=1
            b = input(f"Введите {counter} число: ")
            if b == '':
                print("Вы не ввели число!")
                exit()
            number=int(b)
            finalValue = pervCount - number
            a = finalValue
            print(finalValue)   