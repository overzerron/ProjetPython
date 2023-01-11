############################## Jacky ##############################
## Code par Jacky :

import library as l

###################################################################
##############################  Cha  ##############################
## Code par Cha :
subnet = 0
nombreHotes = 0
def mainCha():
    ipW,ipX,ipY,ipZ = 192,168,1,1
    mskW,mskX,mskY,mskZ = 255,255,255,0
    choix = 1
    nbBinaire = []
    nbHotes = 2
    if choix == 1 :
        ###division par nb d'hotes     
        resteDiv = masque % 2
        nbBinaire.append(resteDiv)
        masque = masque // 2
        for i in range(3):
        if resteDiv == 1 :
            resteDiv = masque % 2
            nbBinaire.append(resteDiv)
            masque = masque // 2
            if resteDiv = 0 :
                return True


###################################################################
