############################## Jacky ##############################
## Code par Jacky :

import library as l

###################################################################
##############################  Cha  ##############################
## Code par Cha :
            
def mainCha():
    ipW,ipX,ipY,ipZ = 192, 168, 1, 0 #l.askIp()
    mskW,mskX,mskY,mskZ = 255, 255, 255, 192 #l.askMask()
    ipBinary = l.ipToBinary(ipW,ipX,ipY,ipZ)
    mskBinary = l.ipToBinary(mskW,mskX,mskY,mskZ)
    if l.askTypeDiv() :
        somme = 32
        nbAddressMax = 0
        for nb in (mskBinary):
            somme -= nb
        nbAddressMax = 2**(somme+1)

        nbHost = l.askHostNb(nbAddressMax-2)

        i=0
        while nbHost > 2**i-2:
            i = i+1
        nbDiv = int(nbAddressMax / 2**i)
    else:
        nbDiv = l.askNetNb()

###################################################################
