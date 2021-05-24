from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import *
from PIL import ImageTk, Image
import random

Rez = 100

class GAME(object):
    def __init__(self, a, b, znak, ball):
        self.a = a
        self.b = b
        self.znak = znak
        self.ball = ball

    def sumator(self):
        if (self.znak == '+'):
            #print(str(self.a) + "+" + str(self.b))
            suma_2 = int(self.a + self.b)
            return suma_2
        if (self.znak == '-'):
            #print(str(self.a) + "-" + str(self.b))
            suma_2 = int(self.a - self.b)
            return suma_2
        if (self.znak == '*'):
            #print(str(self.a) + "*" + str(self.b))
            suma_2 = int(self.a * self.b)
            return suma_2
        if (self.znak == '/'):
            #print(str(self.a) + "/" + str(self.b))
            suma_2 = int(self.a / self.b)
            return suma_2

        # suma = int(input())
        #
        # if(suma == suma_2):
        #     return 1
        # else:
        #     return 0

if __name__ == "__main__":
    a = 0
    b = 0
    znak = ''
    ball = 0

    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 4)

    if (c == 1):
        znak = '+'
    if (c == 2):
        znak = '-'
    if (c == 3):
        znak = '*'
    if (c == 4):
        znak = '/'

    start = GAME(a, b, znak, ball)