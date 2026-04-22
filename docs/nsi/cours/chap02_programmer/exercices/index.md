# Exercices Python

## Exercice 1
Identifier les types des valeurs suivantes :

```python
"Exercice", 123., True, 1e10, "False", '3,14'
```

---

## Exercice 2
Identifier les erreurs dans le code suivant et les corriger :

```python
pi = 3,14
def aire-cercle(rayon)
    return pi * r * 2
print(aire_cercle(10)
```
---

## Exercice 3
Écrire l’expression qui calcule la moyenne de deux nombres `a` et `b`.

---

## Exercice 4
Calculer les valeurs des expressions suivantes pour `x = 0`, `x = 10` et `x = -20` :

```python
x < 10 and x > -10
x < -10 or x > 10
x <= 10 and x * x >= 100
x > -25 and x < -5 or x > 5 and x < 25
```

---

## Exercice 5
Qu’est-ce qu’affiche chacun des programmes suivants ?

```python
if (12 * 2 == 24):
    print("Logique.")
```

```python
if (12 * 2 == 24) == False:
    print("Logique.")
```

```python
if (12 * 2 == 23) == False:
    print("Logique.")
print("Ou pas.")
```

```python
if (12 * 2 == 23):
    print("Logique.")
else:
    print("Ou pas.")
```

---

## Exercice 6
Combien de fois s’exécute le corps de chacune des boucles ci-dessous, et quelle est la valeur de `s` à la fin ?

```python
s = 0
for i in range(10):
    s = s + i
```

```python
s = 1
for i in range(1, 6):
    s = s * i
```

```python
s = 0
while s < 20:
    s = s + 5
```

```python
s = 1
while s <= 100:
    s = s * 2
```

---

## Exercice 7
Écrire une boucle qui affiche la table de multiplication par 7 :

```python
7 x 1 = 7
7 x 2 = 14
...
```

---

## Exercice 8
Écrire une boucle qui calcule la factorielle du nombre introduit dans `n`.

---

## Exercice 9
a. Quelle est la valeur de `a` à la fin du programme suivant ?

```python
n = 0
a = 27
b = 5
while a >= b:
    n = n + 1
    a = a - b
```

b. Montrer que `n` est le quotient de la division euclidienne de `a` par `b`.

c. Ajouter une instruction conditionnelle (`if`) pour vérifier ce résultat.

---

## Exercice 11
Écrire une fonction `pair` qui retourne `True` si le nombre passé en argument est pair.

---

## Exercice 12
a. Quelle est la valeur de `a` à la fin du programme suivant ?

```python
a = 21

def double(x):
    print(x * 2)

a = double(a)
```

b. Qu’affiche ce programme ?


## Exercice 13
Montrer les identités suivantes (algèbre de Boole) en écrivant et exécutant un programme qui calcule les valeurs des expressions pour toutes les valeurs possibles de `a` et `b` :

```python
not (a and b) == not a or not b
not (a or b) == not a and not b
```

On rappelle que `a and b` est vrai seulement si `a` et `b` sont vrais, `a or b` est vrai si `a` ou `b` est vrai, et `not a` est vrai si `a` est faux.

---

## Exercice 14
L’opérateur booléen `or` ne correspond pas toujours à ce que l’on entend par “ou” dans la vie quotidienne.

Écrire une fonction `xor(a, b)` qui retourne le ou exclusif de `a` et `b`.

---

## Exercice 15
a. Écrire un programme qui indique si une année est bissextile.

b. Écrire un programme pour calculer le nombre de jours du mois `m` de l’année `a`.

---

## Exercice 16
a. Écrire les fonctions suivantes :

```python
def est_bissextile(annee):
    """ retourne True si l'année est bissextile """
```

```python
def nb_jours_mois(mois, annee):
    """ retourne le nombre de jours du mois """
```

b. Écrire une fonction :

```python
def nb_jours(jour, mois, annee):
    """ retourne le nombre de jours depuis le début de l'année """
```

c. Écrire une fonction :

```python
def jour_semaine(jour, mois, annee, jour0):
    """ retourne le jour de la semaine """
```

---

## Exercice 17
a. Écrire une boucle `for` qui affiche les nombres pairs entre 2 et 20.

b. Écrire une boucle `while` équivalente.

c. Faire de même pour les nombres entre 20 et 2 par ordre décroissant.

---

## Exercice 18
La fonction `random()` produit un nombre aléatoire entre 0 et 1.

Écrire une fonction qui affiche de manière aléatoire des chaînes comme :
"Haha", "Hahaha", ..., "Hahahaha" (entre 1 et 10 répétitions).

---

## Exercice 19
a. Écrire une boucle qui affiche les puissances de 2 inférieures à un million.

b. Modifier le programme pour compter ces puissances.

---

## Exercice 20
Écrire un programme qui affiche les chiffres d’un nombre à partir du dernier.

Exemple pour 1234 :

```
4
3
2
1
```

---

## Exercice 21
a. Écrire un programme qui affiche les 100 premiers nombres de Fibonacci.

b. Modifier pour afficher aussi le rapport entre deux nombres consécutifs.

---

## Exercice 22
Suite de Syracuse :

a. Écrire une fonction `Syracuse(n)` qui affiche la suite.

b. Modifier pour afficher le nombre d’étapes.

c. Modifier pour retourner le plus grand nombre atteint.

---

## Exercice 23
a. Écrire un programme qui affiche toutes les combinaisons de deux dés pour obtenir un nombre donné entre 2 et 12.

b. Étendre pour tous les nombres de 2 à 12.

c. Adapter pour trois dés.

d. Afficher seulement le nombre de combinaisons.

---

## Exercice 24
a. Écrire une fonction qui teste si un nombre est premier.

b. Adapter avec une boucle `while`.

c. Optimiser en testant jusqu’à √n.

d. Afficher les M premiers nombres premiers.

---

## Exercice 25
a. Écrire une fonction `jeu(a, b)` simulant pierre-feuille-ciseaux.

b. Écrire une fonction qui simule plusieurs parties et compte les scores.

c. Simuler 50 tours et afficher les scores.


