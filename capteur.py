
class capteur():
    def capteurMap(self,Environement):
        Position_Dirty = []
        Position_Bijoux = []
        T = 5
        for i in range(T):
            for j in range(T):
                if(Environement.map[i][j][1]==1):
                    Position_Dirty.append([i,j])
                if(Environement.map[i][j][2]==1):
                    Position_Bijoux.append([i,j])
        return Position_Dirty