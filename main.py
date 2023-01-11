############################## Jacky ##############################
## Code par Jacky :

import library as l

###################################################################
##############################  Cha  ##############################
## Code par Cha :
            
def mainCha():
    ipW,ipX,ipY,ipZ = l.askIp()
    mskW,mskX,mskY,mskZ = l.askMask()
    ipBinary = l.ipToBinary(ipW,ipX,ipY,ipZ)
    mskBinary = l.ipToBinary(mskW,mskX,mskY,mskZ)
    if l.askTypeDiv() :
        somme = 32
        nbHostMax = -2
        for nb in (mskBinary):
            somme -= nb
        for i in range(somme):
            nbHostMax += 2**i
        nbHost = l.askHostNb(nbHostMax)
        
        

###################################################################
