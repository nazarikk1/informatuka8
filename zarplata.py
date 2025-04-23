zar = int(input("Введіть зарплату: "))
tax = zar * 0.15
pension = zar * 0.036
social = zar * 0.3676
paid = zar - tax - pension - social
vat = tax + pension + social
print("Ваша зарплата: ", paid)
print("Податки разом: ", vat)
print()
print("Прибутковий податок: ", tax)
print("Пенсійний внесок: ", pension)
print("Соціальний внесок: ", social)