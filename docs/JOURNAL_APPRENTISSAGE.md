# Journal d'apprentissage

Ce fichier regroupe tout ce que j'ai appris au fil du projet. Il est mis à jour après chaque leçon et
chaque contrôle de compréhension, et il sert de support de révision avant les entretiens.

*Ces notes sont rédigées en français, alors que les autres documents du projet sont en anglais.*

---

## Phase 0 : cadrage du projet

### La question de recherche

> L'entropie aide-t-elle un investisseur multi-actifs, dont la devise de référence est le CHF, à comprendre et à gérer le risque **au-delà de ce que disent déjà la volatilité et les corrélations** ?

Les trois piliers du projet :
1. **Le désordre du marché** : l'entropie de permutation des rendements et l'entropie spectrale de la matrice de corrélation.
2. **La diversification** : l'Effective Number of Bets (Meucci, 2009), c'est-à-dire le nombre de paris réellement indépendants dans un portefeuille.
3. **L'application** : un overlay de réduction du risque déclenché par l'entropie, testé avec des règles fixées à l'avance.

### Les hypothèses, formulées correctement

Une hypothèse doit avoir une **direction** et un **test**. Décrire l'outil ne suffit pas.

| | Hypothèse | Le point clé à dire en entretien |
|---|---|---|
| **H1** | L'entropie de permutation est **plus basse** en période de stress (baisse de plus de 15 % depuis le plus haut). | En crise, le marché devient plus « ordonné » : les investisseurs suivent le mouvement et des tendances apparaissent. |
| **H2** | L'entropie apporte une information sur le **risque futur** que la volatilité actuelle ne contient pas déjà. | La volatilité actuelle prédit déjà bien la volatilité future, car la volatilité forme des grappes. Le test consiste à vérifier si l'ajout de l'entropie améliore cette prévision. Si ce n'est pas le cas, elle n'apporte rien. |
| **H3** | L'entropie spectrale de la matrice de corrélation **baisse** en crise. | Le risque se concentre alors sur un seul facteur : tout baisse ensemble, et la diversification disparaît au moment où on en a besoin. |
| **H4** | Un portefeuille qui paraît diversifié par ses poids détient en réalité **peu de paris indépendants**. | L'ENB mesure la concentration du **risque**, pas celle du rendement. Dans un 60/40, environ 90 % du risque vient des actions : l'ENB est proche de 1. |
| **H5** | Un overlay fixé à l'avance améliore le **rendement ajusté du risque**, après coûts, sur une période jamais vue. | Réduire l'exposition réduit *toujours* le risque. La vraie question est de savoir si cela améliore le ratio de Sharpe et le drawdown maximal une fois les coûts payés. |

### Les périodes in-sample et out-of-sample

- Les paramètres de la **stratégie** (fenêtre de calcul, seuil de déclenchement) sont réglés **uniquement** sur 2006–2015.
- Le test est fait **une seule fois** sur 2016–2026, une période que le modèle n'a jamais vue.
- **Le but est d'éviter le surapprentissage** (*overfitting*). En réglant les paramètres sur toutes les données, on finit toujours par trouver une combinaison qui « marche » sur le papier.
- L'analogie : réviser le CFA sur des examens blancs. Si on a déjà vu les questions du vrai examen, le score ne prouve rien.
- Chaque période contient au moins une crise (2008, puis 2020 et 2022), ce qui rend le test exigeant.

### Markowitz : ce qu'il suppose vraiment

- Les données d'entrée sont les **rendements espérés (μ)** et la **matrice de covariance** (volatilités et corrélations). On parle donc d'optimisation **moyenne-variance**.
- La loi normale n'est **pas** une hypothèse nécessaire. Markowitz donne le vrai optimum dans deux cas :
  1. les rendements sont **normaux** (ou elliptiques), et la moyenne et la variance décrivent alors toute la distribution ;
  2. l'utilité de l'investisseur est **quadratique**. C'est l'idée de U = E(r) − ½·A·σ² au CFA niveau 1.
- En dehors de ces cas, c'est une approximation qui ignore l'asymétrie et les queues épaisses.
- **À dire en entretien** : *« L'entropie complète l'analyse moyenne-variance. »* Éviter de dire que Markowitz est « faux ».
- **Attention** : seule l'entropie de permutation est robuste aux queues épaisses. L'entropie spectrale et l'ENB reposent encore sur la covariance.

---

## Phase 1 : la théorie de l'entropie

### Leçon 1 : l'entropie de Shannon (27/11/2026)

#### L'intuition : la surprise

Plus un événement est improbable, plus il apporte d'information quand il se produit.

$$\text{surprise}(p) = -\log_2(p)$$

| p | Surprise | Interprétation |
|---|---|---|
| 1 | 0 bit | Événement certain : on n'apprend rien |
| 0,5 | 1 bit | Pile ou face |
| 0,25 | 2 bits | Une chance sur quatre |
| 0,01 | 6,6 bits | Événement rare, donc très informatif |

#### La formule : la surprise moyenne

$$H = -\sum_i p_i \log_2(p_i)$$

- C'est une **espérance**, comme le rendement espéré E(r) = Σ pᵢ·rᵢ, sauf qu'on fait la moyenne des surprises au lieu des rendements.
- **Chaque surprise est pondérée par sa probabilité** : un événement rare est très surprenant, mais il arrive peu souvent.
- **Toutes les issues entrent dans la somme Σ**, y compris les plus rares.
- L'unité est le **bit** (avec log₂).

#### Les bornes et la normalisation

- **H = 0** quand une issue est certaine.
- **H = log₂(n)**, son maximum, quand les *n* issues sont équiprobables. Avec 2 issues, le maximum vaut 1 bit ; avec 3 issues, 1,585 bit ; avec 6 issues, 2,585 bits.
- L'**entropie normalisée** vaut H / log₂(n) et se situe entre 0 et 1. Proche de 0, il y a de l'ordre ; proche de 1, du désordre.
- **Contrôle de cohérence** : H ne peut jamais dépasser log₂(n). Un résultat supérieur révèle une erreur de méthode.

#### Calculer log₂

- log₂(x) répond à la question : « à quelle puissance faut-il élever 2 pour obtenir x ? ». Par exemple, log₂(8) = 3 et log₂(0,5) = −1.
- Pour une probabilité, comprise entre 0 et 1, log₂ est **négatif**, d'où le signe moins devant la formule.
- **À la calculatrice** : log₂(x) = ln(x) / ln(2). **Dans Excel** : `=LOG(x;2)`. **En Python** : `np.log2(x)`.

#### Les résultats de référence

| Cas | H | Entropie normalisée |
|---|---|---|
| Pièce équilibrée (0,5 / 0,5) | 1 bit | 1 |
| Pièce truquée (0,9 / 0,1) | 0,469 bit | 0,469 |
| 20 jours : 4 baisses, 6 jours stables, 10 hausses | 1,485 bit | 0,937 |
| Certitude (1 / 0) | 0 | 0 |

Dans le cas de la pièce truquée, c'est face, l'issue rare, qui contribue le plus à H : 0,332, contre 0,137 pour pile.

#### Les leçons clés pour le projet

1. **L'intuition trompe.** Un marché avec 50 % de jours en hausse paraît orienté, mais son entropie normalisée vaut 0,937 : il est proche du désordre maximal. Sur de vrais marchés, les entropies sont presque toujours **proches de 1**. Les signaux seront donc de **petits écarts**, par exemple de 0,98 à 0,93, d'où la nécessité de tests statistiques rigoureux.
2. **L'entropie ignore l'amplitude.** Un marché qui bouge de ±0,1 % et un autre qui bouge de ±5 % peuvent avoir la même entropie. Elle mesure donc **autre chose que la volatilité**, et c'est le cœur de H2.
3. **Shannon et la volatilité ignorent l'ordre des jours.** C'est l'image du sac de billes : l'entropie de Shannon compte les couleurs dans le sac, et mélanger les billes ne la change pas. Mais le mélange peut détruire une régularité.

| | Série A : +1, −1, +1, −1… | Série B : même nombre de hausses et de baisses, dans le désordre |
|---|---|---|
| Volatilité | 1 % | 1 % |
| Entropie de Shannon | 1 bit | 1 bit |
| Prévisibilité du jour suivant | **100 %** | **50 %** |

→ C'est ce défaut que corrige l'**entropie de permutation** (leçon 2).

**À dire en entretien** : *« L'entropie de Shannon et la volatilité ignorent toutes les deux l'ordre des observations. Or, sur les marchés, l'information se trouve souvent dans la séquence : tendances, retours à la moyenne, comportements moutonniers. C'est pour ça que j'utilise l'entropie de permutation. »*

#### Python : ce que j'ai appris

```python
def shannon_entropy(probabilities):
    p = np.asarray(probabilities, dtype=float)   # liste → tableau numpy
    p = p[p > 0]                                 # masque booléen : retire les zéros
    return -np.sum(p * np.log2(p))               # -Σ p × log₂(p)

def normalized_shannon_entropy(probabilities):
    n = len(probabilities)                       # n compté AVANT le retrait des zéros
    h = shannon_entropy(probabilities)
    return h / np.log2(n)
```

- **Le masque booléen** : `p > 0` pose la question à chaque élément et renvoie des `True` ou `False`. `p[p > 0]` ne garde que les `True`. Je m'en servirai sans arrêt en pandas, par exemple pour ne garder que les jours de crise.
- **Pourquoi retirer les zéros** : `np.log2(0)` vaut `-inf`. Un événement impossible n'ajoute aucune surprise moyenne, car p × log₂(p) tend vers 0.
- **Un paramètre, pas des valeurs en dur.** `probabilities` est la « case » qui reçoit la liste passée à chaque appel, comme une cellule A1 dans une formule Excel. Écrire les chiffres en dur dans la fonction revient à taper `=0,05/100` au lieu de `=A1/B1`.
- **Tester sur plusieurs cas dont on connaît la réponse.** Une fonction écrite en dur passe un test unique : c'est le deuxième test qui révèle l'erreur.
- **Les cas limites** : avec une seule issue (n = 1), on calcule 0/0, ce qui donne `nan`. La question *« que fait votre code si… ? »* est fréquente en entretien.
- `-0.0` vaut bien zéro : c'est un artefact des nombres décimaux, et `-0.0 == 0` renvoie `True`.

#### L'environnement de travail

- J'écris le code dans **VS Code avec des notebooks Jupyter**, et j'exécute une cellule avec **Maj + Entrée**.
- J'ouvre toujours le **dossier du projet**, pas un fichier isolé, et je choisis le noyau **`.venv`** (étiquette « Virtual Env »), jamais le Python général du PC.
- Le **mode restreint** (*Restricted Mode*) désactive les extensions Python et Jupyter. Il faut faire confiance au dossier de son propre projet, mais rester prudent avec un dossier téléchargé.
- La routine sur deux PC : `git pull` en commençant, puis commit et `git push` en terminant.

Notebook : `notebooks/01_shannon_entropy.ipynb`

---

### Leçon 2 : l'entropie de permutation (28/11/2026, en cours)

*La théorie et l'exercice à la main sont faits ; le code reste à faire.*

#### L'idée

Au lieu de compter des billes dans un sac, comme le fait Shannon, on regarde **la forme de petits morceaux de la série**. L'entropie de permutation (Bandt & Pompe, 2002) voit donc l'**ordre** des observations.

#### Les 6 motifs de 3 jours

Il y a 3! = 6 façons de ranger 3 nombres. On reconnaît un motif en se posant **deux questions** :
1. **Quelle allure ?** Montée, descente, pic ou creux.
2. **Pour un pic ou un creux : où finit le 3ᵉ jour par rapport au 1er ?** Plus haut ou plus bas.

| N° | Motif | Allure | Exemple |
|---|---|---|---|
| ① | Montée | ↗↗ | 1, 2, 3 |
| ② | Descente | ↘↘ | 3, 2, 1 |
| ③ | Pic, finit plus haut | ↗↘ | 1, 3, 2 |
| ④ | Pic, finit plus bas | ↗↘ | 2, 3, 1 |
| ⑤ | Creux, finit plus haut | ↘↗ | 2, 1, 3 |
| ⑥ | Creux, finit plus bas | ↘↗ | 3, 1, 2 |

#### La méthode en 3 étapes

1. **Faire glisser une fenêtre de 3 jours** le long de la série, en avançant d'un jour à chaque fois. N valeurs donnent **N − 2 fenêtres**.
2. **Classer** chaque fenêtre dans l'un des 6 motifs, puis **compter** les fréquences.
3. **Appliquer la formule de Shannon** aux fréquences des motifs. Le maximum vaut log₂(6) = **2,585 bits**, et on normalise en divisant par ce nombre.

C'est la même formule que Shannon, mais appliquée aux **motifs** au lieu des états.

#### Les résultats de référence

| Série | Motifs | H | Entropie normalisée |
|---|---|---|---|
| 1, 2, 3, …, 8 | un seul (①), p = 1 | 0 | **0** : ordre parfait |
| 4, 7, 9, 10, 6, 11 (exemple corrigé) | ① ×2, ④ ×1, ⑤ ×1 | 1,5 bit | 0,580 |
| 3, 5, 2, 8, 9, 4, 6, 7 (mon exercice) | ① ×2, ④ ×2, ⑤ ×1, ⑥ ×1 | 1,918 bit | **0,742** |
| Une longue série aléatoire | les 6 motifs à fréquences égales | ≈ 2,585 bits | ≈ 1 : désordre maximal |

- L'entropie normalisée **n'a pas d'unité** : on divise des bits par des bits.
- Valeurs utiles : log₂(1/3) = −1,585 et log₂(1/6) = −2,585.

#### Les leçons clés pour le projet

1. **Elle est insensible à l'amplitude.** Multiplier toute la série par 10 ne change aucun motif, donc aucune entropie. Un krach de −10 % compte comme un jour de baisse ordinaire. Elle est donc **robuste aux queues épaisses et aux valeurs extrêmes**, alors qu'une seule valeur extrême peut faire exploser une volatilité. C'est ce qui la rend **complémentaire de la volatilité**.
2. **Une séquence parfaitement régulière a une entropie nulle.** C'est l'intuition de **H1** : en période de stress, les séquences de rendements deviendraient plus régulières, et l'entropie de permutation baisserait.
3. **Elle distingue les séries A et B**, là où Shannon et la volatilité échouent. C'est à vérifier dans le code.
4. **Les égalités** (plusieurs fois la même valeur dans une fenêtre) demandent une règle pour départager les valeurs. Elles sont rares sur de vrais rendements, mais présentes dans les séries A et B.

**À dire en entretien** : *« L'entropie de permutation ne regarde que l'ordre relatif des rendements, jamais leur taille. Elle est donc robuste aux valeurs extrêmes, et elle capte des régularités de séquence que la volatilité ne voit pas. »*
