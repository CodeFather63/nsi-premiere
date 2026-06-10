# Checkpoint Interaction en QCM


!!! info "Consigne"
    Choisir la (ou les) bonne(s) réponse(s).

---

## 1. Qu’affiche l’instruction `print` suivante ?

```python
a = 10
b = 20
print(f'{a+b} = {a}+{b}')
```

a) a+b = 30  
b) a+b = 10+20  
c) 30 = 10+20  
d) 30 = a+b  

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : c**

</details>

---

## 2. Quelle chaîne de formatage est correcte ?

a) `f 'Bonjour , {prenom}'`  
b) `"Bonjour, {prenom}"`  
c) `f 'Bonjour, {prenom}'`  
d) `Bonjour + prenom`  

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : c**

</details>

---

## 3. Si l’utilisateur tape 123 en réponse à `input("entrer un nombre : ")`, quel est le type ?

a) entier  
b) flottant  
c) chaîne  
d) booléen  
e) autre  

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : c**

</details>

---

## 4. Pour quelles entrées l’instruction suivante provoque-t-elle une erreur ?

```python
reponse = float(input("Réponse : "))
```

a) 123  
b) 12,3  
c) 12.3  
d) Zero  
e) 1e5  

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponses : b et d**

</details>

---

## 5. Quel programme crée un bouton qui écrit « Hello » ?

### a)
```python
def hello():
    write("Hello")
button("Hello", hello())
```

### b)
```python
def hello():
    write("Hello")
button("Hello", hello)
```

### c)
```python
def hello():
    write("Hello")
button("Hello", "hello")
```

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : b**

</details>

---

## 6. Quelle définition de `mystere` permet d’afficher "22" ?

```python
def appel(f):
    print(f() + f())

appel(mystere)
```

a)
```python
def mystere():
    return 2
```

b)
```python
def mystere():
    return 11
```

c)
```python
def mystere():
    return "2"
```

d)
```python
def mystere():
    return "11"
```

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponses : b et c**

</details>

---

## 7. Quelle instruction permet d’afficher la valeur du slider ?

```python
def rappel():
    ???
v = slider("Valeur", 1, 100)
button("Go", rappel)
```

a) `print(v)`  
b) `print(slider)`  
c) `print(get_int(v))`  
d) `print(int(v))`  

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : c**

</details>

---

## 8. Quel est le résultat de ce programme ?

```python
begin_horizontal()
begin_vertical()
button("1", b)
button("2", b)
end_vertical()
button("3", b)
button("4", b)
begin_vertical()
button("5", b)
button("6", b)
end_vertical()
end_horizontal()
```

a)
```
1   3   5
2   4   6
```

b)
```
1           5
    3   4   
2           6
```

c)
```
1   2
3   4
5   6
```

d)
```
1   2   3   4   5   6
```


e)
```
1 
2
3
4
5
6
```

<details>
<summary><strong>Corrigé</strong></summary>

✅ **Réponse : b**

</details>

---

!!! tip "Bilan"
    1. c  
    2. c  
    3. c  
    4. b, d  
    5. b  
    6. b, c  
    7. c  
    8. b 
