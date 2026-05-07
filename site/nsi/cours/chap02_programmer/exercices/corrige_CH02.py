################################################################################################
########                                                                                ########
########                                                                                ########
########                    EXERCICES CHAPITRE 2                                        ########
########                                                                                ########
########                                                                                ########
################################################################################################

from random import randint
from math import isqrt


#################################################################################################
#######            EXERCICE_1

print("\nEXERCICE 1")
for element in ("Exercice", 123., True, 1e10, "False", '3,14'):
    print(element, "->", type(element))


################################################################################################
########            EXERCICE_2

print("\nEXERCICE 2")
# Erreurs corrigées :
# - 3,14  -> 3.14
# - aire-cercle -> aire_cercle
# - parenthèse manquante après la définition
# - r -> rayon
# - formule : pi * rayon ** 2
# - parenthèse manquante au print

pi = 3.14


def aire_cercle(rayon):
    return pi * rayon ** 2


print(aire_cercle(10))


################################################################################################
########            EXERCICE_3

print("\nEXERCICE 3")
a = 8
b = 14
moyenne = (a + b) / 2
print(f"Moyenne de {a} et {b} =", moyenne)


################################################################################################
########            EXERCICE_4

print("\nEXERCICE 4")
for x in (0, 10, -20):
    print(f"\nx = {x}")
    print("x < 10 and x > -10 ->", x < 10 and x > -10)
    print("x < -10 or x > 10 ->", x < -10 or x > 10)
    print("x <= 10 and x * x >= 100 ->", x <= 10 and x * x >= 100)
    print("x > -25 and x < -5 or x > 5 and x < 25 ->", x > -25 and x < -5 or x > 5 and x < 25)


################################################################################################
########            EXERCICE_5

print("\nEXERCICE 5")

print("\nProgramme 1 :")
if (12 * 2 == 24):
    print("Logique.")

print("\nProgramme 2 :")
if (12 * 2 == 24) == False:
    print("Logique.")

print("\nProgramme 3 :")
if (12 * 2 == 23) == False:
    print("Logique.")
print("Ou pas.")

print("\nProgramme 4 :")
if (12 * 2 == 23):
    print("Logique.")
else:
    print("Ou pas.")


################################################################################################
########            EXERCICE_6

print("\nEXERCICE 6")

s = 0
nb = 0
for i in range(10):
    s = s + i
    nb += 1
print("Boucle 1 :", nb, "itérations ; s =", s)

s = 1
nb = 0
for i in range(1, 6):
    s = s * i
    nb += 1
print("Boucle 2 :", nb, "itérations ; s =", s)

s = 0
nb = 0
while s < 20:
    s = s + 5
    nb += 1
print("Boucle 3 :", nb, "itérations ; s =", s)

s = 1
nb = 0
while s <= 100:
    s = s * 2
    nb += 1
print("Boucle 4 :", nb, "itérations ; s =", s)


################################################################################################
########            EXERCICE_7

print("\nEXERCICE 7")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")


################################################################################################
########            EXERCICE_8

print("\nEXERCICE 8")


def factorielle(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


n = 5
print(f"{n}! =", factorielle(n))


################################################################################################
########            EXERCICE_9

print("\nEXERCICE 9")

n = 0
a = 27
b = 5
a_initial = a
while a >= b:
    n = n + 1
    a = a - b

print("a final =", a)
print("n =", n)
print("Vérification :", a_initial, "=", b, "*", n, "+", a)

if a_initial == b * n + a and 0 <= a < b:
    print("Le résultat est bien une division euclidienne.")
else:
    print("Le résultat n'est pas correct.")


################################################################################################
########            EXERCICE_10

print("\nEXERCICE 10")
print("Aucun énoncé fourni pour l'exercice 10.")


################################################################################################
########            EXERCICE_11

print("\nEXERCICE 11")


def pair(nombre):
    return nombre % 2 == 0


print("pair(8) ->", pair(8))
print("pair(7) ->", pair(7))


################################################################################################
########            EXERCICE_12

print("\nEXERCICE 12")


a = 21


def double(x):
    print(x * 2)


a = double(a)
print("Valeur finale de a =", a)


################################################################################################
########            EXERCICE_13

print("\nEXERCICE 13")
for a in (False, True):
    for b in (False, True):
        expr1_gauche = not (a and b)
        expr1_droite = (not a) or (not b)
        expr2_gauche = not (a or b)
        expr2_droite = (not a) and (not b)
        print(f"a={a}, b={b} ->",
              expr1_gauche == expr1_droite,
              expr2_gauche == expr2_droite)


################################################################################################
########            EXERCICE_14

print("\nEXERCICE 14")


def xor(a, b):
    return (a and not b) or (not a and b)


print("xor(True, False) ->", xor(True, False))
print("xor(True, True) ->", xor(True, True))


################################################################################################
########            EXERCICE_15

print("\nEXERCICE 15")


def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


annee = 2024
print(annee, "bissextile ?", est_bissextile(annee))


def jours_mois(m, a):
    if m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if m in (4, 6, 9, 11):
        return 30
    if m == 2:
        return 29 if est_bissextile(a) else 28
    return None


print("Février 2024 :", jours_mois(2, 2024), "jours")


################################################################################################
########            EXERCICE_16

print("\nEXERCICE 16")


def nb_jours_mois(mois, annee):
    return jours_mois(mois, annee)


def nb_jours(jour, mois, annee):
    total = 0
    for m in range(1, mois):
        total += nb_jours_mois(m, annee)
    total += jour
    return total


def jour_semaine(jour, mois, annee, jour0):
    # jour0 = rang du 1er janvier (exemple : 0=lundi, 6=dimanche)
    return (jour0 + nb_jours(jour, mois, annee) - 1) % 7


print("Nombre de jours depuis le début de l'année pour le 15/3/2024 :", nb_jours(15, 3, 2024))
print("Jour de semaine pour le 15/3/2024 avec jour0=0 :", jour_semaine(15, 3, 2024, 0))


################################################################################################
########            EXERCICE_17

print("\nEXERCICE 17")
print("Pairs de 2 à 20 avec for :")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

print("Pairs de 2 à 20 avec while :")
i = 2
while i <= 20:
    print(i, end=" ")
    i += 2
print()

print("De 20 à 2 avec for :")
for i in range(20, 1, -2):
    print(i, end=" ")
print()

print("De 20 à 2 avec while :")
i = 20
while i >= 2:
    print(i, end=" ")
    i -= 2
print()


################################################################################################
########            EXERCICE_18

print("\nEXERCICE 18")


def rire_aleatoire():
    n = randint(1, 10)
    print("Ha" * n)


rire_aleatoire()


################################################################################################
########            EXERCICE_19

print("\nEXERCICE 19")
puissance = 1
compteur = 0
while puissance < 1_000_000:
    print(puissance)
    compteur += 1
    puissance *= 2
print("Nombre de puissances affichées :", compteur)


################################################################################################
########            EXERCICE_20

print("\nEXERCICE 20")


def affiche_chiffres_inverse(nombre):
    while nombre > 0:
        print(nombre % 10)
        nombre //= 10


affiche_chiffres_inverse(1234)


################################################################################################
########            EXERCICE_21

print("\nEXERCICE 21")


def fibonacci_100():
    a, b = 0, 1
    for _ in range(100):
        print(a, end=" ")
        a, b = b, a + b
    print()


fibonacci_100()

print("Rapports entre termes consécutifs :")
a, b = 1, 1
for _ in range(20):
    print(f"{b}/{a} = {b / a}")
    a, b = b, a + b


################################################################################################
########            EXERCICE_22

print("\nEXERCICE 22")


def Syracuse(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(1)



def Syracuse_etapes(n):
    etapes = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        etapes += 1
    return etapes



def Syracuse_max(n):
    maximum = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        if n > maximum:
            maximum = n
    return maximum


Syracuse(10)
print("Étapes pour 10 :", Syracuse_etapes(10))
print("Maximum atteint pour 10 :", Syracuse_max(10))


################################################################################################
########            EXERCICE_23

print("\nEXERCICE 23")


def combinaisons_2_des(somme):
    resultat = []
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            if d1 + d2 == somme:
                resultat.append((d1, d2))
    return resultat


print("Combinaisons pour obtenir 7 avec 2 dés :", combinaisons_2_des(7))

for somme in range(2, 13):
    print(f"Somme {somme} : {len(combinaisons_2_des(somme))} combinaisons")


def combinaisons_3_des(somme):
    resultat = []
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                if d1 + d2 + d3 == somme:
                    resultat.append((d1, d2, d3))
    return resultat


print("Combinaisons pour obtenir 10 avec 3 dés :", combinaisons_3_des(10))
print("Nombre de combinaisons pour 10 avec 3 dés :", len(combinaisons_3_des(10)))


################################################################################################
########            EXERCICE_24

print("\nEXERCICE 24")


def est_premier(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def est_premier_while(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True



def est_premier_rapide(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True



def premiers_m(M):
    trouves = 0
    n = 2
    while trouves < M:
        if est_premier_rapide(n):
            print(n, end=" ")
            trouves += 1
        n += 1
    print()


print("est_premier(17) ->", est_premier(17))
print("est_premier_while(18) ->", est_premier_while(18))
print("est_premier_rapide(19) ->", est_premier_rapide(19))
print("10 premiers nombres premiers :")
premiers_m(10)


################################################################################################
########            EXERCICE_25

print("\nEXERCICE 25")
# 0 = pierre, 1 = feuille, 2 = ciseaux


def jeu(a, b):
    if a == b:
        return 0
    if (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
        return 1
    return 2



def plusieurs_parties(nb_parties):
    score_a = 0
    score_b = 0
    for _ in range(nb_parties):
        a = randint(0, 2)
        b = randint(0, 2)
        resultat = jeu(a, b)
        if resultat == 1:
            score_a += 1
        elif resultat == 2:
            score_b += 1
    return score_a, score_b


score_a, score_b = plusieurs_parties(50)
print("Score joueur A :", score_a)
print("Score joueur B :", score_b)

################################################################################################
