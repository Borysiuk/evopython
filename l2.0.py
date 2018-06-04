num = int(input("input number"))
n = 0
if num > 10:
    print(num)
elif 0 < num < 5:
    n = num + 11
    if n > 13:
        print("больше на 13")
    else:
        print(n)
else:
    num -= 100
    if -200 < num < -50:
        print("число в промежутке от -200 до -50")
    else:
        print("что то пошло направо")
