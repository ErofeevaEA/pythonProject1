"""Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат."""

x = int(input ('введите x: '))
y = int(input ('введите y: '))
z = int(input ('введите z: '))
def checkPredicate():
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result


if checkPredicate == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")