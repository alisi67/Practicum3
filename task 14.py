a=input('Введите число: ')
k=0
while k<1:
    if a.isdigit():
        print('Введено целое число: ',a)
        break
    else:
        a=input('Ошибка. Попробуйте еще раз. Введите число: ')