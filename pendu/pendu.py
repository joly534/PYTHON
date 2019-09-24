from random import *
from donnees import *
from fonctions import *



print('Bonjour, bienvenue dans le jeu du pendu !!!\nles règles sont simples : il faut trouver le mot caché en faisant moins de 6 erreurs .\nAlors bonne chance !!!')
reponse = input('Voulez vous jouer ?')
while (reponse == 'oui'):
    mot = trouver_mot()
    essai = input('Entrez une lettre')
    
