maListe = []
i = a = 0

print("Entrez un chiffre")
maListe.append(input())
while i<4:
	print("Entrez un chiffre")
	maListe.append(input())
	print(maListe)
	i+=1

while a<100:
	print("Xx"*a)
	a += 1 
	if a == 100:
		while a>0:
			a-=1
input()