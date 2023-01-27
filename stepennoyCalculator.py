print("Выберите операцию \n1 - умножить\n2 - поделить\n3 - сложить\n4 - вычесть\n5 - возведение в степень (первое число возводится во второе)")
operator = int(input())
if operator > 5:
    print("Вы ввели число больше 5")
    exit()
elif operator < 1:
    print("Вы ввели число меньше 1")
    exit()

n1 = input("Введите первое число: ")
if n1 == '':
    print("Вы не ввели число!")
    exit()
a=int(n1)
n2 = input("Введите второе число: ")
if n2 == '':
    print("Вы не ввели число!")
    exit()
b=int(n2)



if operator==1:
    print(a*b)
if operator==2:
    if b == 0:
       print("На ноль делить нельзя!")
       exit()
    print(a/b)
if operator==3:
    print(a+b)
if operator==4:
    print(a-b)
if operator==5:
    print(a**b)
