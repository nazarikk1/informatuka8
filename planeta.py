Nazva = input("Назва планети? ")  
R = float(input("Радіус орбіти? "))  
V = float(input("Швидкість руху? "))  

Period = 2 * 3.14 * R / (V * 24)  

print("Період обертання =", round(Period, 3), "діб")  
print("Рік на планеті", Nazva, "триває", round(Period, 3), "діб")