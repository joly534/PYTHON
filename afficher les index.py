ch = 'true'

while (ch == 'true'):
    choix = input('voulez vous jouer ? ')    
    if choix == 'oui':
        saisie = input('tapez un mot : ')
        nb_lettre = len(saisie)
        for lettre in saisie:
            print('Voici les lettres composants le mot que vous avez saisie : ' + lettre)



        print('\nle mot saisi est : ' + saisie)
        print('le mot saisie contient ' + str(nb_lettre) + ' lettres ')
    elif (choix != 'oui') & (choix != 'non'):
        print('Vous devez répondre par oui ou par non')
    else:
        ch = 'false'
    

