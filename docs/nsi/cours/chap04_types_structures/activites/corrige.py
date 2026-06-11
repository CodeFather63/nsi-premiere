# coding: utf-8

##### ##### #####   ##### ##### ##### ##### ##### #####
#####     EXERCICES — TUPLES, LISTES ET DICTIONNAIRES
##### ##### #####   ##### ##### ##### ##### ##### #####


###################################
#####                         #####
#####      EXERCICE 1         #####
#####         Points          #####
#####                         #####
###################################

def milieu(p1: tuple, p2: tuple) -> tuple:
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

##### test #####
# print(milieu((0, 0), (4, 6)))   # (2.0, 3.0)


###################################
#####                         #####
#####      EXERCICE 2         #####
#####          Dates          #####
#####                         #####
###################################

def anterieur(d1: tuple, d2: tuple) -> bool:
    # On compare année, puis mois, puis jour
    j1, m1, a1 = d1
    j2, m2, a2 = d2
    if a1 != a2:
        return a1 < a2
    if m1 != m2:
        return m1 < m2
    return j1 < j2

def age(d1: tuple, d2: tuple) -> int:
    j1, m1, a1 = d1
    j2, m2, a2 = d2
    annees = a2 - a1
    # Si l'anniversaire n'est pas encore passé cette année, on enlève 1
    if (m2, j2) < (m1, j1):
        annees -= 1
    return annees

##### test #####
# print(anterieur((1, 1, 2000), (1, 1, 2010)))   # True
# print(age((15, 3, 1990), (15, 3, 2024)))        # 34


###################################
#####                         #####
#####      EXERCICE 3         #####
#####        Personnes        #####
#####                         #####
###################################

def nom_annee(personne: tuple) -> tuple:
    # personne = ((prénom, nom), (j, m, a))
    nom = personne[0][1]
    annee = personne[1][2]
    return (nom, annee)

##### test #####
# p = (("Alice", "Dupont"), (12, 5, 1995))
# print(nom_annee(p))   # ("Dupont", 1995)


###################################
#####                         #####
#####      EXERCICE 4         #####
#####        Moyenne          #####
#####                         #####
###################################

def moyenne(tableau: list) -> float:
    total: float = 0
    for x in tableau:
        total += x
    return total / len(tableau)

##### test #####
# print(moyenne([1, 2, 3, 4, 5]))   # 3.0


###################################
#####                         #####
#####      EXERCICE 5         #####
#####    Tableau ordonné      #####
#####                         #####
###################################

def est_ordonne(tableau: list) -> bool:
    for i in range(len(tableau) - 1):
        if tableau[i] > tableau[i + 1]:
            return False
    return True

##### test #####
# print(est_ordonne([1, 2, 3, 4]))   # True
# print(est_ordonne([1, 3, 2, 4]))   # False


###################################
#####                         #####
#####      EXERCICE 6         #####
#####      Zip et Unzip       #####
#####                         #####
###################################

def unzip(t: list) -> tuple:
    tx: list = []
    ty: list = []
    for x, y in t:
        tx.append(x)
        ty.append(y)
    return (tx, ty)

def zip(tx: list, ty: list) -> list:
    t: list = []
    for i in range(len(tx)):
        t.append((tx[i], ty[i]))
    return t

##### test #####
# t = [(0,0), (0,100), (50,150)]
# print(unzip(t))           # ([0, 0, 50], [0, 100, 150])
# print(zip([0, 1], [2, 3])) # [(0, 2), (1, 3)]


###################################
#####                         #####
#####      EXERCICE 7         #####
#####    Divisible par 7      #####
#####                         #####
###################################

# a) Tableau de 1000 booléens
divisible_7: list = [False] * 1000
for i in range(0, 1000, 7):
    divisible_7[i] = True

# b) Combien de nombres < 1000 sont divisibles par 7 ?
compte: int = 0
plus_grand: int = 0
for i in range(1000):
    if divisible_7[i]:
        compte += 1
        plus_grand = i
# print(f"Nombre de multiples de 7 < 1000 : {compte}")
# print(f"Plus grand multiple de 7 < 1000 : {plus_grand}")


###################################
#####                         #####
#####      EXERCICE 8         #####
#####       Palindrome        #####
#####                         #####
###################################

def palindrome(chaine: str) -> bool:
    for i in range(len(chaine) // 2):
        if chaine[i] != chaine[len(chaine) - 1 - i]:
            return False
    return True

##### test #####
# print(palindrome("ressasser"))   # True
# print(palindrome("bonjour"))     # False


###################################
#####                         #####
#####      EXERCICE 9         #####
#####   Entier depuis chaîne  #####
#####                         #####
###################################

def chaine_vers_entier(chaine: str) -> int:
    resultat: int = 0
    for c in chaine:
        # ord('0') = 48, donc ord(c) - ord('0') donne le chiffre
        resultat = resultat * 10 + (ord(c) - ord('0'))
    return resultat

##### test #####
# print(chaine_vers_entier("12345"))   # 12345


###################################
#####                         #####
#####      EXERCICE 10        #####
#####      Mot de passe       #####
#####                         #####
###################################

def mot_de_passe_valide(mdp: str) -> bool:
    if len(mdp) < 8:
        return False
    majuscule: bool = False
    minuscule: bool = False
    chiffre: bool = False
    special: bool = False
    for c in mdp:
        if c.isupper():
            majuscule = True
        elif c.islower():
            minuscule = True
        elif c.isdigit():
            chiffre = True
        else:
            special = True
    return majuscule and minuscule and chiffre and special

##### test #####
# print(mot_de_passe_valide("Abc1!xyz"))   # True
# print(mot_de_passe_valide("abc"))        # False


###################################
#####                         #####
#####      EXERCICE 11        #####
#####    Nombre de mots       #####
#####                         #####
###################################

# Version avec split
def nb_mots_split(phrase: str) -> int:
    return len(phrase.split())

# Version sans split
def nb_mots(phrase: str) -> int:
    if len(phrase) == 0:
        return 0
    compte: int = 1
    for c in phrase:
        if c == ' ':
            compte += 1
    return compte

##### test #####
# print(nb_mots_split("Le petit chat est mort"))   # 5
# print(nb_mots("Le petit chat est mort"))         # 5


###################################
#####                         #####
#####      EXERCICE 12        #####
#####    Longueur des mots    #####
#####                         #####
###################################

# Version avec split
def longueur_mots_split(phrase: str) -> list:
    return [len(mot) for mot in phrase.split()]

# Version sans split
def longueur_mots(phrase: str) -> list:
    longueurs: list = []
    longueur_courante: int = 0
    for c in phrase:
        if c == ' ':
            longueurs.append(longueur_courante)
            longueur_courante = 0
        else:
            longueur_courante += 1
    longueurs.append(longueur_courante)
    return longueurs

##### test #####
# print(longueur_mots("Le petit chat est mort"))   # [2, 5, 4, 3, 4]


###################################
#####                         #####
#####      EXERCICE 13        #####
#####       Capitales         #####
#####                         #####
###################################

capitales: dict = {
    "France": "Paris",
    "Allemagne": "Berlin",
    "Espagne": "Madrid",
    "Italie": "Rome",
    "Royaume-Uni": "Londres",
    "Portugal": "Lisbonne",
    "Belgique": "Bruxelles",
    "Pays-Bas": "Amsterdam",
}

def pays_de_capitale(ville: str) -> str | None:
    for pays, capitale in capitales.items():
        if capitale == ville:
            return pays
    return None

##### test #####
# print(pays_de_capitale("Paris"))    # "France"
# print(pays_de_capitale("Tokyo"))    # None


###################################
#####                         #####
#####      EXERCICE 14        #####
#####  Personnes (dico)       #####
#####                         #####
###################################

personnes: dict = {
    "Jean Aymar": {"taille": 178, "pays": "USA", "age": 31},
    "Clio Patre": {"pays": "Portugal", "age": 32, "taille": 179}
}

def age_personne(nom: str) -> int | None:
    if nom not in personnes:
        return None
    return personnes[nom]["age"]

def taille_moyenne() -> float:
    total: int = 0
    for p in personnes.values():
        total += p["taille"]
    return total / len(personnes)

##### test #####
# print(age_personne("Jean Aymar"))   # 31
# print(taille_moyenne())             # 178.5


###################################
#####                         #####
#####      EXERCICE 15        #####
#####    Cartes à jouer       #####
#####                         #####
###################################

COULEURS: list = ["Pique", "Coeur", "Carreau", "Trèfle"]
NOMS_VALEURS: dict = {11: "Valet", 12: "Dame", 13: "Roi", 14: "As"}

def carte_valide(carte: tuple) -> bool:
    valeur, couleur = carte
    return 2 <= valeur <= 14 and couleur in COULEURS

def nom_carte(carte: tuple) -> str:
    valeur, couleur = carte
    if valeur in NOMS_VALEURS:
        nom_valeur = NOMS_VALEURS[valeur]
    else:
        nom_valeur = str(valeur)
    return f"{nom_valeur} de {couleur}"

# c) Jeu de 52 cartes
jeu: list = []
for couleur in COULEURS:
    for valeur in range(2, 15):
        jeu.append((valeur, couleur))

# d) Tirer une carte au hasard
from random import randint
def tirer_carte() -> tuple:
    return jeu[randint(0, len(jeu) - 1)]

##### test #####
# print(nom_carte((14, "Trèfle")))   # "As de Trèfle"
# print(nom_carte((7, "Pique")))     # "7 de Pique"
# print(nom_carte(tirer_carte()))


###################################
#####                         #####
#####      EXERCICE 16        #####
#####  Calcul de distances    #####
#####                         #####
###################################

from math import sqrt

dessin1 = [(100, 100), (200, 200), (200, 100), (100, 200), (100, 100)]

def distance(p1: tuple, p2: tuple) -> float:
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def dimensions(dessin: list) -> tuple:
    xs = [p[0] for p in dessin]
    ys = [p[1] for p in dessin]
    largeur = max(xs) - min(xs)
    hauteur = max(ys) - min(ys)
    return (largeur, hauteur)

def longueur_dessin(dessin: list) -> float:
    total: float = 0
    for i in range(len(dessin) - 1):
        total += distance(dessin[i], dessin[i + 1])
    return total

##### test #####
# print(distance((0, 0), (3, 4)))      # 5.0
# print(dimensions(dessin1))            # (100, 100)
# print(longueur_dessin(dessin1))


###################################
#####                         #####
#####      EXERCICE 17        #####
#####   Inverser un tableau   #####
#####                         #####
###################################

def inverse_tableau(t: list) -> list:
    resultat: list = list(t)  # copie pour éviter l'alias
    for i in range(len(resultat) // 2):
        j = len(resultat) - 1 - i
        resultat[i], resultat[j] = resultat[j], resultat[i]
    return resultat

def inverse_chaine(chaine: str) -> str:
    return "".join(inverse_tableau(list(chaine)))

##### test #####
# print(inverse_tableau([1, 2, 3]))   # [3, 2, 1]
# print(inverse_chaine("bonjour"))    # "ruojnob"


###################################
#####                         #####
#####      EXERCICE 18        #####
#####    Tester le hasard     #####
#####                         #####
###################################

from random import random
from matplotlib.pyplot import bar, show

def histogramme_random(n: int) -> None:
    t: list = [0] * 10
    for _ in range(n):
        valeur = random()
        indice = int(valeur * 10)
        if indice == 10:
            indice = 9
        t[indice] += 1
    bar(range(len(t)), t)
    show()

##### test #####
# histogramme_random(1000)
# histogramme_random(1000000)


###################################
#####                         #####
#####      EXERCICE 19        #####
#####      Loi Normale        #####
#####                         #####
###################################

from random import randint
from matplotlib.pyplot import bar, show

# a) Lancement de deux dés
def histogramme_deux_des(n: int) -> None:
    t: list = [0] * 13
    for _ in range(n):
        somme = randint(1, 6) + randint(1, 6)
        t[somme] += 1
    bar(range(13), t)
    show()

# b) Lancement de n dés
def histogramme_n_des(nb_des: int, nb_tirages: int) -> None:
    maximum = nb_des * 6
    t: list = [0] * (maximum + 1)
    for _ in range(nb_tirages):
        somme = sum(randint(1, 6) for _ in range(nb_des))
        t[somme] += 1
    bar(range(maximum + 1), t)
    show()

# c) Pile ou face
def histogramme_pile_ou_face(nb_series: int) -> None:
    t: list = [0] * 101
    for _ in range(nb_series):
        piles = sum(randint(0, 1) for _ in range(100))
        t[piles] += 1
    bar(range(101), t)
    show()

##### test #####
# histogramme_deux_des(10000)
# histogramme_n_des(5, 10000)
# histogramme_pile_ou_face(10000)


###################################
#####                         #####
#####      EXERCICE 20        #####
#####   Taux d'imposition     #####
#####                         #####
###################################

from matplotlib.pyplot import plot, show

# a) Tranches : (limite_haute, taux)
tranches: list = [
    (10000,        0.00),
    (25000,        0.11),
    (75000,        0.30),
    (150000,       0.41),
    (float('inf'), 0.45),
]

# b) Calcule le montant de l'impôt pour un revenu donné
def impot(revenu: float) -> float:
    total: float = 0
    limite_precedente: float = 0
    for limite, taux in tranches:
        if revenu <= limite:
            total += (revenu - limite_precedente) * taux
            break
        else:
            total += (limite - limite_precedente) * taux
            limite_precedente = limite
    return total

# c) Graphe impôt en fonction du revenu
def graphe_impot() -> None:
    tx = list(range(0, 200001, 5000))
    ty = [impot(r) for r in tx]
    plot(tx, ty)
    show()

# d) Taux marginal d'imposition
def graphe_taux_marginal() -> None:
    tx = list(range(1, 200001, 5000))
    ty = [impot(r) / r * 100 for r in tx]
    plot(tx, ty)
    show()

# e) Comparaison
# print(f"Revenu 15000  : impôt={impot(15000):.0f}€, taux marginal={impot(15000)/15000*100:.1f}%")
# print(f"Revenu 50000  : impôt={impot(50000):.0f}€, taux marginal={impot(50000)/50000*100:.1f}%")
# print(f"Revenu 200000 : impôt={impot(200000):.0f}€, taux marginal={impot(200000)/200000*100:.1f}%")


###################################
#####                         #####
#####      EXERCICE 21        #####
#####       Anagramme         #####
#####                         #####
###################################

def retire_element(t: list, e) -> bool:
    for i in range(len(t)):
        if t[i] == e:
            t.pop(i)
            return True
    return False

def meme_contenu(t1: list, t2: list) -> bool:
    copie = list(t2)  # copie pour éviter l'alias
    for e in t1:
        if not retire_element(copie, e):
            return False
    return len(copie) == 0

def anagramme(s1: str, s2: str) -> bool:
    return s1 != s2 and meme_contenu(list(s1), list(s2))

##### test #####
# print(anagramme("chien", "niche"))   # True
# print(anagramme("bonjour", "jour"))  # False


###################################
#####                         #####
#####      EXERCICE 22        #####
#####  Mélanger un tableau    #####
#####                         #####
###################################

from random import randint

def melanger(t: list) -> list:
    source: list = list(t)  # copie pour éviter l'alias
    resultat: list = []
    while len(source) > 0:
        i = randint(0, len(source) - 1)
        resultat.append(source.pop(i))
    return resultat

##### test #####
# print(melanger([1, 2, 3, 4, 5]))
# jeu_melange = melanger(jeu)


###################################
#####                         #####
#####      EXERCICE 23        #####
#####        Bataille         #####
#####                         #####
###################################

def duel(c1: tuple, c2: tuple) -> int:
    if c1[0] == c2[0]:
        return 0
    elif c1[0] > c2[0]:
        return 1
    else:
        return 2

def tirer() -> tuple:
    return jeu[randint(0, len(jeu) - 1)]

def jouer() -> tuple:
    nb_duels: int = 0
    gagnant: int = 0
    while gagnant == 0:
        c1 = tirer()
        c2 = tirer()
        nb_duels += 1
        gagnant = duel(c1, c2)
    return (gagnant, nb_duels)

##### test #####
# print(jouer())   # ex: (1, 3) => joueur 1 gagne en 3 duels


###################################
#####                         #####
#####      EXERCICE 24        #####
#####  Inverser un dico       #####
#####                         #####
###################################

def inverse_dict(dico: dict) -> dict:
    return {valeur: cle for cle, valeur in dico.items()}

# b) Pas toujours possible : si deux clés ont la même valeur,
#    l'inversion perd de l'information.
# c) Vrai seulement si le dictionnaire est une bijection
#    (toutes les valeurs sont distinctes).

##### test #####
# print(inverse_dict(capitales))


###################################
#####                         #####
#####      EXERCICE 25        #####
#####        Scrabble         #####
#####                         #####
###################################

valeurs_Scrabble: dict = {10: 'kwxyz', 8: 'jq', 4: 'fhv', 3: 'bcp', 2: 'dmg'}

# b) Construire lettres_Scrabble
lettres_Scrabble: dict = {}
for score, lettres in valeurs_Scrabble.items():
    for lettre in lettres:
        lettres_Scrabble[lettre] = score
for c in "abcdefghijklmnopqrstuvwxyz":
    if c not in lettres_Scrabble:
        lettres_Scrabble[c] = 1

# c) Valeur d'un mot
def valeur_mot(mot: str) -> int:
    total: int = 0
    for c in mot.lower():
        if c in lettres_Scrabble:
            total += lettres_Scrabble[c]
    return total

mots_test = ["entrais", "ratines", "satiner", "riantes", "transie"]
# print(max(mots_test, key=valeur_mot))

# d) Case "lettre compte triple" en position 4 (indice 3)
def valeur_mot_triple(mot: str, position: int) -> int:
    total: int = 0
    for i, c in enumerate(mot.lower()):
        if c in lettres_Scrabble:
            if i == position:
                total += lettres_Scrabble[c] * 3
            else:
                total += lettres_Scrabble[c]
    return total

# print(max(mots_test, key=lambda m: valeur_mot_triple(m, 3)))


###################################
#####                         #####
#####      EXERCICE 26        #####
#####       Géographie        #####
#####                         #####
###################################

# Les dictionnaires sont définis dans 26.py — les copier ici ou importer

# a) Villes dont la latitude < 23,43
# for ville, (longitude, latitude) in villes_coordonnees.items():
#     if latitude < 23.43:
#         print(ville)

# b) Ville la plus peuplée
# ville_max = max(villes_population, key=lambda v: villes_population[v])
# print(ville_max, villes_coordonnees[ville_max])

# c) Stats par pays
def stats_pays(pays: str) -> None:
    villes = villes_pays[pays]
    total_habitants: int = 0
    total_longitude: float = 0
    total_latitude: float = 0
    for ville in villes:
        total_habitants += villes_population[ville]
        total_longitude += villes_coordonnees[ville][0]
        total_latitude += villes_coordonnees[ville][1]
    n = len(villes)
    print(f"Habitants : {total_habitants}")
    print(f"Longitude moyenne : {total_longitude / n:.2f}")
    print(f"Latitude moyenne  : {total_latitude / n:.2f}")


###################################
#####                         #####
#####      EXERCICE 27        #####
#####  Liste de tâches        #####
#####                         #####
###################################

todo_list: dict = {
    "Faire les courses": True,
    "Ranger le garage": False,
    "Compléter l'exercice 4": False,
}

def taches_restantes() -> int:
    compte: int = 0
    for tache, fait in todo_list.items():
        if not fait:
            print(f"- {tache}")
            compte += 1
    return compte

def gerer_todo() -> None:
    while True:
        # Affichage numéroté
        taches = list(todo_list.keys())
        for i, tache in enumerate(taches):
            statut = "v" if todo_list[tache] else " "
            print(f"{i+1}. [{statut}] {tache}")
        commande: str = input("Commande (+, -N, vN, ?) : ").strip()
        if commande == "+":
            nom = input("Nom de la tâche : ")
            todo_list[nom] = False
        elif commande.startswith("-"):
            i = int(commande[1:]) - 1
            del todo_list[taches[i]]
        elif commande.startswith("v"):
            i = int(commande[1:]) - 1
            todo_list[taches[i]] = not todo_list[taches[i]]
        elif commande == "?":
            for tache, fait in todo_list.items():
                if not fait:
                    print(f"- {tache}")


###################################
#####                         #####
#####      EXERCICE 28        #####
#####        Annuaire         #####
#####                         #####
###################################

annuaire: dict = {}

def parser_contact(chaine: str) -> tuple:
    # Format : "Prénom Nom Téléphone"
    parties = chaine.split()
    tel = parties[-1]
    prenom = parties[0]
    nom = " ".join(parties[1:-1])
    return (nom, prenom, tel)

def ajouter_contact(contact: tuple) -> None:
    nom, prenom, tel = contact
    cle = f"{prenom} {nom}"
    annuaire[cle] = tel

def gerer_annuaire() -> None:
    while True:
        choix = input("(a)jouter ou (r)echercher ? ").strip().lower()
        if choix == "a":
            entree = input("Prénom Nom Téléphone : ")
            ajouter_contact(parser_contact(entree))
        elif choix == "r":
            recherche = input("Prénom et Nom : ")
            if recherche in annuaire:
                print(f"Téléphone : {annuaire[recherche]}")
            else:
                print("Erreur : personne introuvable")

# d) Recherche par nom ou prénom seul
def recherche_partielle(terme: str) -> list:
    resultats: list = []
    for cle, tel in annuaire.items():
        prenom, nom = cle.split(" ", 1)
        if terme == prenom or terme == nom:
            resultats.append((cle, tel))
    return resultats
