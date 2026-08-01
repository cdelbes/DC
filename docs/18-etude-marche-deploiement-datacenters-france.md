# 18 — Étude de marché : le déploiement des data centers en France à 3, 5 et 10 ans

> **Questions** : quelle est la puissance installée aujourd'hui ? Quelle croissance à 3, 5
> et 10 ans ? Et surtout : cette croissance est-elle **centralisée** (gros sites) ou
> **décentralisée** (edge, sites répartis) ?
>
> **Avertissement méthodologique** : les sources publiques **divergent fortement** sur la
> puissance installée (de 566 MW à 1,1 GW) et sur les projections (de 1,8 à 4,3 GW en
> 2033-2035). Ces écarts tiennent au **périmètre retenu** (colocation commerciale seule vs
> ensemble des sites, y compris ceux des entreprises). Ce document affiche les fourchettes
> plutôt qu'un chiffre unique, et précise à chaque fois la source et le périmètre.

---

## 0. Les cinq chiffres à retenir

1. **Puissance installée aujourd'hui : ~0,7 à 1,1 GW IT** sur **~285 à 352 sites**.
2. **Cible 2030 : ~2,3 GW** (France Datacenter) — soit un **doublement à triplement en 4 ans**.
3. **Horizon 2033-2035 : 1,8 GW** (scénario prudent EY-Parthenon, +11 %/an) à **4-4,3 GW**
   (scénario haut). **L'écart entre scénarios est d'un facteur ~2,4** — signe d'une forte
   incertitude.
4. **~18 GW sont déjà « réservés »** auprès de RTE pour ~80 projets (mai 2026), pour
   **28,6 GW de demandes** — soit **~8 fois** ce qui sera réellement construit d'ici 2030.
5. **La croissance en puissance est massivement centralisée** : un seul projet annoncé
   (campus IA francilien, **1,4 GW**) dépasse à lui seul **toute la capacité française
   installée aujourd'hui**.

---

## 1. La situation actuelle (2024-2026)

### 1.1 Puissance et nombre de sites

| Source | Périmètre | Puissance | Sites | Date |
|---|---|---|---|---|
| EY / France Datacenter (baromètre) | data centers **commerciaux** | **566 MW** | ~250 | 2022 |
| RTE / ADEME (via Mission Open Data) | ensemble | **714 MW** | ~350 | fin 2024 |
| RTE / ADEME | ensemble | — | **~352** | janv. 2026 |
| CPIM | sites **en service** | **~1 100 MW IT** | 285 | 2026 |

→ **Lecture** : la France se situe autour de **0,7-1,1 GW IT**, sur **~300-350 sites**.
La croissance récente est rapide : **+40 % en un an** pour atteindre 714 MW fin 2024, et
**+16 %/an depuis 2016** sur le segment commercial.

**Taille moyenne : ~3 MW par site.** La majorité du parc français est donc constituée
d'installations **modestes**, souvent opérées par des acteurs nationaux ou par des
entreprises pour leurs propres besoins — un point important pour la suite.

### 1.2 Concentration géographique

| Zone | Part / capacité |
|---|---|
| **Île-de-France** | **52,4 %** du marché français (2025) ; **582 à 671 MW** en exploitation, **~900 MW en projet** |
| Marseille | 2ᵉ pôle (atterrissement des câbles sous-marins) |
| Lille / Hauts-de-France, Lyon | pôles secondaires en croissance |
| Reste du territoire | dispersé, sites de petite taille |

En 2025, l'Île-de-France a absorbé **41 MW** de demande et mis en service **66 MW** —
année record en offre neuve.

---

## 2. La croissance prévue à 3, 5 et 10 ans

### 2.1 Synthèse des projections

| Horizon | Puissance installée | Source / scénario |
|---|---|---|
| **Aujourd'hui** | 0,7 – 1,1 GW | RTE / ADEME / CPIM |
| **~3 ans (2029)** | **~1,4 – 1,8 GW** | interpolation des trajectoires ci-dessous |
| **~5 ans (2030-2031)** | **~2,3 GW** | **France Datacenter** — et **500 data centers** |
| **~8 ans (2033)** | **1,8 GW** | **EY-Parthenon**, +11 %/an (scénario **prudent**) |
| **~10 ans (2035)** | **4 – 4,3 GW** | scénario **haut** (vs 714 MW en 2024) |

> ⚠️ **L'écart 2033-2035 est considérable** : 1,8 GW (EY) contre 4-4,3 GW (scénario haut).
> Traduction : personne ne sait vraiment. La variable décisive n'est pas la demande — elle
> est là — mais **la capacité du réseau à raccorder** (§3).

### 2.2 Croissance en consommation électrique (RTE)

| Horizon | Consommation | Part de la consommation française |
|---|---|---|
| 2030 | **15 – 20 TWh** | ~3 % |
| 2035 | **23 – 28 TWh** | ~4 % |

L'**ADEME** retient une trajectoire de **+12,5 %/an** de consommation électrique du secteur
entre 2025 et 2035, et alerte : cette expansion, en scénario tendanciel, serait
**« incompatible avec l'Accord de Paris »**.

### 2.3 Croissance en valeur

| Segment | 2025-2026 | 2031 | TCAC |
|---|---|---|---|
| Marché total | 6,87 Md$ (2026) | **10,92 Md$** | **+9,7 %/an** |
| **Hyperscale** | 1,49 Md$ (2026) | **4,19 Md$** | **+23,0 %/an** |

→ Le **hyperscale croît 2,4 fois plus vite** que le marché global. C'est le cœur de la
réponse à ta question.

---

## 3. Le fait structurant : la file d'attente réseau

C'est l'élément le plus important de cette étude, et le moins connu.

| Indicateur | Valeur | Date |
|---|---|---|
| Capacité **réservée** auprès de RTE | **~18 GW** pour **~80 projets** | mai 2026 |
| Capacité réservée un an et demi plus tôt | 5 GW | fin 2024 |
| **Demandes totales** | **28,6 GW** | mai 2026 |
| Capacité qui sera réellement installée en 2030 | **~2,3 GW** | France Datacenter |
| Délais de raccordement | **2 à 7 ans** | RTE |

### Ce que ça signifie

- **La file d'attente représente ~8 fois ce qui sera construit.** L'écart s'explique par
  les « **projets fantômes** » : des développeurs réservent de la capacité pour sécuriser
  une option, sans certitude de construire.
- **RTE change de doctrine** : passage de « *premier demandeur, premier servi* » à
  « **premier prêt, premier servi** », pour prioriser les projets matures.
- **Le réseau électrique — et non l'immobilier — est devenu le facteur déterminant** du
  lieu d'implantation d'un data center en France.
- L'État accorde à certains grands data centers le statut de **« projet d'intérêt national
  majeur »** pour accélérer les procédures administratives et de raccordement.

> 📌 **Conséquence directe pour le projet de Rodez** : la rareté n'est pas le foncier, c'est
> **la puissance raccordable rapidement**. Une capacité disponible **immédiatement** (tes
> 2,5 MW) a de la valeur dans ce contexte — c'est précisément la thèse du doc 10 et 14. Mais
> la contrepartie est que la doctrine « premier prêt » **récompense les dossiers avancés**
> (PTF signée, permis purgé), pas les intentions.

---

## 4. Centralisé ou décentralisé ? — la réponse

### 4.1 En puissance : massivement centralisé

Les grands projets annoncés écrasent tout le reste :

| Projet | Puissance | Investissement | Statut |
|---|---|---|---|
| **Campus IA francilien** (MGX / Bpifrance / Mistral / NVIDIA) | **1,4 GW** | ~8,5 Md€ | annoncé mai 2025, travaux S2 2026, mise en service 2028 |
| **Data4 / Brookfield — Cambrai** | **1 GW** | 20 Md€ d'ici 2030 | annoncé |
| **SoftBank — Hauts-de-France** | 3 data centers | « dizaines de milliards € » | annoncé |
| **Digital Realty — Dugny** (93) | cible ~200 MW | 2 Md€ | permis obtenu |
| **Mistral / NVIDIA — Fouju** (77) | 96 MW → **200 MW** | — | en construction |
| **EDF × OpCore — Montereau** (77) | « plusieurs centaines de MW » | ~4 Md€ | négociation exclusive |
| **Digital Realty — MRS5 Marseille** | — | 300 M€ | en cours |
| **Le Bosquel** (80) — calcul IA | « titanesque » | — | horizon 2031 |

**48 projets avancés** ont été cartographiés sur le territoire, pour **plus de 109 Md€**
d'investissements annoncés ou engagés, avec une concentration des mises en service entre
**2026 et 2028**.

> **Le chiffre qui tranche** : le seul campus IA francilien (**1,4 GW**) représente **plus
> que toute la capacité installée en France aujourd'hui** (0,7-1,1 GW). Deux ou trois
> projets de ce type suffisent à absorber l'intégralité de la croissance prévue à 2030.

### 4.2 En nombre de sites : le tissu reste décentralisé, mais marginal en MW

| Segment | Réalité |
|---|---|
| **Colocation** | **67,9 %** du marché en valeur (2025) — encore dominant |
| **Hyperscale / self-built** | croissance la plus rapide : **+16,7 % à +23 %/an** |
| **Edge** | existe et se structure, mais **marginal en puissance** |

**Le segment edge en chiffres** :
- **UltraEdge** : **51 MW** au total, 248 sites dont 90 edge data centers, 7 « datapoles »,
  400 M€ d'investissement d'ici 2028.
- **nLighten** : 8 sites en France, 30+ en Europe — croissance par **rachat de sites
  existants**, pas par construction sur terrain nu (cf. doc 12 et 14).

→ Les **51 MW** d'UltraEdge — le premier acteur edge français — représentent **~2 % de la
cible 2,3 GW de 2030**. L'edge se développe **en nombre de sites**, pas en puissance.

### 4.3 La distinction essentielle : déconcentration géographique ≠ décentralisation d'échelle

C'est le point que la plupart des analyses confondent.

| | Ce qui se passe |
|---|---|
| **Décentralisation géographique** | ✅ **Oui** — l'Île-de-France passe de 52,4 % du marché à une part décroissante ; le « **reste de la France** » croît à **+17,8 %/an**, plus vite que l'IDF |
| **Décentralisation d'échelle** | ❌ **Non** — ce qui part en région, ce sont des **très gros sites** (Cambrai 1 GW, Hauts-de-France, Montereau), pas des petits |

**Pourquoi la région ?** Pas pour la proximité des utilisateurs, mais parce que
**Hauts-de-France, Grand Est et vallée du Rhône disposent de capacités réseau** capables
d'absorber de nouveaux sites sans années d'attente. Le foncier et le réseau commandent,
pas la latence.

Constat EY : les **hyperscale sont surreprésentés en Île-de-France**, tandis que les sites
**de plus petite taille sont répartis sur le territoire** — mais ce tissu diffus est
largement **hérité** (data centers d'entreprises, opérateurs régionaux), il n'est pas le
moteur de la croissance.

### 4.4 Réponse synthétique

> **La croissance française des data centers d'ici 2030 est massivement CENTRALISÉE en
> puissance et DÉCONCENTRÉE en géographie.**
>
> On construit **de très gros sites**, de plus en plus **loin de Paris**, là où le réseau
> électrique peut les accueillir. On ne construit pas un maillage de petits sites.

---

## 5. Ce que cette étude change pour le projet de Rodez

### 5.1 🔴 Confirmations défavorables

1. **Le marché va vers le gros.** Un site de 1-2 MW ne participe pas à la vague de
   croissance : celle-ci se joue en centaines de MW et en GW. Cela **confirme le doc 14**.
2. **L'edge reste marginal en puissance** (~2 % du marché) et croît par **rachat d'actifs
   en exploitation**, pas par acquisition de terrains à équiper.
3. **Les régions gagnantes sont nommées** : Hauts-de-France, Grand Est, vallée du Rhône.
   **L'Occitanie n'apparaît dans aucune des dynamiques citées.**
4. **La doctrine « premier prêt, premier servi »** de RTE favorise les dossiers matures et
   financés — un porteur individuel avec une simple intention part avec un handicap.

### 5.2 🟢 Confirmations favorables

1. **La contrainte n°1 du marché est le raccordement** (2 à 7 ans de délai, 8 GW de projets
   fantômes). Une capacité **disponible tout de suite** est exactement ce qui manque. C'est
   la seule vraie force du site.
2. **Le marché ne saturera pas** : 15-20 TWh en 2030, 23-28 TWh en 2035 selon RTE, +12,5 %/an
   selon l'ADEME. La demande est structurelle, pas conjoncturelle.
3. **La taille moyenne du parc français est de ~3 MW** : le tissu de petits sites existe
   bel et bien (300-350 sites), même s'il n'est pas le moteur de la croissance. Ton
   projet s'inscrit dans ce tissu-là — un marché de **remplacement et de proximité**, pas
   de croissance explosive.
4. **La déconcentration géographique est réelle** et s'accélère (+17,8 %/an hors IDF) :
   la tendance va dans le bon sens, même si elle profite surtout aux grands sites.

### 5.3 La lecture stratégique

Le bon cadrage pour ton projet n'est **pas** « surfer sur la vague de croissance IA » — tu
n'es pas sur ce segment. C'est plutôt :

> **Un site de proximité de 1 MW, sur un marché de ~300 sites de taille comparable,
> adressant une demande régionale (souveraineté, edge, PRA, santé), avec pour atout
> différenciant une puissance disponible immédiatement dans un pays où le raccordement
> prend 2 à 7 ans.**

C'est un positionnement **défendable et honnête**, mais c'est un marché **de niche**, pas le
marché des 109 Md€. Toute présentation qui laisserait entendre le contraire serait démontée
par un interlocuteur informé.

---

## 6. Tableau de bord — à retenir

| Question | Réponse |
|---|---|
| Puissance installée aujourd'hui | **0,7 – 1,1 GW IT**, ~300-350 sites, ~3 MW/site en moyenne |
| Croissance à 3 ans (2029) | ~1,4 – 1,8 GW |
| Croissance à 5 ans (2030) | **~2,3 GW** et ~500 sites |
| Croissance à 10 ans (2035) | **1,8 GW** (prudent) à **4,3 GW** (haut) — forte incertitude |
| Consommation électrique | 15-20 TWh (2030) → 23-28 TWh (2035), soit 3-4 % de la conso nationale |
| Type dominant en **puissance** | **Centralisé / hyperscale** (+23 %/an) |
| Type dominant en **nombre de sites** | Colocation et petits sites (67,9 % du marché en valeur) |
| Dynamique géographique | **Déconcentration** vers Hauts-de-France, Grand Est, vallée du Rhône |
| Vraie contrainte du marché | **Le raccordement électrique** (2-7 ans, 18 GW réservés vs 2,3 GW construits) |
| Place d'un site de 1 MW | **Marché de niche régional**, hors de la vague de croissance |

## Sources

- [Les data centers en chiffres clés — RTE](https://www.rte-france.com/bases-electricite/consommation-electricite/essor-data-centers-france)
- [RTE envisage de sortir de la règle « premier demandeur, premier servi » — L'Usine Nouvelle](https://www.usinenouvelle.com/electronique-informatique/cloud-computing/datacenters/sortir-de-la-regle-du-premier-demandeur-premier-servi-rte-envisage-de-changer-de-politique-pour-reduire-les-delais-de-raccordement-electrique-des-datacenters.RDEXNYUWVNAXTHKGFVVU5FYL24.html)
- [Data centers : 18 GW réservés, le réseau électrique sous tension — Sciences et Démocratie](https://www.sciences-et-democratie.net/intelligence-artificielle-33269-data-centers-18-gw-reseau-electrique-tension)
- [Explosion des demandes de raccordement — Fournisseur-Énergie](https://www.fournisseur-energie.com/actualites/data-centers-hausse-raccordement/)
- [Premier baromètre de la filière des datacenters — EY / France Datacenter](https://www.ey.com/fr_fr/insights/tmt/premier-barometre-de-la-filiere-des-datacenters) · [enseignements du baromètre 2025 — CNER](https://cner-france.com/datacenters-en-france-les-enseignements-du-barometre-2025-dey-et-france-datacenter/)
- [Les tendances autour des datacenters EDGE en France — EY](https://www.ey.com/fr_fr/insights/tmt/les-tendances-autour-des-datacenters-edge-en-france)
- [Combien de data centers en France 2026 : 350 sites et 714 MW — Mission Open Data](https://www.mission-open-data.fr/nombre-data-centers-france-2026-chiffres/)
- [Taille et part du marché des centres de données en France (colocation 67,9 %, IDF 52,4 %) — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/france-data-center-market) · [marché hyperscale France](https://www.mordorintelligence.com/industry-reports/france-hyperscale-data-center-market)
- [Le marché des data centers croît et s'élargit à de nouvelles régions — Batirama](https://www.batirama.com/article/96970-le-marche-des-data-centers-en-france-croit-rapidement-et-s-elargit-a-de-nouvelles-regions.html)
- [ADEME : l'expansion des data centers « incompatible » avec l'Accord de Paris — AEF Info](https://www.aefinfo.fr/depeche/748945-la-carte-des-data-centers-en-projet-leur-forte-expansion-est-incompatible-avec-laccord-de-paris-avertit-lademe) · [communiqué ADEME](https://www.ademe.fr/presse/communique-national/centres-de-donnees-numeriques-perspectives-devolution-de-leurs-consommations/)
- [Carte des mégaprojets data centers IA confirmés en France — franceinfo](https://www.franceinfo.fr/internet/carte-un-data-center-pres-de-chez-vous-decouvrez-ou-sont-situes-les-projets-de-mega-centres-de-donnees-confirmes-en-france_8039498.html)
- [Le marché des Data Centers en Île-de-France — JLL](https://www.jll.com/fr-fr/insights/market-dynamics/data-center-france) · [marché EMEA — Cushman & Wakefield](https://www.cushmanwakefield.com/fr-fr/france/insights/global-data-center-market-comparison)
- [UltraEdge : 400 M€, 7 datapoles — L'Usine Nouvelle](https://www.usinenouvelle.com/electronique-informatique/cloud-computing/datacenters/ultraedge-qui-a-repris-les-datacenters-de-sfr-veut-investir-400-millions-deuros-dici-a-2028-pour-creer-sept-datapoles-regionaux-en-france.647LJJKWMNA5XGD5RORUAULBPQ.html)
