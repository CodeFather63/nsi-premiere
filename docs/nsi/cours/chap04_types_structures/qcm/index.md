# QCM — Types et structures

???+ question "Question 1"

    Quelles sont les valeurs de `a` et `b` à la fin du programme suivant ?

    ```python
    a = 10
    b = 20
    a, b = (b, a)
    ```

    - a) `a = 10` et `b = 10`
    - b) `a = 10` et `b = 20`
    - c) `a = 20` et `b = 10`
    - d) `a = 20` et `b = 20`

    ??? success "Réponse"
        **c) `a = 20` et `b = 10`**

---

???+ question "Question 2"

    Quelles expressions parmi les suivantes ne sont pas des tuples Python ?

    - a) `a = ('Bonjour', 42)`
    - b) `a, b = ('Bonjour', 42)`
    - c) `a = (10,)`
    - d) `a = ('John', (10, "Pique"))`
    - e) `a = ['Bonjour', 42]`
    - f) `a = (10)`
    - g) `a = {'Bonjour', 42}`
    - h) `a = ()`

    ??? success "Réponse"
        **b), e), f) et g)**

        - b) est une affectation multiple, pas un tuple
        - e) est un tableau (liste)
        - f) est simplement l'entier 10 entre parenthèses
        - g) est un ensemble (`set`)

        On peut vérifier avec ce programme Python :

        ```python
        a, b = ('Bonjour', 42)

        expressions = {
            "a) a = ('Bonjour', 42)":         ('Bonjour', 42),
            "b) a, b = ('Bonjour', 42)":      b,
            "c) a = (10,)":                   (10,),
            "d) a = ('John', (10, 'Pique'))": ('John', (10, "Pique")),
            "e) a = ['Bonjour', 42]":         ['Bonjour', 42],
            "f) a = (10)":                    (10),
            "g) a = {'Bonjour', 42}":         {'Bonjour', 42},
            "h) a = ()":                      (),
        }

        print(f"{'Expression':<35} {'Valeur':<25} {'Type':<10} {'Tuple ?'}")
        print("-" * 85)
        for desc, val in expressions.items():
            est_tuple = "✅ OUI" if isinstance(val, tuple) else "❌ NON"
            print(f"{desc:<35} {str(val):<25} {type(val).__name__:<10} {est_tuple}")
        ```

---

???+ question "Question 3"

    Quelle est la valeur de `a` à la fin du programme suivant ?

    ```python
    x, y = ((12, "31"), [False])
    (u, v) = x
    a = (v)
    ```

    - a) `(u, "31")`
    - b) `(12,)`
    - c) `False`
    - d) `"31"`

    ??? success "Réponse"
        **d) `"31"`**

---

???+ question "Question 4"

    Comment accéder sans erreur au 5e élément d'un tableau `t` dont on ne connaît pas encore la taille ?

    - a) `a = t[5]`
    - b) `if len(t) > 4: a = t[4]`
    - c) `if len(t) >= 5: a = t[4]`
    - d) `if len(t) > 4: a = t[5]`
    - e) `if len(t) == 5: a = t[4]`
    - f) `a = t[4]`

    ??? success "Réponse"
        **b) et c)**

        Le 5e élément est à l'indice 4. Il faut vérifier que le tableau contient au moins 5 éléments (`len(t) > 4` ou `len(t) >= 5`), puis accéder à `t[4]`.

---

???+ question "Question 5"

    Quelle instruction affiche le premier et le dernier éléments du tableau `t` ?

    - a) `print(t[0], t[len(t)])`
    - b) `print(t[0], t[len(t)-1])`
    - c) `print(t[1], t[len(t)-1])`
    - d) `print(t[1], t[len(t)])`

    ??? success "Réponse"
        **b) `print(t[0], t[len(t)-1])`**

        Le premier élément est à l'indice 0, et le dernier à l'indice `len(t)-1`.

---

???+ question "Question 6"

    Qu'affiche le programme suivant ?

    ```python
    t = ["un", "trois", "deux"]
    print(t[1], t[2])
    ```

    - a) un deux
    - b) un trois
    - c) deux trois
    - d) trois deux

    ??? success "Réponse"
        **d) trois deux**

        `t[1]` vaut `"trois"` et `t[2]` vaut `"deux"`.

---

???+ question "Question 7"

    Qu'affiche le programme suivant ?

    ```python
    d = {1:"un", 3:"trois", 2:"deux"}
    print(d[1], d[2])
    ```

    - a) un deux
    - b) un trois
    - c) deux trois
    - d) trois deux

    ??? success "Réponse"
        **a) un deux**

        `d[1]` vaut `"un"` et `d[2]` vaut `"deux"`.

---

???+ question "Question 8"

    Quelle(s) expression(s) a (ont) pour valeur `('1', 1)` ?

    ```python
    v = [{'1': 0, '2': 1},
         {'2': 2, '1': 1, '0': 0}]
    ```

    - a) `v[1]['1']`
    - b) `('1', v[1]['1'])`
    - c) `(v[0]['1'], v[1]['1'])`
    - d) `(v[0][0], v[1][1])`

    ??? success "Réponse"
        **b) `('1', v[1]['1'])`**

        `v[1]['1']` vaut `1`, donc `('1', v[1]['1'])` vaut bien `('1', 1)`.

---

???+ question "Question 9"

    Quelle est la valeur de `a[1]` à l'issue de l'exécution du programme suivant ?

    ```python
    a = [10, 20, 30]
    b = a
    b[1] = 2
    a = a.copy()
    ```

    - a) 10
    - b) 20
    - c) 30
    - d) 2

    ??? success "Réponse"
        **d) 2**

        `b = a` crée un alias : `b` et `a` référencent le même tableau. La modification `b[1] = 2` change donc aussi `a[1]`. Le `a.copy()` final crée une copie, mais `a[1]` vaut déjà `2` à ce stade.
