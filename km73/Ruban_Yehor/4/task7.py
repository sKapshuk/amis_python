a1 = int(input("Введите координаты X первой клетки (от 1 до 8) - "))
b1 = int(input("Введите координаты Y первой клетки (от 1 до 8) - "))
a2 = int(input("Введите координаты X второй клетки (от 1 до 8) - "))
b2 = int(input("Введите координаты X второй клетки (от 1 до 8) - "))
if (a1 % 2 == 0)&(b1 % 2 == 0):
    color1 = 1
elif (a1 % 2 != 0)&(b1 % 2 != 0):
    color1 = 1
else:
    color1 = 2
if (a2 % 2 == 0)&(b2 % 2 == 0):
    color2 = 1
elif (a2 % 2 != 0)&(b2 % 2 != 0):
    color2 = 1
else:
    color2 = 2
if (color1 == color2):
    ans = "Обе клетки одинакового цвета"
else:
    ans = "Клетки разного цвета"
print(ans)
input()
    