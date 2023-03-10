import re as R

validIpv4Regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

class Network:
	address = "x.x.x.x"
	mask = "x.x.x.x"
	max_host_count = 0

def ipToBinary(w,x,y,z):
    mskBin = []
    for msk in [w,x,y,z]:
        listMsk = []
        for i in range(8):
            listMsk.append(msk%2)
            msk = msk // 2
        listMsk.reverse()
        mskBin += listMsk
    return mskBin

def binaryToIp(ipBin):
	listIp = []
	for j in range(4):
		cmp = 0
		for i in range(8):
			cmp += (ipBin[i+8*j]*2**(7-i))
		listIp.append(cmp)
	return listIp[0], listIp[1], listIp[2], listIp[3]

def displayNetwork(network,id):
	print("############# Réseau no %d ############# \n\
Adresse sous-réseau :\t\t%s\n\
Masque du sous-réseau :\t\t%s\n\
Nombre d'hote disponible :\t%d\n\n"%(id,network.address,network.mask,network.max_host_count))

def askIp():
	check = input("Donnez l'adresse ip du réseau à diviser :\n")
	while not(R.fullmatch(validIpv4Regex,check)):
		print("\nAdresse réseau invalide.")
		check = input("Veuillez donner une l'adresse ip de réseau valide :\n")
	w,x,y,z = check.split(".")
	return(int(w),int(x),int(y),int(z))

def checkMaskValidity(binMask):
	i=0
	valid = True
	while i<32 and binMask[i]==1:
		i=i+1
	valid = i!=32
	while i<32 and valid:
		valid = valid and binMask[i]==0
		i=i+1
	return valid


def askMask():
	check = input("Donnez le masque du réseau à diviser :\n")
	valid = R.fullmatch(validIpv4Regex,check)
	if(valid):
		w,x,y,z = check.split(".")
		w,x,y,z = int(w),int(x),int(y),int(z)
		valid = checkMaskValidity(ipToBinary(w,x,y,z))

	while not(valid):
		print("\nMasque invalide.")
		check = input("Donnez un masque de réseau valide :\n")
		w,x,y,z = check.split(".")
		w,x,y,z = int(w),int(x),int(y),int(z)
		valid = checkMaskValidity(ipToBinary(w,x,y,z))


	return(w,x,y,z)

def askTypeDiv():
	check = input("Voulez-vous diviser par nombre d'hôte (1) ou par nombre de sous-réseaux (2) ?\n")
	while not(R.fullmatch(r"^(1|2)$",check)):
		print("\nChoix indisponible.")
		check = input("Voulez-vous diviser par nombre d'hôte (1) ou par nombre de sous-réseaux (2) ?\n")
	return(check == "1")

def askHostNb(maxHostNb):
	check = input("Combien d'hôtes souhaitez-vous ?\n")
	while not(R.fullmatch(r"^\d+$",check) and int(check)>0 and int(check)<=maxHostNb):
		print("\nCe nombre d'hôte n'est pas possible pour votre configuration réseau.")
		check = input("Combien d'hôtes souhaitez-vous (de 0 à %d) ?\n"%(maxHostNb))
	return(int(check))

def askNetNb(maxNetNb):
	check = input("Combien de sous-réseaux souhaitez-vous ?\n")
	while not(R.fullmatch(r"^\d+$",check) and int(check)>0 and int(check)<=maxNetNb):
		print("\nCe nombre d'hôte n'est pas possible pour votre configuration réseau.")
		check = input("Combien de sous-réseaux souhaitez-vous (de 1 à %d) ?\n"%(maxNetNb))
	return(int(check))

def getFirstNullBitRank(mskBinary):
		i=0
		valid = True
		while i<32 and mskBinary[i]==1:
			i=i+1
		return i
