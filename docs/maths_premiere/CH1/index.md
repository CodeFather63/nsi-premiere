# Mathématiques Première — Chapitre 1 : Probabilités Conditionnelles

*Lycée Fénelon*

---

## Rappels — Probabilités

### Expérience aléatoire, issues, univers

**Définition 1**
- Une **expérience aléatoire** produit un résultat dont on peut dire deux choses :
  - on connaît tous les résultats possibles,
  - on ne peut pas savoir quel résultat va être produit avant de réaliser l'expérience.
- Un résultat possible s'appelle une **issue** ou **éventualité**.
- L'ensemble des issues possibles s'appelle l'**univers de l'expérience aléatoire** ou **univers des possibles**. On le note souvent $\Omega$.

### Événements associés à une expérience aléatoire

**Définition 2**
On appelle **événement** toute partie de l'univers des possibles.
Un événement réduit à une seule issue est appelé **événement élémentaire**.

**Règles de base**

| Langage des ensembles | Langage des événements | Notation |
|---|---|---|
| $A$ est une partie de $\Omega$ | $A$ est un événement | $A \subset \Omega$ |
| $A$ est vide | l'événement $A$ est **impossible** | $A = \emptyset$ |
| $A$ est égal à $\Omega$ | l'événement $A$ est **certain** | $A = \Omega$ |
| $C$ est la réunion de $A$ et $B$ | $C$ est l'événement ($A$ ou $B$) | $C = A \cup B$ |
| $C$ est l'intersection de $A$ et $B$ | $C$ est l'événement ($A$ et $B$) | $C = A \cap B$ |
| $A$ et $B$ sont disjoints | $A$ et $B$ sont des événements **incompatibles** | $A \cap B = \emptyset$ |
| $A$ et $B$ sont complémentaires | $A$ et $B$ sont des événements **contraires** | $B = \overline{A}$ |

### Loi de probabilité

**Définition 3**
Lorsqu'une expérience aléatoire comporte un nombre fini d'issues, on définit sur l'ensemble $\Omega = \{\omega_1, \dots, \omega_r\}$ des issues une **loi de probabilité** en se donnant une suite de nombres $(p_1, \dots, p_r)$ vérifiant :
- pour tout $i$ tel que $1 \leqslant i \leqslant r$ : $p_i \geqslant 0$,
- $\displaystyle\sum_{i=1}^{r} p_i = 1$.

**Définition 4**
Lorsque toutes les issues ont la même probabilité, on dit qu'il y a **équiprobabilité** ou que la loi est **équirépartie** sur $\Omega$ ou **uniforme**. Dans ce cas, si l'univers des issues $\Omega$ a $r$ éléments, quelle que soit l'issue $\omega_i$ :
$$P(\omega_i) = p_i = \frac{1}{r}.$$

### Probabilité d'un événement

**Définition 5**
La **probabilité d'un événement** $A$ est la somme de toutes les probabilités des issues appartenant à $A$. On pose $P(\emptyset) = 0$.

**Propriété 1**
Lorsque toutes les issues sont équiprobables, on a :
$$P(A) = \frac{\text{nombre d'éléments de } A}{\text{nombre d'éléments de } \Omega} = \frac{\text{Card}(A)}{\text{Card}(\Omega)} = \frac{\text{nombre d'issues favorables à la réalisation de } A}{\text{nombre d'issues possibles}}$$

### Propriétés des probabilités

Ces propriétés, étudiées en classe de seconde, sont rassemblées dans le tableau suivant :

| Parties de $\Omega$ | Langage des événements | Propriété |
|---|---|---|
| $A$ | $A$ est un événement | $0 \leqslant P(A) \leqslant 1$ |
| $\emptyset$ | événement impossible | $P(\emptyset) = 0$ |
| $\Omega$ | événement certain | $P(\Omega) = 1$ |
| $A \cap B = \emptyset$ | $A$ et $B$ sont incompatibles | $P(A \cup B) = P(A) + P(B)$ |
| $\overline{A}$ | $\overline{A}$ est l'événement contraire de $A$ | $P(\overline{A}) = 1 - P(A)$ |
| $A ; B$ | $A$ et $B$ des événements quelconques | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |

---

## Fiche 1 — Probabilités Conditionnelles et arbres pondérés

Dans tout ce chapitre, $\Omega$ désigne un univers, $A$ et $B$ deux événements de $\Omega$ et $P$ une probabilité sur $\Omega$.

### I. Approche de la notion de probabilité conditionnelle

**Exercice 1.** Les 400 élèves de Terminale d'un lycée sont répartis en deux groupes selon leur langue vivante 1 (LV1) : anglais ou allemand. Le tableau suivant précise cette répartition pour les garçons et les filles. Un élève est choisi au hasard dans le fichier des Terminales. On définit les événements suivants :
- $A$ : « l'élève choisi fait anglais »
- $D$ : « l'élève choisi fait allemand »
- $F$ : « l'élève choisi est une fille »
- $G$ : « l'élève choisi est un garçon »

| | Anglais | Allemand |
|---|---|---|
| Garçons | 130 | 50 |
| Filles | 140 | 80 |

1. Préciser l'univers de l'expérience aléatoire ainsi que la loi de probabilité.
2. Calculer la probabilité :
   a. que l'élève soit une fille, notée $P(F)$ ;
   b. que l'élève ait pour LV1 l'allemand, notée $P(D)$.
3. Sachant que l'élève est une fille, quelle est la probabilité que sa LV1 soit l'allemand ?
4. Comparer ce résultat avec $\dfrac{P(D \cap F)}{P(F)}$.

Nous avons calculé à la question 3) la probabilité de $D$ sachant que $F$ est réalisé. Ce nombre, que nous noterons $P_F(D)$ en cours, est égal dans cet exercice à :
$$\frac{\text{effectif de } D \cap F}{\text{effectif de } F} = \frac{\text{fréquence de } D \cap F}{\text{fréquence de } F}$$

Cela explique le résultat obtenu en 4). Nous nous appuierons là-dessus pour la définition de la probabilité conditionnelle.

### II. Généralisation — Probabilités conditionnelles — Définition

**Définition 1**
Si $P(A) \neq 0$, **la probabilité de $B$ sachant $A$**, notée $P_A(B)$, est définie par :
$$P_A(B) = \frac{P(A \cap B)}{P(A)}.$$

**Remarque**
Si $P(B) \neq 0$, on a de manière symétrique :
$$P_B(A) = \frac{P(B \cap A)}{P(B)} = \frac{P(A \cap B)}{P(B)}.$$

**Exemple**
Dans un lycée, on demande aux élèves et aux professeurs s'ils préfèrent avoir cours le matin ou l'après-midi. On obtient les résultats donnés dans le tableau ci-dessous :

| | Matin | Après-midi | Total |
|---|---|---|---|
| Élèves | 657 | 438 | 1 095 |
| Professeurs | 84 | 21 | 105 |
| Total | 741 | 459 | 1 200 |

On choisit une personne au hasard (parmi élèves et professeurs) et on note :
- $E$ l'événement : « La personne tirée au sort est un élève » ;
- $M$ l'événement : « La personne tirée au sort préfère avoir cours le matin ».

1. Calculer $P(E)$ et $P(E \cap M)$.
   On est dans une situation d'équiprobabilité donc :
   - $P(E) = \dfrac{\text{card}(E)}{\text{card}(\Omega)} = \dfrac{1095}{1200} = 0{,}9125$ ;
   - $P(E \cap M) = \dfrac{\text{card}(E \cap M)}{\text{card}(\Omega)} = \dfrac{657}{1200} = 0{,}5475$.
2. En déduire $P_E(M)$ avec la formule de la définition précédente.
   On en déduit que $P_E(M) = \dfrac{P(E \cap M)}{P(E)} = \dfrac{0{,}5475}{0{,}9125} = 0{,}6$.
3. Retrouver ce résultat sans utiliser la formule du cours.
   $P_E(M)$ est « la probabilité que la personne tirée au sort préfère avoir cours le matin sachant que c'est un élève », cette probabilité peut donc être obtenue en calculant :
   $$\frac{\text{card}(E \cap M)}{\text{card}(E)} = \frac{657}{1095} = 0{,}6.$$

### III. Application aux arbres pondérés

**Exercice 2 - Avec un arbre pondéré.**
On reprend la situation de l'exercice précédent que l'on présente sous la forme d'arbre pondéré par des probabilités.

Arbre : depuis la racine, deux branches $F$ (pondération $\frac{11}{20}$) et $\overline{F}$ ; depuis $F$, deux branches $D$ (pondération $\frac{4}{11}$) et $\overline{D}$ ; depuis $\overline{F}$, deux branches $D$ et $\overline{D}$ (pondérations à compléter).

1. L'une des deux pondérations présentes sur cet arbre est une probabilité conditionnelle. Dire laquelle et l'exprimer avec la notation vue au paragraphe 1.
2. a. Exprimer $P_F(D)$ en fonction de $P(F)$ et $P(F \cap D)$.
   b. En déduire $P(F \cap D)$ en fonction de $P_F(D)$ et $P(F)$.
   c. Quelle règle bien connue sur les arbres pondérés retrouve-t-on ?
   d. Compléter la construction de l'arbre en indiquant les probabilités manquantes.

**Propriété 1**
Les principales règles de construction des arbres pondérés ou arbres probabilistes sont :
- la somme des probabilités des événements (disjoints) correspondant aux branches partant d'un même nœud est 1 ;
- les probabilités présentes sur les 2ᵉ, 3ᵉ, etc. branches d'un chemin sont des probabilités conditionnelles.

**Remarques**
- Dans le cas de deux événements $A$ et $B$ de probabilités non nulles, on a deux représentations possibles (arbre en $A$/$\overline A$ puis $B$/$\overline B$, ou l'inverse en $B$/$\overline B$ puis $A$/$\overline A$), avec les pondérations conditionnelles correspondantes ($P_A(B)$, $P_A(\overline B)$, $P_{\overline A}(B)$, $P_{\overline A}(\overline B)$ ou symétriquement). C'est le contexte qui induira de représenter la situation par un arbre ou l'autre.
- Le premier point de la propriété illustre le fait que les événements $A_1, A_2, \dots$ et $A_n$ correspondant aux branches partant du premier nœud sont des événements disjoints, de probabilités non nulles et tels que $A_1 \cup A_2 \cup \dots \cup A_n = \Omega$.
  On dit alors que $A_1, A_2, \dots$ et $A_n$ forment une **partition de l'univers $\Omega$**.

**Propriété 2**
Si $P(A) \neq 0$ et $P(B) \neq 0$, alors $P(A \cap B) = P(A) \times P_A(B) = P(B) \times P_B(A)$.

Cette formule permet de justifier l'une des règles d'utilisation des arbres pondérés :
*la probabilité de l'événement correspondant à un chemin de l'arbre est le produit des probabilités inscrites sur les branches de ce chemin.*

*Démonstration : Conséquence directe de la définition d'une probabilité conditionnelle.* $\square$

**Exemple (Représenter une situation à l'aide d'un arbre pondéré)**

Sur l'étal d'un maraîcher, il y a $\frac{3}{4}$ de légumes rouges et le reste de légumes verts.
- Parmi les légumes rouges 30% sont des poivrons et 70% sont des tomates.
- Parmi les légumes verts 80% sont des poivrons et 20% sont des tomates.

On choisit un légume au hasard sur l'étal et on considère les événements :
- $A$ : « le légume choisi est une tomate » ;
- $R$ : « le légume choisi est Rouge » ;
- $V$ : « le légume choisi est Vert ».

1. Représenter la situation par un arbre.
   Pour le premier nœud, les deux possibilités sont $R$ : « le légume choisi est rouge » et son événement contraire $\overline{R}$ soit $V$ : « le légume choisi est vert ». Il reste ensuite à distinguer tomates et poivrons pour les « deuxièmes nœuds ». Comme l'événement « le légume choisi est un poivron » n'est pas nommé par une lettre, on a utilisé $\overline{A}$ pour le représenter dans l'arbre mais on aurait aussi pu introduire une nouvelle notation.

   Arbre : $R$ (0,75) → $A$ (0,7), $\overline A$ (0,3) ; $V$ (0,25) → $A$ (0,2), $\overline A$ (0,8).

2. Calculer $P(R \cap A)$.
   $P(R \cap A) = P(R) \times P_R(A) = 0{,}75 \times 0{,}7 = 0{,}525$.

### Exercices

**Exercice 3.** $A, B, C, D, E$ et $H$ désignent des événements quelconques d'un univers $\Omega$.
1. Trouver l'erreur dans l'arbre de probabilité suivant : arbre partant en $A$ / $B$ (racine sans pondération sommant à 1 clairement identifiée), puis $A \to \overline{A}, \overline{B}$ et $B \to \overline{A}, \overline{B}$ (les branches secondaires reprennent les mêmes labels $\overline A/\overline B$ ce qui est incohérent).
2. Quelle(s) condition(s) doivent vérifier les événements $C$, $D$ et $E$ pour que l'arbre ci-dessous (racine → $C$ (0,2) → $H$ (0,1)/$\overline H$ (0,9) ; racine → $D$ (0,35) → $H$ (0,15)/$\overline H$ (0,85) ; racine → $E$ ($P(E)$) → $H$ (0,99)/$\overline H$ (0,01)) soit un arbre pondéré correct ?

**Exercice 4.**
1. On considère deux événements $R$ et $S$ tels que $P(R) = \dfrac{1}{4}$, $P_R(S) = \dfrac{5}{6}$ et $P_{\overline{R}}(\overline{S}) = \dfrac{11}{12}$.
   Construire un arbre pondéré avec ces événements $R$ et $S$.
2. Tao ne sait pas s'il lui reste de quoi préparer à manger dans son réfrigérateur. Il estime la probabilité que ce soit le cas à 0,8.
   - Dans ce cas (s'il a de quoi préparer à manger), il estime que la probabilité que le repas qu'il se préparera soit bon est de 0,65.
   - Sinon, il ira dans son restaurant favori dans lequel il estime que la probabilité que le repas servi soit bon est de 0,99.

   Construire un arbre pondéré représentant la situation après avoir explicité les notations des événements apparaissant dans cet arbre.

**Exercice 5.** On considère deux événements $A$ et $B$ tels que $P(A) = 0{,}1$ et $P(A \cap B) = 0{,}06$. Calculer $P_A(B)$.

**Exercice 6.** On considère deux événements $C$ et $D$ tels que $P(D) = 0{,}6$ et $P(C \cap \overline{D}) = 0{,}35$. Calculer $P_{\overline{D}}(C)$.

**Exercice 7.** On considère deux événements incompatibles $E$ et $F$ de probabilités non nulles. Calculer $P_E(F)$.

**Exercice 8.** On considère deux événements $A$ et $B$ tels que $P(A) = 0{,}37$, $P(B) = 0{,}68$ et $P(A \cup B) = 0{,}84$. Calculer :
1. $P_A(B)$
2. $P_B(A)$

**Exercice 9.** On considère deux événements $A$ et $B$ tels que $P(A) = 0{,}63$ et $P_A(B) = 0{,}06$. Calculer :
1. $P(A \cap B)$
2. $P(A \cap \overline{B})$

**Exercice 10.** On considère deux événements $E$ et $F$ tels que $P(E) = \dfrac{1}{3}$ et $P_{\overline{E}}(F) = \dfrac{7}{12}$. Calculer :
1. $P(\overline{E} \cap F)$
2. $P(\overline{E} \cap \overline{F})$

**Exercice 11 - Avec des phrases.**
1. Dans une bibliothèque, les statistiques montrent que : 55% des adhérents sont des garçons ; 20% des adhérents sont des garçons ayant emprunté plus de 50 livres.
   Quand on rencontre un garçon sortant de la bibliothèque, quelle est la probabilité qu'il ait emprunté plus de 50 livres ?
2. Quand on joue à un jeu de grattage, la probabilité d'obtenir « 3 télés » est de 0,000001.
   Si c'est le cas, on est invité à la télévision pour faire tourner une roue comportant 100 sections équiprobables dont 5 offrent un gain de 1 000 000 €.
   Quelle est la probabilité de gagner 1 000 000 € à ce jeu ?
3. « Je suis sûr à 95% de manquer le bus, auquel cas je serai en retard. Et même si je l'ai, il y aura une chance sur trois que je sois quand même en retard ».
   Quelle est la probabilité que cette personne soit à l'heure ?
4. Dans le lecteur MP3 d'Anita, 17% des titres sont du rock français. Plus généralement, 61% des titres du lecteur sont des titres français.
   On met le lecteur en mode aléatoire et le premier titre est français. Quelle est la probabilité que ce soit du rock ?

**Exercice 12.** Après les contrôles de mathématiques, 60% du temps, Issa dit « Je suis sûr que j'ai loupé ». Ses amis sont pourtant formels : « Quand il dit ça, il a quand même 15 ou plus les 3/4 du temps. Et quand il ne dit rien, on peut être sûr à 95% qu'il va avoir 15 ou plus. »
Après un devoir de mathématiques, on considère les événements :
- $L$ : « Issa dit qu'il a manqué le devoir » ;
- $B$ : « Issa a 15 ou plus au devoir ».

1. Recopier et compléter l'arbre (racine → $L$ / $\overline{L}$ → chacun $B$/$\overline B$).
2. Calculer $P(L \cap B)$ et interpréter cette probabilité dans les termes de l'énoncé.
3. Calculer la probabilité qu'il ne dise rien et qu'il ait moins de 15.

**Exercice 13.** Dans une playlist, Naïm a mis 10 albums et réglé le lecteur en sélection aléatoire. Le logiciel de sélection aléatoire choisit d'abord un album puis choisit une chanson dans cet album.
Quelle est la probabilité que la 1ʳᵉ chanson jouée soit la préférée de Naïm, qui se trouve dans un album de 12 titres ? On représentera la situation par un arbre.

**Exercice 14.** On considère deux événements $A$ et $B$ et le tableau de probabilités ci-dessous :

| | $A$ | $\overline{A}$ | Total |
|---|---|---|---|
| $B$ | 0,44 | | |
| $\overline{B}$ | | 0,13 | 0,32 |
| Total | | | 1 |

1. Compléter ce tableau.
2. Lire $P(A)$, $P(\overline{B})$, $P(A \cap \overline{B})$ et $P(\overline{A} \cap \overline{B})$.
3. Calculer $P_A(B)$, $P_A(\overline{B})$, $P_{\overline{A}}(B)$ et $P_{\overline{A}}(\overline{B})$. On écrira les résultats sous forme de fractions irréductibles.
4. Recopier et compléter l'arbre en partant de $A/\overline A$ puis $B/\overline B$.
5. De même, recopier et compléter l'arbre en partant de $B/\overline B$ puis $A/\overline A$.

**Exercice 15. Groupes sanguins et facteur rhésus**
Dans une population, les individus sont répartis en quatre groupes sanguins : A, B, AB et O et à l'intérieur de chaque groupe, en rhésus + ou rhésus -, selon le tableau suivant (en %).

| groupe | A | B | AB | O |
|---|---|---|---|---|
| Rhésus + | 32,8 | 8,1 | 4,15 | 36 |
| Rhésus - | 7,2 | 1,9 | 0,85 | 9 |

Un individu est choisi au hasard. Calculer la probabilité :
1. qu'il soit du groupe O, sachant qu'il a un rhésus -.
2. qu'il ait un rhésus -, sachant qu'il est du groupe O.

**Exercice 16.** Dans un lycée, 40% des garçons et 15% des filles mesurent plus de 1,80 m. De plus, 60% des élèves sont des filles. Sachant qu'un élève choisi au hasard mesure plus de 1,80 m, quelle est la probabilité que ce soit une fille ?

**Exercice 17.** On lance deux dés équilibrés. On considère les événements suivants :
$A$ : « la somme est paire », $B$ : « on a obtenu au moins un six » et $C$ : « on a obtenu un double ».
1. Calculer $P(A), P(B), P(C), P(A \cap B), P(A \cap C)$ et $P(B \cap C)$.
2. En déduire $P_A(B)$, $P_A(C)$, $P_B(A)$, $P_B(C)$, $P_C(A)$, $P_C(B)$.

**Exercice 18.** Une urne contient 5 boules rouges, 3 jaunes et 2 vertes, indiscernables au toucher.
1. On tire successivement et sans remise 2 boules de l'urne. Calculer la probabilité d'obtenir 2 rouges ? 2 jaunes ? 2 vertes ? 2 boules de même couleur ?
2. Mêmes questions si l'on remet dans l'urne la boule issue du premier tirage.

**Exercice 19 - Trois à la suite.** A-t-on $P(A \cap B \cap C) = P(A) \times P_A(B) \times P_B(C)$ ?
Si oui, le démontrer, si non, modifier la formule pour en obtenir une correcte.

---

## Fiche 2 — Formule des Probabilités totales

**Propriété 3 (Formule des probabilités totales)**
- Si $P(A) \neq 0$ et $P(A) \neq 1$ alors :
$$P(B) = P(A \cap B) + P(\overline{A} \cap B) = P(A) \times P_A(B) + P(\overline{A}) \times P_{\overline{A}}(B).$$
- De même, si $A_1, A_2, \dots$ et $A_n$ forment une partition de $\Omega$, c'est-à-dire sont $n$ évènements disjoints, de probabilités non nulles et tels que $A_1 \cup A_2 \cup \dots \cup A_n = \Omega$ alors
$$P(B) = P(A_1 \cap B) + P(A_2 \cap B) + \dots + P(A_n \cap B) = P(A_1) \times P_{A_1}(B) + P(A_2) \times P_{A_2}(B) + \dots + P(A_n) \times P_{A_n}(B).$$

*Démonstration :*
- On a $B = (A \cap B) \cup (\overline{A} \cap B)$. De plus, les évènements $A \cap B$ et $\overline{A} \cap B$ sont disjoints. Par conséquent, on a : $P(B) = P(A \cap B) + P(\overline{A} \cap B)$.
  On en déduit que : $P(B) = P(A) \times P_A(B) + P(\overline{A}) \times P_{\overline{A}}(B)$.
- Le second point se démontre de même car les évènements $A_k \cap B$ pour $k$ allant de 1 à $n$ forment une partition de $B$. $\square$

**Remarque**
La formule des probabilités totales permet de justifier une autre règle d'utilisation des arbres pondérés : *la probabilité d'un évènement est la somme des probabilités associées aux chemins qui permettent de réaliser cet évènement.*

**Exemple (Utiliser la formule des probabilités totales)**
En 2015, la répartition des élèves ayant passé le baccalauréat général en France métropolitaine et dans les DOM est : 17% d'élèves de la filière L, 31% de la filière ES et 52% de la filière S. Par ailleurs, les taux de réussite dans ces filières sont 90,6% en L, 91,2% en ES et 91,8% en S. On tire au hasard un élève ayant passé le bac général en 2015.

1. Dresser un arbre pondéré représentant la situation.
   On obtient l'arbre où :
   - $L$ est l'évènement : « la personne a passé le bac L » ;
   - $E$ est l'évènement : « la personne a passé le bac ES » ;
   - $S$ est l'évènement : « la personne a passé le bac S » ;
   - $B$ est l'évènement : « la personne a obtenu le bac ».

   Arbre : $L$ (0,17) → $B$ (0,906) / $\overline B$ (0,094) ; $E$ (0,31) → $B$ (0,912) / $\overline B$ (0,088) ; $S$ (0,52) → $B$ (0,918) / $\overline B$ (0,082).

2. Quelle est la probabilité que la personne tirée au hasard ait obtenu le bac ?
   La formule des probabilités totales donne
   $$P(B) = P(L) \times P_L(B) + P(E) \times P_E(B) + P(S) \times P_S(B) = 0{,}17 \times 0{,}906 + 0{,}31 \times 0{,}912 + 0{,}52 \times 0{,}918 = 0{,}9141.$$

3. Déterminer $P_{\overline{B}}(S)$.
   On sait que $P_{\overline{B}}(S) = \dfrac{P(\overline{B} \cap S)}{P(\overline{B})}$ où :
   - $P(\overline{B} \cap S) = P(S) \times P_S(\overline{B}) = 0{,}52 \times 0{,}082 = 0{,}04264$ ;
   - $P(\overline{B}) = 1 - P(B) = 1 - 0{,}9141 = 0{,}0859$.

   On en déduit donc que $P_{\overline{B}}(S) = \dfrac{0{,}04264}{0{,}0859} \approx 0{,}496$.

### Exercices

**Exercice 20.** On considère deux évènements $A$ et $B$ tels que $P(A) = 0{,}8$ et $P(A \cap B) = 0{,}48$.
1. Montrer que $P(A \cap \overline{B}) = 0{,}32$.
2. Calculer $P_A(\overline{B})$.

**Exercice 21.** On considère deux évènements $E$ et $F$ tels que $P(E) = 0{,}4$ et $P(\overline{E} \cap \overline{F}) = 0{,}12$. Calculer $P_{\overline{E}}(F)$.

**Exercice 22.** On considère deux évènements $A$ et $B$ tels que $P(A) = 0{,}45$ ; $P(B) = 0{,}6$ et $P(A \cup B) = 0{,}71$. Calculer :
1. $P_A(B)$
2. $P_A(\overline{B})$
3. $P_{\overline{B}}(A)$
4. $P_{\overline{B}}(\overline{A})$

**Exercice 23 - D'après Bac.**
Sophie a mis des dragées dans une boîte, les unes contiennent une amande, les autres non :
- 30% des dragées contiennent une amande ;
- 40% des dragées avec amande sont bleues, les autres sont roses ;
- 75% des dragées sans amande sont bleues, les autres sont roses.

Sophie choisit au hasard une dragée dans la boîte et on considère les événements :
- $A$ : « la dragée choisie contient une amande » ;
- $B$ : « la dragée choisie est bleue ».

1. Recopier et compléter l'arbre pondéré ci-contre.
2. Montrer que $P(A \cap B) = 0{,}12$.
3. Calculer $P(B)$.
4. En déduire $P_B(A)$.
5. Calculer $P_{\overline{B}}(A)$.
6. Sophie préfère les dragées contenant une amande. Doit-elle plutôt choisir une dragée bleue ou bien une dragée rose ?

**Exercice 24 - Améliorer la qualité.**
Ordralfabétix est poissonnier et 15% du poisson qu'il vend a été pêché par ses soins, 30% vient d'un grossiste armoricain et le reste d'un grossiste de Lutèce.
Il a remarqué que 5% de ses clients sont mécontents du poisson qu'il a lui-même pêché, 10% du poisson provenant du grossiste armoricain et 90% du poisson de Lutèce.
Un client achète un poisson à Ordralfabétix.
On considère les évènements suivants :
- $O$ : « Le poisson a été pêché par Ordralfabétix »
- $A$ : « Le poisson provient du grossiste armoricain »
- $L$ : « Le poisson provient du grossiste de Lutèce »
- $M$ : « Le client est mécontent du poisson »

1. Recopier et compléter l'arbre probabiliste ci-contre.
2. a. Calculer $P(M)$.
   b. Un client est mécontent du poisson acheté. Quelle est la probabilité que ce poisson ait été pêché par Ordralfabétix ?
3. Ordralfabétix souhaite ramener le taux de mécontentement à 30% en continuant à pêcher 15% de sa production. Déterminer les proportions de poisson qu'il doit commander à chaque grossiste pour atteindre son objectif.

**Exercice 25 - Épidémiologie.**
Dans un pays, une épidémie touche 10% de la population. Un test de dépistage de la maladie a été mis au point mais il n'est pas parfait :
- si un individu n'est pas touché par la maladie, le test est tout de même positif dans 1% des cas ;
- si un individu est touché par la maladie, le test est tout de même négatif dans 0,1% des cas.

1. Représenter la situation par un arbre pondéré.
2. Toute la population passe le test de dépistage et on décide de donner un traitement à tous les individus ayant un test positif.
   a. Montrer que le traitement est donné à 10,89% de la population.
   b. À quel pourcentage de la population le traitement est-il donné à tort ?

**Exercice 26 - Réduire les coûts.**
Sur une chaîne de production d'un composant électronique, on effectue des tests qualité :
- Un premier examen visuel est effectué éliminant 5% des composants, qui sont détruits.
- Les composants restants passent un test de fiabilité qui est réussi par 90% des composants qui sont alors mis en vente.
- Parmi les composants n'ayant pas réussi le test de fiabilité, 30% peuvent être réparés facilement et mis en vente, le reste est détruit.

On prélève un composant au hasard sur cette chaîne.
1. Représenter la situation par un arbre de probabilité. On notera $E$ l'événement « le composant réussit l'examen visuel », $F$ « le composant réussit le test de fiabilité » et $V$ « le composant est mis en vente ».
2. Calculer $P(\overline{F} \cap V)$, $P(V)$ et $P_V(\overline{F})$.

**Exercice 27.** Compléter l'arbre 2 en utilisant l'arbre 1 :
Arbre 1 : $A$ (1/5) → $B$ (1/8) / $\overline{B}$ (7/8) ; $\overline{A}$ (4/5) → $B$ (4/9) / $\overline{B}$ (5/9).
Arbre 2 : (à partir de $B/\overline{B}$ puis $A/\overline{A}$, à compléter).

**Exercice 28.** Chez Edmond, la vaisselle se joue toujours aux jeux vidéo de la façon suivante : on lance une pièce et :
- si c'est pile, il affronte sa mère à un jeu de combat où il n'a que 30% de chance de gagner ;
- si c'est face, il affronte son père à un jeu de puzzle (avec des briques) où il a 40% de chance de perdre.

S'il perd sa partie, il fait la vaisselle, sinon, ses parents s'affrontent sur un jeu de stratégie où ils sont aussi bons l'un que l'autre pour savoir qui fera la vaisselle.
Ce soir, c'est le père d'Edmond qui est de vaisselle. Quelle est la probabilité que le premier duel ait eu lieu sur le jeu de puzzle ?

**Exercice 29 - Question ouverte.**
D'après l'« Enquête nationale prénatale » de 2010 réalisée par l'Inserm, la probabilité d'une grossesse donnant lieu à une naissance prématurée en France est de 6,6% mais est accentuée par le fait que la grossesse soit multiple (jumeaux, triplés, etc) ou non.
Plus précisément, cette probabilité est de 41,7% en cas de grossesse multiple contre 5,5% sinon.
Déterminer la probabilité d'une grossesse multiple.

**Exercice 30 - Génétique.**
Le daltonisme est une maladie génétique à transmission récessive liée au chromosome X c'est-à-dire que l'allèle responsable est récessif, pour un gène présent sur le chromosome X.
- Pour une femme, on distinguera le fait d'être malade (présence de l'allèle responsable sur les deux chromosomes X), porteuse de la maladie (présence de l'allèle responsable sur un seul chromosome X) et saine (absence totale de l'allèle responsable).
- Pour un homme, la présence de l'allèle sur l'unique chromosome X assure qu'il est malade.

Béatrice a un père daltonien mais elle-même n'est pas malade.
Sachant que 8% des hommes sont daltoniens, quelle est la probabilité que Béatrice ait un enfant daltonien ?
On admettra que le daltonisme ou non d'une personne n'influence pas préférentiellement le don d'un chromosome X ou Y.

**Exercice 31.**
1. Dans l'urne de l'exercice 18, on tire successivement et sans remise 2 boules.
   On note les événements $R_1$ : « la première boule tirée est rouge », $R_2$ : « la deuxième boule tirée est rouge », et de même $J_1$, $J_2$, $V_1$ et $V_2$.
   a. À l'aide d'une partition convenable, calculer $P(R_2)$.
   b. Calculer de même $P(J_2)$ et $P(V_2)$.
   c. Comparer les nombres trouvés à $P(R_1)$ ; $P(J_1)$ et $P(V_1)$. Remarque ?
2. Dans la même urne, on réalise à présent trois tirages successifs sans remise. Calculer la probabilité de $R_3$ : « la troisième boule tirée est rouge ». Remarque ?

**Exercice 32.** Trois personnes A, B et C choisissent une case au hasard dans une figure en forme de croix composée de douze cases (une rangée centrale de huit cases, avec une case au-dessus et une case au-dessous de la deuxième case en partant de la droite, formant une zone grise de quatre cases au centre).

On s'intéresse à l'événement $G$ : « la case est grise ».

A affirme : « $P(G) = \dfrac{1}{3}$ » ; B répond : « mais non, $P(G) < \dfrac{1}{4}$ » ; enfin, C prétend : « $P(G) > \dfrac{1}{2}$ ».

1. Envisager les trois protocoles suivants au choix de la case :
   a. choix d'une case parmi les douze
   b. choix d'une colonne au hasard, puis d'une case au hasard dans cette colonne
   c. choix d'une ligne au hasard, puis d'une case au hasard dans cette ligne.
   Dans chaque cas, calculer $P(G)$.
2. Quelle est la morale de cette histoire ?

---

## Fiche 3 — Indépendance de deux événements

**Définition 2**
On dit que $A$ et $B$ sont **indépendants** lorsque :
$$P(A \cap B) = P(A) \times P(B).$$

**Remarque**
Attention à ne pas confondre « indépendants » et « incompatibles » qui est synonyme de disjoints c'est-à-dire que $A \cap B = \emptyset$ et non pas $P(A \cap B) = P(A) \times P(B)$.

**Exemple**
Dans la population, il y a :
- 71% de porteurs de lunettes parmi lesquels 37% ont 55 ans ou plus ;
- 63% de personnes de moins de 55 ans.

On tire au sort une personne dans la population et on considère les deux évènements :
- $A$ : « la personne a 55 ans ou plus » ;
- $L$ : « la personne porte des lunettes ».

Les évènements $A$ et $L$ sont-ils indépendants ?

On détermine puis on compare $P(A) \times P(L)$ et $P(A \cap L)$.
D'après l'énoncé, $P(L) = 0{,}71$. De plus, $P(A) = 1 - 0{,}63 = 0{,}37$, donc : $P(A) \times P(L) = 0{,}37 \times 0{,}71 = 0{,}2627$.

D'autre part, d'après l'énoncé, $P_L(A) = 0{,}37$, donc :
$$P(A \cap L) = P(L) \times P_L(A) = 0{,}71 \times 0{,}37 = 0{,}2627.$$

Comme $P(A) \times P(L) = P(A \cap L)$, on en déduit que $A$ et $L$ sont indépendants.

**Propriété 4**
Si $P(A) \neq 0$ (ou $P(B) \neq 0$) alors :
$A$ et $B$ sont indépendants si et seulement si $P_A(B) = P(B)$ (ou $P_B(A) = P(A)$).

*Démonstration :*
Soit $A$ un événement tel que $P(A) \neq 0$,
$A$ et $B$ sont indépendants si et seulement si $P(A \cap B) = P(A) \times P(B)$
si et seulement si $P(A) \times P_A(B) = P(A) \times P(B)$
si et seulement si $P_A(B) = P(B)$. $\square$

**Remarques**
1. Cette formulation rend plus naturelle la définition : il paraît normal de considérer comme « indépendants », au sens intuitif du terme, deux événements $A$ et $B$ dès lors que la probabilité de $B$ est la même que la probabilité de $B$ sachant $A$. En effet, $P_A(B) = P(B)$ traduit le fait que savoir que $A$ est réalisé ne modifie pas la probabilité de $B$, autrement dit, que la réalisation de $A$ n'a pas d'influence sur la réalisation de $B$.
2. Dans l'exemple précédent, on aurait donc pu conclure directement puisque $P(A) = P_L(A)$.

**Propriété 5**
Si $A$ et $B$ sont deux évènements indépendants alors $\overline{A}$ et $B$ sont indépendants.

*Démonstration :*
Soit $A$ et $B$ deux évènements indépendants.
Montrons que $P(\overline{A} \cap B) = P(\overline{A}) \times P(B)$.
D'après la formule des probabilités totales, on a : $P(B) = P(\overline{A} \cap B) + P(A \cap B)$
D'où : $P(\overline{A} \cap B) = P(B) - P(A \cap B)$.
De plus, comme $A$ et $B$ sont indépendants, on a $P(A \cap B) = P(A) \times P(B)$.
On obtient ainsi :
$$P(\overline{A} \cap B) = P(B) - P(A) \times P(B) = (1 - P(A)) \times P(B) = P(\overline{A}) \times P(B).$$
D'où le résultat. $\square$

**Exemple**
Dans l'exemple précédent, les événements $A$ : « la personne a 55 ans ou plus » et $\overline{L}$ : « la personne ne porte pas de lunettes » sont donc également indépendants.

**Remarque**
Plus généralement, si $A$ et $B$ sont indépendants alors :
- $\overline{A}$ et $B$ sont indépendants,
- $\overline{A}$ et $\overline{B}$ sont indépendants,
- $A$ et $\overline{B}$ sont indépendants.

### Exercices

**Exercice 33.** On considère deux évènements indépendants $A$ et $B$ tels que $P(A) = 0{,}15$ et $P(A \cap B) = 0{,}085$. Calculer $P(B)$.

**Exercice 34.** On considère deux évènements indépendants $E$ et $F$ tels que $P(\overline{F}) = 0{,}53$ et $P(E \cap F) = 0{,}25$. Calculer $P(E)$.

**Exercice 35.** On considère deux évènements indépendants $C$ et $D$ tels que $P(C \cup D) = 0{,}23$ et $P(C) = 0{,}11$. Calculer $P(D)$.

**Exercice 36 - Indépendants et incompatibles ?**
Deux évènements incompatibles de probabilités non nulles peuvent-ils être indépendants ?

**Exercice 37 - Couleurs aléatoires.**
On considère l'algorithme suivant où la commande $entalea(n;p)$ donne un entier aléatoire entre $n$ et $p$ :

```
1: a prend la valeur entalea(1;3)
2: if a = 1 then
3:     b prend la valeur entalea(1;3)
4:     if b = 1 then
5:         print "rouge"
6:     else
7:         print "orange"
8:     end if
9: end if
10: if a = 2 then
11:     b prend la valeur entalea(1;4)
12:     if b = 1 then
13:         print "rouge"
14:     else
15:         print "orange"
16:     end if
17: end if
18: if a = 3 then
19:     b prend la valeur entalea(1;24)
20:     if b <= 7 then
21:         print "rouge"
22:     else
23:         print "orange"
24:     end if
25: end if
```

Les évènements suivants sont-ils indépendants ?
1. « a = 3 » et « l'algorithme affiche rouge ».
2. « a = 3 » et « l'algorithme affiche orange ».
3. « a = 1 » et « l'algorithme affiche rouge ».

**Exercice 38.** Dans un magasin de meubles, il y a 55% de canapés dont 14% en cuir, 30% de fauteuils dont 20% en cuir et le reste est constitué de poufs dont 42% en cuir.
Un client se présente et choisit un meuble.
On considère les évènements :
- $F$ : « le meuble choisi est un fauteuil » ;
- $C$ : « le meuble choisi est en cuir ».

Montrer que ces deux évènements sont indépendants.

**Exercice 39.** Lily a dans sa poche deux pièces de 20 centimes, trois de 50 centimes et une de 1 euro.
Elle tire successivement (sans remise) deux pièces de sa poche. Les évènements « les deux pièces sont du même montant » et « les deux pièces lui permettent d'acheter un croissant à 1 euro » sont-ils indépendants ?

**Exercice 40.** Aujourd'hui Nathalie a décidé d'aller donner son sang. Ben hésite alors : « Je vais peut-être en profiter pour aller faire du vélo le long des bords de Seine ». On considère que la probabilité qu'il aille faire du vélo est 0,85.
Nathalie ayant un petit volume sanguin, il est possible qu'on ne l'autorise pas à donner son sang (elle est « refusée » une fois sur cinq) auquel cas, si Ben est parti faire du vélo, il ne sera pas là quand elle rentrera. Dans tous les autres cas, il sera là quand elle rentrera.
En admettant que les évènements « Nathalie n'est pas autorisée à donner son sang » et « Ben choisit d'aller faire du vélo » soient indépendants, quelle est la probabilité que Ben soit là quand Nathalie rentrera ?

**Exercice 41.** Dans la chorale d'un lycée, il y a 7 élèves de Seconde, 9 élèves de Première et $n$ élèves de Terminale.
De plus, parmi les élèves de Seconde, il n'y a qu'une seule fille, contre 3 parmi les élèves de Première et 6 parmi les élèves de Terminale.
On tire au sort un élève de la chorale.
1. Déterminer pour quelle(s) valeur(s) de $n$ les évènements « l'élève est en Terminale » et « l'élève est une fille » sont indépendants.
2. Pour $n = 24$, que peut-on dire de l'indépendance éventuelle des évènements :
   a. « l'élève est en Terminale » et « l'élève est un garçon » ?
   b. « l'élève est en Première » et « l'élève est une fille » ?

**Exercice 42.**
1. Soit A et B deux événements indépendants. Montrer qu'il en est de même pour :
   a. $A$ et $\overline{B}$
   b. $B$ et $\overline{A}$
   c. $\overline{A}$ et $\overline{B}$
2. Deux archers tirent simultanément. Les deux événements « A atteint la cible » et « B atteint la cible » sont indépendants et de probabilités $\dfrac{4}{5}$ et $\dfrac{7}{8}$.
   Calculer la probabilité des événements :
   a. A et B atteignent tous deux la cible
   b. seul A atteint sa cible
   c. la cible est manquée
   d. la cible est atteinte
   e. un seul tireur atteint la cible

**Exercice 43.** Un avion se maintient en vol si le moteur central ou les moteurs sur les ailes fonctionnent.
Le moteur central a pour sécurité $P_1 = \dfrac{199}{200}$, les moteurs d'ailes ont chacun la sécurité $P_2 = \dfrac{9}{10}$ et les moteurs fonctionnent ou non indépendamment les uns des autres. Quel est la probabilité que l'avion tombe ?

**Exercice 44.** On lance deux fois une pièce de monnaie. Les événements A, B et C sont définis par : $A$ : « pile sort en premier », $B$ : « pile sort en second » et $C$ : « les deux sorties sont identiques »
1. Montrer que $A$ et $B$ sont indépendants, puis que $A$ et $C$ et enfin $B$ et $C$ le sont.
2. Comparer $P(A \cap B \cap C)$ et $P(A)P(B)P(C)$.

**Exercice 45.** Contrôle de probabilités aujourd'hui en Terminale... Mais « le prof de math » est terriblement distrait : il se trompe d'étage une fois sur cinq, oublie sa clé de salle une fois sur dix, et oublie ses sujets à la maison une fois sur quinze. Quelle est la probabilité que le contrôle ait lieu, sans retard ?

---

## Fiche 4 — Exercices de bac

**Exercice 46.** Dans tout l'exercice, les résultats seront arrondis, si nécessaire, au dix millième. On étudie un test de dépistage pour une certaine maladie dans une population donnée. On sait que 1% de la population est atteint de la maladie. Des études ont montré que si une personne est malade, alors le test se révèle positif dans 97% des cas et si une personne n'est pas malade, le test est négatif dans 98% des cas. Pour une personne à qui on fait passer le test de dépistage on associe les événements :
- M : la personne est malade,
- T : le test est positif.

1. Recopier et compléter sur la copie l'arbre de probabilité suivant en utilisant les données de l'exercice (racine → $M$ / $\overline M$ → chacun $T$/$\overline T$).
2. Justifier que $P(\overline{M} \cap T) = 0{,}0198$.
3. Montrer que $P(T) = 0{,}0295$.
4. Calculer $P_T(M)$.
5. Une personne dont le test se révèle positif est-elle nécessairement atteinte par cette maladie ?

**Exercice 47.** Un cafetier propose à ses clients des cookies au chocolat ou aux noisettes en s'approvisionnant dans trois boulangeries. Un client prend un cookie au hasard. On note :
- $C$ l'événement « le cookie est au chocolat »,
- $N$ l'événement « le cookie est aux noisettes »,
- $B_1$ l'événement « le cookie provient de la boulangerie 1 »,
- $B_2$ l'événement « le cookie provient de la boulangerie 2 »,
- $B_3$ l'événement « le cookie provient de la boulangerie 3 »,

On suppose que :
- la probabilité que le cookie provienne de la boulangerie 1 est de 0,49 ;
- la probabilité que le cookie provienne de la boulangerie 2 est de 0,36 ;
- $P_{B_2}(C) = 0{,}4$ où $P_{B_2}(C)$ est la probabilité conditionnelle de $C$ sachant $B_2$ ;
- la probabilité que le cookie soit aux noisettes sachant qu'il provient de la troisième boulangerie est de 0,3.

L'arbre pondéré ci-dessous correspond à la situation et donne une information supplémentaire : le nombre 0,6 sur la branche de $B_1$ à $C$.

Arbre : $B_1$ (à compléter) → $C$ (0,6) / $\overline C$ ; $B_2$ (à compléter) → $C$ / $\overline C$ ; $B_3$ (à compléter) → $C$ / $\overline C$.

1. Exprimer par une phrase l'information donnée par le nombre 0,6 sur la branche de $B_1$ à $C$.
2. Recopier et compléter sur la copie l'arbre pondéré ci-dessus.
3. Définir par une phrase l'événement $B_1 \cap C$ et calculer sa probabilité.
4. Montrer la probabilité $P(C)$ d'avoir un cookie au chocolat est égale à 0,543.
5. Calculer la probabilité d'avoir un cookie provenant de la boulangerie 2 sachant qu'il est au chocolat. On donnera le résultat arrondi au millième.

**Exercice 48.** Les résultats seront donnés sous forme de fractions irréductibles.
Une enquête a été menée auprès de lycéens pour estimer la proportion de ceux qui ont déjà consommé du cannabis. Pour encourager les réponses sincères, on met en place le protocole suivant : Chaque adolescent lance d'abord un dé équilibré à 6 faces et l'enquêteur qui va l'interroger ne connaît pas le résultat du lancer. À la question « Avez-vous déjà consommé du cannabis ? », l'adolescent doit répondre :
- « non » si le résultat du lancer est 5, qu'il ait ou non déjà consommé du cannabis ;
- « oui » si le résultat du lancer est 6, qu'il ait ou non déjà consommé du cannabis ;
- « oui » ou « non » dans les autres cas, mais de façon sincère.

On note :
- $N$ : l'événement l'adolescent a répondu « non » ;
- $O$ : l'événement l'adolescent a répondu « oui » ;
- $C$ : l'événement l'adolescent a déjà consommé effectivement du cannabis ;
- $\overline{C}$ : l'événement l'adolescent n'a jamais consommé du cannabis.

Sur les lycéens qui ont participé à cette enquête on constate que la probabilité qu'un adolescent ait répondu « oui » est de $\dfrac{3}{5}$, soit $p(O) = \dfrac{3}{5}$. On veut déterminer la probabilité, notée $p$, qu'un adolescent ait déjà consommé du cannabis. On a donc $p(C) = p$.

1. Justifier que la probabilité qu'un adolescent ait répondu « oui » sachant qu'il n'a jamais consommé de cannabis est $\dfrac{1}{6}$.
2. On a ci-dessous l'arbre de probabilités représentant la situation (racine → $C$ (probabilité $p$) → $O$ / $N$ (pondération $\frac{1}{6}$ indiquée) ; racine → $\overline{C}$ → $O$ (pondération $\frac{1}{6}$) / $N$). Compléter cet arbre.
3. a. Démontrer que la probabilité $p$ qu'un adolescent ait déjà consommé du cannabis vérifie l'équation : $\dfrac{2}{3}p + \dfrac{1}{6} = \dfrac{3}{5}$.
   b. En déduire la valeur de $p$.
4. Sachant qu'un adolescent a répondu « non » pendant l'enquête, quelle est la probabilité qu'il n'ait jamais consommé de cannabis ?

---

## Fiche 5 — Exercices d'approfondissement

**Exercice 49.** Une urne contient 5 boules noires et 5 boules blanches. On en prélève n successivement et avec remise, n étant un entier naturel supérieur ou égal à 2. On considère les deux événements suivants :
- A : « on obtient des boules des 2 couleurs »
- B : « on obtient au plus 1 blanche ».

1. a. Calculer la probabilité de l'événement : « toutes les boules tirées sont de même couleur ».
   b. Calculer la probabilité de l'événement : « on obtient exactement 1 boule blanche »
   c. En déduire que les probabilités $P(A \cap B)$, $P(A)$, $P(B)$ sont : $P(A \cap B) = \dfrac{n}{2^n}$, $P(A) = 1 - \dfrac{1}{2^{n-1}}$ et $P(B) = \dfrac{n+1}{2^n}$.
2. Montrer que $P(A \cap B) = P(A) \times P(B)$ si, et seulement si :
   $$2^{n-1} = n + 1.$$
3. Soit $u$ la fonction définie sur $\mathbb{N} \setminus \{0, 1\}$ par,
   $$u(n) = 2^{n-1} - (n+1).$$
   Calculer $u(2)$, $u(3)$ et $u(4)$. Démontrer que, pour tout entier $n$ naturel supérieur ou égal à 2, $u(n+1) > u(n)$.
4. En déduire la valeur de $n$ tel que les entiers les événements $A$ et $B$ soient indépendants.

**Exercice 50. La loi de Hardy-Weinberg (1908) pour les génotypes**
Lorsqu'un gène peut prendre deux formes $A$ et $a$, un individu peut avoir l'un des trois génotypes : $AA$, $Aa$ ou $aa$.

1. Établir les lois du génotype de l'enfant (les différents génotypes possibles et leur probabilité) dans les cas où les génotypes des parents sont
   a. AA et Aa
   b. Aa et Aa

On considère une population (génération 0) dans laquelle les proportions respectives de ces trois génotypes sont $p_0$, $q_0$ et $r_0$. On admet que les couples se forment au hasard quant aux génotypes considérés (appariement aléatoire).

2. Exprimer, en fonction de $p_0$, $q_0$ et $r_0$ la probabilité $p_1$ qu'un enfant de la génération 1 ait le génotype $AA$, puis celles notées $q_1$ et $r_1$, qu'il ait le génotype $Aa$ ou $aa$.
3. Montrer que $p_1$, $q_1$ et $r_1$ s'expriment seulement à l'aide de $\alpha = p_0 - r_0$. En déduire $p_2$, $q_2$ et $r_2$ (ces mêmes proportions à la génération 2) et conclure.

**Exercice 51. Loi de Hardy Weinberg pour les allèles**
Les notations de l'exercice sont celles de l'exercice précédent. On note $(u_n)$ et $(v_n)$ les proportions des allèles $A$ et $a$ dans la population.

1. Montrer que $u_n = p_n + \dfrac{q_n}{2}$ et $v_n = r_n + \dfrac{q_n}{2}$.
2. En déduire que les nombres $u_n$ et $v_n$ sont indépendants de $n$ et les exprimer à l'aide de $\alpha$.
