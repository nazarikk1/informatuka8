def func(s, h, a, b):
    return s / ((a + b) / 2 * h)

s = int(input("Введіть площу доріжки в парку: "))
a = int(input("Введіть довжину сторони плитки a: "))
b = int(input("Введіть довжину сторони плитки b: "))
h = int(input("Введіть висоту плитки h: "))

rez = func(s, h, a, b)
print("Кількість плиток =", round(rez, 2), "шт.")