import random

nombreEssai =0

print('Bonjour ! Comment vopus apellez-vous?')
nom = input()

number = random.randint(1,20)
print('Bien, ' + nom + ',je pense à un nombre entre 1 et 20.')

for nombreEssai in range(6):
    print('Essayez de le deviner.')
    essai = input()
    essai = int(essai)

    if essai < number:
        print('Trop petit.')

    if essai > number:
        print('Trop grand.')

    if essai == number:
        break

if essai == number:
    nombreEssai = str(nombreEssai + 1)
    print('Bravo, ' + nom + ' ! Vous avez trouvé le bon nombre en ' + nombreEssai + ' essai(s) !')

if essai != number:
    number = str(number)
    print('Raté ! Le nombre auquel je pensais était ' + number + '.')

