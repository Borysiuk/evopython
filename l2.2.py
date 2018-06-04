key = int(input("Сохраните пароль 4 цифры"))
krf = int(input("Введите пароль"))
n = 5
if krf == key:
    print("Доступ открыт")
else:
    while n != 0:
        print("Количество попыток", n)
        krf = int(input("Введите пароль"))
        n -= 1
    print("Ваши попытке исчерпаны")
