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
    somme = 32
    nbAddressMax = 0
    for nb in (mskBinary):
        somme -= nb
    nbAddressMax = 2**(somme+1)
    nbNetMax = nbAddressMax / 4
    if l.askTypeDiv() :
        nbHost = l.askHostNb(nbAddressMax-2)

        i=0
        while nbHost > 2**i-2:
            i = i+1
        nbDiv = int(nbAddressMax / 2**i)
    else:
        nbDiv = l.askNetNb(nbNetMax)

    ### Division du réseau ###
    firstNullBitRank = getFirstNullBitRank(mskBinary)
    divNumReal = 1
    startMskIp = firstNullBitRank
    while divNumReal < nbDiv:
        divNumReal *= 2
        mskBinary[startMskIp] = 1
        startMskIp += 1
    resultMsk = l.binaryToIp(mskBinary)

    ipList = []
    for i in range(firstNullBitRank, startMskIp+1):
        tmpIp = ipBinary
        ipList.append(l.binaryToIp(tmpIp))
        tmpIp[i]

###################################################################

mainCha()
