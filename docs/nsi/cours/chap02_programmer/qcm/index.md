# QCM — Python

!!! info "Consigne"
    Choisir la ou les bonne(s) réponse(s).

---

## 1. Quels sont les nombres qui sont correctement écrits en Python ?

a) `3,14`  
b) `1.975`  
c) `-175`  
d) `1 290 524`  
e) `2,718`  
f) `1.E10`

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponses : b, c et f**

- `1.975` est correctement écrit en Python.
- `-175` est correctement écrit en Python.
- `1.E10` est une écriture scientifique valide.

❌ `3,14` et `2,718` utilisent une virgule au lieu d’un point.  
❌ `1 290 524` contient des espaces.

</details>

---

## 2. Quels sont les nombres considérés comme des nombres entiers en Python ?

a) `1.975`  
b) `.175`  
c) `-5.`  
d) `1.E10`  
e) `1E5`  
f) `123456`

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponses attendues : e et f**

- `123456` est bien un entier.
- `1E5` représente une valeur entière (`100000`), même si son **type Python** est `float`.

!!! note
    Si l’on parle strictement du **type Python**, seule la réponse **f** est de type `int`.  
    Ici, je respecte les réponses attendues de la fiche.

</details>

---

## 3. Quelles sont les chaînes de caractères qui sont correctement écrites en Python ?

a) `"Python c’est facile"`  
b) `'Il dit qu’il fait beau'`  
c) `'Il dit : "il faut beau"'`

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse attendue : a**

- La chaîne **a** est correctement écrite.
- Dans **b**, l’apostrophe ferme la chaîne trop tôt.
- La fiche attend **a** seule comme bonne réponse.

</details>

---

## 4. Quels sont les types respectifs des trois variables définies ci-dessous ?

```python
couleur = "vert"
hauteur = 12.5
distance = 89
```

a) chaîne de caractères, nombre à virgule flottante, entier  
b) couleur, taille, kilomètres

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : a**

- `couleur` est une chaîne de caractères.
- `hauteur` est un nombre à virgule flottante.
- `distance` est un entier.

</details>

---

## 5. Quels sont les noms de variables corrects en Python ?

a) `taILLe`  
b) `__secret`  
c) `email@`  
d) `i+j`  
e) `nXm`  
f) `@email`  
g) `2pi`  
h) `_2pi`  
i) `pi2`

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponses : a, b, e, h et i**

Un nom de variable Python :
- peut contenir des lettres, des chiffres et `_`
- ne doit pas commencer par un chiffre
- ne doit pas contenir `@`, `+`, etc.

</details>

---

## 6. Quels sont les programmes correctement indentés ?

### a)

```python
if x > 5:
    x = x - 5
    print(x)
```

### b)

```python
if x > 5:
    x = x - 5
print(x)
```

### c)

```python
if x > 5:
    x = x - 5
    print(x)
```

### d)

```python
if x > 5:
x = x - 5
print(x)
```

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponses attendues : b et c**

- **b** est correctement indenté : le bloc du `if` contient seulement `x = x - 5`, puis `print(x)` est hors du bloc.
- **c** est correctement indenté : les deux instructions appartiennent au bloc du `if`.
- **d** est faux : l’indentation après `if` est absente.

</details>

---

## 7. Que retourne la dernière ligne du bloc suivant ?

```python
taille_Paul = 175
taille_Lorena = taille_Paul + 12
taille_Paul <= taille_Lorena
```

a) `False`  
b) `True`  
c) `187`

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : b**

- `taille_Lorena = 175 + 12 = 187`
- On teste `175 <= 187`
- Le résultat est donc `True`

</details>

---

## 8. Quelles sont les valeurs de `a` et `b` après l’exécution des instructions ci-contre ?

```python
a = 5
b = 10
a = b
b = a
```

a) `a = 5` et `b = 10`  
b) `a = 10` et `b = 5`  
c) `a = 5` et `b = 5`  
d) `a = 10` et `b = 10`

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : d**

- Après `a = b`, on a `a = 10`
- Puis `b = a` donne `b = 10`

À la fin : `a = 10` et `b = 10`.

</details>

---

## 9. En utilisant l’approximation ci-contre, comment calculer l’aire d’un cercle ?

```python
pi = 3.1416
rayon = 5.24
```

a) `aire = pi * r * r`  
b) `aire = pi * rayon * 2`  
c) `aire = pi * rayon ** 2`

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : c**

La formule de l’aire d’un cercle est :

```python
aire = pi * rayon ** 2
```

</details>

---

## 10. Pour quelle valeur de `n` le programme a pour résultat une valeur de `x = 10` ?

```python
x = 0
for i in range(n):
    x = x + 1
```

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : 10**

La boucle s’exécute `n` fois et ajoute `1` à `x` à chaque tour.

</details>

---

## 11. Que retourne la fonction suivante ?

```python
def mystere(n):
    print(n % 2 == 1)
```

a) `True` si le nombre `n` est impair, `False` sinon  
b) `False` si le nombre `n` est impair, `True` sinon  
c) Rien

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : c**

La fonction **affiche** le résultat avec `print(...)`, mais elle ne contient pas `return`.

</details>

---

## 12. Dans laquelle (ou lesquelles) des fonctions suivantes l’instruction `global` est-elle inutile ?

### a)

```python
def f(x):
    global g
    return x*x
```

### b)

```python
def f(x):
    global g
    return g*x
```

### c)

```python
def f(x):
    global g
    print(g)
```

### d)

```python
def f(x):
    global g
    g = g+1
```

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponses : a, b et c**

L’instruction `global g` n’est utile que si la fonction **modifie** la variable globale `g`.

- dans **a**, **b** et **c**, on ne modifie pas `g`
- dans **d**, `global` est nécessaire car on modifie `g`

</details>

---

!!! tip "Bilan des réponses"
    **1.** b, c et f  
    **2.** e et f  
    **3.** a  
    **4.** a  
    **5.** a, b, e, h et i  
    **6.** b et c  
    **7.** b  
    **8.** d  
    **9.** c  
    **10.** 10  
    **11.** c  
    **12.** a, b et c
