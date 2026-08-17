# 29 — Après l'appel du chargé de projet Enedis : préparer le RDV et tester la demande

> Appel reçu le **17/08/2026**, le jour même du dépôt (réf. demande **260817I200009**,
> dossier **RACNMP26005657**). Ce document acte ce que l'appel change, corrige une erreur
> de périmètre sur le transformateur, prépare le rendez-vous sur site, et répond à la
> question de fond : **y a-t-il un acheteur pour 2 MW à Rodez ?**

---

## 1. Ce que l'appel change — et ce qu'il ne change pas

### ✅ Trois vraies bonnes nouvelles

| Point | Pourquoi c'est important |
|---|---|
| **Rappel le jour même** | Un dossier HTA propre, sur un site réel, avec mandat joint. Le traitement rapide n'est pas de la chance : c'est la conséquence du cadrage. |
| **Devis / proposition de raccordement au lieu de l'étude anticipée payante** | Le récapitulatif du dépôt disait *« cette prestation est payante conformément au barème raccordement »*. Le chargé de projet te bascule sur un **chiffrage réel et gratuit**. Tu obtiens plus, pour zéro euro. |
| **Pas de permis de construire** | Parce qu'on réutilise le bâtiment existant. C'est exactement le cadrage retenu au doc 24 §3bis, et c'est **6 à 12 mois de gagnés**. |

### ⚠️ Ce que ça ne change pas

- **Le coût du raccordement reste inconnu.** Le HTA « au coin de la rue » rend l'extension
  courte, donc *a priori* peu coûteuse — mais le poste de livraison et un éventuel
  renforcement pèsent bien plus lourd que les mètres de câble. **Ton intuition sur le
  risque de renforcement est juste : c'est là qu'est la vraie incertitude.**
- **La capacité n'est toujours pas réservée** (voir §2 — c'est le point critique).
- **La question du doc 21 reste entière** : *qui paie le raccordement ?*

### 🟢 Ce qui change dans le produit vendu

Passer de 1 MW à **2 MW** avec **bâtiment existant réutilisable** modifie la nature de
l'offre. Tu ne vends plus « un terrain ». Tu vends :

> **2 MW raccordables vite, dans un bâtiment qui existe déjà, sans permis à obtenir.**

Ce n'est pas un produit immobilier, c'est un **produit de délai**. Voir §6 — c'est ce qui
rend le dossier défendable.

---

## 2. ⚠️ Le point à ne surtout pas rater au RDV : à partir de quand la capacité est-elle à toi ?

C'est **la** question du rendez-vous, et elle prime sur toutes les autres.

Le raccordement fonctionne au **premier arrivé, premier servi**. Une demande déposée ne
réserve rien. Ce qui réserve la capacité, c'est généralement **l'acceptation de la
proposition de raccordement — signature + acompte**.

D'où la tension à résoudre :

| | |
|---|---|
| Tu veux | connaître le coût **sans** engager d'argent |
| Mais | la capacité n'est sécurisée qu'**en payant** |
| Et | un autre projet peut préempter le départ HTA entre-temps |

**Trois questions à poser mot pour mot :**

1. *« À partir de quel moment exact la capacité est-elle réservée à mon dossier ? »*
2. *« Quel est le montant de l'acompte à l'acceptation, en pourcentage et en euros, et
   selon quel échéancier ? »*
3. *« Quelle est la durée de validité de la proposition, et que se passe-t-il si je la
   laisse expirer — puis-je en redemander une sans repartir de zéro ? »*

> 🎯 **La réponse à la question 2 est le chiffre qui décide de la suite du projet.**
> Si réserver 2 MW suppose de sortir plusieurs dizaines de milliers d'euros, tu ne peux pas
> le faire seul : il faut un partenaire, un exploitant, ou basculer sur le bail. C'est la
> question « qui paie le raccordement ? » du doc 21 qui arrive enfin sous forme chiffrée.

---

## 3. 🔴 Correction de périmètre : le transformateur n'est pas à toi

Tu as noté « prendre des infos sur le coût d'un transfo de 2 MW ». **C'est un faux pas, et
il coûterait cher.** Voici le découpage réel d'un raccordement HTA.

```
   RÉSEAU ENEDIS          │  POINT DE LIVRAISON  │        TOI            │   EXPLOITANT
─────────────────────────────────────────────────────────────────────────────────────────
  Départ HTA 20 kV        │   Cellules HTA       │  Poste de livraison   │  Transfos HTA/BT
  Extension ~260 m        │   Comptage           │  Génie civil, local   │  TGBT, onduleurs
  (éventuel renforcement) │                      │  Terrain, accès       │  Groupes, clim, IT
─────────────────────────────────────────────────────────────────────────────────────────
   ◄── barème Enedis ──►  │                      │  ◄── ton CAPEX ──►    │ ◄─ son CAPEX ─►
```

### Pourquoi ne pas acheter le transformateur

1. **Il est en aval du point de livraison** — il ne conditionne ni le raccordement, ni la
   capacité réservée. Il n'apporte **aucun dé-risquage** au dossier.
2. **C'est l'exploitant qui le dimensionne**, et selon des critères que tu ne peux pas
   anticiper : redondance (N+1 ? 2N ?), donc **deux ou trois transfos** plutôt qu'un seul de
   2 000 kVA ; type sec ou immergé selon la sécurité incendie ; tenue aux harmoniques des
   onduleurs ; tension secondaire. **Un transfo acheté à l'aveugle a toutes les chances
   d'être le mauvais.**
3. **C'est du capital immobilisé qui se déprécie**, sur un projet où ta force est
   justement de **ne rien immobiliser** (doc 27 : la marge de développement).
4. Tu as d'ailleurs laissé le champ *« nombre de transformateurs HTA/BT prévus »* vide dans
   ta demande — **c'était le bon réflexe**, garde-le.

### Ce qu'il faut chiffrer à la place : le **poste de livraison HTA**

C'est l'ouvrage qui est réellement de ton côté : local ou cabine préfabriquée, cellules
HTA, comptage, génie civil, mise à la terre.

**Et la bonne façon de le chiffrer, c'est de demander à Enedis de l'inclure dans la
proposition** — pas d'aller chercher des devis privés. Enedis peut souvent le réaliser en
prestation, et de toute façon le chiffrage est gratuit dans le cadre du dossier en cours.

> 📌 Je n'ai **pas trouvé de barème public fiable** pour un poste de livraison HTA ni pour
> l'extension HTA au mètre linéaire — les grilles publiées en ligne concernent la BT et ne
> se transposent pas. **Raison de plus pour laisser Enedis chiffrer** : leur devis sera à la
> fois gratuit, exact et opposable, là où un devis privé serait payant et approximatif.

**Question à poser au RDV** : *« Le poste de livraison est-il chiffré dans votre proposition,
ou dois-je le faire réaliser par un tiers ? »*

---

## 4. Préparer le rendez-vous sur site

### À apporter

- [ ] Le **plan de masse** du géomètre (celui du dossier propriétaire)
- [ ] L'**extrait cadastral** et le plan de situation (déjà joints à la demande)
- [ ] Le **mandat signé** (papier, au cas où)
- [ ] Une **facture d'électricité** du dépôt si tu as réussi à l'obtenir → **le PRM**
- [ ] Les **références** : demande 260817I200009 / dossier RACNMP26005657

### Repérage à faire toi-même avant, sur place

- [ ] Où passe exactement le **HTA « au coin de la rue »** — photo, distance au portail
- [ ] Où pourrait se poser le **poste de livraison** : accès **camion et grue** depuis la
      voirie, à moins de 30 m environ de la limite de propriété, sans traverser le bâtiment
- [ ] Le **tracé possible du câble** entre la rue et ce point (revêtement à ouvrir ?)
- [ ] L'**arrivée télécom** existante (regard, fourreaux) → utile aussi pour la fibre
- [ ] Vérifier que l'emplacement pressenti **ne condamne pas** l'extension future du bâtiment

### Les 12 questions à poser

**Capacité et risque de renforcement — le cœur du sujet**

1. Le départ HTA peut-il accueillir **2 MW** sans renforcement ? Et **1 MW** ?
2. Si un renforcement est nécessaire, **de quelle nature** (câble, poste source, protections)
   et **quel ordre de grandeur** de coût ?
3. La limite vient-elle **du départ** ou du **poste source** amont ?
4. Y a-t-il des **demandes concurrentes en file d'attente** sur ce départ ?
5. Existe-t-il un **palier de puissance** en dessous duquel le renforcement disparaît ?
   *(Question à haute valeur : peut-être que 1,5 MW passe et 2 MW ne passe pas. Ça change tout.)*

**Coût et engagement**

6. À partir de quand la **capacité est-elle réservée** ?
7. **Montant et échéancier de l'acompte** à l'acceptation ?
8. **Durée de validité** de la proposition, et conséquence d'une expiration ?
9. Le **poste de livraison** est-il chiffré dans votre proposition ?

**Délais et suite**

10. **Délai de réalisation** une fois la proposition acceptée ?
11. Confirmez-vous qu'**aucune autorisation d'urbanisme** n'est requise dans ce montage ?
12. Le dossier reste-t-il valable si **le bénéficiaire change** (vente de la parcelle ou
    entrée d'un exploitant) — le raccordement est-il **transférable** ?

> ⚠️ **La question 12 est stratégique.** Tout ton modèle repose sur l'idée de céder un
> foncier *déjà raccordé*. Si le raccordement n'est pas transférable à un repreneur, la
> survaleur RTB s'effondre. **Fais-toi confirmer ce point par écrit.**

### Ce qu'il ne faut PAS dire

- ❌ « J'ai 2,5 MW disponibles » → la carte est indicative, ils le savent mieux que toi
- ❌ « Je vais revendre le terrain » → tu deviens un intermédiaire spéculatif à leurs yeux ;
  reste sur **« projet de data center sur le site familial »**, ce qui est vrai
- ❌ Toute mention de **Tenergie**

---

## 5. La fibre : ce qu'il faut demander, et à qui

**Attention à une confusion** : il n'existe pas de « demande de raccordement fibre » à
guichet unique comme chez Enedis. La fibre s'obtient en **demandant des devis à des
opérateurs**, qui se chargent eux-mêmes du raccordement.

Le doc 11 avait conclu 🟢 sur la faisabilité. Ce qui manque, ce sont **deux ou trois devis
écrits** — c'est ça, la pièce du dossier RTB.

### Le bon produit

Pas de la FTTH grand public : de la **FTTO** (fibre dédiée, point à point), débit
symétrique, **GTR 4 h**.

### Qui contacter

| Opérateur | Pourquoi lui | Angle |
|---|---|---|
| **FullSave** (Toulouse) | opérateur FTTO **et** exploitant de data centers à Toulouse | 🎯 **double intérêt** : fournisseur *et* client potentiel (§6) — tu as déjà un e-mail en brouillon |
| **Céleste** | FTTO nationale, GTR 4 h, opérateur data center | comparatif de prix |
| **Orange Business** | présent en propre sur Rodez (zone AMII) | référence de marché |
| **ALL'Fibre / SIEDA** | délégataire du réseau public Aveyron | savoir ce qui existe déjà **dans la rue** |

### Ce qu'il faut demander précisément

> *« Devis FTTO pour un site en ZA de Bel-Air à Rodez, 35 rue de la Ferronnerie :
> 1 Gbit/s symétrique évolutif 10 Gbit/s, GTR 4 h. Merci de préciser : (a) les frais d'accès
> au service et le délai de raccordement, (b) l'abonnement mensuel, (c) **s'il existe une
> seconde adduction physiquement distincte** pour de la redondance, et à quelles conditions. »*

Le point (c) est le seul vrai inconnu technique, et c'est celui qui compte pour un data
center. Le reste est de la commodité.

> 💡 **Ne signe rien.** Un devis écrit avec délai suffit au dossier. Un abonnement fibre
> souscrit trop tôt, c'est de l'OPEX sur un site vide.

---

## 6. Y a-t-il un vrai marché pour 2 MW à Rodez ? — réponse franche

### 6.1 La bonne nouvelle : ton avantage n'est pas le foncier, c'est le délai

Le constat qui domine le marché français en 2026 : **c'est le réseau électrique, et non la
disponibilité de terrain, qui détermine où s'installe un data center.** Les délais de
raccordement annoncés côté RTE pour les grands sites vont de **2 à 7 ans**, et les files
d'attente sur les marchés cœur se comptent en années, contre environ 2 ans de construction.

Autrement dit : **partout, le temps est devenu la ressource rare.**

Or ton site cumule trois raccourcis :

| Raccourci | Gain |
|---|---|
| Raccordement **Enedis HTA** (pas RTE), extension courte | mois plutôt qu'années |
| **Bâtiment existant** réutilisable | pas de construction lourde |
| **Aucun permis de construire** | 6-12 mois économisés |

**C'est ça, ton produit.** Pas « 2 631 m² à Rodez ». Mais : *« 2 MW opérationnels en 2027,
dans un bâtiment debout, sans autorisation à obtenir. »*

### 6.2 La mauvaise nouvelle, inchangée : 2 MW reste petit

Le doc 14 tient toujours. Les acteurs du *powered land* (Hadès, Datalok, les sites de
l'État) travaillent sur **18 à 150 hectares** et des dizaines de MW. Les grands projets
français en développement visent **50 à 250 MW**. À cette échelle, **2 MW n'est pas un
projet, c'est une note de bas de page.**

**Conséquence directe : ne construis pas ta stratégie sur les fonds fonciers.** Ils te
répondront poliment que c'est trop petit. L'appel Datalok du 26 août sert à **confirmer
cette borne**, pas à trouver un acheteur.

### 6.3 Qui, alors ? — trois familles réalistes

**A. Les opérateurs edge régionaux en croissance externe** ⭐

C'est la cible la plus crédible, parce qu'ils opèrent précisément à cette échelle.

| Acteur | Situation | Verdict |
|---|---|---|
| **nLighten France** *(ex-Euclyde)* | 8 sites en France ; stratégie **buy-and-build** assumée ; déjà présent à **Besançon**, ce qui prouve qu'ils vont en ville moyenne | 🎯 **nouvelle cible n°1** — à ajouter au doc 12 |
| **UltraEdge** | modèle *Datapole* = un site majeur + **sites complémentaires dans un rayon de ~100 km** ; datapole Toulouse annoncé | 🟡 Rodez est à **150 km**, un peu hors rayon — mais l'angle **PRA** (doc 22) est exactement leur logique. À tester, sans y croire trop fort (doc 19 : ils évitent le greenfield) |
| **FullSave** | opérateur **et** hébergeur toulousain | 🎯 le plus accessible, et tu le contactes déjà pour la fibre |

⚠️ **Le biais commun à connaître** : ces acteurs rachètent des **data centers en
exploitation**, pas du terrain. Ta question doit donc être formulée en conséquence (§6.4).

**B. Le site de repli / PRA pour Toulouse** ⭐

C'est la conclusion du doc 22, et elle se renforce : 150 km de Toulouse, au-delà du seuil
de 50-100 km qu'exigent les plans de continuité, avec une latence compatible réplication
synchrone. **C'est l'usage où « Rodez » est un atout et non un handicap.**

Cible : les hébergeurs toulousains et les DSI de grandes entreprises régionales.

**C. Les utilisateurs finaux régionaux**

RAGT (semences, siège à Rodez), Bosch à Onet-le-Château, Unicor, le Centre Hospitalier de
Rodez (données de santé, hébergement HDS), Rodez Agglomération, le Département de l'Aveyron.

⚠️ **Limite honnête** : aucun d'eux ne consomme 2 MW. On parle de 100 à 500 kW. Ils peuvent
être **client d'ancrage**, pas repreneur du site.

### 6.4 La question à poser, reformulée

Ta question de départ était « voulez-vous acheter du foncier à Rodez ». Elle échouait
parce qu'aucun de ces acteurs n'achète de foncier. La bonne formulation, maintenant que tu
as un dossier Enedis réel :

> *« Je peux livrer en 2027, à Rodez, un bâtiment industriel existant de 487 m² avec
> **2 MW HTA raccordés** et de la fibre dédiée, **sans permis de construire à obtenir** —
> j'ai un dossier de raccordement ouvert chez Enedis et un chargé de projet nommé.*
> *Trois questions : (1) est-ce une taille qui vous intéresse ? (2) à quel stade de maturité
> vous engageriez-vous — dossier ouvert, proposition signée, ou site en service ?
> (3) **qui finance le raccordement** dans un montage de ce type ? »*

Les questions (2) et (3) valent plus que la (1). **Un « non » assorti de la réponse à (3)
est une réunion réussie.**

### 6.5 Verdict

**Il y a un marché, mais il est étroit et il n'est pas là où tu le cherchais.** Pas les
fonds fonciers ; les **opérateurs edge en croissance externe** et l'**angle PRA toulousain**.

Et le test coûte zéro euro : cinq appels sur trois semaines suffisent à trancher.

---

## 7. Séquencement — et ce qu'il ne faut pas dépenser

### Cette semaine

| Action | Coût | Pourquoi |
|---|---|---|
| **Kbis récent** (monidenum.fr) | 0 € | ⚠️ toujours pas fait, toujours bloquant |
| **Caler le RDV Enedis** et le préparer avec le §4 | 0 € | chemin critique |
| **Relancer pour le PRM** *(Lilian GAU, Cabinet AGENDA, 06 88 94 97 77)* | 0 € | utile au RDV |
| **Envoyer les 3-4 demandes de devis FTTO** (§5) | 0 € | en parallèle, sans attendre |
| **Envoyer les e-mails** Hadès + FullSave *(brouillons prêts)* | 0 € | avec la formulation §6.4 |

### Dans les trois semaines

- **Appel Datalok le 26 août** — objectif révisé : **confirmer la borne basse du marché**
  (« à partir de combien de MW regardez-vous un site ? »), pas vendre
- **Contacter nLighten France** — nouvelle cible prioritaire
- **Tester l'angle PRA** auprès de FullSave et d'un hébergeur toulousain

### ❌ Ce qu'il ne faut PAS faire maintenant

| À éviter | Pourquoi |
|---|---|
| Acheter ou faire chiffrer un **transformateur** | hors périmètre (§3) — c'est le CAPEX de l'exploitant |
| Signer le **devis assainissement** (21,7 k€) | statut obligatoire/volontaire toujours non clarifié |
| **Souscrire** un abonnement fibre | un devis suffit |
| Payer une **étude privée** de raccordement | Enedis chiffre gratuitement |
| **Accepter la proposition** de raccordement | tant que la réponse à « qui paie ? » est inconnue |
| Déposer une **seconde demande** à 2 MW | le chargé de projet requalifie le dossier existant |

---

## 8. Ce qu'il faut retenir

1. **L'appel est une vraie victoire** : chiffrage gratuit, pas de permis, interlocuteur nommé.
2. **La question du RDV n'est pas le coût, c'est l'engagement** : quand la capacité est-elle
   réservée, et combien faut-il payer pour ça ?
3. **Le transformateur n'est pas à toi** — ne dépense pas là-dessus.
4. **Le raccordement doit être transférable**, sinon tout le modèle tombe. À confirmer par écrit.
5. **Ton produit, c'est le délai, pas le foncier.**
6. **Le marché existe mais il est étroit** : opérateurs edge en croissance externe, et PRA
   toulousain. Pas les fonds fonciers.

---

## Sources

- [Data centers en France : carte des régions et opérateurs 2026 — Travail Industrie](https://travail-industrie.com/blog/article-titre/carte-data-centers-france-regions-implantations)
- [Powered Shell Data Centers: What Developers Need to Know — Build Inc.](https://build.inc/insights/powered-shell-data-centers)
- [Datacenters IA et électricité : ce que prépare RTE — ECOinfos](https://www.les-energies-renouvelables.eu/article/actualites/energies/datacenters-ia-electrification-france-rte-856/)
- [nLighten acquires seven edge data centers from EXA Infrastructure — Edge Infrastructure Review](https://www.edgeir.com/nlighten-acquires-seven-edge-data-centers-from-exa-infrastructure-to-expand-into-europe-20240410)
- [nLighten acquires Paris data center from French managed services firm — DCD](https://www.datacenterdynamics.com/en/news/nlighten-acquires-paris-data-center-from-french-managed-services-firm/)
- [UltraEdge lance officiellement ses Datapoles — DCmag](https://dcmag.fr/ultraedge-lance-officiellement-ses-datapoles-des-ecosystemes-dhebergement-de-proximite-ultra-connectes/)
- [Fibre optique dédiée entreprise, GTR 4 h — Céleste](https://www.celeste.fr/fibre-optique-et-acces-internet-entreprise/fibre-optique-dediee-entreprise/)
- [Internet FullSave : fibre FTTO pour entreprises](https://www.fullsave.com/offres/business-internet/)
- [Très haut débit / ALL'Fibre — SIEDA](https://www.sieda.fr/tres-haut-debit)
- [Combien coûte un raccordement au réseau Enedis ? — Lab Énergies](https://www.lab-energies.fr/articles/cout-raccordement-enedis)
