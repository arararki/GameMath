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

    def PRINT(self):
        def chec():
            if (self.ball == 11):
                global Rez
                Rez = 1
                window.destroy()
            if (self.ball == -11):
                Rez = 0
                window.destroy()
    
            def Potverd():
            s = suma.get()
            if not s.isdigit():
                mb.showerror(
                    "Ошибка",
                    "Должно быть введено число")
            else:
                if (start.sumator() == int(suma.get())):
                    self.ball += 1

                    self.a = random.randint(1, 100)
                    self.b = random.randint(1, 100)
                    c = random.randint(1, 4)

                    if (c == 1):
                        self.znak = '+'
                    if (c == 2):
                        self.znak = '-'
                    if (c == 3):
                        self.znak = '*'
                    if (c == 4):
                        self.znak = '/'
                else:
                    self.ball -= 1

                    self.a = random.randint(1, 100)
                    self.b = random.randint(1, 100)
                    c = random.randint(1, 4)

                    if (c == 1):
                        self.znak = '+'
                    if (c == 2):
                        self.znak = '-'
                    if (c == 3):
                        self.znak = '*'
                    if (c == 4):
                        self.znak = '/'

                lbl1.config(text=str(self.a) + " " + str(self.znak) + " " + str(self.b) + " = ")
                # lbl2.config(text=str(self.znak))
                # lbl3.config(text=str(self.b))
                lbl4.config(text="Ваши баллы: " + str(self.ball))

                chec()