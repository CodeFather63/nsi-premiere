########################
######## PARTIE A  #####
########################

def carre(n:int):

    print("X " * n)

    for i in range(n-2):
        print("X " + "  " * (n-2) + "X")

    print("X " * n)


#carre(12)

########################
######## PARTIE B  #####
########################
def croix(n):
    m = n // 2
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == m or j == m:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()


def diagonale(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()


def origami(n):
    m = n // 2
    for i in range(n):
        for j in range(n):
            if (
                i == 0 or i == n - 1 or j == 0 or j == n - 1
                or (i >= m and i == j)
                or (i + j == n - 1 and i >= m)
            ):
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()

def origami(cote):
    """ Affiche un carré avec une diagonale et une demi-diagonale"""
    mediane = cote // 2 # Important à définir quand `cote` n'est pas impair.
    
    # Les lignes de notre dessin.
    for i in range(cote):
        if i == 0 or i == cote-1:
            # Première ou dernière ligne.
            print("X " * cote)
        else:
            # On construit les lignes restantes caractère par caractère.
            ligne = ""
            for j in range(cote):
                # Extrémités :
                if j == 0 or j == cote-1:
                    ligne += "X "

                # Diagonale montante :
                elif j == cote - i - 1:
                    ligne += "X "
                
                # Diagonale descendante dans la seconde moitié :
                elif j == i and i >= mediane:
                    ligne += "X "
                    
                else:
                    ligne += "  "
                
            print(ligne)


def triangle(n):
    for i in range(n - 1):
        for j in range(2 * n - 1):
            if j == n - 1 - i or j == n - 1 + i:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()

    for j in range(2 * n - 1):
        print("X", end=" ")
    print()




def triangle_inv(n):
    largeur = 2 * n - 1

    for i in range(n):
        for j in range(largeur):
            if i == 0 or i == n - 1:
                print("X", end=" ")
            else:
                k = n - 1 - i
                if j <= k or j >= largeur - 1 - k:
                    print("X", end=" ")
                else:
                    print(" ", end=" ")
        print()

        
'''croix(12)
diagonale(12)
origami(12)
triangle(12)
triangle_inv(12)'''

########################
######## PARTIE C  #####
########################
import random


def sapin(n):

    print(" " * n + "*")

    for i in range(n):

        print(" "*(n-i) + "/", end="")

        for j in range(2*i):

            if random.random() < 0.2:
                print("o", end="")
            else:
                print("'", end="")

        print("\\")

    for i in range(3):
        print(" " * n + "|||")


sapin(12)
