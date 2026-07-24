# 09 — Décryptage du ROI Calculator de Policloud (pour monter en compétence)

> Ce document explique, pas à pas et pour un non-spécialiste, le fichier
> `roi_calculator.xlsx` partagé par Policloud. Objectif : comprendre **le business
> d'un data center en chiffres**, et surtout **ce que ce fichier dit — et ne dit pas —
> pour le projet de Rodez**.

---

## 0. À retenir avant tout (le piège le plus important)

**Ce fichier ne modélise pas un data center. Il modélise le business d'UN conteneur GPU.**

Il se place du point de vue de **l'acheteur d'un conteneur Policloud** (toi, potentiellement) :
tu achètes une « boîte » remplie de cartes graphiques (GPU), et tu gagnes de l'argent en
**louant sa puissance de calcul à l'heure**. Policloud te vend la boîte **et** encaisse
30 % des revenus pour gérer la commercialisation.

Il manque **toute la couche “bâtiment”** : terrain, raccordement Enedis, désamiantage,
dalle, permis, refroidissement du local, sécurité. Ça, c'est **ton** sujet Rodez, et
c'est **en plus** de ce fichier (voir §9).

---

## 1. Les deux couches d'un data center (indispensable à distinguer)

| Couche | Ce que c'est | Qui la porte dans ton projet | Où c'est traité |
|---|---|---|---|
| **1. La coquille (le contenant)** | terrain, alimentation électrique, refroidissement, sécurité, bâtiment/conteneur | **toi** (le foncier de ton père + raccordement) | docs 02, 06, 07, 08 |
| **2. L'informatique (le contenu)** | serveurs, GPU, CPU, stockage — ce qui **génère le chiffre d'affaires** | Policloud (le matériel) + toi (l'investissement) | **ce fichier** |

Le fichier Policloud = **couche 2 uniquement**. Un vrai business plan de ton projet
combine les deux.

---

## 2. Le produit modélisé, en chiffres

Le fichier compare deux formats de conteneur :

| | **P100** (petit) | **P360** (grand) |
|---|---|---|
| Serveurs | 13 | 45 |
| **GPU** (8 par serveur) | **104** | 360 |
| CPU disponibles à la location | 5 616 | 19 440 |
| Capacité de **stockage** | 2 000 To | 1 000 To |
| Puissance électrique (hypothèse du modèle) | **45 kW** ⚠️ | 250 kW |
| **Prix d'achat** (GPU RTX 5090) | **2 500 000 €** | 7 800 000 € |
| Prix d'achat (GPU RTX 6000 Pro, +haut de gamme) | 3 300 000 € | 10 500 000 € |

- **GPU** = *Graphics Processing Unit*, la carte graphique. C'est le composant vedette :
  très demandé pour l'**IA** et le calcul. Ici, RTX 5090 (grand public/prosumer) ou
  RTX 6000 Pro (pro).
- **CPU** = le processeur classique. Le modèle les loue « en plus », comme un revenu
  secondaire.
- Le prix d'achat, c'est **ton CAPEX matériel** (couche 2) : 2,5 M€ pour un P100.

> ⚠️ **Alerte n°1 — la puissance électrique du P100 (45 kW) semble sous-évaluée.**
> 104 cartes RTX 5090 consomment à elles seules ~60 kW (≈575 W/carte), avant serveurs et
> refroidissement. Un P100 “réel” tire plutôt **80–100 kW**. Ce chiffre est **capital** :
> il détermine ta facture d'électricité **et** le dimensionnement de ton raccordement
> Enedis (voir §9). À faire préciser par Policloud.

---

## 3. D'où vient l'argent : 3 sources de revenus

Le principe est toujours le même : **quantité × prix unitaire × taux d'utilisation × temps**.
(Une année = 8 760 heures.)

### a) Location des GPU — le cœur du réacteur
- Prix : **0,80 €/heure** par carte RTX 5090 (1,60 €/h pour la RTX 6000 Pro).
- Taux de commercialisation (= taux d'occupation, « à quel point c'est loué ») :
  **100 % les années 1-3**, puis 90 %.
- Calcul P100 : 104 GPU × 0,80 € × 100 % × 8 760 h = **728 832 €/an**.

### b) Location des CPU — le revenu d'appoint
- Prix : **0,04 €/heure** par CPU, utilisation **50 %**, démarre en **année 2**.
- Calcul P100 : 5 616 CPU × 0,04 € × 50 % × 8 760 h = **983 923 €/an**.

### c) Stockage — 4 gammes, du grand public au premium
Le stockage se vend **au To et par mois**. La capacité brute (2 000 To) est divisée par
un facteur de **redondance de 2,5** (on garde 2,5 copies pour la fiabilité → moins de To
vendables), puis répartie en 4 usages :

| Gamme | Prix / To / mois | Part de la capacité | Taux de vente |
|---|---|---|---|
| Fichiers grand public | 3,40 € | 10 % | 50 % |
| Stockage S3 (type cloud) | 7 € | 50 % | 60 % |
| Stockage réseau | 50 € | 20 % | 70 % |
| Stockage HPC (calcul intensif) | 100 € | 20 % | 75 % |

- Total stockage P100 : **≈ 232 992 €/an**.
- À retenir : plus le stockage est “premium/rapide”, **plus le prix au To explose**
  (×30 entre le grand public et le HPC).

### Revenu brut total (P100, à pleine maturité)
728 832 (GPU) + 983 923 (CPU) + 232 992 (stockage) = **≈ 1 945 000 €/an**.

---

## 4. Le partage 70 / 30 (le point business à bien saisir)

Tu ne gardes pas 100 % de ces revenus. Le modèle applique un **partage : 70 % pour toi
(le propriétaire de la boîte), 30 % pour Policloud** (qui exploite la plateforme qui
trouve les clients et commercialise la puissance).

- Ta part (70 %) à maturité : 1 945 000 × 70 % = **≈ 1 362 000 €/an**.
- La part Policloud (30 %) : ≈ 583 000 €/an.

C'est le modèle classique d'un **“GPU cloud” en marque blanche** : tu apportes le capital
et le site, l'opérateur apporte la clientèle et la techno, et on partage.

---

## 5. Les coûts

### CAPEX (investissement de départ) — couche 2 seulement
- **2 500 000 €** : achat du conteneur P100 équipé (RTX 5090), payé en année 0.
- **Rafraîchissement matériel (refresh)** : en **année 6**, on remet à niveau **40 %** du
  matériel (GPU qui vieillissent) → **1 000 000 €**, étalé sur 2 ans (500 k€ + 500 k€).
  En contrepartie, le prix de location GPU remonte de **+25 %** (matériel plus récent).

### OPEX (charges annuelles) — pour toi, propriétaire
| Poste | P100 | P360 |
|---|---|---|
| Maintenance annuelle | 99 000 € | 350 000 € |
| Assurance | 15 000 € | 40 000 € |
| Fibre (connexion internet) | 24 000 € | 24 000 € |
| **Électricité** | **0 €** ⚠️ (« à renseigner par le client ») | 0 € ⚠️ |
| **Total hors électricité** | **138 000 €/an** | 414 000 €/an |

> ⚠️ **Alerte n°2 — l'électricité est à ZÉRO dans le modèle.** C'est volontaire (Policloud
> te laisse la remplir), mais c'est **le poste le plus important d'un data center** et il
> fausse tous les résultats tant qu'il est vide. Estimation à insérer pour un P100 :
> - à 45 kW (hypothèse du fichier) : 45 × 8 760 × 0,15 €/kWh ≈ **59 000 €/an** ;
> - à 100 kW (plus réaliste) : 100 × 8 760 × 0,15 €/kWh ≈ **131 000 €/an**.
>
> Autrement dit, la vraie charge annuelle d'un P100 n'est pas 138 k€ mais plutôt
> **200 à 270 k€**. Le business reste rentable, mais **la marge dépend directement du
> prix de ton électricité** — d'où l'importance de ton raccordement et de ton contrat de
> fourniture (docs 02 et 08).

---

## 6. Les indicateurs financiers, expliqués simplement

Ce sont les 4 chiffres que tout investisseur regarde. Voici ce qu'ils veulent dire.

| Indicateur | Question à laquelle il répond | En clair |
|---|---|---|
| **Payback** (délai de retour) | « En combien de temps je récupère ma mise ? » | ici **~3 ans** |
| **Cash-flow cumulé** | « Combien j'ai en poche, net, à la fin ? » | ici **+8,0 M€ à 10 ans** (sur 2,5 M€ investis) |
| **TRI / IRR** (taux de rentabilité interne) | « Quel rendement annuel moyen, en % ? » | ici **25 % à 5 ans, 35 % à 10 ans** |
| **MoM / MOIC** (multiple) | « Combien de fois je multiplie ma mise ? » | ici **~3,2× le capital net à 10 ans** |

**Comment lire le TRI** : c'est comme un “taux d'intérêt” du projet. Un TRI de 25 % veut
dire que le projet rapporte comme un placement à 25 %/an. En capital-investissement, on
vise souvent 15-25 % ; **25-35 % est très bon** (… mais ces chiffres supposent
l'électricité à 0 et une location à 100 %, donc à relativiser).

---

## 7. Le déroulé année par année (P100, tel quel dans le fichier)

*Rappel : électricité = 0, location GPU à 100 % puis 90 %, achat comptant.*

| Année | Encaissements | Décaissements | Flux net | Cumul net |
|---|---|---|---|---|
| 0 | 0 | −2 500 k€ (achat) | −2 500 k€ | −2 500 k€ |
| 1 | 510 k€ (GPU seul) | −138 k€ | +372 k€ | −2 128 k€ |
| 2 | 1 219 k€ (+CPU +stockage) | −138 k€ | +1 081 k€ | −1 047 k€ |
| **3** | 1 362 k€ | −138 k€ | +1 224 k€ | **+177 k€ ← remboursé** |
| 4 | 1 311 k€ | −138 k€ | +1 173 k€ | +1 350 k€ |
| 5 | 1 311 k€ | −138 k€ | +1 173 k€ | +2 523 k€ |
| 6 | 1 426 k€ | −638 k€ (refresh) | +788 k€ | +3 311 k€ |
| 7 | 1 426 k€ | −638 k€ (refresh) | +788 k€ | +4 098 k€ |
| 8 | 1 426 k€ | −138 k€ | +1 288 k€ | +5 386 k€ |
| 9 | 1 426 k€ | −138 k€ | +1 288 k€ | +6 674 k€ |
| 10 | 1 426 k€ | −138 k€ | +1 288 k€ | +7 962 k€ |

Lecture : on paie 2,5 M€ au départ, on est dans le rouge 2-3 ans, **le seuil est franchi
en année 3**, puis la boîte génère ~1,2 M€/an de trésorerie nette. L'année 1 est plus
faible car CPU et stockage ne démarrent qu'en année 2.

---

## 8. L'option financement (mentionnée dans le fichier)

Le modèle prévoit d'**emprunter** pour acheter le matériel plutôt que de payer comptant
(bloc « FINANCING Terms » : 1er versement, taux d'intérêt, début de remboursement,
durée 4 ans). Dans la version reçue, le financement est à 0 (achat comptant). Intérêt du
financement : **réduire la mise initiale** et donc **gonfler le TRI** (effet de levier),
au prix d'intérêts à payer. À activer quand on négociera un vrai plan de financement.

---

## 9. Ce que ce fichier NE dit PAS (et qui te concerne directement)

C'est le point le plus important pour ton projet Rodez. Le modèle Policloud est un
**argumentaire de vente** de conteneur : il est optimiste et **ignore la couche 1**.
À ajouter pour ton business plan :

1. **Tout le site (couche 1)** : achat/bail du terrain, **raccordement Enedis** (extension
   HTA ~250 m + poste de livraison), **désamiantage + démolition** du hangar (~25-55 k€),
   dalle, clôture, permis de construire, refroidissement du local. → docs 02, 06, 07, 08.
2. **L'électricité (à 0 dans le fichier)** — voir alerte n°2. C'est ta marge.
3. **Le taux de location à 100 %** est très optimiste : il suppose que **toute** la
   puissance GPU trouve preneur en permanence. La vraie question business = **la demande**.
   Qui loue ? À quel prix tiendra le 0,80 €/h dans 3 ans ?
4. **L'obsolescence des GPU** : une carte perd de sa valeur locative vite (le refresh à
   40 % en année 6 le reconnaît). Risque technologique réel.
5. **Le prix de vente des GPU (0,80 €/h)** dépend d'un marché IA très volatil.

### Le pont avec Rodez : de la boîte au data center

C'est ici que **tes deux sujets se rejoignent**. Ta capacité de raccordement (**~2,5 MW**
disponibles, doc 08) te dit **combien de boîtes** tu peux alimenter :

| Format | Puissance/boîte | Nb de boîtes dans 2,5 MW | GPU total | CAPEX matériel |
|---|---|---|---|---|
| P100 @ 45 kW (fichier) | 45 kW | ~55 | énorme, peu réaliste | — |
| P100 @ ~100 kW (réaliste) | ~100 kW | **~20-25** | ~2 000-2 600 | ~50-60 M€ |
| P360 @ 250 kW | 250 kW | **~10** | ~3 600 | ~78 M€ |

⇒ Ton foncier de 2 522 m² + 2,5 MW autorisent, sur le papier, une **vraie ferme de calcul**
(plusieurs boîtes), pas un simple conteneur. Mais l'investissement matériel se compte
alors en **dizaines de millions** : le sujet devient **le financement et la demande**,
pas la faisabilité technique.

**Approche raisonnable pour ton BP** : démarrer petit (**1 à 2 boîtes**, phase pilote),
prouver la demande et le taux de location réels, puis monter en puissance par tranches en
réutilisant le même raccordement — exactement la logique modulaire des docs 03 et 06.

---

## 10. Lexique express

- **GPU / CPU** : carte graphique (calcul IA/intensif) / processeur classique.
- **CAPEX** : dépense d'investissement, en une fois (achat matériel).
- **OPEX** : dépenses de fonctionnement, récurrentes (élec, maintenance…).
- **Taux de commercialisation / utilisation** : part de la capacité effectivement louée.
- **Redondance** : copies multiples des données pour la fiabilité (ici ×2,5).
- **Refresh** : renouvellement périodique du matériel qui vieillit.
- **Payback** : durée pour récupérer la mise de départ.
- **TRI (IRR)** : rendement annuel moyen du projet, en %.
- **MoM / MOIC** : multiple de la mise (×2 = tu doubles ta mise).
- **Cash-flow** : trésorerie nette (encaissé − décaissé) sur une période.
- **kW / kWh** : puissance (débit) / énergie consommée (puissance × temps).
- **PUE** : ratio d'efficacité énergétique d'un data center (énergie totale ÷ énergie IT ;
  1,0 = parfait, 1,2-1,4 = bon). Non traité dans le fichier Policloud, à intégrer.

---

## 11. Prochaine étape proposée

Construire **ton** business plan (couche 1 + couche 2) : reprendre la logique de ce
fichier pour la partie revenus, y **injecter l'électricité réelle**, y **ajouter les coûts
de site** (raccordement, désamiantage, terrain/bail, permis), et décliner **1 à 2 boîtes
en pilote** puis la montée en puissance. C'est l'objet de la trame `docs/05` — je peux le
transformer en tableur chiffré dès que : (a) le prix élec / la puissance réelle du P100
sont connus, (b) la pré-étude Enedis donne le coût du raccordement.

*Source : `roi_calculator.xlsx` (Policloud), analysé cellule par cellule. Chiffres du
modèle repris tels quels ; les alertes ⚠️ signalent les hypothèses à challenger.*
