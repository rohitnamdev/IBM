<<<<<<< HEAD
def getPotentialOfWinner(potentials,k):
    winning = 0
    p0 = potentials[0]
    for i in range(1,len(potentials)):
        if winning != k:
            if p0 > potentials[i]:
                winning+=1
            else:
                p0 = potentials[i]
                winning=1
        else:
            break
    return p0
=======
def getPotentialOfWinner(potentials,k):
    winning = 0
    p0 = potentials[0]
    for i in range(1,len(potentials)):
        if winning != k:
            if p0 > potentials[i]:
                winning+=1
            else:
                p0 = potentials[i]
                winning=1
        else:
            break
    return p0
>>>>>>> 491d2fb (Add new files to IBM folder)
print(getPotentialOfWinner([1,3,2,4,5],2))