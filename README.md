# Projet Python de division de réseau par masques

Le but de ce projet est de recréer le diviseur de réseaux par bits de [ce site](https://www.sebastienadam.be/ipcalculator/) développé par Sebastien ADAM.

Dans ce projet, on se concentrera principalement sur la partie calculatoire de la division de réseaux et on expliquera dans les grandes lignes la logique des fonctions utilitaires.

1. Division en sous réseaux
0. Calcul du nombre d'hôtes et conversion
0. Fonctions supplémentaires

## 1/ La division en sous réseaux

## 2/ Le calcul du nombre d'hôte et conversion

## 3/ Fonctions supplémentaires

1. Demandes utilisateur

	L'interface CLI nous permet de bloquer l'utilisateur lorsqu'il donne des informations erronnées. C'est pourquoi la protection des données entrantes est importante pour ne pas calculer de divisions impossibles comme par exemple un masque `0.0.0.0` ou `255.254.1.0` est impossible.

	C'est la raison pour laquelle, toutes les demandes faites à l'utilisateur sont bloquées et bouclent tant qu'il n'a pas donné d'informations justes.

	```Python
	def askTypeDiv():
		# Demande
		check = input("Voulez-vous diviser par nombre d'hôte (1) ou par nombre de sous-réseaux (2) ?\n")
		# Vérification
		while not(R.fullmatch(r"^(1|2)$",check)):
			# Message d'erreur et demande
			print("\nChoix indisponible.")
			check = input("Voulez-vous diviser par nombre d'hôte (1) ou par nombre de sous-réseaux (2) ?\n")
			# Retour de valeurs formatées
		return(check == "1")
	```
1. Conversion en binaire des adresses IP

	Afin de vérifier la validité du masque et faire les calculs détaillés au point __3/__, nous avons créé un convertisseur d'adresse IP en chaîne de caractères `string` vers quatre variables entières nommées `w`, `x`, `y` et `z`.

	Chaque variable sera ensuite convertie en binaire par bit de poids le plus faible à celui le plus fort via division par deux, puis la liste résultante sera inversée et concaténée dans une liste que l'on retourne à la fin de la conversion.

	```Python
	def ipToBinary(w,x,y,z):
		# Liste de bits
		mskBin = []
		# Pour chaque partie du masque
		for msk in [w,x,y,z]:
			# Liste temporaire de bits
			# (du plus faibe au plus fort)
			listMsk = []
			for i in range(8):
				listMsk.append(msk%2)
				msk = msk // 2
				# Conversion en binaire puis inversion
				listMsk.reverse()
				# Concaténation
				mskBin += listMsk
		return mskBin
	```

1. Vérification de la validité du masque

	Pour la vérification du masque, il a fallu lire dans l'ordre tous les bits à `1` jusqu'au premier `0` et si l'on trouve le moindre `1` à partir de ce premier `0`, le masque est invalidé. Si il n'y a que des bits à `1` dans la liste, le masque est également invalidé.

	Dès que la liste est parcourue en entier avec au moins un `0` en fin de liste, le masque est validé.

	```Python
	def checkMaskValidity(binMask):
		i=0
		valid = True
		# Tant que les bits sont à 1,
		# on parcours la liste
		while i<32 and binMask[i]==1:
			i=i+1

		# Si on a atteint la fin de la liste,
		# masque invalide (aucun zéro trouvés)
		valid = i<32
		while i<32 and valid:
			# Au premier 1 trouvé,
			# le masque est invalidé
			valid = valid and binMask[i]==0
			i=i+1
		# Booléen sur la validité du masque
		return valid
	```
