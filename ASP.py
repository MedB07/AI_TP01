from capteur import *
from Environement import *
from File import *
from math import sqrt
import time

class aspirateur:
    def __init__ (self,Effecteur,environement,File):
        self.autonomie = 100
        self.score = 0
        self.Xasp = 3
        self.Yasp = 3
        self.environement = environement
        self.File =File
        self.BDI = [] # liste du chemin a faire
        self.positionDirty = []
        self.positionBijoux = []

    def getPosition(self):
        position = []
        position = [self.Xasp,self.Yasp]
        return position

######## Partie non informe####################
    def nonInforme(self):
        tableau = self.environement.map   #tableau eq grid
        position = [self.Xasp,self.Yasp]
        # il faut remettre les parents des cases à leurs états initiaux ([-1,-1])
        for i in range(5):
            for j in range(5):
                self.environement.map[i][j][3] = [-1,-1]

        self.File.addFile(position)
        while (self.File.tailleFile()!= 0):
            x = self.File.file[0][0]
            y = self.File.file[0][1]
            if (tableau[x][y][1] == 1):
                return [x,y]
            if (tableau[x][y][2] == 1):
                return [x,y]
            if (x!=0 and tableau[x-1][y][3]==[-1,-1]):
                tableau[x-1][y][3] = [x,y]
                self.File.addFile([x-1,y])
            if (x!=4 and tableau[x+1][y][3]==[-1,-1]):
                tableau[x+1][y][3] = [x,y]
                self.File.addFile([x+1,y])
            if (y!=0 and tableau[x][y-1][3]==[-1,-1]):
                tableau[x][y-1][3] = [x,y]
                self.File.addFile([x,y-1])
            if (y!=4 and tableau[x][y+1][3]==[-1,-1]):
                tableau[x][y+1][3] = [x,y]
                self.File.addFile([x,y+1])
            self.File.removeFile([x,y])



    def moveNotInformed(self, captMap):
        self.BDI = []
        tableau = self.environement.map
        chemin = []
        position = [self.Xasp,self.Yasp]
        i=10
        while(captMap != position and i != 0):
            i -= 1
            chemin.append(captMap)
            captMap = tableau[captMap[0]][captMap[1]][3]
            #print(i, position, captMap)

        chemin.reverse()
        for j in chemin:
            self.BDI.append(j)
            #print(j)

    def nearestBDI(self,listCapteur):
        m = len(listCapteur)
        self.moveNotInformed(listCapteur[0])
        l = self.BDI
        n = len(l)
        for i in range(1,m):
            self.moveNotInformed(listCapteur[i])
            if(len(self.BDI)<n):
                l = self.BDI
                n = len(l)
        return l

######## Partie informe####################

    def heuristique(self, position_finale):
        l = [[0 for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                l[i][j] = sqrt((i-position_finale[0])**2 + (j-position_finale[1])**2)
        return l

    def informe(self, heuristique, position_finale):
        tableau = self.environement.map   #tableau eq grid
        noeud_list = []   # eq list_nodes
        position = [self.Xasp,self.Yasp]
        # il faut remettre les parents des cases à leurs états initiaux ([-1,-1])
        for i in range(5):
            for j in range(5):
                tableau[i][j][3]= [-1,-1]
        noeud = [position, heuristique[position[0]][position[1]], 0]
        noeud_list.append(noeud)
        while (noeud[0]!= position_finale):
            x = noeud[0][0]
            y = noeud[0][1]
            if (x!=0 and tableau[x-1][y][3]==[-1,-1]):
                tableau[x-1][y][3] = [x,y]
                noeud_list.append([[x-1, y], heuristique[x-1][y], noeud[2]+1])
            if (x!=4 and tableau[x+1][y][3]==[-1,-1]):
                tableau[x+1][y][3] = [x,y]
                noeud_list.append([[x+1, y], heuristique[x+1][y], noeud[2]+1])
            if (y!=0 and tableau[x][y-1][3]==[-1,-1]):
                tableau[x][y-1][3] = [x,y]
                noeud_list.append([[x, y-1], heuristique[x][y-1], noeud[2]+1])
            if (y!=4 and tableau[x][y+1][3]==[-1,-1]):
                tableau[x][y+1][3] = [x,y]
                noeud_list.append([[x, y+1], heuristique[x][y+1], noeud[2]+1])
            #print(noeud_list)
            if len(noeud_list)>1:
                noeud_list.remove(noeud)
                noeud = noeud_list[0]
                for node in noeud_list:
                    if (node[1] + node[2] < noeud[1] + noeud[2]):
                        noeud = node
            if len(noeud_list)==1:
                #print(noeud_list)
                break
        #print(tableau)


    def chemin(self, position_final):
        self.BDI = []
        tableau = self.environement.map
        chemin = []
        position = [self.Xasp,self.Yasp]
        i=10
        while(position_final != position and i != 0):
            i -= 1
            chemin.append(position_final)
            position_final = tableau[position_final[0]][position_final[1]][3]

        chemin.reverse()
        for j in chemin:
            self.BDI.append(j)
        print(self.BDI)


    def position_finale(self):
        tableau = self.environement.map
        pos_cible =[]
        distance = 50
        for i in range(1,5):
            for j in range(1,5):
                if (tableau[i][j][1]== 1 or tableau[i][j][2] ==1):
                    if ((self.Yasp-i)**2+(self.Xasp-j)**2<distance):
                        distance = (self.Yasp-i)**2+(self.Xasp-j)**2
                        pos_cible.append([i,j])
        return pos_cible[len(pos_cible)-1]























