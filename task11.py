ball = int(input("Введите балл: "))

if ball >= 90:
  grade = "A"
elif ball >= 80:
  grade = "B"
elif ball >= 70:
  grade = "C"
elif ball >= 60:
  grade = "D"
  print(f"Оценка: {grade}")