################################################################################################
########                                                                                ########
########                    CORRIGÉ — EXERCICES CHAPITRE 2                              ########
########                                                                                ########
########   Ce corrigé n'utilise que ce qui a été vu en cours :                          ########
########   variables, conditions, boucles for / while et fonctions.                     ########
########   Pas de listes ni de tuples.                                                  ########
########                                                                                ########
################################################################################################

from random import random   # random() renvoie un nombre décimal entre 0 (inclus) et 1 (exclu)
from math import sqrt       # sqrt(n) renvoie la racine carrée de n (utile à l'exercice 24)


################################################################################################
########            EXERCICE 1 — Types des valeurs

print("\n===== EXERCICE 1 =====")
# type(valeur) indique le type d'une valeur.
print("Exercice", "->", type("Exercice"))   # str   : texte entre guillemets
print(123., "->", type(123.))               # float : le point en fait un nombre décimal
print(True, "->", type(True))               # bool  : booléen (True ou False)
print(1e10, "->", type(1e10))               # float : 1e10 = 1 × 10^10, écriture scientifique
print("False", "->", type("False"))         # str   : entre guillemets, ce n'est PAS un booléen
print('3,14', "->", type('3,14'))           # str   : entre apostrophes, c'est du texte


################################################################################################
########            EXERCICE 2 — Trouver et corriger les erreurs

print("\n===== EXERCICE 2 =====")
# Erreurs du code de départ :
# 1) pi = 3,14         -> en Python, la virgule décimale s'écrit avec un POINT : 3.14
# 2) aire-cercle       -> le tiret est interdit dans un nom (c'est une soustraction) : aire_cercle
# 3) def ...(rayon)    -> il manque les deux-points ":" à la fin de la ligne def
# 4) r                 -> la variable r n'existe pas, le paramètre s'appelle rayon
# 5) pi * r * 2        -> formule fausse : l'aire est pi × rayon² donc pi * rayon ** 2
# 6) print(...         -> il manque la parenthèse fermante

pi = 3.14


def aire_cercle(rayon):
    return pi * rayon ** 2


print(aire_cercle(10))   # affiche 314.0


################################################################################################
########            EXERCICE 3 — Moyenne de deux nombres

print("\n===== EXERCICE 3 =====")
a = 8
b = 14
# Les parenthèses sont indispensables : la division est prioritaire sur l'addition.
# a + b / 2 donnerait 8 + 7 = 15, et non la moyenne.
moyenne = (a + b) / 2
print("Moyenne de", a, "et", b, "=", moyenne)   # 11.0


################################################################################################
########            EXERCICE 4 — Évaluer des expressions booléennes

print("\n===== EXERCICE 4 =====")
# Pour ne pas recopier trois fois les mêmes lignes, on écrit une fonction
# qu'on appelle pour chaque valeur de x.
# Rappel : "and" est prioritaire sur "or" (comme × sur +).


def evalue(x):
    print("x =", x)
    print("  x < 10 and x > -10                     ->", x < 10 and x > -10)
    print("  x < -10 or x > 10                      ->", x < -10 or x > 10)
    print("  x <= 10 and x * x >= 100               ->", x <= 10 and x * x >= 100)
    print("  x > -25 and x < -5 or x > 5 and x < 25 ->", x > -25 and x < -5 or x > 5 and x < 25)


evalue(0)     # True  False False False
evalue(10)    # False False True  True
evalue(-20)   # False True  True  True


################################################################################################
########            EXERCICE 5 — Qu'affichent ces programmes ?

print("\n===== EXERCICE 5 =====")

print("Programme 1 :")
if (12 * 2 == 24):              # 24 == 24 est True : on entre dans le if
    print("Logique.")           # -> affiche "Logique."

print("Programme 2 :")
if (12 * 2 == 24) == False:     # True == False est False : on n'entre pas
    print("Logique.")           # -> n'affiche rien

print("Programme 3 :")
if (12 * 2 == 23) == False:     # False == False est True : on entre
    print("Logique.")
print("Ou pas.")                # pas indenté : hors du if, s'affiche toujours
                                # -> affiche "Logique." puis "Ou pas."

print("Programme 4 :")
if (12 * 2 == 23):              # False : on va dans le else
    print("Logique.")
else:
    print("Ou pas.")            # -> affiche "Ou pas."


################################################################################################
########            EXERCICE 6 — Nombre de tours de boucle et valeur finale de s

print("\n===== EXERCICE 6 =====")
# On ajoute un compteur nb pour vérifier le nombre de tours.

# Boucle 1 : i prend les valeurs 0, 1, ..., 9 -> 10 tours ; s = 0+1+...+9 = 45
s = 0
nb = 0
for i in range(10):
    s = s + i
    nb = nb + 1
print("Boucle 1 :", nb, "tours ; s =", s)

# Boucle 2 : i prend les valeurs 1, 2, 3, 4, 5 (6 exclu) -> 5 tours ; s = 1×2×3×4×5 = 120
s = 1
nb = 0
for i in range(1, 6):
    s = s * i
    nb = nb + 1
print("Boucle 2 :", nb, "tours ; s =", s)

# Boucle 3 : s vaut 5, 10, 15, 20 -> 4 tours ; à 20 la condition s < 20 est fausse
s = 0
nb = 0
while s < 20:
    s = s + 5
    nb = nb + 1
print("Boucle 3 :", nb, "tours ; s =", s)

# Boucle 4 : s vaut 2, 4, 8, 16, 32, 64, 128 -> 7 tours ; 128 > 100 donc on s'arrête
s = 1
nb = 0
while s <= 100:
    s = s * 2
    nb = nb + 1
print("Boucle 4 :", nb, "tours ; s =", s)


################################################################################################
########            EXERCICE 7 — Table de multiplication par 7

print("\n===== EXERCICE 7 =====")
# range(1, 11) donne 1, 2, ..., 10 (la borne de fin est exclue).
for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)


################################################################################################
########            EXERCICE 8 — Factorielle

print("\n===== EXERCICE 8 =====")
# n! = 1 × 2 × 3 × ... × n
# On part de 1 (élément neutre de la multiplication, surtout pas 0 !)
# et on multiplie par chaque entier de 2 à n.
n = 5
factorielle = 1
for i in range(2, n + 1):       # n + 1 car la borne de fin est exclue
    factorielle = factorielle * i
print(n, "! =", factorielle)    # 120


################################################################################################
########            EXERCICE 9 — Division euclidienne par soustractions

print("\n===== EXERCICE 9 =====")
n = 0
a = 27
b = 5
a_initial = a                   # on garde la valeur de départ, car a va être modifié

while a >= b:                   # tant qu'on peut encore retirer b...
    n = n + 1                   # ... on compte une soustraction de plus
    a = a - b                   # ... et on retire b

# a. a vaut 27, 22, 17, 12, 7, puis 2 : à la fin a = 2
print("a final =", a)
print("n =", n)

# b. On a retiré b exactement n fois, donc a_initial = b × n + a,
#    et on s'est arrêté quand a < b : a est le reste, n est le quotient.
#    Ici : 27 = 5 × 5 + 2.

# c. Vérification avec un if
if a_initial == b * n + a and a < b:
    print("Vérifié :", a_initial, "=", b, "x", n, "+", a)
else:
    print("Erreur dans le calcul.")


################################################################################################
########            (Pas d'exercice 10 dans l'énoncé)
################################################################################################


################################################################################################
########            EXERCICE 11 — Fonction pair

print("\n===== EXERCICE 11 =====")
# Un nombre est pair si le reste de sa division par 2 vaut 0.
# La comparaison "nombre % 2 == 0" vaut déjà True ou False :
# on peut la renvoyer directement, pas besoin de if.


def pair(nombre):
    return nombre % 2 == 0


print("pair(8) ->", pair(8))    # True
print("pair(7) ->", pair(7))    # False


################################################################################################
########            EXERCICE 12 — print n'est pas return

print("\n===== EXERCICE 12 =====")
a = 21


def double(x):
    print(x * 2)                # AFFICHE 42, mais ne RENVOIE rien


a = double(a)                   # l'appel affiche 42, puis a reçoit ce que renvoie la fonction
print("Valeur finale de a =", a)

# b. Le programme affiche 42 (pendant l'appel de double).
# a. Une fonction sans return renvoie la valeur spéciale None.
#    Donc a vaut None à la fin, et non 42.
#    Pour que a vaille 42, il faudrait écrire : return x * 2


################################################################################################
########            EXERCICE 13 — Lois de De Morgan

print("\n===== EXERCICE 13 =====")
# a et b sont des booléens : il n'y a que 4 couples possibles.
# On écrit une fonction qui teste les deux identités pour un couple,
# puis on l'appelle pour les 4 couples.


def teste(a, b):
    gauche1 = not (a and b)
    droite1 = (not a) or (not b)
    gauche2 = not (a or b)
    droite2 = (not a) and (not b)
    print("a =", a, " b =", b, " -> identité 1 :", gauche1 == droite1,
          " identité 2 :", gauche2 == droite2)


teste(True, True)
teste(True, False)
teste(False, True)
teste(False, False)
# Les 8 résultats valent True : les deux identités sont toujours vraies.

# Pour aller plus loin : avec deux boucles imbriquées.
# "i == 1" vaut False quand i vaut 0, et True quand i vaut 1.
print("Version avec boucles :")
for i in range(2):
    for j in range(2):
        teste(i == 1, j == 1)


################################################################################################
########            EXERCICE 14 — OU exclusif

print("\n===== EXERCICE 14 =====")
# Table de vérité :   a      b      xor
#                     True   True   False
#                     True   False  True
#                     False  True   True
#                     False  False  False
# xor est vrai exactement quand a et b sont DIFFÉRENTS : c'est l'opérateur !=


def xor(a, b):
    return a != b
    # Autre écriture possible, avec and / or / not :
    # return (a and not b) or (not a and b)


print("xor(True, True)   ->", xor(True, True))     # False
print("xor(True, False)  ->", xor(True, False))    # True
print("xor(False, True)  ->", xor(False, True))    # True
print("xor(False, False) ->", xor(False, False))   # False


################################################################################################
########            EXERCICE 15 — Années bissextiles et jours d'un mois (programmes)

print("\n===== EXERCICE 15 =====")

# a. Règle : divisible par 4, sauf si divisible par 100, sauf si divisible par 400.
#    "divisible par 4" se teste avec le reste : annee % 4 == 0
annee = 1900
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(annee, "est bissextile")
else:
    print(annee, "n'est pas bissextile")    # 1900 : divisible par 100 mais pas par 400
# À tester aussi avec 2024 (oui), 2023 (non), 2000 (oui).

# b. Nombre de jours du mois m de l'année a
m = 2
a = 2024
if m == 2:
    # Février : cas particulier, on réutilise la règle de la question a
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        jours = 29
    else:
        jours = 28
elif m == 4 or m == 6 or m == 9 or m == 11:
    jours = 30
else:
    jours = 31
print("Le mois", m, "de", a, "a", jours, "jours")   # 29


################################################################################################
########            EXERCICE 16 — Les mêmes calculs sous forme de fonctions

print("\n===== EXERCICE 16 =====")

# a. On transforme les programmes de l'exercice 15 en fonctions :
#    on remplace les print par des return pour pouvoir réutiliser les résultats.


def est_bissextile(annee):
    """ retourne True si l'année est bissextile """
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0


def nb_jours_mois(mois, annee):
    """ retourne le nombre de jours du mois """
    if mois == 2:
        if est_bissextile(annee):       # on réutilise la fonction précédente
            return 29
        else:
            return 28
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
        return 30
    else:
        return 31


print("est_bissextile(2000) ->", est_bissextile(2000))   # True
print("nb_jours_mois(2, 2023) ->", nb_jours_mois(2, 2023))   # 28

# b. On additionne les jours de tous les mois AVANT le mois en cours,
#    puis on ajoute les jours déjà passés dans le mois en cours.


def nb_jours(jour, mois, annee):
    """ retourne le nombre de jours depuis le début de l'année """
    total = 0
    for m in range(1, mois):            # mois 1, 2, ..., mois-1
        total = total + nb_jours_mois(m, annee)
    total = total + jour
    return total


print("nb_jours(15, 3, 2024) ->", nb_jours(15, 3, 2024))   # 31 + 29 + 15 = 75

# c. jour0 = jour de la semaine du 1er janvier (0 = lundi, 1 = mardi, ..., 6 = dimanche).
#    Le 1er janvier correspond à nb_jours = 1, donc le décalage depuis le 1er janvier
#    est nb_jours - 1. Le % 7 permet de "revenir au début" après dimanche.


def jour_semaine(jour, mois, annee, jour0):
    """ retourne le jour de la semaine (0 = lundi, ..., 6 = dimanche) """
    return (jour0 + nb_jours(jour, mois, annee) - 1) % 7


# Le 1er janvier 2024 était un lundi (jour0 = 0).
print("jour_semaine(15, 3, 2024, 0) ->", jour_semaine(15, 3, 2024, 0))   # 4 = vendredi


################################################################################################
########            EXERCICE 17 — Nombres pairs avec for et while

print("\n===== EXERCICE 17 =====")
# end=" " remplace le retour à la ligne par un espace : tout s'affiche sur une ligne.

# a. range(début, fin exclue, pas) : un pas de 2 ne donne que les pairs.
print("a. for :     ", end=" ")
for i in range(2, 21, 2):       # 21 et pas 20, sinon 20 serait exclu
    print(i, end=" ")
print()

# b. Les 4 briques du while : départ, condition, action, progression.
print("b. while :   ", end=" ")
i = 2                           # départ
while i <= 20:                  # condition
    print(i, end=" ")           # action
    i = i + 2                   # progression (sans elle : boucle infinie !)
print()

# c. En décroissant : le pas est négatif et la fin (exclue) est 1.
#    Sans le signe -, range(20, 1, 2) serait vide : rien ne s'afficherait.
print("c. for :     ", end=" ")
for i in range(20, 1, -2):
    print(i, end=" ")
print()

print("c. while :   ", end=" ")
i = 20
while i >= 2:
    print(i, end=" ")
    i = i - 2
print()


################################################################################################
########            EXERCICE 18 — Rire aléatoire

print("\n===== EXERCICE 18 =====")
# random() est entre 0 et 1 (exclu) ; × 10 donne entre 0 et 10 (exclu) ;
# int() arrondit vers le bas : entier de 0 à 9 ; + 1 : entier de 1 à 10.
# "ha" * n répète la chaîne n fois. On met la majuscule au premier "ha".


def rire_aleatoire():
    n = int(random() * 10) + 1
    print("Ha" + "ha" * (n - 1) + " !")


rire_aleatoire()
rire_aleatoire()
rire_aleatoire()


################################################################################################
########            EXERCICE 19 — Puissances de 2 inférieures à un million

print("\n===== EXERCICE 19 =====")
# On ne sait pas à l'avance combien il y en a : boucle while.
puissance = 1                   # 2 puissance 0
compteur = 0                    # b. compteur initialisé AVANT la boucle
while puissance < 1000000:
    print(puissance, end=" ")
    compteur = compteur + 1     # b. un de plus à chaque tour
    puissance = puissance * 2   # on passe à la puissance suivante
print()
print("Nombre de puissances :", compteur)   # 20 (de 2^0 à 2^19 = 524288)


################################################################################################
########            EXERCICE 20 — Chiffres d'un nombre à partir du dernier

print("\n===== EXERCICE 20 =====")
# nombre % 10  -> dernier chiffre      (1234 % 10 = 4)
# nombre // 10 -> on retire ce chiffre (1234 // 10 = 123)
# Quand il n'y a plus de chiffres, nombre vaut 0 : on s'arrête.
nombre = 1234
while nombre > 0:
    print(nombre % 10)
    nombre = nombre // 10


################################################################################################
########            EXERCICE 21 — Suite de Fibonacci

print("\n===== EXERCICE 21 =====")
# Chaque terme est la somme des deux précédents : il faut garder DEUX valeurs en mémoire.

# a. Les 100 premiers termes : 0, 1, 1, 2, 3, 5, 8, ...
a = 0
b = 1
for i in range(100):
    print(a, end=" ")
    c = a + b                   # terme suivant
    a = b                       # on décale : a prend l'ancienne valeur de b...
    b = c                       # ... puis b prend le nouveau terme
    # L'ordre compte : si on écrivait b = c avant a = b,
    # a recevrait le nouveau terme et on perdrait l'ancien b.
print()

# b. Même boucle, en affichant aussi le rapport b / a entre deux termes consécutifs.
#    Au premier tour a vaut 0 : on ne peut pas diviser par 0, on saute ce cas.
#    Le rapport se rapproche de 1.618... (le nombre d'or).
a = 0
b = 1
for i in range(100):
    if a != 0:
        print(a, " rapport", b, "/", a, "=", b / a)
    else:
        print(a, " (pas de rapport : division par 0)")
    c = a + b
    a = b
    b = c


################################################################################################
########            EXERCICE 22 — Suite de Syracuse

print("\n===== EXERCICE 22 =====")
# On ne sait pas combien d'étapes il faudra pour atteindre 1 : boucle while.
# On utilise // (division entière) pour que n reste un entier (5 et non 5.0).


# a. Afficher la suite
def Syracuse(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:          # n pair
            n = n // 2
        else:                   # n impair
            n = 3 * n + 1
    print(1)                    # la boucle s'arrête à 1 sans l'afficher : on l'ajoute


Syracuse(10)                    # 10 5 16 8 4 2 1


# b. Afficher aussi le nombre d'étapes : un compteur, comme à l'exercice 19
def Syracuse_etapes(n):
    etapes = 0
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        etapes = etapes + 1
    print(1)
    print("Nombre d'étapes :", etapes)


Syracuse_etapes(10)             # 6 étapes


# c. Renvoyer le plus grand nombre atteint : une variable "maximum"
#    mise à jour quand on rencontre un nombre plus grand.
def Syracuse_max(n):
    maximum = n                 # au départ, le plus grand vu est n lui-même
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n > maximum:
            maximum = n
    return maximum


print("Maximum atteint pour 10 :", Syracuse_max(10))   # 16
print("Maximum atteint pour 27 :", Syracuse_max(27))   # 9232 !


################################################################################################
########            EXERCICE 23 — Combinaisons de dés

print("\n===== EXERCICE 23 =====")
# Deux boucles imbriquées sur range(1, 7) testent toutes les paires (d1, d2) : 6 × 6 = 36.


# a. Toutes les combinaisons de deux dés pour une somme cible
def combinaisons_2_des(cible):
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            if d1 + d2 == cible:
                print("(", d1, ",", d2, ")", end=" ")
    print()


print("Somme 7 :", end=" ")
combinaisons_2_des(7)           # 6 combinaisons

# b. Pour toutes les sommes de 2 à 12 : une boucle de plus autour
for cible in range(2, 13):
    print("Somme", cible, ":", end=" ")
    combinaisons_2_des(cible)


# c. Trois dés : trois boucles imbriquées (6 × 6 × 6 = 216 cas)
def combinaisons_3_des(cible):
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                if d1 + d2 + d3 == cible:
                    print("(", d1, ",", d2, ",", d3, ")", end=" ")
    print()


print("Somme 10 avec 3 dés :", end=" ")
combinaisons_3_des(10)


# d. Seulement le nombre de combinaisons : on remplace le print par un compteur
def nombre_combinaisons_2_des(cible):
    compteur = 0
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            if d1 + d2 == cible:
                compteur = compteur + 1
    return compteur


for cible in range(2, 13):
    print("Somme", cible, ":", nombre_combinaisons_2_des(cible), "combinaisons")


################################################################################################
########            EXERCICE 24 — Nombres premiers

print("\n===== EXERCICE 24 =====")
# n est premier s'il est supérieur ou égal à 2 et n'a aucun diviseur entre 2 et n-1.


# a. Avec une boucle for
def est_premier(n):
    if n < 2:                   # 0 et 1 ne sont pas premiers
        return False
    for i in range(2, n):
        if n % i == 0:          # i divise n : n n'est pas premier
            return False        # return arrête immédiatement la fonction
    return True                 # aucun diviseur trouvé


# b. Avec une boucle while : la condition de la boucle dit elle-même quand s'arrêter.
#    On avance i tant qu'il ne divise pas n ; on s'arrête au premier diviseur trouvé.
#    Si ce premier diviseur est n lui-même, n est premier.
def est_premier_while(n):
    if n < 2:
        return False
    i = 2
    while i < n and n % i != 0:
        i = i + 1
    return i == n


# c. Si n = a × b avec a <= b, alors a <= racine de n.
#    Donc si n a un diviseur, il en a forcément un inférieur ou égal à racine de n :
#    inutile de chercher plus loin. Pour 1 000 003 : 1000 tests au lieu d'un million.
def est_premier_rapide(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):   # + 1 pour inclure la racine elle-même
        if n % i == 0:
            return False
    return True
    # Variante sans sqrt : i = 2, puis while i * i <= n : ...


# d. Les M premiers nombres premiers : on teste les entiers un par un
#    et on compte ceux qui sont premiers jusqu'à en avoir M.
def premiers(M):
    trouves = 0
    n = 2
    while trouves < M:          # on ne sait pas jusqu'où aller : while
        if est_premier_rapide(n):
            print(n, end=" ")
            trouves = trouves + 1
        n = n + 1
    print()


print("est_premier(17)        ->", est_premier(17))          # True
print("est_premier_while(18)  ->", est_premier_while(18))    # False
print("est_premier_rapide(19) ->", est_premier_rapide(19))   # True
print("Les 10 premiers nombres premiers :", end=" ")
premiers(10)                    # 2 3 5 7 11 13 17 19 23 29


################################################################################################
########            EXERCICE 25 — Pierre-feuille-ciseaux

print("\n===== EXERCICE 25 =====")
# Codage des coups : 0 = pierre, 1 = feuille, 2 = ciseaux
# Qui gagne : la pierre casse les ciseaux, la feuille enveloppe la pierre,
#             les ciseaux coupent la feuille.


def nom_coup(n):
    """ bonus : renvoie le nom du coup pour un affichage lisible """
    if n == 0:
        return "pierre"
    elif n == 1:
        return "feuille"
    else:
        return "ciseaux"


# a. jeu(a, b) renvoie 0 en cas d'égalité, 1 si le joueur A gagne, 2 si le joueur B gagne.
def jeu(a, b):
    if a == b:
        return 0
    # Les 3 cas où A gagne, regroupés avec or
    if (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
        return 1
    return 2                    # tous les autres cas : B gagne


# b. Simuler plusieurs parties et compter les scores.
#    int(random() * 3) donne un entier au hasard : 0, 1 ou 2.
#    Les compteurs sont créés AVANT la boucle, sinon ils seraient remis à 0 à chaque tour.
def plusieurs_parties(nb_parties):
    score_a = 0
    score_b = 0
    egalites = 0
    for i in range(nb_parties):
        a = int(random() * 3)
        b = int(random() * 3)
        resultat = jeu(a, b)
        if resultat == 1:
            score_a = score_a + 1
        elif resultat == 2:
            score_b = score_b + 1
        else:
            egalites = egalites + 1
    # Affichage APRÈS la boucle : seulement les scores finaux
    print("Joueur A :", score_a, " Joueur B :", score_b, " Égalités :", egalites)


# Vérification de jeu() sur un exemple
print(nom_coup(0), "contre", nom_coup(2), "->", jeu(0, 2))   # 1 : la pierre gagne

# c. 50 tours
plusieurs_parties(50)

################################################################################################
