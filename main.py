import library as l

def main():
    ipW,ipX,ipY,ipZ = l.askIp()
    mskW,mskX,mskY,mskZ = l.askMask()
    ipBinary = l.ipToBinary(ipW,ipX,ipY,ipZ)
    mskBinary = l.ipToBinary(mskW,mskX,mskY,mskZ)
    somme = 32
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
    firstNullBitRank = l.getFirstNullBitRank(mskBinary)
    divNumReal = 1
    startMskIp = firstNullBitRank
    while divNumReal < nbDiv:
        divNumReal *= 2
        mskBinary[startMskIp] = 1
        startMskIp += 1
    resultMsk = "%d.%d.%d.%d"%(l.binaryToIp(mskBinary))

    addressList = []
    for j in range(firstNullBitRank,32):
        ipBinary[j]=0

    somme = 32
    for nb in (mskBinary):
        somme -= nb
    nbHostMax = 2**(somme+1)-2

    for i in range(divNumReal):
        tmpIp = ipBinary
        j=firstNullBitRank
        k=i+1
        while i>0:
            tmpIp[j]=i%2
            j+=1
            i=i//2
        tmpNet = l.Network()
        tmpNet.address = "%d.%d.%d.%d"%(l.binaryToIp(tmpIp))
        tmpNet.mask = resultMsk
        tmpNet.max_host_count = nbHostMax
        l.displayNetwork(tmpNet,k)

###################################################################

main()
