import os
from random import randrange
from tkinter import * 

fenetre = Tk()
print("*******************************************************\n*                                                     *\n*                   MEMORY CHIFFRES                   *\n*                                                     *\n*******************************************************")
nbMyster= int(randrange(1,30))
nbChoisit = int(input("Entrez un chiffre entre 1 et 30\n"))
def choisir ():
	while nbChoisit != nbMyster:
		if (nbChoisit < nbMyster):
			print("Votre chiffre est trop petit !!!")
			choisir()
		else :
			print("votre chiffre est trop grand !!!")
			choisir()
	print("Bravo Vous avez gagné !!!")


choisir ()

fenetre.mainloop()
os.system("pause")