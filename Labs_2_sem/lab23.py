import math
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("Треугольник ABC является прямоугольным.")
else:
    angle_c = math.degrees(math.acos((a*2 + b*2 - c*2) / (2*a*b)))
    print("Угол C равен5: ", angle_c)