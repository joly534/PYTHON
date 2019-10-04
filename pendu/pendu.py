import random
PENDU_IMG = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
    ===''', '''
 +---+
 0   |
 |   |
     |
    ===''', '''
 +---+
 0   |
/|   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''']

mots = 'angle armoire banc bureau cabinet carreau chaise classe clef coin couloir dossier eau ecole entrer escalier etagere exterieur fenetre interieur lavabo '.split()

def getMotHasard(listeMot):
    motIndex = random.randint(0, len(listeMot) - 1)
    return listeMot[motIndex]

def afficherPlateau(lettresMauvaises, lettresCorrectes, motSecret):
    print(PENDU_IMG[len(lettresMauvaises)])
    print()

    print('Mauvaises lettres :', end=' ')
    for lettre in lettresMauvaises:
        print(lettre, end=' ')
    print()

    blancs = '_' * len(motSecret) 
    for i in range(len(motSecret)):
        if motSecret[i] in lettresCorrectes:
            blancs = blancs[:i] + motSecret[i] + blancs[i+1:]

    for lettre in blancs:
        print(lettre, end=' ')
    print()

def afficheLettreSaisie(dejaSaisie):

    while True:
        print('Proposez une lettre :')
        saisie = input()
        saisie = saisie.lower()
        if len(saisie) != 1:
            print('Proposez une seule lettre.')
        elif saisie in dejaSaisie:
            print('Vous avez déja proposé cette lettre.')
        elif saisie not in 'abcdefghijklmnopqrstuvwxyz':
            print('Proposez une lettre !!!')
        else:
            return saisie

def jouerEncore():
    print('Voulez-vous rejouer (oui ou non) ?')
    return input().lower().startswith('o')

print('P E N D U')
lettresMauvaises = ''
lettresCorrectes = ''
motSecret = getMotHasard(mots)
gameIsDone = False

while True:
    afficherPlateau(lettresMauvaises, lettresCorrectes, motSecret)

    saisie = afficheLettreSaisie(lettresMauvaises + lettresCorrectes)

    if saisie in motSecret:
        lettresCorrectes = lettresCorrectes + saisie

        trouverToutesLettres = True
        for i in range(len(motSecret)):
            if motSecret[i] not in lettresCorrectes:
                trouverToutesLettres = False
                break
        if trouverToutesLettres:
            print('Oui ! Le mot secret est "' + motSecret + '" ! Vous avez gagné !!!')
            gameIsDone= True
    else:
        lettresMauvaises = lettresMauvaises + saisie

        if len(lettresMauvaises) == len(PENDU_IMG) - 1:
            afficherPlateau(lettresMauvaises, lettresCorrectes, motSecret)
            print(' Vous avez épuisé toutes vos chances !\nAprès '
                    + str(len(lettresMauvaises))
                    + ' mauvaises lettres et '
                    + str(len(lettresCorrectes))
                    + 'lettres exactes, le mot secret était "'
                    + motSecret + '".')
            gameIsDone = True

    if gameIsDone:
        if jouerEncore():
            lettresMauvaises = ''
            lettresCorrectes = ''
            gameIsDone = False
            motSecret = getMotHasard(mots)
        else:
            break
