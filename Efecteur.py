from Environement import *
import ASP
class Effecteur():
    def __init__(self):
        self.c = 0
    def generate_aspirateur(self,a):
        E.map[a.Xasp][a.Yasp][0]=1
    def delete_aspirateur(self,a):
        E.map[a.Xasp][a.Yasp][0]=0
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


if __name__ == "__main__":
    e = Effecteur()
    a = ASP.aspirateur()
    E = environement()
    e.generate_aspirateur(a)
    E.generate_Bijoux(1,1)
    E.generate_Dirty(1,4)
    E.affichage()
    e.moveright()
    E.affichage()
    e.movedown()
    E.affichage()

