# Exercices – Chapitre 6 : Trier et chercher

## Exercice 1 — Choisir la (ou les) bonne(s) réponse(s)

### 1) Associer à chaque programme sa complexité dans le pire cas (aux constantes près) pour un tableau de taille n.

**Programmes :**
- a) Tri par sélection
- b) Tri par insertion
- c) Recherche dichotomique
- d) Recherche linéaire

**Complexités :**
- 1) log2(n)
- 2) n
- 3) n log2(n)
- 4) n²

---

### 2) Indiquer la complexité du programme suivant.

```python
for i in range(len(t)):
    if t[i] > t[i+1]:
        t[i], t[i+1] = t[i+1], t[i]
```

- a) Linéaire  
- b) Quadratique  
- c) Le programme peut ne pas terminer  

---

### 3) Indiquer la complexité du programme suivant.

```python
left = 0
right = len(t) - 1
v = 5
while left < right:
    mid = (left + right) // 2
    if t[mid] > v:
        right = mid
print(t[left])
```

- a) Linéaire  
- b) Quadratique  
- c) Le programme peut ne pas terminer  

---

### 4) Indiquer la complexité du programme suivant.

```python
for i in range(len(t)):
    for j in range(i):
        print(t[j])
```

- a) Linéaire  
- b) Quadratique  
- c) Le programme peut ne pas terminer  

---

### 5) Indiquer la complexité du programme suivant.

```python
for i in range(len(t)):
    for j in range(len(t), 0, -1):
        print(t[j])
```

- a) Linéaire  
- b) Quadratique  
- c) Le programme peut ne pas terminer  

---

### 6) L’algorithme de recherche linéaire trouvera plus rapidement les éléments :

- a) les plus petits  
- b) les plus grands  
- c) en tête du tableau d’entrée  

---

### 7) Associer à chaque programme de tri son résultat en partant de :  
`t0 = ['abe', 'Be', 'dda', 'ac', 'abe']`

**Programmes :**

a)
```python
t = t0.copy()
sorted(t)
print(t)
```

b)
```python
t = t0.copy()
t.sort()
print(t)
```

c)
```python
t = t0.copy()
t.sort(reverse=True)
print(t)
```

**Résultats :**
- 1) `['abe', 'Be', 'dda', 'ac', 'abe']`
- 2) `['Be', 'abe', 'abe', 'ac', 'dda']`
- 3) `['dda', 'ac', 'abe', 'abe', 'Be']`

---

### 8) Compléter le code du tri par sélection suivant.

```python
def tri_selection(t):
    """ Trie t sur place. """
    for i in range(len(t)-1):
        j_min = i
        for j in range(...):
            # j_min = indice du minimum
            # parmi t[i], ..., t[j-1]
            if t[j] < t[j_min]:
                j_min = j
        if j_min != i:
            # on échange les cases i et j_min
            t[i], t[j_min] = ...
```

---

## Exercice 2 — Effet de `sorted`

Que valent `t` et `t1` après exécution du code suivant ?

```python
a = ['15', '7', '2']
t = sorted(a)
t1 = sorted([x*2 for x in a])
```

---

## Exercice 3 — Recherche dichotomique

### a)
Combien d’itérations vont être nécessaires à la recherche dichotomique vue en cours pour trouver `15` dans le tableau :

```
[1, 2, 15, 17, 30]
```

### b)
Même question pour le tableau :

```
[-4, -2, 0, 2, 10, 15, 18]
```

### c)
Quand on multiplie par 2 la taille du tableau, de combien augmente le nombre d’itérations des pires recherches dichotomiques, c’est-à-dire comment évolue `log2(n)` lorsque `n` est multiplié par 2 ?

---

## Exercice 4 — Effet d’un passage de tri

On donne le programme suivant :

```python
t = [1, 5, 3, 2]
for j in range(len(t)-1):
    if t[j] > t[j+1]:
        t[j], t[j+1] = t[j+1], t[j]
```

Que vaut `t` à la fin du programme ?

- a) `[1, 5, 3, 2]`  
- b) `[1, 3, 2, 5]`  
- c) `[5, 3, 2, 1]`  
- d) `[1, 2, 3, 5]`  

---

## Exercice 5 — Tri par sélection (compléter un algorithme)

On considère l’algorithme de tri de tableau suivant : à chaque étape, on parcourt le sous-tableau des éléments non rangés et on place le plus petit élément en première position de ce sous-tableau.

**Exemple avec le tableau :**  
`t = [41, 55, 21, 18, 12, 6, 25]`

- **Étape 1** : on parcourt tous les éléments du tableau, on permute le plus petit élément avec le premier.  
  Le tableau devient :
  ```
  [6, 55, 21, 18, 12, 41, 25]
  ```

- **Étape 2** : on parcourt tous les éléments sauf le premier, on permute le plus petit élément trouvé avec le second.  
  Le tableau devient :
  ```
  [6, 12, 21, 18, 55, 41, 25]
  ```

Et ainsi de suite.

Le programme ci-dessous implémente cet algorithme.

```python
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = ...
    tab[i] = ...
    tab[j] = ...

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(...):
        imin = ...
        for i in range(..., N):
            if tab[i] < ...:
                imin = i
        echange(tab, ..., ...)
```

Compléter ce code de façon à obtenir :

```python
>>> tab = [41, 55, 21, 18, 12, 6, 25]
>>> tri_selection(tab)
>>> tab
[6, 12, 18, 21, 25, 41, 55]
```
---

## Exercice 6 — Implémenter le tri par sélection

Écrire une fonction `tri_selection` qui prend en paramètre un tableau `tab` de nombres entiers (type `list`) et qui le modifie afin qu’il soit trié par ordre croissant.

On utilisera l’algorithme suivant :

- on recherche le plus petit élément du tableau, en la parcourant du rang 0 au dernier rang, et on l’échange avec l’élément d’indice 0 ;
- on recherche ensuite le plus petit élément du tableau restreint du rang 1 au dernier rang, et on l’échange avec l’élément d’indice 1 ;
- on continue de cette façon jusqu’à ce que le tableau soit entièrement trié.

**Exemple :**

```python
>>> tab = [1, 52, 6, -9, 12]
>>> tri_selection(tab)
>>> tab
[-9, 1, 6, 12, 52]
```
---
Pour ceux qui désirent un editeur Python : 
---
<iframe
  src="https://basthon.fr/?editor=python"
  width="100%"
  height="500"
  style="border:1px solid #ccc; border-radius:8px;">
</iframe>




