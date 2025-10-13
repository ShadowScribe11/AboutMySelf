month = int(input("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    season = "Зима"
    if month == 3 or month == 4 or month == 5:
        season = "Весна"
        if month == 6 or month == 7 or month == 8:
            season = "Лето"
            if month == 9 or month == 10:
                season = "Осень"
print(season)

