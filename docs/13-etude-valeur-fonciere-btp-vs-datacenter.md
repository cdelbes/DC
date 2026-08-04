# 13 — Étude de marché : valeur du foncier « vente BTP » vs « data center »

> Objet : chiffrer, pour la discussion avec le propriétaire, **combien vaut la parcelle**
> selon deux voies — (1) la vente immédiate à l'acheteur BTP, (2) sa valorisation en
> foncier data center (vente RTB ou bail). Chiffres = **ordres de grandeur** à affiner ;
> les valeurs data center sont des **fourchettes conditionnelles**, pas des promesses.
> Parcelle : ZA Bel-Air, Rodez, **~2 522 m²**, bâti existant (hangar, **toiture amiantée**).

---

## 1. Voie 1 — Vente à l'acheteur BTP (le scénario de référence)

**Prix du foncier en zone d'activités de l'agglo de Rodez : 65 à 135 €/m²** (terrains
industriels/artisanaux, marché 2025).

| Base | Calcul | Valeur foncière indicative |
|---|---|---|
| Bas de fourchette | 2 522 × 65 € | **≈ 164 000 €** |
| Haut de fourchette | 2 522 × 135 € | **≈ 340 000 €** |

Ajustements propres à ce bien :
- **+ Bâti existant** : un dépôt fonctionnel (hangar + cour) a une valeur d'usage pour un
  repreneur BTP → peut **remonter** le prix au-dessus du foncier nu.
- **− Passif amiante** : la toiture amiantée est une **charge** (désamiantage ~25-55 k€,
  cf. doc 06) qu'un acheteur avisé **déduit** du prix, ou qu'il subira plus tard.
- **Nature** : vente **one-shot**, définitive. Le propriétaire **sort** de l'actif.

> 🔢 **À renseigner** : le **montant réel de l'offre BTP** (connu du propriétaire). C'est
> la valeur à battre. Les fourchettes ci-dessus servent à situer si l'offre est « dans le
> marché », basse ou haute.

---

## 2. Voie 2 — Valorisation « data center » : les 4 leviers

La valeur data center **ne remplace pas** la valeur foncière : elle **s'y ajoute** via
quatre leviers. Chacun est activable indépendamment.

> 🔴 **Révisé une seconde fois par `docs/20`** (benchmark sur données cadastrales réelles) :
> parcelle **2 631 m²** (et non 2 522), bâti **487 m²**, acquisition **275 000 € en 2018**.
> Valeur actuelle estimée **215-380 k€** (médian ~300 k€), valeur RTB **295-637 k€**
> (médian ~465 k€), soit un multiple réaliste de **×1,4 à ×1,7**. Chiffres du doc 20 à
> utiliser en priorité.
>
> 🔴 **Révisé par `docs/14`** (étude de marché approfondie) : le levier 1 ci-dessous
> retenait un multiple ×1,5-3 emprunté au marché international. L'étude du marché
> **français** conclut qu'il faut lui préférer une **méthode par coût de remplacement** —
> la survaleur est bornée par ce que le site fait économiser à l'acheteur (raccordement,
> autorisations, désamiantage, temps), soit **+150 à +400 k€**, ce qui donne une
> fourchette RTB de **~320 à 700 k€**. Chiffres à utiliser en priorité.

### Levier 1 — Survaleur « powered land » (vente d'un site dé-risqué)
Un foncier **RTB** (électricité sécurisée + permis + terrain propre) vaut, sur le marché
data center européen, **2 à 4× un terrain comparable sans puissance** (cf. doc 10).
À l'échelle modeste de Rodez (1-2,5 MW, pas hyperscale), on retient une hypothèse
**prudente de ×1,5 à ×3** :

| | Base foncière | Hypothèse | Valeur RTB indicative |
|---|---|---|---|
| Prudent | 164 000 € | ×1,5 | **≈ 250 000 €** |
| Central | ~250 000 € | ×2 | **≈ 500 000 €** |
| Haut | 340 000 € | ×3 | **≈ 1 000 000 €** |

⇒ potentiellement **+100 k€ à +700 k€** au-dessus de la vente BTP — **si un acheteur
data center est trouvé** (docs 12). C'est la variable clé, à valider par le test de marché.

### Levier 2 — Bail foncier (revenu récurrent, le propriétaire GARDE le terrain)
Au lieu de vendre, **louer** le terrain à l'exploitant du data center (bail commercial ou
emphytéotique 20-40 ans). C'est le **montage EnR classique** (comme un bail de centrale
PV), mais **bien plus rémunérateur** au m² pour un data center.

- Un bail de **centrale solaire au sol** rapporte typiquement ~2 000-4 000 €/ha/an → très
  peu pour 0,25 ha.
- Un **bail data center** se négocie sur la **puissance et l'usage industriel**, sans
  commune mesure : le foncier « électrifié » devient un actif à revenu **long et indexé**.
- Intérêt pour le propriétaire : **il ne se dessaisit pas**, il transmet un actif qui
  **produit un loyer** — logique patrimoniale (transmission).

> 🔢 Montant à caler avec un exploitant (doc 12). Le message : **revenu récurrent sur
> décennies** vs **encaissement unique** de la vente BTP.

### Levier 3 — Résolution du passif amiante
Le projet **prend en charge le désamiantage/démolition** (intégré au montage data center).
Pour le propriétaire, c'est un **passif qui disparaît** (~25-55 k€ + risque) — valeur
souvent oubliée dans la comparaison, mais réelle : l'acheteur BTP, lui, **répercutera**
ce coût dans son offre.

### Levier 4 — Valeur d'option (le droit d'attendre)
Se donner ~12-18 mois pour dé-risquer **crée de la valeur sans la détruire** : à l'issue,
le propriétaire **choisit** la meilleure sortie (vente BTP toujours possible, vente data
center, ou bail). Le coût d'attente est **faible** ; le gain potentiel est **élevé et
asymétrique** (downside protégé par l'offre BTP qui reste la base).

---

## 3. Tableau comparatif de synthèse

| Critère | **Vente BTP (maintenant)** | **Voie data center (après dé-risquage)** |
|---|---|---|
| Valeur foncière | ~164-340 k€ (à confronter à l'offre réelle) | idem **+ survaleur RTB ×1,5-3** *ou* **loyer récurrent** |
| Forme du gain | encaissement **unique**, définitif | **vente premium** *ou* **revenu long terme** (bail) |
| Passif amiante | **déduit** de l'offre / subi | **pris en charge** par le projet |
| Maîtrise de l'actif | **cédée** | **conservée** possible (bail) — logique patrimoniale |
| Délai | immédiat | +12-24 mois (dé-risquage) |
| Risque pour le propriétaire | nul (mais gain plafonné) | **faible** : la sortie BTP reste la base de repli |
| Condition clé | — | **trouver l'acheteur/exploitant** (test de marché, doc 12) |

**Message central** : la voie data center **domine** la vente BTP dans presque tous les
cas de figure, **à condition** de trouver le débouché — et le coût de le vérifier est
faible pour le propriétaire.

---

## 4. Ce que ça implique pour la négociation

- L'enjeu n'est **pas** de renoncer à la vente BTP, mais de **différer** la décision le
  temps de tester la voie data center — **sans fermer** l'option BTP.
- Outil juridique adapté : une **promesse de vente sous conditions suspensives** (obtention
  raccordement + permis) **ou** une **option/exclusivité** de 12-18 mois au profit du
  porteur de projet. Le propriétaire reste protégé (si le projet échoue, la vente BTP
  reprend) et intéressé (si le projet réussit, il capte la survaleur ou le loyer).
- La **valeur à battre reste l'offre BTP réelle** : à obtenir du propriétaire pour chiffrer
  précisément l'écart.

## 5. À compléter pour un chiffrage ferme

- [ ] **Montant exact de l'offre BTP** (propriétaire).
- [ ] Surface et état du **bâti** (valeur d'usage vs coût de démolition).
- [ ] **Coût du raccordement** (pré-étude Enedis, doc 08) — pèse sur la survaleur RTB.
- [ ] **Marque d'intérêt d'un acheteur/exploitant** data center (doc 12) — valide le levier 1/2.
- [ ] Devis **désamiantage** (doc 06) — chiffre le levier 3.

## Sources

- [Prix des terrains industriels en ZA de l'agglo de Rodez (65-135 €/m²) — immo-hub / marché local](https://immo-hub.org/terrains-et-locaux-d-activites/a-vendre-terrains-industriels-entre-2-115-a-2-350-m2-a-rodez-proche-de-millau-12)
- [Terrains industriels à vendre en Aveyron — BureauxLocaux](https://www.bureauxlocaux.com/immobilier-d-entreprise/annonces/aveyron-12/vente-terrains)
- [Prix moyen des terrains à Rodez — Terrain-Construction](https://www.terrain-construction.com/prix-moyen-terrain/aveyron-12/rodez-12000)
- Survaleur « powered land » 2-4× : voir `docs/10-strategie-rtb-powered-land.md` et ses sources.
