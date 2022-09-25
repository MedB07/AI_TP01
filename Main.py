from tkinter import *
#from Environement import *
from Effecteur import *
from capteur import *
from ASP import *

c = 100                          # Longueur d'un côté d'une case
n = 5                           # Nombre de cases par ligne et par colonne
cases = []                      # Liste contenant les objets cases

fen = Tk()
fen.title('nettoyage de map')


dessin = Canvas(fen, width = 600, height = 600, bg = 'white')
dessin.grid(row = 20, column = 20, columnspan=2, padx=10, pady=10)

for ligne in range(n):          # Les cases de chaque ligne seront stockées dans "transit"
    transit=[]
    for colonne in range(n):    # Conception des cases d'une ligne
        transit.append(dessin.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)       # Ajout de la ligne à la liste principale


photo_pouss = PhotoImage(file='Image/poussiere.png')
photo_bijoux = PhotoImage(file='Image/bijoux.png')
photo_aspi = PhotoImage(file='Image/aspirateur.png')




env = environement(dessin)
f = File()
D = ASP.aspirateur(Effecteur,env,f)
e = Effecteur(env,D,dessin)
e.generate_aspirateur(photo_aspi)



env.generate_Dirty(photo_pouss)
a = env.generate_Bijoux(photo_bijoux)
# dessin.delete(D)


# D.nonInforme()
# print(env.map)
# env.affichage()
# c = capteur()
# R = c.capteurMap(env)
# print(D.nearestBDI(R))

position_finale = D.position_finale()
heuristique = D.heuristique(position_finale)
D.informe(heuristique , position_finale)
D.chemin(position_finale)
# D.excecution_informe()
env.affichage()



"""
a = dessin.create_image(20+200,20+200,anchor=NW,image=photo_pouss)
dessin.delete(a) #Deletes the rectangle
dessin.create_image(20+200,20+400,anchor=NW,image=photo_bijoux)
dessin.create_image(20,20,anchor=NW,image=photo_aspi)

"""



#fen.mainloop()                  # Boucle d'attente des événements



