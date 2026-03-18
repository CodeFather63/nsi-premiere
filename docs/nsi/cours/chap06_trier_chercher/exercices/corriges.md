# Corrigés – Chapitre 6 : Trier et chercher

## Exercice 1 — Choisir la (ou les) bonne(s) réponse(s)

### 1) Complexités

Correspondances correctes :
- a) Tri par sélection → **4) n²**
- b) Tri par insertion → **4) n²** (pire cas)
- c) Recherche dichotomique → **1) log2(n)**
- d) Recherche linéaire → **2) n**

---

### 2)
Bonne réponse : **a) Linéaire**  
Une seule boucle parcourant le tableau.

---

### 3)
Bonne réponse : **a) Linéaire**  
La boucle `while` réduit l’intervalle mais la condition n’est pas une vraie dichotomie complète.

---

### 4)
Bonne réponse : **b) Quadratique**  
Deux boucles imbriquées, nombre d’affichages proportionnel à n².

---

### 5)
Bonne réponse : **b) Quadratique**  
Deux boucles imbriquées indépendantes de i.

---

### 6)
Bonne réponse : **c) en tête du tableau d’entrée**  
La recherche linéaire s’arrête dès que l’élément est trouvé.

---

### 7)
Correspondances correctes :
- a) → **1**
- b) → **2**
- c) → **3**

---

### 8)
Code complété :

```python
def tri_selection(t):
    for i in range(len(t)-1):
        j_min = i
        for j in range(i+1, len(t)):
            if t[j] < t[j_min]:
                j_min = j
        if j_min != i:
            t[i], t[j_min] = t[j_min], t[i]
```

---

## Exercice 2 — Effet de `sorted`

```python
a = ['15', '7', '2']
```

- `t = ['15', '2', '7']` (tri lexicographique de chaînes)
- `t1 = ['1515', '22', '77']` puis tri lexicographique → `['1515', '22', '77']`

---

## Exercice 3 — Recherche dichotomique

### a)
Tableau de taille 5 → **3 itérations** au maximum.

### b)
Tableau de taille 7 → **3 itérations** au maximum.

### c)
Lorsque n est multiplié par 2 :
- `log2(2n) = log2(n) + 1`  
➡️ le nombre d’itérations augmente de **1**.

---

## Exercice 4 — Effet d’un passage de tri

À la fin de l’exécution, le tableau vaut :
- **b) [1, 3, 2, 5]**

---

## Exercice 5 — Tri par sélection (compléter un algorithme)

```python
def echange(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    N = len(tab)
    for k in range(N-1):
        imin = k
        for i in range(k+1, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, k, imin)
```

---

## Exercice 6 — Implémenter le tri par sélection

```python
def tri_selection(tab):
    n = len(tab)
    for i in range(n-1):
        imin = i
        for j in range(i+1, n):
            if tab[j] < tab[imin]:
                imin = j
        tab[i], tab[imin] = tab[imin], tab[i]
```
