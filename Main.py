from tkinter import *

c = 100                          # Longueur d'un côté d'une case
n = 5                           # Nombre de cases par ligne et par colonne
cases = []                      # Liste contenant les objets cases

fen = Tk()
fen.title('nettoyage de map')


dessin = Canvas(fen, width = 1000, height = 1000, bg = 'white')
dessin.grid(row = 20, column = 20, columnspan=2, padx=10, pady=10)

for ligne in range(n):          # Les cases de chaque ligne seront stockées dans "transit"
    transit=[]
    for colonne in range(n):    # Conception des cases d'une ligne
        transit.append(dessin.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)       # Ajout de la ligne à la liste principale

fen.mainloop()                  # Boucle d'attente des événements



