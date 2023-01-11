# Request ip adress, mask, div nb host ou div nb res, nb host, nb net
import re as R

validIpv4Regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

class Network:
	address = "x.x.x.x"
	mask = "x.x.x.x"
	first_host = "x.x.x.x"
	last_host = "x.x.x.x"
	broadcast_host = "x.x.x.x"
	max_host_count = 0
	
def ipToBinary(w,x,y,z):
    mskBin = []
    for msk in [w,x,y,z]:
        listMsk = []
        for i in range(3):
            listMsk.append(msk%2)
            msk = msk // 2
        listMsk.reverse()
        mskBin += listMsk
    return mskBin

def displayNetwork(network,id):
	print("############# Réseau no %d ############# \n\
Adresse sous-réseau :\t\t%s\n\
Masque du sous-réseau :\t\t%s\n\
Adresse du premier hôte :\t%s\n\
Adresse du dernier hôte :\t%s\n\
Adresse de diffusion :\t\t%s\n\
Nombre d'hote disponible :\t%d\n\n"%(id,network.address,network.mask,network.first_host,network.last_host,network.broadcast_host,network.max_host_count))

def askIp():
	check = input("Donnez l'adresse ip du réseau à diviser :\n")
	while not(R.fullmatch(validIpv4Regex,check)):
		print("\nAdresse réseau invalide.")
		check = input("Veuillez donner une l'adresse ip de réseau valide :\n")
	w,x,y,z = check.split(".")
	return(int(w),int(x),int(y),int(z))

def askMask():
	check = input("Donnez le masque du réseau à diviser :\n")
	while not(R.fullmatch(validIpv4Regex,check)):
		print("\nMasque invalide.")
		check = input("Donnez un masque de réseau valide :\n")
	w,x,y,z = check.split(".")
	return(int(w),int(x),int(y),int(z))

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
		print("\nCe nombre d'hôte n'est pas possible pour votre configuration réseau."%(maxNetNb))
		check = input("Donnez un masque de réseau valide :\n")
	return(int(check))

