# Примеры логических операторов
age = 25
has_license = True

# AND - оба условия должны быть True
can_drive = (age >= 18) and has_license
print(can_drive)  # True

# OR - хотя бы одно условие True
is_weekend = True
is_holiday = False
can_rest = is_weekend or is_holiday
print(can_rest)  # True

# NOT - инверсия результата
is_raining = True
can_walk = not is_raining
print(can_walk)  # False