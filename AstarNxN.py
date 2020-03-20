import random
import math

trou = 9

taquin = [4,1,2,
          7,9,3,
          8,5,6]

nbSwap = 0
mouvementPrecedent = 0
n = math.sqrt(len(taquin))



def legalMoove(tab): # renvoi une liste de mouvements possible en fonction de la position du trou
    index = tab.index(trou)
    if index == 0:  # coin haut gauche
        return [1, 3]
    if index == (n - 1):  # coin haut droit
        return [-1, 3]
    if index == ((n * n) - 1) - (n - 1):  # coin bas gauche
        return [-3, 1]
    if index == (n * n) - 1:  # coin bas droit
        return [-3, -1]
    if 0 < index < (n - 1):  # bordure haute
        return [-1, 3, 1]
    if ((n * n) - 1) - (n - 1) < index < (n * n) - 1:  # bordure basse
        return [-3, -1, 1]
    if index % n == 0:  # bordure gauche
        return [-3, 1, 3]
    if index % n == (n - 1):  # bordure droite
        return [-3, -1, 3]
    else:  # centre
        return [-3, -1, 1, 3]

def choixMouvement(list): # choix meilleurs mouvement entre h1 et h2
    plusCourt = testSucc(taquin,list[0])
    meilleurMouv = list[0]
    for s in range(0,len(list)):
        if testSucc(taquin,list[s]) > plusCourt:
            meilleurMouv = list[s]
            plusCourt = testSucc(taquin,list[s])
    return meilleurMouv

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def nombreElemOk(list): #h2
    count = 0
    for s in range(0, len(list)):
        if s+1 == list[s]:
            count += 1
    return count

def distOrigine(nb):
    target = (nb - 1)
    pos = taquin.index(nb)
    dist = 0

    if pos == target:
        return dist

    elif pos < target:
        while target - 3 >= pos:
            dist += 1
            target -= 3
        dist += abs(pos - target)
        return dist

    elif pos > target:
        while pos - 3 >= target:
            dist += 1
            pos -= 3
        dist += abs(pos - target)
        return dist

def SommeDist(list): #h1
    somme = 0
    for s in range(0,len(list)):
        somme += distOrigine(list[s])
    return somme

def testSucc(list, mouv): #test h1 + h2
    tab = list.copy()
    posX = tab.index(trou)
    swapPositions(tab, posX, mouv + posX)
    return SommeDist(tab) + nombreElemOk(tab)


print("taquin : ",taquin)
print("nombre elem ok : ",nombreElemOk(taquin))
print("trou : ", trou)
print("position trou : ", taquin.index(trou))
print("taille : ", n)



def afficherTaquin():
    tab1 = []
    tab2 = []
    tab3 = []

    tab1.append(taquin[0])
    tab1.append(taquin[1])
    tab1.append(taquin[2])
    tab2.append(taquin[3])
    tab2.append(taquin[4])
    tab2.append(taquin[5])
    tab3.append(taquin[6])
    tab3.append(taquin[7])
    tab3.append(taquin[8])

    print(tab1)
    print(tab2)
    print(tab3)
    print()


chemin = []

while nombreElemOk(taquin) !=  len(taquin):
        posX = taquin.index(trou)
        mouvementPossible = legalMoove(taquin)

        if nbSwap == 0:
            mouvementChoisi = choixMouvement(mouvementPossible)
        elif nbSwap > 0:
            mouvementPossible.remove(mouvementPrecedent * -1)
            mouvementChoisi = choixMouvement(mouvementPossible)

        mouvementPrecedent = mouvementChoisi
        chemin.append(mouvementChoisi)
        posElementChoisi = posX + mouvementChoisi
        swapPositions(taquin, posX, posElementChoisi)
        nbSwap += 1

        print()
        afficherTaquin()
        print("étapes nb : ", nbSwap)
        print("somme distance du taquin : ", SommeDist(taquin))
        print("nb elements ok : ", nombreElemOk(taquin))
        print("choix possible : ", legalMoove(taquin))
        print("")





print()
print("chemin : ", chemin)