# Exercices
# =========
# 
# Exercices Newbie
# ----------------

# ### Exercice 1 
# 

def input_bool(message):
    """ Demande une saisie booléenne """
    while True:
        r = input(message)
        if r == 'o' or r == 'oui':
            return True
        if r == 'n' or r == 'non':
            return False
        print('Répondre oui ou non !')

input_bool('Fait-il beau ? ')

# ### Exercice 2
# 
# a) Écrire un programme qui saisit une valeur en degrés …
# 

temp = input('Température à convertir : ')
print(float(temp)*9/5 + 32)

# b) Modifier le programme pour que l’utilisateur puisse saisir également …

temp = input('Température à convertir : ')
unite = input('Centigrades (C) ou Fahrenheit (F) ? ')
if unite == 'C':
    print(float(temp)*9/5 + 32)
elif unite == 'F':
    print((float(temp) - 32) * 5/9)
else:
    print('Unité non reconnue')

#c


from nsi_ui import *

def convertir():
    temp = get_float(v)
    unite = get_string(u).upper()

    if unite == 'C':
        resultat = temp * 9/5 + 32
        set_text(sortie, f"{temp} °C = {resultat} °F")
    elif unite == 'F':
        resultat = (temp - 32) * 5/9
        set_text(sortie, f"{temp} °F = {resultat} °C")
    else:
        set_text(sortie, "Unité non reconnue")

v = entry("Température")
u = entry("Unité (C/F)")

button("Convertir", convertir)

sortie = label("")

main_loop()


# ### Exercice 3
# 

entree = input('Entrer un chiffre entre 1 et 9 : ')
n = int(entree)
if n > 0 and n < 10:
    for i in range(1, 11):
        print(f'{i:2} x {n} = {i*n:2}')
else:
    print('Entrée invalide')


# ### Exercice 4
# 

from nsi_ui import *



monnaie1 = "EUR"
monnaie2 = "USD"
taux = 1.20


def convert():
    """ Convertit le montant saisi dans les deux monnaies """
    m = get_float(montant)

    r1 = m * taux
    r2 = m / taux
    set_text(conv1, str(m) + str(monnaie1) + " = " + str(r1) + str(monnaie2))
    set_text(conv2, str(m) + str(monnaie2) + " = " + str(r2) + str(monnaie1))

# Construire l'interface
montant = entry("Montant")
button("Convertir",convert)
begin_vertical()
conv1 = label('conversion')
conv2 = label('conversion')
end_vertical()
main_loop()

# ### Exercice 5
# 
# a) Reprendre le programme du cours qui ajoute deux nombres …

from nsi_ui import *

# Note : nécessaire seulement dans Jupyter
clear_ui()

# champs de saisie de texte pour entrer les valeurs de a et b
champA = entry("Valeur de a")
champB = entry("Valeur de b")

def ajouter():
    """ Afficher la somme des valeurs des champs A et B """
    a = get_float(champA)   # valeur entrée dans le champ A
    b = get_float(champB)   # valeur entrée dans le champ B
    set_text(resultat, a+b) # afficher le resultat

def soustraire():
    """ Afficher la difference des valeurs des champs """
    a = get_float(champA)
    b = get_float(champB)
    set_text(resultat, a-b)

button("Différence", soustraire)
button("Somme", ajouter) # bouton pour lancer le calcul
resultat = label("")     # zone d'affichage du résultat

main_loop()              # lancer l'interface

# b) Utiliser des conteneurs pour que l’interface ait l’apparence suivante …
# 

# Note : nécessaire seulement dans Jupyter
clear_ui()

def ajouter():
    """ Afficher la somme des valeurs des champs A et B """
    a = get_float(champA)   # valeur entrée dans le champ A
    b = get_float(champB)   # valeur entrée dans le champ B
    set_text(resultat, f'Somme = {a+b}') # afficher le resultat

def soustraire():
    """ Afficher la difference des valeurs des champs """
    a = get_float(champA)
    b = get_float(champB)
    set_text(resultat, f'Différence = {a-b}')

# Contruction de l'interface
begin_vertical()
begin_horizontal()
champA = slider("Valeur de a", 0, 100)
champB = slider("Valeur de b", 0, 100)
end_horizontal()

begin_horizontal()
button("Somme", ajouter)
button("Différence", soustraire)
end_horizontal()

resultat = label("")
end_vertical()

main_loop()

# ### Exercice 6 
# 

from nsi_ui import *

# Note : nécessaire seulement dans Jupyter
clear_ui()

# L'heure courante
H = 12
M = 0

def avance_heure():
    """ Ajouter 1 à l'heure H """
    global H
    H = H + 1
    if H > 23:
        H = 0
    set_value(heures, H)

def recule_heure():
    """ Retirer 1 de l'heure H """
    global H
    H = H - 1
    if H < 0:
        H = 23
    set_value(heures, H)

def avance_minute():
    """ Ajouter 1 aux minutes M """
    global M, H
    M = M + 1
    if M >= 59:
        M = 0
        avance_heure()
    set_value(minutes, M)

def recule_minute():
    """ Retirer 1 des minutes M """
    global M, H
    M -= 1
    if M < 0:
        M = 59
        recule_heure()
    set_value(minutes, M)

# Construire l'interface
button("-", recule_heure)
heures = entry("")
set_width(heures, 4)
button("+", avance_heure)
label("heure")

button("-", recule_minute)
minutes = entry("")
set_width(minutes, 4)
button("+", avance_minute)
label("minutes")

set_value(heures, H)
set_value(minutes, M)

main_loop()

