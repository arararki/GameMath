from math import*

def for1():
    x = int(input("X = "))
    y = int(input("Y = "))
    z = int(input("Z = "))
    return (sqrt(cos(6*(x**4))+47*(y**3))-((z**8)+(x**4))+sqrt(71*(z**7)+(y**5)))

def for2():
    x = int(input("X = "))
    if x < 67:
        return 89*(((x**7)+98*(x**5))**6)+x
    if 67 <= x < 90:
        return 58*(x**7)-(x**6)
    if x >= 90:
        return 39*(31*(x**5)+cos(x))-22*(x**2)

def for3():
    n = int(input("N = "))
    m = int(input("M = "))
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            sum1 += log10(i)-17*(i**4)
            sum2 += (i**6)-(j**8)+61

    sum2 = sum2 * 61
    return sum1+sum2



print("Ответ первый: " + str("{:e}".format(for1())))
print("Ответ второй: " + str("{:e}".format(for2())))
print("Ответ третий: " + str("{:e}".format(for3())))