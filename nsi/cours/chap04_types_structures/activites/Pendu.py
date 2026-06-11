##### ##### #####   ##### ##### ##### 
#####           LE PENDU         ####
##### ##### #####   ##### ##### #####

###################################
#####                         #####
##### 1. PROPOSER UNE LETTRE  #####
#####                         #####
###################################

def demander_lettre_base():
    lettre = input("Proposez une lettre : ")
    while len(lettre) != 1:
        print("Attention, je n'ai besoin que d'une seule lettre !")
        lettre = input("Proposez une lettre : ")
    return lettre

def demander_lettre_bonus():
    caracteres_autorises = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'-"
    lettre = input("Proposez une lettre : ")
    while len(lettre) != 1 or lettre not in caracteres_autorises:
        print("Attention, je n'ai besoin que d'une seule lettre, apostrophe ou tiret !")
        lettre = input("Proposez une lettre : ")
    return lettre

def demander_lettre() -> str:
    caracteres_autorises: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'-"
    lettre: str = input("Proposez une lettre : ")
    while len(lettre) != 1 or lettre not in caracteres_autorises:
        print("Attention, je n'ai besoin que d'une seule lettre, apostrophe ou tiret !")
        lettre = input("Proposez une lettre : ")
    return lettre

##### test des fonctions #####

#demander_lettre_typee()

#################################
#####                       #####
#####  2. MOT a TROU        #####
#####                       #####
#################################


def remplace(reference: str, actuel: str, lettre: str) -> str | None: # | = String ou None

####   |  Sur clavier Mac : Alt + Shift + L    et  |  Sur clavier PC : Alt Gr + 6

    # Si la lettre n'est pas dans le mot de référence, on retourne None
    if lettre not in reference:
        return None
    
    # On convertit actuel en liste pour pouvoir modifier les caractères un à un
    actuel_liste: list[str] = list(actuel)
    
    # On parcourt reference et on remplace dans actuel_liste aux bons indices
    for i in range(len(reference)):
        if reference[i] == lettre:
            actuel_liste[i] = lettre
    
    # On recolle la liste en chaîne avec join() et on retourne le résultat
    return "".join(actuel_liste)


##### test  #####
#print(remplace("boom", "b---", "o"))   # "boo-"
#print(remplace("boom", "b---", "z"))   # None

###################################
#####                         #####
#####     3. PROGRAMME        #####
#####                         #####
###################################

def pendu(mot: str, nb_erreurs: int) -> None:
    # On initialise le mot actuel avec des tirets
    mot_actuel: str = "-" * len(mot)
    
    # On initialise la liste des lettres déjà jouées
    lettres_jouees: list[str] = []
    
    # On initialise le compteur d'erreurs
    erreurs: int = 0
    
    # La partie continue tant que le mot n'est pas deviné et qu'il reste des essais
    while mot_actuel != mot and erreurs < nb_erreurs:
        print(f"Mot actuel : {mot_actuel}")
        print(f"Lettres jouées : {lettres_jouees}")
        print(f"Erreurs restantes : {nb_erreurs - erreurs}")
        
        # On demande une lettre à l'utilisateur
        lettre: str = demander_lettre()
        
        # Si la lettre a déjà été jouée, on passe
        if lettre in lettres_jouees:
            print("Vous avez déjà proposé cette lettre !")
            continue
        
        # On ajoute la lettre à la liste des lettres jouées
        lettres_jouees.append(lettre)
        
        # On tente de mettre à jour le mot actuel
        resultat: str | None = remplace(mot, mot_actuel, lettre)
        
        if resultat is None:
            # La lettre n'est pas dans le mot, c'est une erreur
            print("Mauvaise lettre !")
            erreurs += 1
        else:
            # La lettre est dans le mot, on met à jour mot_actuel
            mot_actuel = resultat
    
    
    # Fin de partie

    if mot_actuel == mot:
        print(f"Bravo, vous avez trouvé le mot : {mot} !")
    else:
        print(f"Perdu ! Le mot était : {mot}")


###################################
#####                         #####
#####      3. BONUS            #####
#####                        #####
###################################



import turtle

def init_turtle() -> turtle.Turtle:
    # On initialise la fenêtre et le crayon
    turtle.speed(5)
    turtle.hideturtle()
    t: turtle.Turtle = turtle.Turtle()
    t.speed(5)
    t.hideturtle()
    return t

def dessiner_potence(t: turtle.Turtle) -> None:
    # Socle
    t.penup()
    t.goto(-100, -150)
    t.pendown()
    t.goto(100, -150)
    # Pied du poteau
    t.goto(0, -150)
    t.goto(0, 150)
    # Bras horizontal
    t.goto(80, 150)
    # Corde
    t.goto(80, 100)
    t.penup()

def dessiner_tete(t: turtle.Turtle) -> None:
    # Cercle pour la tête
    t.goto(80, 60)
    t.pendown()
    t.circle(40)
    t.penup()

def dessiner_corps(t: turtle.Turtle) -> None:
    # Trait vertical pour le corps
    t.goto(80, 60)
    t.pendown()
    t.goto(80, -20)
    t.penup()

def dessiner_bras_gauche(t: turtle.Turtle) -> None:
    t.goto(80, 40)
    t.pendown()
    t.goto(40, 0)
    t.penup()

def dessiner_bras_droit(t: turtle.Turtle) -> None:
    t.goto(80, 40)
    t.pendown()
    t.goto(120, 0)
    t.penup()

def dessiner_jambe_gauche(t: turtle.Turtle) -> None:
    t.goto(80, -20)
    t.pendown()
    t.goto(40, -70)
    t.penup()

def dessiner_jambe_droite(t: turtle.Turtle) -> None:
    t.goto(80, -20)
    t.pendown()
    t.goto(120, -70)
    t.penup()

# Liste des étapes du dessin dans l'ordre
ETAPES: list = [
    dessiner_tete,
    dessiner_corps,
    dessiner_bras_gauche,
    dessiner_bras_droit,
    dessiner_jambe_gauche,
    dessiner_jambe_droite,
]

def dessiner_etape(t: turtle.Turtle, erreur: int) -> None:
    # Dessine l'étape correspondant au numéro d'erreur (1 à 6)
    if 1 <= erreur <= len(ETAPES):
        ETAPES[erreur - 1](t)



def pendu(mot: str, nb_erreurs: int) -> None:
    mot_actuel: str = "-" * len(mot)
    lettres_jouees: list[str] = []
    erreurs: int = 0

    # Initialisation turtle
    t: turtle.Turtle = init_turtle()
    dessiner_potence(t)

    while mot_actuel != mot and erreurs < nb_erreurs:
        print(f"Mot actuel : {mot_actuel}")
        print(f"Lettres jouées : {lettres_jouees}")
        print(f"Erreurs restantes : {nb_erreurs - erreurs}")

        lettre: str = demander_lettre()

        if lettre in lettres_jouees:
            print("Vous avez déjà proposé cette lettre !")
            continue

        lettres_jouees.append(lettre)
        resultat: str | None = remplace(mot, mot_actuel, lettre)

        if resultat is None:
            print("Mauvaise lettre !")
            erreurs += 1
            dessiner_etape(t, erreurs)  # On dessine l'étape correspondante
        else:
            mot_actuel = resultat

    if mot_actuel == mot:
        print(f"Bravo, vous avez trouvé le mot : {mot} !")
    else:
        print(f"Perdu ! Le mot était : {mot}")
    
    turtle.done()

pendu("bonjour", 6)
