# SOLUTIONS  – Chapitre 6 : Trier et chercher

## Exercice 1 — Choisir la (ou les) bonne(s) réponse(s)

### 1) Associer à chaque programme sa complexité dans le pire cas (aux constantes près) pour un tableau de taille n.

Programmes :
- a) Tri par sélection --> 4 --> n²
- b) Tri par insertion --> 4 --> n²
- c) Recherche dichotomique --> 1 --> log2(n)
- d) Recherche linéaire  --> 2 --> n

### 2) a) Linéaire  

### 3) b) Quadratique  

### 4) b) Quadratique  

### 5) b) Quadratique  

### 6) c) en tête du tableau d’entrée  

---

### 7)

a) 1) ['abe', 'Be', 'dda', 'ac', 'abe']


b) 2) ['Be', 'abe', 'abe', 'ac', 'dda']


c) 3) ['dda', 'ac', 'abe', 'abe', 'Be']

---

### 8) i+1,len(t) puis t[j_min],t[i]

## Exercice 2 :
```python
print(t) # t == ['15','2','7']
print(t1) # t1 == ['1515','22','77']
```
Le « piège » est ici que l'on trie sur des chaînes de caractères et non des entiers. Donc la chaîne de caractère '15' est plus petite que '7' puisqu'on compare son premier caractère, '1', avec '7'. 

Remarque: sur l'entrée donnée, cela n'a pas d'impact, mais sur d'autres entrées, il serait important de noter qu'on commence par multiplier la chaîne avant de trier. 

Par exemple:
```python
`sorted([x*2 for x in ['32','3','4'] ]) == ['3232', '33', '44']`
```
alors que 
```python
`[x*2 for x in sorted(['32','3','4']) ] == ['33', '3232', '44']`
```


