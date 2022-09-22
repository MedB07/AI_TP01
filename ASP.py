from capteur import *

class aspirateur:
    def __init__ (self,Effecteur):
        self.autonomie = 100
        self.score = 0
        self.Xasp = 3
        self.Yasp = 3

        self.positionDirty = []
        self.positionBijoux = []

    def getPosition(self):
        position = []
        position = [self.Xasp,self.Yasp]
        return position












    # def ElementPlusProche(self):
    #     Distance = 0
    #     ElementPlusProche = [0 0]
    #     for i in range(len(self.positionBijoux)):
    #         Distance = abs(self.position[0] - self.positionBijoux[i][0]) + abs(self.position[1] - self.positionBijoux[i][1])
    #












