# 3 Пользователь вводит длины трех сторон треугольника (a,b,c) тип float. Напишите программу, которая проверяет,
# является ли треугольник прямоугольным (с**2=a**2+b**2) 3, 4, 5

side_a = float(input('Side a: '))
side_b = float(input('Side b: '))
side_c = float(input('Side c: '))

if side_c ** 2 == side_a ** 2 + side_b ** 2:
    print('Yes this is a Right triangle')
else:
    print('No this is not a Right triangle')

