num = int(input("Введите число: "))
if num > 0:
    sign = "Положительное"
elif num < 0:
    sign = "Отрицательное"
else:
    chet_nechet = "Нечетное"
    print(f"{sign}, {chet_nechet}")
