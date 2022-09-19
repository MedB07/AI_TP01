import random
from tkinter import *
class environement:
    def __init__(self):
        self.map = [[[0,0,0] for i in range(5)] for i in range(5)]


    def generate_Dirty(self):
        x = random.randint(0,4)
        y= random.randint(0,4)
        self.map[x][y][1] = 1

    def delete_Dirty(self):
        x = random.randint(0,4)
        y= random.randint(0,4)
        self.map[x][y][1]=0
    def generate_Bijoux(self):
        x = random.randint(0,4)
        y= random.randint(0,4)
        self.map[x][y][2]=1
    def delete_Bijoux(self):
        x = random.randint(0,4)
        y= random.randint(0,4)
        self.map[x][y][2] = 0

    def affichage(self):
        print(" ###############################")
        for L in self.map:
            print(" # ", end = '')
            for l in L :
                if l[0] == 0:
                    print(" ",end = '')
                else :
                    print("A", end = '')
                if l[1] == 0:
                    print(" ",end = '')
                else :
                    print("D",end = '')
                if l[2] == 0:
                    print(" ",end = '')
                else :
                    print("B",end = '')
                print(" # ", end = '')
            print("")
        print(" ###############################")




if __name__ == "__main__":

    e = environement()
    e.generate_Bijoux()
    e.generate_Dirty()
    e.generate_Bijoux()
    e.generate_Dirty()
    e.generate_Bijoux()
    e.generate_Dirty()
    e.affichage()

