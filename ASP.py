from capteur import *
from Environement import *

class aspirateur:
    def __init__ (self,Effecteur,environement):
        self.autonomie = 100
        self.score = 0
        self.Xasp = 3
        self.Yasp = 3
        self.environement = environement
        self.BDI = [] # liste du chemin a faire
        self.positionDirty = []
        self.positionBijoux = []

    def getPosition(self):
        position = []
        position = [self.Xasp,self.Yasp]
        return position

    #Partie Non Informé
    def nonInforme(self):
        tableau = self.environement.map   #tableau eq grid
        file = []
        position = [self.Xasp,self.Yasp]
        # il faut remettre les parents des cases à leurs états initiaux ([-1,-1])
        for i in range(5):
            for j in range(5):
                self.environement.map[i][j][3] = [-1,-1]

        file.append(position)
        while (len(file) != 0):
            x = file[0][0]
            y = file[0][1]
            if (tableau[x][y][1] == 1):
                return [x,y]
            if (tableau[x][y][2] == 1):
                return [x,y]
            if (x!=0 and tableau[x-1][y][3]==[-1,-1]):
                tableau[x-1][y][3] = [x,y]
                file.append([x-1,y])
            if (x!=4 and tableau[x+1][y][3]==[-1,-1]):
                tableau[x+1][y][3] = [x,y]
                file.append([x+1,y])
            if (y!=0 and tableau[x][y-1][3]==[-1,-1]):
                tableau[x][y-1][3] = [x,y]
                file.append([x,y-1])
            if (y!=4 and tableau[x][y+1][3]==[-1,-1]):
                tableau[x][y+1][3] = [x,y]
                file.append([x,y+1])
            file.remove([x,y])

    def moveNotInformed(self, captMap):
        tableau = self.environement.map   #tableau eq grid
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
            print(j)













    #
    # def ElementPlusProche(self):
    #     Distance = 0
    #     ElementPlusProche = [0 0]
    #     for i in range(len(self.positionBijoux)):
    #         Distance = abs(self.position[0] - self.positionBijoux[i][0]) + abs(self.position[1] - self.positionBijoux[i][1])
    #


















