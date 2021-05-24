from math import*

def zad1():
    x = int(input("X = "))
    y = int(input("Y = "))
    z = int(input("Z = "))
    return (sqrt(cos(6*(x**4))+47*(y**3))-((z**8)+(x**4))+sqrt(71*(z**7)+(y**5)))

print("Ответ первый: " + str("{:e}".format(zad1())))