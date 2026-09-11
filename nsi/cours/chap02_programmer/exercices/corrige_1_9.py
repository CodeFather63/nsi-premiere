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

