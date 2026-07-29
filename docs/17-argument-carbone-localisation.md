# 17 — L'argument carbone de la localisation : analyse et usage pour le projet

> **Source** : post LinkedIn de **Charles Gorintin** (cofondateur d'Alan et de Mistral AI),
> « *La même requête d'IA émet vingt fois moins de CO2 lorsqu'elle est servie depuis un
> data center en France.* »
>
> ✅ **Texte lu** (capture d'écran fournie). Chaque chiffre a été **vérifié sur source
> primaire** — le résultat du fact-check figure au §2.

---

## 1. Ce que dit le post (résumé fidèle)

1. **Intensité carbone** : 19,6 g/kWh en France en 2025, avec 95 % de production
   bas-carbone (RTE), contre **~420 g en Virginie**, capitale mondiale du data center
   → d'où le facteur **×20**.
2. **Échelle de la consommation** : l'IA pèse **0,5 % de l'électricité mondiale** ;
   une requête consomme **0,24 Wh et cinq gouttes d'eau**.
3. **L'autre côté du bilan** : selon l'AIE, l'adoption large des applications d'IA
   existantes éviterait **1,4 Gt de CO₂/an en 2035**, soit **3 à 4× les émissions de tous
   les data centers** à la même date.
4. **« Reste une variable qui compte : le lieu. »**
5. **Argument de fuite carbone** : « Refuser un data center en France ne supprime aucune
   requête. Elle sera servie ailleurs, sur un réseau au gaz ou au charbon, avec un manque
   à gagner économique pour nous. Chaque gigawatt que nous ne construisons pas ici se
   construit là où l'électricité est plus sale. »
6. **Capacité d'accueil** : **92 TWh exportés en 2025**, record pour la 2ᵉ année
   consécutive. « Toute la croissance prévue tient dans une fraction de nos exports. »
7. **Conclusion** : « Le geste écologique, cette fois, consiste à construire. En France. »

---

## 2. Fact-check — le post est solide

| Affirmation | Vérification | Verdict |
|---|---|---|
| 19,6 g/kWh en France en 2025, 95 % bas carbone | RTE, Bilan électrique 2025 : plus bas historique, 2ᵉ rang européen derrière la Norvège ; 95 % de production bas carbone confirmé | ✅ exact |
| ~420 g en Virginie | Cohérent avec l'intensité du réseau PJM (~350-450 g) | ✅ plausible |
| **Facteur ×20** | 420 / 19,6 = **×21,4** | ✅ **exact avec cette base** |
| 92 TWh exportés en 2025 | RTE : **92,3 TWh**, record battant les 89 TWh de 2024, 2ᵉ année consécutive, ~17 % de la production, **5,4 Md€** de recettes. France 1er exportateur européen | ✅ exact |
| 0,24 Wh et cinq gouttes d'eau par requête | Correspond aux chiffres publiés par Google pour une requête texte médiane (~0,24 Wh, ~0,26 mL) | ✅ exact, **mais périmètre restreint** (voir §3) |
| IA = 0,5 % de l'électricité mondiale | Cohérent avec l'AIE (data centers ~1,5 %, l'IA en étant un sous-ensemble) | ✅ plausible |
| AIE : 1,4 Gt évitées en 2035, 3-4× les émissions des data centers | AIE, *Energy and AI* : 1 400 Mt dans le **« Widespread Adoption Case »**, soit 3× le *Lift-off Case* et 4× le *Base Case* | ⚠️ exact **mais conditionnel** (voir §3) |

### 🔄 Correction de mon analyse précédente

Dans la version antérieure de ce document (rédigée **sans** avoir pu lire le post), j'avais
qualifié le facteur ×20 de « haut de fourchette ». **C'était une prudence mal placée** :
la comparaison retenue est **France vs Virginie**, et 420/19,6 = 21,4. Non seulement le
chiffre est exact, mais la Virginie est **le bon point de comparaison** pour un data
center — c'est là que l'industrie s'implante réellement, bien plus pertinent qu'une
moyenne européenne.

---

## 3. Les deux nuances à connaître (pour ne pas être pris en défaut)

Le post est un **plaidoyer** — les chiffres sont exacts, mais deux méritent un contexte
si un contradicteur les attaque.

**a) Le 1,4 Gt de l'AIE est un scénario conditionnel, pas une prévision.**
L'AIE précise elle-même : *« il n'existe actuellement aucune dynamique susceptible
d'assurer l'adoption large de ces applications, et leur impact agrégé, même en 2035,
pourrait être marginal si les conditions nécessaires ne sont pas créées »* (accès aux
données, infrastructure numérique, compétences, contraintes réglementaires).
→ À citer comme **potentiel**, jamais comme acquis.

**b) Les 0,24 Wh par requête sont une médiane pour du texte.**
Ce chiffre exclut l'**entraînement** des modèles et concerne les prompts textuels — la
génération d'image et surtout de vidéo est bien plus lourde. Le chiffre est honnête pour
ce qu'il mesure, mais ne résume pas l'empreinte de l'IA.

*Ces nuances n'invalident pas la thèse — elles évitent de la sur-vendre.*

---

## 4. Ce que ça change pour le projet de Rodez

### 4.1 🔴 Ce que l'argument **ne fait pas** : différencier ton site

Le raisonnement porte sur **la France contre la Virginie**. À l'intérieur de la France, le
mix est national : **Rodez n'a aucun avantage carbone sur Fouju, Marseille ou Bordeaux**.
L'argument valide **le marché**, pas **le terrain**. C'est cohérent avec la segmentation
établie au doc 14.

⚠️ **Attention à l'échelle rhétorique** : le post raisonne en **gigawatts** et en politique
nationale. Reprendre « chaque gigawatt que nous ne construisons pas ici » pour un projet de
**1 MW** serait disproportionné et desservirait le dossier. L'argument doit être
**redimensionné** avant usage.

### 4.2 🟢 Les deux apports vraiment nouveaux et utilisables

**a) L'argument de fuite carbone — le meilleur outil pour l'acceptabilité locale**

> « Refuser un data center en France ne supprime aucune requête. Elle sera servie ailleurs,
> sur un réseau au gaz ou au charbon. »

C'est un argument de **fuite carbone** classique, rigoureux, et c'est **la meilleure réponse
à une opposition locale**. Or ton projet devra passer par la **mairie de Rodez**, un
**permis de construire** et potentiellement des **riverains** (doc 06-07). Si le sujet
« data center = gouffre énergétique » surgit — et il surgira —, cette formulation est la
réponse la plus efficace, parce qu'elle déplace le débat du *faut-il ?* vers le *où ?*.

**Version calibrée pour un projet de 1 MW** :
> « La demande de calcul existe et croît, que ce site se fasse ou non. La question n'est
> pas de la supprimer mais de savoir où elle est servie : ici, sur une électricité à
> 19,6 g/kWh, ou ailleurs, sur du gaz ou du charbon à 420 g. »

**b) Les 92 TWh d'exports — la réponse à « le réseau ne tiendra pas »**

C'est l'objection numéro un contre les data centers en France, et le post y répond avec un
fait vérifié : la France a **exporté 92,3 TWh en 2025** (record, 2ᵉ année consécutive,
~17 % de sa production, 5,4 Md€ de recettes). Toute la croissance data center prévue tient
dans **une fraction** de ce surplus.

→ Applicable directement à ton dossier : les **2,5 MW disponibles** sur ton départ HTA ne
sont pas une anomalie locale, ils s'inscrivent dans un **surplus structurel national**.
C'est un argument que **Tenergie est particulièrement légitime à porter**.

### 4.3 🟢 Ce qui reste différenciant pour Rodez (inchangé)

L'empreinte d'une requête = *(énergie IT × **PUE**) × **intensité carbone du réseau***.

Le post agit sur le second facteur — **national, donc identique partout en France**. Tes
deux leviers propres au site portent sur le premier et sur la traçabilité :

1. **Le PUE** : à ~590 m d'altitude, le free cooling réduit l'énergie non-IT. **Cumulatif**
   avec l'argument national, et **spécifique au site**.
2. **L'adossement renouvelable Tenergie** : un PPA ou une autoconsommation locale permet de
   revendiquer mieux qu'un mix national moyen — une **traçabilité de la fourniture**. C'est
   le seul angle qui fait passer de « la France est bas carbone » à « **ce site-ci** est bas
   carbone, et je peux le prouver ».

### 4.4 🟢 Le levier commercial (inchangé)

**CSRD** (reporting du scope 3, donc de l'informatique hébergée) et **directive européenne
sur l'efficacité énergétique** (data centers > 500 kW) transforment le bas carbone en
**critère d'achat**. Pour les cibles du doc 12 (RAGT, CH de Rodez, collectivités), « local
+ bas carbone + données en Aveyron » devient un argument de **conformité**.

---

## 5. Formulations prêtes à l'emploi

**Pour le teaser / les acheteurs (doc 15)**
> « Électricité française à **19,6 gCO₂/kWh** (RTE 2025, 95 % bas carbone) — **~20× moins
> carbonée qu'en Virginie** — combinée à un **free cooling d'altitude** (~590 m) et à un
> **adossement renouvelable possible**. »

**Pour la mairie / l'acceptabilité locale (doc 07)**
> « La demande de calcul croîtra que ce projet se fasse ou non. Servie ici, elle l'est sur
> l'une des électricités les moins carbonées au monde ; refusée, elle part sur des réseaux
> au gaz ou au charbon. La France a par ailleurs exporté **92 TWh en 2025** : la capacité
> existe. »

**Pour un client soumis à CSRD (doc 12)**
> « Hébergement en France sur un réseau à 19,6 gCO₂/kWh, PUE réduit par le climat, données
> restant en Aveyron : un scope 3 numérique parmi les plus faibles disponibles, et
> documentable. »

---

## 6. Synthèse

| Usage | Verdict |
|---|---|
| Prouver le vent porteur du marché français | ✅ oui — chiffres RTE vérifiés |
| Différencier Rodez d'un autre site français | ❌ non — le mix est national |
| **Répondre à une opposition locale (fuite carbone)** | ✅ **oui — le meilleur apport du post** |
| **Répondre à « le réseau ne tiendra pas » (92 TWh)** | ✅ **oui — fait vérifié, et Tenergie est légitime** |
| Argument commercial CSRD | ✅ oui, combiné à la proximité |
| Argument **spécifique au site** | ✅ seulement via **PUE d'altitude** + **PPA renouvelable** |
| Citer la source | ⚠️ citer **RTE** et **l'AIE**, pas le post (l'auteur est partie prenante côté Mistral) |
| Reprendre la rhétorique « gigawatts » | ❌ disproportionné pour 1 MW — redimensionner |

## Sources

- Post LinkedIn de Charles Gorintin (capture fournie) — texte repris au §1.
- [Bilan électrique 2025 — RTE, émissions](https://analysesetdonnees.rte-france.com/en/annual-review-2025/ghg-emissions) · [échanges / exports](https://analysesetdonnees.rte-france.com/en/annual-review-2025/trade)
- [Record d'exportation 92,3 TWh en 2025 — SFEN](https://www.sfen.org/rgn/le-nucleaire-en-chiffres-923-twh-delectricite-exportes-2025-record-porte-hausse-production/) · [L'Énergeek](https://lenergeek.com/2026/02/25/electricite-92-twh-exportes-en-2025-un-record-historique-en-france/)
- [IEA — *Energy and AI*, AI and climate change (1,4 Gt, Widespread Adoption Case et ses réserves)](https://www.iea.org/reports/energy-and-ai/ai-and-climate-change) · [rapport complet (PDF)](https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf)
- [Production d'électricité bas carbone en Europe — SFEN](https://www.sfen.org/rgn/production-delectricite-bas-carbone-en-europe-le-graphique-qui-souligne-la-singularite-francaise/)
- [AI: five charts putting data-centre energy use into context — Carbon Brief](https://www.carbonbrief.org/ai-five-charts-that-put-data-centre-energy-use-and-emissions-into-context)
