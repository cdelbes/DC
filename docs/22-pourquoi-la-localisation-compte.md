# 22 — Pourquoi un data center est-il plus difficile à développer à Rodez qu'en métropole ?

> **La question posée** : « Tant qu'un data center est connecté au réseau électrique et à
> la fibre, sa localisation physique importe peu — il peut rendre le même service où
> qu'il soit. »
>
> **Réponse courte** : **techniquement, tu as raison** — et le marché est en train de te
> donner raison à grande échelle. **Économiquement, il y a six barrières réelles**, et
> aucune n'est technique. Surtout, elles ne dépendent pas de la géographie mais du
> **modèle d'affaires** : le handicap d'une petite ville est proportionnel au **nombre de
> clients** dont on a besoin, pas aux mégawatts installés.

---

## 1. Ton intuition est juste — la physique le confirme

La latence est l'argument le plus invoqué contre les sites régionaux. Regardons les
chiffres réels.

Dans une fibre optique, la lumière se propage à ~**200 000 km/s** (l'indice du verre ralentit
la lumière d'environ un tiers). Le temps d'aller-retour (RTT) minimum est donc de
**10 µs par kilomètre**.

| Liaison depuis Rodez | Distance | RTT théorique | RTT réel estimé* |
|---|---|---|---|
| Toulouse | ~150 km | 1,5 ms | **~2-3 ms** |
| Marseille | ~350 km | 3,5 ms | ~5-7 ms |
| Paris | ~550 km | 5,5 ms | **~8-10 ms** |

\* *en ajoutant le routage, les équipements et les chemins fibre non rectilignes.*

**Points de comparaison** :
- seuil de perception humaine : **~100 ms** ;
- une requête base de données dans le même bâtiment : **< 1 ms** ;
- une page web charge des dizaines d'allers-retours — mais 8 ms de plus par requête reste
  imperceptible pour un ERP, une messagerie, une sauvegarde ou du stockage.

**Conclusion : pour l'immense majorité des usages professionnels, la latence depuis Rodez
n'est pas un obstacle.** L'argument « il faut être près des utilisateurs » est **très
largement surestimé**.

### Et le marché te donne raison

- Les centres de calcul IA se construisent **en zone rurale** : Le Bosquel (Somme),
  Cambrai (1 GW) — précisément parce que l'entraînement de modèles se moque de la latence.
- Le segment « **reste de la France** » croît à **+17,8 %/an**, plus vite que l'Île-de-France
  (doc 18).
- Les régions qui gagnent (Hauts-de-France, Grand Est, vallée du Rhône) sont choisies pour
  leur **capacité réseau électrique**, pas pour leur proximité aux utilisateurs.
- Le constat du marché est explicite : « **le réseau électrique, et non l'immobilier, est
  devenu le facteur déterminant** du lieu d'implantation ».

**Tu as donc raison sur le sens de l'histoire.** La contrainte s'est déplacée de la fibre
vers l'électricité — et c'est exactement là que ton site est fort.

---

## 2. Alors pourquoi est-ce plus dur ? Les six vraies barrières

Aucune n'est technique. Toutes sont économiques ou structurelles.

### ① L'interconnexion : le coût caché du réseau

C'est la barrière la plus mal comprise. Un data center ne vaut pas par sa fibre, mais par
le **nombre de réseaux qu'il peut atteindre directement**.

- **En métropole** (Paris, Marseille) : des points d'échange (France-IX, Equinix) où l'on
  **peere gratuitement ou à très bas coût** avec des centaines de réseaux. Marseille est
  même un atterrissement de câbles sous-marins.
- **À Rodez** : il faut **acheter du transit** et payer le **backhaul** (transport) vers
  Toulouse ou Paris. C'est un coût **récurrent au Mbps** que le concurrent métropolitain ne
  supporte pas. Et pour être redondant, il en faut **deux**.

→ Tu peux rendre le même service, mais avec une **structure de coûts durablement plus
élevée** sur la partie réseau.

### ② La densité de clients : le vrai tueur

C'est **la barrière dominante**, et elle n'a rien à voir avec la technique.

Un data center a des **coûts fixes énormes** (coque, raccordement, froid, sécurité,
supervision) et un coût marginal faible par baie remplie. **Tout se joue sur le taux de
remplissage.**

Illustration de la mécanique :

| | Remplissage 80 % | Remplissage 30 % |
|---|---|---|
| Revenus | 100 % du plan | **37 %** du plan |
| Coûts | ~100 % du plan | **~75 %** du plan (les fixes restent) |
| Résultat | bénéficiaire | **lourdement déficitaire** |

Or le **vivier de clients** n'est pas le même :

| | Métropole (Toulouse, ~1,5 M hab.) | Rodez Agglo (~60 000 hab.) |
|---|---|---|
| Entreprises adressables | des **milliers** | quelques **dizaines** |
| Prospects sérieux pour de la colocation | des centaines | ~10 à 20 |

→ Le problème n'est pas de **servir** les clients depuis Rodez. C'est d'en **trouver assez
pour remplir**.

### ③ L'effet de réseau : les clients veulent être entre eux

Un data center fonctionne comme une **place de marché**. Les clients (opérateurs, ESN,
hébergeurs) veulent s'interconnecter **entre eux** — c'est souvent la raison première de
venir.

Un site avec 30 opérateurs et 500 clients attire mécaniquement plus qu'un site avec 3
opérateurs et 20 clients. **Le succès appelle le succès**, et la concentration
métropolitaine s'auto-entretient. C'est un effet de réseau classique, très difficile à
contrer par la seule qualité technique.

### ④ L'écosystème technique et humain

- **Remote hands** et astreinte 24/7 : qui intervient à 3 h du matin ?
- **Maintenance spécialisée** : froid, électricité HTA, extinction gaz, pièces détachées.
- **Concurrence fournisseurs** : en métropole, plusieurs prestataires se disputent le
  marché ; à Rodez, on fait venir une équipe de Toulouse.

→ **OPEX plus élevé** et **crédibilité SLA plus difficile** à démontrer face à un client
exigeant.

### ⑤ La redondance des infrastructures

Une métropole offre **plusieurs routes fibre indépendantes** et **plusieurs postes
sources**. C'est ce qui permet de viser une certification Tier III/IV.

Ton site, lui, est en **bout de départ HTA** — alimentation radiale, sans bouclage
(doc 08). Obtenir un vrai niveau de redondance coûte plus cher qu'en métropole.

### ⑥ La liquidité financière

Un investisseur valorise la facilité de revente. Un data center métropolitain a **beaucoup
d'acheteurs potentiels** ; un site à Rodez en a **peu** (docs 14 et 19). Cela se traduit
par une **exigence de rentabilité plus élevée** et une **valorisation plus faible** — pas
parce que l'actif est mauvais, mais parce qu'il est **moins liquide**.

---

## 3. La synthèse qui réconcilie tout

> **Le handicap d'une petite ville n'est pas géographique. Il est fonction du modèle
> d'affaires — et plus précisément du NOMBRE DE CLIENTS dont on a besoin.**

| Modèle | Nb de clients requis | La localisation compte-t-elle ? | Pourquoi |
|---|---|---|---|
| **IA / HPC, entraînement** | **1** | ❌ **non** | insensible à la latence, le client apporte son réseau |
| **Wholesale / build-to-suit** | **1** | ❌ **non** | un tenant unique, souvent son propre backbone |
| **Site de secours (PRA)** | 1 à quelques-uns | ❌ **non — c'est même un atout** | voir §4 |
| **Hébergement d'un opérateur** (modèle bailleur) | **1** | 🟡 peu | l'opérateur apporte ses clients |
| **Colocation retail** | **des dizaines** | ✅ **oui, énormément** | densité de clients + interconnexion + écosystème |
| **Edge / CDN basse latence** | variable | ✅ **oui** | doit être près de la population servie |

**Applique-le à ton projet** : un site de 1 MW rempli par **20 à 50 petits clients** est
très difficile à Rodez. Le **même** site de 1 MW rempli par **1 ou 2 clients** (un
opérateur, un client-ancre) est parfaitement viable.

**Ce n'est donc pas la taille en mégawatts qui pose problème — c'est la granularité de la
demande.** Et cela recoupe exactement la conclusion du doc 21 : le montage réaliste passe
par **un exploitant** ou **un client-ancre**, pas par une commercialisation de détail.

---

## 4. 💡 L'angle où Rodez est objectivement MEILLEUR qu'une métropole

Il existe un usage où l'éloignement n'est pas une contrainte mais **le produit lui-même** :
le **site de secours / plan de reprise d'activité (PRA)**.

Les bonnes pratiques du secteur :
- un site secondaire doit être **géographiquement séparé du principal, typiquement de plus
  de 50 à 100 km**, pour que les deux ne soient pas frappés par le même sinistre ;
- la **réplication synchrone** (zéro perte de données) exige une **latence inférieure à
  10 ms**.

**Position de Rodez par rapport à Toulouse :**

| Critère | Exigence | Rodez → Toulouse | Verdict |
|---|---|---|---|
| Séparation géographique | > 50-100 km | **~150 km** | ✅ risques indépendants |
| Latence pour réplication synchrone | < 10 ms | **~2-3 ms** | ✅ très confortable |
| Accessibilité pour les équipes | quelques heures de route | **~1 h 30** | ✅ |

> **Rodez est dans la zone idéale pour être le site de secours de Toulouse** : assez loin
> pour que les risques soient décorrélés (inondation, incendie, panne réseau, événement
> local), assez près pour la réplication synchrone et pour qu'une équipe s'y rende dans la
> journée.
>
> **Ce n'est pas un lot de consolation, c'est un argument commercial de premier ordre** —
> et il retourne complètement l'objection de la distance.

Autres atouts propres au site qui ne dépendent pas de la métropole :
- **PUE réduit** par le climat d'altitude (586 m, free cooling) → coût d'exploitation ;
- **puissance disponible immédiatement**, quand le raccordement prend 2 à 7 ans ailleurs ;
- **foncier bon marché** ;
- **souveraineté territoriale** (données qui restent en Aveyron).

---

## 5. Ce que ça change concrètement pour ton projet

### ✅ Ce que tu peux affirmer sans être contredit

- « La latence n'est pas un sujet : 2-3 ms de Toulouse, 8-10 ms de Paris. »
- « Le marché me donne raison : les centres IA vont en zone rurale, et le hors-Île-de-France
  croît plus vite que la métropole. »
- « La contrainte du marché s'est déplacée vers l'électricité — et c'est là que je suis
  fort. »

### ⚠️ Ce qu'il ne faut pas nier

- L'interconnexion coûtera plus cher qu'en métropole (transit + backhaul).
- Le vivier de clients locaux est étroit — **c'est la vraie limite**.
- L'écosystème technique est à importer.

### 🎯 La conséquence stratégique

**Ne cherche pas à vendre un modèle de colocation retail.** Il exige un nombre de clients
que le territoire ne peut pas fournir, et c'est là que l'objection « pourquoi pas la
métropole » devient imparable.

**Cible les modèles à faible granularité** :
1. **Site de secours / PRA** pour des acteurs toulousains — l'argument le plus fort ;
2. **Hébergement d'un opérateur** (tu es bailleur, il apporte ses clients) ;
3. **Un client-ancre** local significatif (RAGT, santé, collectivité) ;
4. **Calcul / IA batch**, insensible à la latence.

> **Formulation à retenir pour tes contacts** :
> *« La question n'est pas de savoir si un data center peut fonctionner à Rodez —
> techniquement, oui, et la latence vers Toulouse est de 2 à 3 millisecondes. La question
> est de savoir combien de clients il faut pour le remplir. C'est pourquoi je ne cherche
> pas à faire de la colocation de détail, mais à accueillir un opérateur ou un usage de
> secours. »*

Cette phrase montre que tu as compris le vrai sujet — et c'est exactement ce qui te
crédibilisera face à un professionnel.

## Sources

- [De l'importance de la distance dans un PRA — LeMagIT](https://www.lemagit.fr/conseil/De-limportance-de-la-distance-dans-un-PRA) · [Construire une stratégie de réplication à distance — LeMagIT](https://www.lemagit.fr/conseil/Construire-une-strategie-de-replication-de-donnees-a-distance)
- [Réplication synchrone vs asynchrone (latence < 10 ms) — Evidian SafeKit](https://www.evidian.com/fr/produits/haute-disponibilite-logiciel-clustering-application/replication-synchrone-versus-replication-asynchrone/) · [Réplication asynchrone — DataCore](https://www.datacore.com/products/sansymphony/asynchronous-remote-replication/)
- [Plan de reprise d'activité : concevoir un PRA efficace — SHPV](https://www.shpv.fr/blog/disaster-recovery-plan/)
- Dynamiques de marché, croissance hors Île-de-France, contrainte réseau : `docs/18-etude-marche-deploiement-datacenters-france.md`
- Critères d'implantation edge et modèle des opérateurs : `docs/12`, `docs/19`
