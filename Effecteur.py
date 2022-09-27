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
        asp = self.dessin.create_image(20+100*self.a.Yasp,20+100*self.a.Xasp,anchor=NW,image=img)
        return asp

    def delete_aspirateur(self):
        self.E.map[self.a.Xasp][self.a.Yasp][0]=0

    def moveright(self):
        if self.a.Yasp!=4:
            self.E.map[self.a.Xasp][self.a.Yasp][0]=0
            self.a.Yasp+=1
            self.E.map[self.a.Xasp][self.a.Yasp][0]=1
            self.a.energie-=1
    def moveleft(self,):
        if self.a.Yasp!=0:
            self.E.map[self.a.Xasp][self.a.Yasp][0]=0
            self.a.Yasp-=1
            self.E.map[self.a.Xasp][self.a.Yasp][0]=1
            self.a.energie-=1
    def moveup(self,):
        if self.a.Xasp!=0:
            self.E.map[self.a.Xasp][self.a.Yasp][0]=0
            self.a.Xasp-=1
            self.E.map[self.a.Xasp][self.a.Yasp][0]=1
            self.a.energie-=1
    def movedown(self,):
        if self.a.Xasp!=4:
            self.E.map[self.a.Xasp][self.a.Yasp][0]=0
            self.a.Xasp+=1
            self.E.map[self.a.Xasp][self.a.Yasp][0]=1
            self.a.energie-=1

    def moveto(self,x1,y1,position):

        if(position[0]<x1):
            self.movedown()
            #position[0] -=1
        if(position[0]>x1):
            self.moveup()
            #position[0] +=1
        if(position[1]<y1):
            self.moveright()
            #position[1] +=1
        if(position[1]>y1):
            self.moveleft()
            #position[1] -=1

    def aspirer(self,line,colum):
        self.E.map[line][colum][1]=0
        self.a.aspirer+=1
        if self.E.map[line][colum][2]==1:
            self.E.map[line][colum][2]=0
            self.a.ramasser+=1
    def ramasser(self,line, colum):
        self.E.map[line][colum][2]=0
        self.a.ramasser+=1

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
