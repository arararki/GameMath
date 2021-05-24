from math import*

def zad1():
    x = int(input("X = "))
    y = int(input("Y = "))
    z = int(input("Z = "))
    return (sqrt(cos(6*(x**4))+47*(y**3))-((z**8)+(x**4))+sqrt(71*(z**7)+(y**5)))

def zad2():
    x = int(input("X = "))
    if x < 67:
        return 89*(((x**7)+98*(x**5))**6)+x
    if 67 <= x < 90:
        return 58*(x**7)-(x**6)
    if x >= 90:
        return 39*(31*(x**5)+cos(x))-22*(x**2)

print("Ответ второй: " + str("{:e}".format(zad2())))

print("Ответ первый: " + str("{:e}".format(zad1())))