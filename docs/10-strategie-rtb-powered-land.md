# 10 — Stratégie « RTB / Powered Land » : valoriser le foncier sans exploiter le data center

> Idée de Charles : plutôt que de construire **et** exploiter le data center, **préparer le
> foncier pour qu'il soit “prêt à recevoir” un data center** (l'équivalent du **RTB —
> Ready To Build** des énergies renouvelables), puis le valoriser/le céder. Analyse du
> concept, exemples en France, et avis.

---

## 1. Le concept existe — et porte un nom : « powered land »

Ton intuition est juste, et le secteur a déjà formalisé exactement cette idée. Dans le
data center, on parle de **« powered land »** (foncier électrifié / prêt à bâtir) : un
terrain **pré-préparé et dé-risqué**, vendu **avant** toute construction verticale, dont
la valeur vient de trois briques sécurisées :

1. **La puissance électrique garantie** (raccordement réseau réservé) — la ressource la
   plus rare aujourd'hui ;
2. **Les autorisations d'urbanisme** (« entitlements » : permis, zonage, purge des
   recours) ;
3. **La connectivité fibre** (souvent fibre noire / dark fiber à proximité).

C'est **le transfert exact du métier de développeur EnR** que tu connais : sécuriser
foncier + raccordement + autorisations, atteindre le **RTB**, puis **vendre le projet
“clé en main pour construire”** à un exploitant (IPP dans les EnR ; hyperscaler, opérateur
de colocation ou fonds d'infrastructure dans le data center).

**Pourquoi ça marche** : le raccordement électrique est devenu le **goulot d'étranglement
n°1** (délais de 3-4 ans, réseaux saturés). Un terrain qui a déjà réglé ce problème fait
gagner **des années** à l'acheteur → il paie pour ça. *« Land alone is no longer
sufficient »* : sans puissance sécurisée, un site parfait est inexploitable ; avec, il
devient un actif recherché.

---

## 2. Ce que ça vaut : le mécanisme de survaleur

La logique de création de valeur (documentée sur le marché) :

- **En Europe, un site avec puissance sécurisée vaut 2 à 4× un terrain comparable sans
  puissance.** C'est le cœur du modèle.
- Ordre de grandeur physique : **~3-4 MW de puissance par acre** (~0,4 ha) — c'est la
  densité de référence du marché.
- **Marge de développement** : les développeurs qui sécurisent foncier + haute tension +
  fibre visent des marges **supérieures de +250 points de base** au rendement d'un actif
  stabilisé (i.e. on est payé pour le risque de développement).

**Exemple emblématique (US, hyperscale)** : dans le comté de Stafford (Virginie), Peterson
Companies a assemblé 504 acres pour **32 M$** (~64 k$/acre), a obtenu les **autorisations
data center** en septembre 2024, puis a **revendu le site autorisé** à Stack Infrastructure
en janvier 2025 pour **302 M$**. La survaleur vient **uniquement** de la puissance
sécurisée + des autorisations. C'est le RTB poussé à l'extrême.

> ⚠️ Ces multiples spectaculaires sont ceux des **métropoles hyperscale américaines**.
> Ils **ne se transposent pas** à un site de 2,5 MW en Aveyron (voir §4). À citer comme
> **preuve de concept**, pas comme promesse de prix.

---

## 3. La preuve que ça se fait déjà en France

Le modèle est en plein déploiement sur le marché français — plusieurs acteurs le pratiquent :

- **EDF ouvre son foncier** : depuis mars 2025, EDF lance des **appels à manifestation
  d'intérêt (AMI)** pour accueillir des data centers sur ses anciens sites industriels
  (ex-centrales), **précisément parce qu'ils bénéficient d'un raccordement réseau
  favorable** qui « réduit de plusieurs années » les délais. Sites annoncés :
  Montereau-Vallée-de-la-Seine (77), La Maxe et Richemont (57), un 4ᵉ près de Lyon ;
  objectif 6 sites en 2026. → EDF **valorise du foncier électrifié**, il ne devient pas
  exploitant IT. C'est du powered land à la française.
- **Montereau (EDF × OpCore/Iliad-InfraVia)** : le site EDF a été apporté à un exploitant
  (OpCore) qui investit ~4 Md€ — **séparation nette entre le propriétaire du foncier
  électrifié et l'exploitant**.
- **Altarea (foncier/promoteur) × Vantage Data Centers** : partenariat annoncé pour un
  campus IA/cloud en France ; **Altarea détient un terrain près de Bordeaux avec 400 MW de
  raccordement déjà sécurisé** — un foncier promoteur + puissance, apporté à un opérateur.
- Le conseil immobilier (CBRE, etc.) décrit désormais le data center comme **« un
  immobilier mesuré en mégawatts »** : la valeur se compte en MW sécurisés, pas en m².

**Conclusion** : ce n'est pas une idée exotique — c'est un **modèle établi**, pratiqué par
des acteurs allant du promoteur (Altarea) à l'énergéticien (EDF). Ta lecture est la bonne.

---

## 4. Les vérités qui te concernent (l'analyse honnête pour Rodez)

Le concept est validé, mais deux réalités **redimensionnent** ce qu'il peut donner sur
**ton** site précis.

### a) L'échelle : 2,5 MW, c'est petit dans ce marché
Tout l'écosystème « powered land » médiatisé (EDF, Altarea, Silver Lake/Hines, les fonds
à 400 M$) vise **des dizaines à des centaines de MW**, voire le gigawatt. **Tu ne vendras
pas à un hyperscaler** (Google, AWS, Microsoft) avec 2,5 MW : c'est ~100× trop petit pour
eux. Ton acheteur potentiel est d'une autre nature :
- **opérateur edge / de colocation régionale** (l'edge cherche justement des sites petits,
  proches des territoires) ;
- **développeur/foncière data center** qui agrège des sites secondaires ;
- **entreprise/collectivité** voulant son propre petit data center (souveraineté, santé) ;
- un acteur type **Policloud** ou intégrateur qui déploie des conteneurs.

Le **pool d'acheteurs est plus étroit** et les **multiples plus modestes** que les
exemples hyperscale. Bonne nouvelle relative : ta **densité** est correcte (2,5 MW sur
~0,25 ha ≈ bien au-delà des 3-4 MW/acre du marché), donc le site est « dense en
puissance » — c'est le **volume absolu** qui est petit, pas la qualité.

### b) La localisation : Rodez n'est pas un hub data center
La demande data center se concentre près des **backbones fibre, des métropoles et des
nœuds réseau** (Paris, Marseille — atterrissement des câbles sous-marins —, Lyon, Bordeaux).
**Rodez est un territoire secondaire, à l'écart des grands axes.** C'est **la principale
faiblesse** de la stratégie RTB ici : le powered land ne crée de la valeur que **là où il
y a une demande data center**.

Tes contre-arguments réels, à documenter :
- **La puissance disponible (2,5 MW) est rare et immédiate** — c'est justement ce qui
  manque partout ailleurs ;
- **foncier bon marché** vs métropoles ;
- **climat frais** (altitude ~590 m) → free cooling, PUE bas, argument coût ;
- **souveraineté / edge régional** (santé, collectivités, secteur public d'Occitanie nord) ;
- parcelle **déjà artificialisée** (argument ZAN).
- **À vérifier absolument : la fibre.** Sans connectivité fibre correcte à Bel-Air, la
  valeur RTB chute fortement. C'est le 3ᵉ pilier du powered land, à instruire en priorité.

---

## 5. Pourquoi cette idée est, malgré tout, la plus intelligente pour toi

Même avec ces réserves, le RTB est probablement **la meilleure porte d'entrée** — pour
des raisons qui collent à ta situation :

| Critère | Exploiter le DC (docs 03-09) | **RTB / Powered land (cette idée)** |
|---|---|---|
| Capital à mobiliser | très élevé (2,5 M€/boîte IT, ou +10 M€ bâtiment) | **faible** : maîtrise foncière + permis + PTF Enedis + désamiantage (quelques centaines de k€) |
| Risque techno (obsolescence GPU) | fort | **nul** (tu ne portes pas l'IT) |
| Risque commercial (taux de location) | fort | **transféré à l'acheteur** |
| Horizon de sortie | 8-10 ans d'exploitation | **~18-24 mois** (à l'atteinte du RTB) |
| Compétence requise | exploitant data center | **développeur EnR — exactement ton métier** |
| Rôle du désamiantage | coût | **brique de dé-risquage qui crée de la valeur** |

**Point-clé** : le RTB **n'est pas une alternative** au projet data center — c'est sa
**première phase, la moins risquée**. On développe jusqu'au RTB, et **à ce jalon on tient
une option** :
- soit **vendre / apporter** le site RTB et encaisser la survaleur (comme Peterson, comme
  EDF) ;
- soit **construire** (ou faire construire par un partenaire type Policloud/Vantage) si
  la demande est là.

Tu ne fermes aucune porte, et tu dépenses peu avant de savoir. C'est **la logique
“développer puis arbitrer” des EnR**, appliquée telle quelle.

---

## 6. Ce qui fait qu'un site est vraiment « RTB » (feuille de route)

Pour transformer le dépôt de ton père en foncier RTB vendable, il faut cocher :

- [ ] **Maîtrise foncière** : promesse de vente / option / bail avec ton père (au lieu de
  la vente au BTP). C'est le socle — sans droit sur le terrain, rien à vendre.
- [ ] **Puissance sécurisée** : passer de « 2,5 MW indiqués sur la carte » à **capacité
  réservée** = **PTF Enedis acceptée + acompte** (doc 08). C'est LA brique qui crée la
  valeur — et elle a un coût. Vérifier la **transférabilité** de la réservation à un
  futur acheteur (le raccordement est attaché au point de livraison/PDL).
- [ ] **Autorisations** : CUb (doc 07) puis **permis de construire** purgé de recours,
  éventuellement pour une enveloppe « data center » suffisamment souple.
- [ ] **Terrain dé-risqué et propre** : **désamiantage + démolition** du hangar (doc 06),
  dalle/pad constructible, VRD, clôture. Un terrain « propre et plat » se vend mieux.
- [ ] **Connectivité fibre** : présence/possibilité d'adduction fibre — **à vérifier en
  priorité** (maillon faible potentiel à Rodez).
- [ ] **Dossier de due diligence** : géotechnique, environnement, PPRi, servitudes — le
  « data room » que l'acheteur voudra.

À l'issue, tu détiens un **actif “powered, permitted, clean”** — l'objet même que les
fonds s'arrachent, à ton échelle.

---

## 7. Mon avis

**C'est une bonne idée, et probablement la bonne première étape.** Trois raisons :

1. **Elle joue sur ta force** (développeur) et évite tes faiblesses (tu n'es pas exploitant
   data center, tu n'as pas le capital IT). Le marché prouve que des acteurs sérieux
   (EDF, Altarea) font exactement ça.
2. **Elle dé-risque tout le reste** : même si le projet d'exploitation ne se fait jamais,
   un foncier RTB a une valeur propre, très supérieure à un dépôt BTP à toiture amiantée.
   Et elle **finance la suite** ou se **revend**.
3. **Elle préserve l'optionalité** : à l'arrivée, tu choisis entre vendre et construire.

**Mais sois lucide sur deux points** qui doivent cadrer les attentes (surtout face à ton
père) :
- **N'attends pas les multiples de la Virginie.** À 2,5 MW en Aveyron, la survaleur sera
  réelle mais **modeste en valeur absolue** ; l'enjeu sera de **trouver le bon acheteur**
  (edge/colo régional), pas un hyperscaler.
- **La localisation est le vrai test.** Avant d'investir dans la PTF et le permis, il faut
  **valider qu'il existe une demande** pour un site de 2,5 MW à Rodez (fibre + un ou deux
  acheteurs plausibles). Si oui, fonce. Si la fibre manque et qu'aucun acheteur ne se
  dessine, le RTB perd son sens et il vaut mieux revenir au scénario “exploitation edge” à
  petite échelle (docs 03/09) ou renoncer.

**Recommandation** : traiter le RTB comme la **Phase 1** du projet, avec deux jalons de
décision peu coûteux avant tout engagement lourd :
1. **Test de marché express** (1-2 semaines) : vérifier la fibre à Bel-Air + sonder 3-4
   acheteurs types (opérateurs edge/colo régionaux, foncières data center, Policloud) sur
   l'appétit pour un site RTB 2,5 MW à Rodez.
2. **Sécurisation** (si test OK) : promesse foncière avec ton père + PTF Enedis + CUb —
   c'est ce qui crée la valeur RTB, pour un capital limité.

---

## 8. Comparatif des 3 postures (pour le dossier propriétaire)

| Posture | Capital | Risque | Horizon | Qui porte quoi | Pour qui |
|---|---|---|---|---|---|
| **0. Vente au BTP** (statu quo) | 0 | 0 | immédiat | rien | baseline à battre |
| **1. RTB / Powered land** ⭐ | faible | faible | 18-24 mois | tu développes, un tiers exploite | **recommandé en premier** |
| **2. Exploitation data center** | très élevé | élevé | 8-10 ans | tu portes tout | si demande avérée + financement |

Le RTB est le **chaînon manquant** entre « vendre au BTP » (valeur faible, définitive) et
« exploiter » (valeur élevée, risquée) : il **capte une survaleur** en gardant le risque
et le capital bas.

## Sources

- [Powered Land: The $1M-an-acre asset fueling the data center frenzy — Bisnow](https://www.bisnow.com/national/news/data-center-development/powered-land-the-1m-an-acre-asset-fueling-the-data-center-frenzy-132995)
- [Powered Land Full Report 2025 — Hines](https://www.hines.com/powered-land/power-play-full-report)
- [From dirt to data: investors unearth opportunities in powered land — Hiffman](https://hiffman.com/from-dirt-to-data-infrastructure-and-real-estate-investors-unearth-opportunities-in-powered-land/)
- [Le marché du Data Center en plein boom — CBRE France](https://www.cbre.fr/insights/articles/le-marche-du-data-center-en-plein-boom)
- [Data centers : un immobilier mesuré en mégawatts — Carte Financement](https://cartefinancement.com/data-centers-immobilier-megawatts-infrastructure/)
- [Data centers en France : EDF mobilise son patrimoine foncier — EDF](https://www.edf.fr/en/the-edf-group/supporting-our-clients/cei-data-centers)
- [Trois sites stratégiques proposés par EDF pour les datacenters — Sfen](https://www.sfen.org/rgn/edf-sites-centres-donnees/)
- [EDF et OpCore : data center à Montereau — communiqué EDF](https://www.edf.fr/en/the-edf-group/dedicated-sections/journalists/all-press-releases/edf-and-opcore-to-develop-a-high-power-data-center-on-site-of-former-thermal-power-plant-in-montereau-vallee-de-la-seine-wider-paris-metropolitan-region)
- [Altarea & Vantage Data Centers : partenariat en France — Business Wire](https://www.businesswire.com/news/home/20260224479112/en/Altarea-and-Vantage-Data-Centers-Announce-Strategic-Partnership-to-Develop-AI-and-Cloud-Data-Center-Campus-in-France)
- [Inside the Site Race: valuing data center land — Marshall & Stevens](https://marshall-stevens.com/insights-center/inside-the-site-race/)
