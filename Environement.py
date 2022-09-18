from aspirateur import *

class environement:
    def __init__(self):
        self.map = [[[0,0,0] for i in range(5)] for i in range(5)]

    def generate_Dirty(self,x,y):
        self.map[x][y][1] = 1
    def delete_Dirty(self,x,y):
        self.map[x][y][1]=0
    def generate_Bijoux(self,x,y):
        self.map[x][y][2]=1
    def delete_Bijoux(self,x,y):
        self.map[x][y][2] = 0
    def generate_aspirateur(self,a):
        self.map[a.Xasp][a.Yasp][0]=1
    def delete_aspirateur(self,a):
        self.map[a.Xasp][a.Yasp][0]=0
    def moveright(self):
        if a.Yasp!=4:
            self.delete_aspirateur(a)
            a.Yasp+=1
            self.generate_aspirateur(a)
    def moveleft(self):
        if a.Yasp!=0:
            self.delete_aspirateur(a)
            a.Yasp-=1
            self.generate_aspirateur(a)
    def moveup(self):
        if a.Xasp!=0:
            self.delete_aspirateur(a)
            a.Xasp-=1
            self.generate_aspirateur(a)
    def movedown(self):
        if a.Xasp!=4:
            self.delete_aspirateur(a)
            a.Xasp+=1
            self.generate_aspirateur(a)
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
    a = aspirateur()
    e.generate_aspirateur(a)
    e.affichage()
    e.moveright()
    e.affichage()
    e.moveup()
    e.affichage()
    e.moveleft()
    e.affichage()
    e.movedown()
    e.affichage()

