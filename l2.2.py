key_save = int(input("Сохраните пароль, введите 4 цифры и нажмите Enter: "))
key_enter = int(input("Введите пароль: "))
n = 5
if key_enter == key_save:
    print("Доступ открыт")
else:
    while n != 0:
        print("Количество попыток", n)
        key_enter = int(input("Введите пароль: "))
        if key_enter == key_save:
            print("Доступ открыт")
            break
        else:
            n -= 1
    else:
        print("Ваши попытки исчерпаны")
