
annee = 2019
p="x"
e=" "

print(34*p)
print(p, e*30, p)
print(p, e, "Voici un petit test python", e, p)
print(p, e*30, p)
print(34*p)
print(" ")
print("Quel est votre age ?")
saisieAge = int(input())
print("Avez vous déja fêté votre anniversaire cette année ?")
saisieAniv = input()
while saisieAniv != "oui" or saisieAniv != "non":
	if saisieAniv == "oui" or saisieAniv == "non":
		if saisieAniv == "oui":
			resultat = annee - saisieAge
			print("Vous êtes né en :", resultat)
			break
		else:
			resultat = annee - saisieAge - 1
			print("Vous êtes né en :", resultat)
			break
	else:
		print("Veuillez répondre par oui ou non")
		saisieAniv = input()	



print("\nFin du programme !!!\n")
input()