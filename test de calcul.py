print("entrez un premier nombre")
a = int(input())
print("entrez un deuxieme nombre")
b = int(input())
print("voulez vous enclencher la phase de décodage : oui ou non ?")
c = input()

if c == "oui":
	while c == "oui":
		d = a*b
		print (d)
		a = d
else:
	print(" T'es pas drole !!!")
input()