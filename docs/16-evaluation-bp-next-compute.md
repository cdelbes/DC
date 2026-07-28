# 16 — Évaluation du Business Plan Next Compute (P100, v14.4 — 02/07/2026)

> **Contexte** : Tenergie envisage une **joint-venture** avec Next Compute. Ce document
> évalue le BP fourni de façon critique — hypothèses, cohérence, répartition de la valeur —
> pour préparer la négociation.
>
> **Méthode** : le modèle a été **entièrement reconstruit en Python** à partir des formules
> du fichier. La reconstruction **reproduit les résultats à l'euro près** (FCFE 15 ans,
> FCFE an 1 et an 5, part de chaque actionnaire, TRI). Les tests de sensibilité du §6 sont
> donc fiables — ils tournent sur la mécanique exacte du fichier.

---

## 1. Verdict en cinq points

1. **Le modèle est sérieusement construit** (15 ans, amortissements ventilés, IS avec
   report déficitaire, réinvestissements, cash sweep). Ce n'est pas un BP bâclé.
2. **Le TRI affiché en couverture (34,1 %) n'est le rendement de personne.** Le TRI réel
   de Tenergie tel que calculé par le fichier lui-même est de **25,3 %** (ligne 84).
3. **La répartition de la valeur est très asymétrique** : Next Compute capte **~65 % de la
   valeur créée** en apportant **67 €** de capital, quand Tenergie apporte **957 275 €** et
   porte 100 % du risque en fonds propres.
4. **Trois erreurs de présentation** ont été identifiées, dont une significative (l'IS
   annoncé en couverture est en réalité le résultat net — surestimation ×3).
5. **Les hypothèses de revenus sont optimistes**, en particulier le CPU (58 % du chiffre
   d'affaires à maturité) dont le prix **augmente de 50 %** et l'usage de 33 % simultanément.
   Sous un jeu d'hypothèses prudent, le TRI de Tenergie tombe à **13,6 %**.

**Conclusion** : le projet reste économiquement viable dans la plupart des scénarios testés
(le TRI ne devient jamais négatif), mais **les termes de la JV, tels que modélisés,
favorisent nettement Next Compute**. C'est un sujet de négociation, pas un sujet de
faisabilité.

---

## 2. Ce que dit le BP (chiffres de couverture)

| Indicateur | Valeur affichée |
|---|---|
| Revenus annuels (an complet) | 1 425 063 € |
| Revenus CGE nets RPM (an complet) | 981 749 € |
| FCFE après IS — an 1 | 85 563 € |
| FCFE après IS — an 6 | 531 563 € |
| **Total FCFE net 15 ans** | **8 886 728 €** |
| **TRI post-impôt (15 ans)** | **34,1 %** ⚠️ *(voir §4.1)* |
| IS total payé (15 ans) | 9 190 628 € ⚠️ *(erreur — voir §4.2)* |
| Réinvestissement total P100 | 1 520 000 € |

**Investissement total : 2 815 713 €**, financé par :

| Source | Montant | Qui |
|---|---|---|
| Fonds propres | **100 €** | Next Compute 67 € / Investisseur tiers 33 € |
| Avance en compte courant @ 7 %, remboursée fin an 5 | **957 242 €** | **Investisseur tiers seul** (Next Compute : 0 €) |
| Mezzanine Junior @ 12 %, 5 ans | **1 858 371 €** | tiers prêteur |

---

## 3. Le point central : qui apporte quoi, qui reçoit quoi

C'est le sujet n°1 pour la négociation de la JV.

### Apports à la signature

| | Next Compute | Tenergie (« Investisseur tiers ») |
|---|---|---|
| Capital social | **67 €** (67 %) | **33 €** (33 %) |
| Avance en compte courant | **0 €** | **957 242 €** |
| **Development Fee encaissée** | **+ 255 974 €** *(10 % du conteneur + frais de dév.)* | — |
| **Position nette jour 0** | **+ 255 907 €** | **− 957 275 €** |

> Next Compute est **cash-positif dès la signature** : la commission de développement
> (255 974 €, financée par l'investissement donc par l'argent de Tenergie et de la dette)
> dépasse très largement son apport en capital de 67 €.

### Valeur captée sur 15 ans

| | Next Compute | Tenergie |
|---|---|---|
| Part du FCFE (67 % / 33 %) | 5 954 041 € | 2 932 620 € |
| Intérêts sur avance (7 %) | — | 335 034 € |
| Remboursement de l'avance | — | 957 242 € |
| Development Fee | 255 974 € | — |
| **Total encaissé** | **6 210 015 €** | **4 224 896 €** |
| Capital engagé | 67 € | 957 275 € |
| **Gain net** | **+ 6 209 948 €** | **+ 3 267 622 €** |
| **Part de la valeur totale créée** | **~65 %** | **~35 %** |

**Formulation directe** : Next Compute capte environ **deux tiers de la valeur** en
engageant **0,007 % du capital**. Tenergie finance la totalité des fonds propres, porte le
risque, et reçoit un tiers de l'upside.

> ⚠️ **Ceci n'est pas nécessairement abusif** : Next Compute apporte du savoir-faire, le
> sourcing, le développement et l'exploitation — c'est un montage « sweat equity contre
> cash » classique. Mais Tenergie doit **savoir qu'elle signe cela**, et le négocier en
> connaissance de cause. C'est une question de gouvernance, pas d'erreur de calcul.

### 🔴 Question critique non traitée par le BP

**Qui garantit la mezzanine de 1 858 371 € ?** Le BP ne le dit pas. Si Tenergie doit
apporter sa garantie, son **exposition réelle passe de 957 k€ à 2,8 M€** — et le rapport
risque/rendement change complètement. **À clarifier avant toute discussion de valorisation.**

---

## 4. Erreurs et anomalies identifiées

### 4.1 🔴 Le TRI de 34,1 % affiché en couverture n'est le rendement d'aucune partie

Le calcul (ligne 75-76) construit un flux : **−957 342 € en an 0**, puis **100 % du FCFE**
les années suivantes.

Or ce FCFE a **déjà déduit** les intérêts de l'avance (335 034 €) et son remboursement
(957 242 €) — sans jamais les recréditer à l'investisseur qui les reçoit.

Le résultat mélange donc deux conventions : il fait supporter à un investisseur la totalité
de la mise, tout en lui attribuant la totalité du FCFE d'une société qu'il ne détient qu'à
33 %, et en lui retirant les flux de son avance.

**Le bon chiffre pour Tenergie est celui de la ligne 84 : 25,3 %** — construit
correctement (33 % du FCFE + intérêts + remboursement de l'avance). Il figure dans le
fichier, mais ce n'est pas celui mis en couverture.

*(Le TRI de Next Compute, ligne 81, s'affiche à 85 856 % — arithmétiquement exact avec
67 € investis, mais dénué de sens ; il illustre surtout l'asymétrie du montage.)*

### 4.2 🔴 L'IS annoncé en couverture est en réalité le résultat net

La couverture indique « **IS total payé (15 ans) : 9 190 628 €** » en pointant la cellule
`BP!F67`. Or la ligne 67 est **« Résultat net après IS »**. L'impôt réellement calculé par
le modèle est en ligne 66 : **2 984 209 €**.

→ L'IS est **surestimé d'un facteur 3** dans la synthèse. Le calcul sous-jacent est
correct ; c'est la cellule référencée qui est fausse.

### 4.3 🟠 Le « mécanisme de protection des revenus » ne protège rien

La section RPM est présentée comme un mécanisme de protection. Or :
- « Garantie minimum revenus conteneur (Hivenet) » = **0 %**
- « Durée de la garantie » = **0 an**
- La ligne « Plancher garantie Hivenet » vaut **0 sur les 15 années**

Le RPM ne fait que **redéfinir le partage** par tranches (95 % / 20 % / 70 %), ce qui donne
à la société **~74,3 %** des revenus à maturité — effectivement **meilleur que le 70 % fixe**
du calculateur Policloud. C'est un vrai plus. Mais **il n'y a aucun plancher de revenus** :
si le taux de remplissage s'effondre, rien n'amortit la chute.

→ Le nom du mécanisme surpromet. À faire préciser : la garantie Hivenet est-elle
négociable à une valeur > 0 ?

### 4.4 🟡 Anomalies mineures de formule

| Anomalie | Détail | Impact |
|---|---|---|
| **Loyer doublé en an 6 et 11** | `=C37*flag*(1+IF(an=6,1,0)+IF(an=11,1,0))` → 12 000 € au lieu de 6 000 € | 12 000 € sur 15 ans — probable copier-coller de la logique de réinvestissement |
| **Montée en charge CPU codée en dur** | `INDEX(...)*9/12` en an 1 uniquement, sur la ligne CPU du BP | ~147 k€ ; le facteur n'apparaît pas dans les hypothèses (chiffre magique) |
| **Ramp-up asymétrique** | Le CPU monte en charge sur 9 mois mais **GPU et stockage sont à 100 % dès l'an 1** | à justifier : pourquoi seul le CPU ? |
| **Conso élec sous-estimée** | `(P_totale × 8760 × dispo × taux_GPU)` : la puissance **fixe** (12,6 kW) et le **froid** (25 kW) tournent en permanence, ils ne devraient pas être multipliés par le taux d'usage GPU | ~940 MWh réels vs 907 modélisés → **~4,4 k€/an** |
| **Prix élec issu de cellules de la ligne « Fibre »** | `C142 = F142*F143 + G142*G143`, où F143/G143 sont sur la ligne fibre | le résultat (135 €/MWh) est juste, mais la construction est fragile |
| **ICR mal défini** | « cash sweep / intérêts » vaut 0,16 à 0,57 — toujours < 1 par construction (le sweep est plafonné à 5 % de l'EBITDA) | métrique non signifiante, affichée comme un test de couverture |

### 4.5 🟠 L'année 5 est un point de tension de trésorerie

**FCFE an 5 = −430 376 €** et **DSCR = 0,34**.

Cause : le remboursement de l'avance (957 242 €) et de la dernière annuité mezzanine
(515 530 €) tombent la même année. Les DSCR sont sains les années 1-4 (1,23 / 1,78 / 2,20 /
2,20) puis décrochent.

→ Un prêteur exigerait probablement d'**étaler le remboursement de l'avance** ou de le
subordonner. À anticiper dans la structuration.

---

## 5. Revue des hypothèses

### 5.1 Revenus — la structure est déséquilibrée vers le CPU

| Source | Revenu à maturité | Part |
|---|---|---|
| GPU (104 × 0,80 €/h × 90 %) | 652 669 € | **32 %** |
| **CPU (5 616 vCPU × 0,06 €/h × 40 %)** | **1 174 804 €** | **58 %** |
| Stockage (4 tiers) | 184 992 € | 9 % |
| **Total** | **2 012 465 €** | |

**Le CPU représente 58 % du chiffre d'affaires** — c'est la ligne la plus importante, et la
moins démontrée. Or :

- Le **prix CPU passe de 0,04 à 0,06 €/h (+50 %)** entre l'an 1 et l'an 3 ;
- **et** le taux d'usage passe de 30 % à 40 % (+33 %) sur la même période.
- Les deux s'améliorent **simultanément**, dans un marché du calcul banalisé où les prix
  ont plutôt tendance à **baisser**.

Autres points :
- **Prix GPU figé à 0,80 €/h pendant 15 ans**, sans érosion, alors que le matériel n'est
  rafraîchi que deux fois (an 6 et an 11).
- **Revenus parfaitement plats de l'an 3 à l'an 15** — 13 années sans variation, ni
  inflation ni érosion, sur un marché en mouvement rapide.
- Cohérence avec le calculateur Policloud (doc 09) : le prix du conteneur (2 530 000 € vs
  2 500 000 €) concorde ✅, mais les hypothèses CPU diffèrent (0,06 €/h @ 40 % ici contre
  0,04 €/h @ 50 % chez Policloud).

### 5.2 OPEX — plusieurs postes absents

| Poste | Traitement dans le BP | Observation |
|---|---|---|
| Électricité | **135 €/MWh figé sur 15 ans** | Aucune indexation. Poste majeur (122 k€/an). **C'est l'hypothèse que Tenergie est la mieux placée pour challenger — et pour améliorer.** |
| Inflation | **Aucune sur aucune ligne** | 15 ans sans inflation sur maintenance, assurance, loyer… |
| **Personnel** | **absent** | Aucun coût de personnel, d'astreinte ou de « remote hands » au-delà de la maintenance Policloud |
| **Impôts locaux (CFE, foncier)** | **absents** | Une société exploitant un site sera redevable de la CFE au minimum |
| Fibre | 8 400 €/an | Le calculateur **Policloud lui-même retient 24 000 €/an** → écart de **15 600 €/an** |
| Assurance | 10 000 €/an | Policloud retient 15 000 €/an |
| Frais bancaires / agent sur la mezzanine | absents | — |

### 5.3 Points techniques à vérifier

- **La capacité de froid est saturante** : `MIN(25 ; 90,6 × 0,35)` = MIN(25 ; **31,7**) → le
  plafond de 25 kW mord. Le besoin théorique dépasse la capacité AC installée. Soit le
  conteneur est thermiquement juste à pleine charge GPU, soit le coefficient de 0,35 est
  prudent. **Question à poser à Policloud.**
- PUE implicite = 115,6 / 90,6 = **1,28** — correct pour un conteneur.
- **Aucune valeur résiduelle en an 15** : le modèle suppose un actif à valeur nulle alors
  que le dernier rafraîchissement date de l'an 11-12. C'est **prudent** — un point positif.

---

## 6. Tests de sensibilité (apport de cette analyse)

Le BP ne contient **aucune analyse de sensibilité**. Voici celle qui manque, calculée sur la
mécanique exacte du fichier. Référence : **TRI Tenergie 25,3 %**.

| Scénario | TRI Tenergie | Gain net Tenergie |
|---|---|---|
| **BASE (hypothèses Next Compute)** | **25,3 %** | 3 267 622 € |
| Inflation OPEX 2 %/an | 24,9 % | 3 127 206 € |
| Charges omises : +40 k€/an (CFE, personnel) | 24,4 % | 3 119 122 € |
| Électricité 135 → 200 €/MWh | 23,9 % | 3 048 792 € |
| GPU : usage 90 % → 70 % | 23,0 % | 2 903 516 € |
| GPU : prix 0,80 → 0,60 €/h | 22,7 % | 2 857 333 € |
| Érosion générale des prix −3 %/an | 22,0 % | 2 336 228 € |
| **CPU : prix reste à 0,04 €/h** | **20,6 %** | 2 388 515 € |
| **CPU : usage 40 % → 25 %** | **20,2 %** | 2 290 382 € |
| **CPU : prix 0,04 €/h ET usage 25 %** | **16,7 %** | 1 734 109 € |
| **COMBINÉ prudent** \* | **13,6 %** | 1 332 197 € |

\* *CPU 0,04 €/h et 30 % d'usage, GPU 0,70 €/h, électricité 170 €/MWh, inflation OPEX 2 %/an,
+30 k€/an de charges omises.*

### Lecture

- **Le modèle est robuste en direction** : dans aucun scénario testé le TRI ne devient
  négatif. Le projet ne s'effondre pas.
- **Mais il est très sensible au CPU** : à lui seul, un CPU qui reste à 0,04 €/h avec 25 %
  d'usage fait passer le TRI de 25,3 % à **16,7 %**.
- **En scénario prudent cumulé, le TRI tombe à 13,6 %** — encore acceptable, mais très loin
  des 34,1 % affichés en couverture, et à un niveau où le risque d'exécution mérite
  rémunération.
- Les postes de coûts (électricité, inflation, charges oubliées) ont un impact **modéré**
  individuellement (1 à 1,5 point chacun). **Le vrai risque est du côté des revenus.**

---

## 7. Ce qui est bien fait (à reconnaître)

Pour être juste, le BP présente de réelles qualités :

- **Modèle cohérent** : la reconstruction indépendante le reproduit à l'euro près.
- **Amortissements correctement ventilés** : infrastructure 30 % sur 15 ans / IT 70 % sur
  5 ans — c'est fiscalement réaliste et rarement bien fait.
- **IS correctement modélisé** : taux réduit 15 % jusqu'à 42 500 €, puis 25 %, avec report
  du déficit de l'an 1. Rigoureux.
- **Cycles de réinvestissement modélisés** (an 6 et an 11, étalés sur 2 ans, avec leur
  propre plan d'amortissement).
- **Disponibilité 99,5 %** appliquée aux revenus — bonne pratique.
- **RPM à tranches** plus favorable que le 70/30 brut de Policloud.
- **Pas de valeur terminale** — hypothèse prudente.
- Le versionnage (**v14.4**) traduit un travail itératif sérieux.

---

## 8. Points de négociation pour la JV

Par ordre d'importance :

1. **Clarifier la garantie de la mezzanine (1,86 M€).** Si Tenergie la garantit, son
   exposition réelle est de 2,8 M€, pas 957 k€. **Question préalable à tout le reste.**
2. **Rééquilibrer le partage.** Deux leviers non exclusifs :
   - relever la part de Tenergie au-delà de 33 % ;
   - ou convertir l'avance en compte courant en **capital**, pour que la détention reflète
     l'apport réel (aujourd'hui : 99,99 % du cash pour 33 % des droits).
3. **Négocier la Development Fee** (255 974 €) : son montant, son calendrier de versement
   (échelonnement lié à des jalons plutôt qu'au closing), ou son imputation partielle en
   capital.
4. **Obtenir un plancher de revenus réel** : la garantie Hivenet est à 0 % sur 0 an. C'est
   une variable du fichier — donc négociable.
5. **Étaler ou subordonner le remboursement de l'avance** pour lisser le trou de l'an 5
   (FCFE −430 k€, DSCR 0,34).
6. **Faire valoir l'apport énergie de Tenergie** : l'électricité (122 k€/an, figée à
   135 €/MWh) est le poste où Tenergie apporte une vraie valeur. Un PPA compétitif ou une
   fourniture interne est un actif à valoriser **dans la négociation du partage**.
7. **Exiger une analyse de sensibilité contradictoire** dans le BP contractuel, avec un cas
   bas documenté.

---

## 9. Questions à poser à Next Compute

1. Sur quelles **références de marché** repose l'hypothèse d'un prix CPU passant de 0,04 à
   0,06 €/h, avec un usage montant simultanément de 30 % à 40 % ? Y a-t-il des contrats ou
   des précédents ?
2. Pourquoi la **couverture affiche 34,1 %** alors que la ligne 84 du BP donne **25,3 %**
   pour l'investisseur tiers ?
3. L'indicateur « **IS total payé** » pointe la ligne du résultat net (9,19 M€ au lieu de
   2,98 M€) — confirmez-vous l'erreur de référence ?
4. **Qui garantit la mezzanine** de 1 858 371 € ?
5. La **garantie de revenus Hivenet** (0 % / 0 an) est-elle négociable ?
6. Pourquoi la **montée en charge de 9 mois** ne s'applique-t-elle qu'au CPU, et pas au GPU
   ni au stockage ?
7. Pourquoi la **capacité de froid (25 kW)** est-elle inférieure au besoin calculé
   (31,7 kW) à pleine charge GPU ?
8. Pourquoi **fibre à 8 400 €/an** et **assurance à 10 000 €/an**, alors que le calculateur
   Policloud retient 24 000 € et 15 000 € ?
9. Où sont les postes **personnel, CFE/taxe foncière et inflation** ?
10. Quelle est la **valeur résiduelle** du conteneur en an 15, et à qui appartient-il ?

---

## 10. Recommandation

**Ne pas rejeter le projet — renégocier les termes.**

L'économie sous-jacente tient : même sous des hypothèses nettement dégradées, le TRI reste
à deux chiffres. Le problème n'est pas la viabilité, c'est **la répartition entre les
partenaires** et **la présentation des indicateurs**.

Avant tout engagement :
- faire corriger les trois erreurs identifiées (§4.1, 4.2, 4.4) et réémettre un BP v15 ;
- exiger que la couverture affiche **le TRI de l'investisseur tiers (25,3 %)** ;
- obtenir un **cas bas contractuel** (le §6 fournit une base) ;
- traiter la **garantie de la mezzanine** comme un point bloquant tant qu'elle n'est pas
  clarifiée.

*Analyse réalisée par reconstruction complète du modèle (vérifiée à l'euro près sur 5
indicateurs). Les tests de sensibilité sont reproductibles.*
