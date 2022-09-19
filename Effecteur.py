from Environement import *
import ASP
class Effecteur():
    def __init__(self,E,a,dessin):
        self.c = 0
        self.E = E
        self.a =a
        self.dessin = dessin
    def generate_aspirateur(self,img):
        self.E.map[self.a.Xasp][self.a.Yasp][0]=1
        asp = self.dessin.create_image(20+100*self.a.Xasp,20+100*self.a.Yasp,anchor=NW,image=img)
        return asp
"""
    def delete_aspirateur(self,a):
        self.E.map[self.a.Xasp][self.a.Yasp][0]=0

    def moveright(self):
        if self.a.Yasp!=4:
            self.delete_aspirateur(self.a)
            self.a.Yasp+=1
            self.generate_aspirateur(self.a)
    def moveleft(self):
        if self.a.Yasp!=0:
            self.delete_aspirateur(self.a)
            self.a.Yasp-=1
            self.generate_aspirateur(self.a)
    def moveup(self):
        if self.a.Xasp!=0:
            self.delete_aspirateur(self.a)
            self.a.Xasp-=1
            self.generate_aspirateur(self.a)
    def movedown(self):
        if self.a.Xasp!=4:
            self.delete_aspirateur(self.a)
            self.a.Xasp+=1
            self.generate_aspirateur(self.a)
"""
"""
if __name__ == "__main__":
    e = Effecteur()
    a = ASP.aspirateur()
    E = environement()
    e.generate_aspirateur(a)
    E.generate_Bijoux()
    E.generate_Dirty()
    E.affichage()
    e.moveright()
    E.affichage()
    e.movedown()
    E.affichage()
"""
