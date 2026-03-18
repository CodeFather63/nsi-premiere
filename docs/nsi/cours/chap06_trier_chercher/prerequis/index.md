# Prérequis – Trier et chercher dans les tableaux

Ce QCM permet de vérifier les connaissances nécessaires avant d’aborder les algorithmes de tri et de recherche.

---

## QCM

### 1. Sélectionner les affirmations correctes.

a) Pour calculer les indices des valeurs minimales d’un tableau `t`, on va utiliser une boucle  
`for x in t` plutôt qu’une boucle `for i in range(len(t))`.

b) Calculer un maximum est plus coûteux que calculer un minimum.

<details>
<summary><strong>Corrigé</strong></summary>

- ✅ **a)** Vrai : for x in ... va être plus efficace
- ❌ **b)** Faux : calculer un maximum ou un minimum a le **même coût** (une comparaison par élément).

</details>

---

### 2. Que vaut la somme 1 + 2 + … + n ?

a) n(n + 1)  

b) n(n + 1) / 2  

c) n(n - 1) / 2  

<details>
<summary><strong>Corrigé</strong></summary>

✅ **b)** La somme des entiers de 1 à n vaut  
n(n + 1) / 2.

</details>

---

### 3. Qu’affichent les programmes suivants ?

#### a) Range avec valeur initiale

```python
for i in range(4, 10):
    print(i)
```

<details>
<summary><strong>Corrigé</strong></summary>

Affiche les entiers de 4 à 9 :

```
4
5
6
7
8
9
```

</details>

---

#### b) Range avec valeur initiale et pas

```python
for i in range(10, 4, -1):
    print(i)
```

<details>
<summary><strong>Corrigé</strong></summary>

Affiche les entiers de 10 à 5 en ordre décroissant :

```
10
9
8
7
6
5
```

</details>

---

#### c) Boucles imbriquées

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

<details>
<summary><strong>Corrigé</strong></summary>

Toutes les combinaisons de `i` et `j` :

```
0 0
0 1
1 0
1 1
2 0
2 1
```

</details>

---

#### d) Tableau de comparaisons

```python
t = [2 < 5 // 2, 'A' < 'a', 'ab' <= 'a']
print(t)
```

<details>
<summary><strong>Corrigé</strong></summary>

- `5 // 2 = 2`, donc `2 < 2` → False  
- `'A' < 'a'` → True (ordre lexicographique ASCII)  
- `'ab' <= 'a'` → False  

Affichage :

```
[False, True, False]
```

</details>

---

#### e) Énumérer un tableau

```python
for i, x in enumerate(['C', 'A']):
    print(i, x.lower())
```

<details>
<summary><strong>Corrigé</strong></summary>

```
0 c
1 a
```

</details>

---

#### f) Construire un tableau par compréhension

```python
print([x.lower() for x in ['C', 'Ab']])
```

<details>
<summary><strong>Corrigé</strong></summary>

```
['c', 'ab']
```

</details>

---

### 4. Comment échanger les valeurs des variables `a` et `b` en Python ?

a) `swap(a, b)`  

b) `a, b = b, a`  

c) `a = b ; b = a`  

<details>
<summary><strong>Corrigé</strong></summary>

✅ **b)** Python permet l’échange direct grâce à l’affectation multiple.  
Les autres propositions sont incorrectes.

</details>
