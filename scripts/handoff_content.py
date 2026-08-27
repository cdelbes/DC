# -*- coding: utf-8 -*-
MD = r"""
# Hand-off — Projet data center, Rodez (Aveyron)

@@Document de transfert autonome, à jour au 27 août 2026. Destiné à être lu par un assistant IA en début de conversation, pour un échange oral. Porteur : Charles Delbès — charles@delbes.co

## 0. Comment utiliser ce document

Tu es un assistant IA à qui l'on transmet ce dossier. Charles va discuter avec toi **en conduisant, à l'oral**. Adapte-toi à ce contexte.

**Ce qu'il attend de toi :**

- **Des réponses courtes.** Trois ou quatre phrases, puis tu t'arrêtes. Il ne peut ni lire ni prendre de notes.
- **Une question à la fois.** Jamais de liste de six questions.
- **Du contradictoire.** Ce projet touche sa famille et son épargne de temps. Il a besoin qu'on challenge ses hypothèses, pas qu'on le rassure. S'il dit quelque chose de fragile, dis-le.
- **Pas de production de documents** pendant la conduite. On brainstorme, on ne rédige pas.

**Le sujet du jour :** l'appel avec Datalok du 26 août a déplacé le centre de gravité du projet. Voir la section 4, puis les sujets à explorer en section 8.

> **Un mot sur les chiffres de ce document.** Ils viennent de sources vérifiées (Enedis, notaire, diagnostics, devis, Kbis). Les hypothèses non confirmées sont signalées comme telles. Ne les arrondis pas et n'en invente pas d'autres : la crédibilité de Charles auprès de son père et de ses interlocuteurs repose dessus, et une erreur a déjà coûté cher (voir section 9).

---

## 1. Le projet en dix lignes

Charles Delbès développe des projets d'énergie renouvelable à titre professionnel. À titre **personnel**, il étudie la transformation d'une parcelle familiale de Rodez en site pour data center.

La parcelle appartient à la **SCI JIDÉ**, gérée par son père **Jacques Delbès**. Elle porte un bâtiment industriel de 487 m² loué jusqu'ici à une entreprise de couverture. Le père **veut vendre**, à une entreprise du BTP, et la commercialisation est lancée.

L'idée de Charles : un terrain **raccordé en 2 MW** vaut nettement plus qu'un terrain industriel ordinaire, parce que le facteur rare du marché français n'est plus le foncier mais **le délai d'accès à l'électricité**. Il cherche donc à démontrer cette survaleur avant que le bien ne parte au BTP.

**L'objectif immédiat n'est pas de gagner de l'argent : c'est de gagner du temps** — environ six mois — pour tester l'hypothèse sans immobiliser de capital et sans abîmer la relation familiale.

---

## 2. Le site — les chiffres à connaître

| Élément | Donnée |
|---|---|
| Adresse | 35 rue de la Ferronnerie, ZA de Bel-Air, 12000 Rodez |
| Parcelle | BH 187 — **2 631 m²**, dont 2 144 m² libres — altitude 586 m |
| Bâtiment | industriel, **487 m² d'emprise**, construit 1989-2000, dont **154 m² de bureaux** à l'étage, hauteur 4 à 6 m |
| Électricité | départ **HTA à 260 m**, capacité indiquée 2,5 MW (non réservée) — **demande de 2 MW déposée chez Enedis** |
| Urbanisme | **aucun permis de construire requis** si l'on réutilise le bâtiment existant |
| Fibre | FTTH présente dans la zone (réseau public ALL'Fibre), FTTO livrable — devis en cours |
| Risques | pas de PPR, pas de pollution répertoriée, pas de termites, sismicité faible |
| Distance | **150 km de Toulouse**, soit 2 à 3 ms de latence |

### Le propriétaire et la valeur

| Élément | Donnée |
|---|---|
| Propriétaire | SCI JIDÉ (SIREN 839 361 771), gérant Jacques Delbès |
| Acquisition | **275 000 €** en juillet 2018 |
| Estimation notariale 2026 | **400 000 à 650 000 €** — le père demandera vraisemblablement 650 000 € |
| Prix de transaction réaliste | **450 000 à 550 000 €** |
| Ancien loyer | 3 500 €/mois, qualifié par le père de « très bas » |
| Offre du BTP | **toujours inconnue** — c'est la seule vraie référence à battre |

### Le passif documenté — environ 61 000 à 119 000 € TTC

| Poste | Montant | Statut |
|---|---|---|
| Mise en conformité assainissement | **21 692 € TTC** | **Obligatoire.** Contrôle Veolia du 25/06/2026 : non conforme, délai « immédiat » |
| Retrait de l'amiante seul | ~39 400 € TTC | Pas obligatoire aujourd'hui, mais toute la toiture (518 m²) est en fibres-ciment |
| Retrait + couverture neuve isolée | **97 140 € TTC** | Devis existant de mai 2026 |

> Ce passif explique l'écart entre les 650 000 € affichés et les 450-550 000 € réalistes. C'est un argument de négociation **documenté par des tiers** — ce n'est pas Charles qui le dit, c'est Rodez Agglomération et un devis de couvreur.

---

## 3. Les deux dernières semaines — ce qui s'est passé

| Date | Événement |
|---|---|
| 13 août | **Mandat Enedis signé** par le père. Premier vrai feu vert. |
| 14 août | Réception des documents du propriétaire : diagnostics, état des risques, devis assainissement, plan de masse |
| 16-17 août | **Kbis à jour obtenu.** Analyse des documents : l'assainissement est **non conforme avec mise en conformité immédiate**, et toute la toiture est amiantée |
| 17 août | **Demande de raccordement déposée chez Enedis** (réf. dossier RACNMP26005657), 1 000 kW en champ structuré, 2 MW demandés en commentaire |
| 17 août | **Rappel du chargé de projet Enedis le jour même.** Il requalifie le dossier : devis gratuit au lieu de l'étude payante, pas de permis nécessaire, puissance portée à **2 MW**, visite sur site à programmer |
| 18-25 août | Benchmark des acteurs de l'amont : développeurs de *powered land*, contractants généraux, constructeurs modulaires, bureaux d'études, opérateurs edge. E-mails préparés pour DATALLIANCE et CBRE |
| 26 août | **Appel Datalok** — voir section 4 |

### Ce qui a changé le produit

Au départ, la cible était 1 MW sur un terrain à viabiliser. Aujourd'hui, l'offre est différente et bien meilleure :

> **2 MW raccordables, dans un bâtiment qui existe déjà, sans permis de construire à obtenir, avec un dossier Enedis ouvert et un chargé de projet nommé.**
>
> Ce n'est pas un produit immobilier, c'est **un produit de délai**. En France en 2026, les délais de raccordement pour les grands sites vont de 2 à 7 ans. Ici, on parle de mois.

---

## 4. L'appel Datalok du 26 août — le point central

Datalok est une **place de marché** de data centers (63 sites référencés, 115 MW), fondée en 2016. Interlocuteur : **Jules Martin**. L'échange était enregistré, un compte rendu écrit doit arriver.

### Ce qui a été validé

| Question | Réponse |
|---|---|
| Un site de 2 MW, est-ce viable ? | **« Ça commence à être petit, mais c'est faisable. »** Le seuil n'est donc pas rédhibitoire |
| L'Aveyron est-il disqualifiant ? | **Non.** Pas de point bloquant particulier |
| Le modèle « terrain viabilisé, revendu à un investisseur qui construit » ? | **Confirmé comme un modèle de marché réel** — ce n'était jusque-là qu'une hypothèse maison |

### Le vrai enseignement : la demande doit être LOCALE

C'est la phrase la plus importante de l'appel : **il faut trouver des clients locaux.** Datalok suggère de passer par la **CCI**.

Cela réoriente tout le projet. Jusqu'ici, la stratégie visait des acteurs nationaux — opérateurs edge, fonds fonciers, développeurs. Or l'analyse avait déjà montré qu'ils ne descendent pas à 2 MW, ou qu'ils rachètent des data centers en exploitation plutôt que du terrain nu. Datalok apporte la pièce manquante :

> À cette échelle, **ce n'est pas l'offre qui déclenche, c'est la demande.**
>
> La chaîne réelle est : **demande locale démontrée, puis confiance de l'investisseur, puis valeur du foncier.**
>
> Un terrain raccordé sans client identifié ne vaut presque rien. Le même terrain avec deux ou trois clients locaux pré-identifiés devient un projet finançable.

### Ce qui n'a pas été obtenu

- **L'ordre de grandeur en euros par MW.** Refusé — c'est précisément ce que Datalok vend.
- **Qui finance le raccordement** dans les opérations qu'ils voient passer. Question posée depuis trois semaines, toujours sans réponse.
- **Le second modèle de montage.** Deux modèles ont été évoqués, un seul a été retenu clairement.
- **Le référencement du site** sur la marketplace.

### La proposition commerciale : 4 000 €

Datalok propose une prestation de conseil à **4 000 €**. Charles la trouve chère. Position retenue pour l'instant : **ne pas payer maintenant**, pour trois raisons.

1. Ce n'est pas la contrainte du moment. L'appel vient d'établir que le facteur limitant est **la demande locale**, pas la valorisation.
2. **Le chiffrage Enedis n'est pas revenu.** Une valorisation faite sans le coût de raccordement repose sur une hypothèse, pas sur une donnée.
3. La même information est demandée gratuitement ailleurs — CBRE et APL Data Center.

Si la prestation devait être engagée plus tard, une question doit être posée : **ces honoraires sont-ils imputables sur une commission en cas de transaction ?** C'est la pratique courante en intermédiation.

### Les cibles locales à instruire

**Prescripteurs, à faire en premier :** CCI Aveyron, Rodez Agglomération (développement économique), Ad'Occ (agence régionale d'Occitanie), agence d'attractivité départementale.

**Clients finaux possibles :** RAGT (semences, siège à Rodez), Bosch (Onet-le-Château), Unicor et Sévéal, **Centre Hospitalier de Rodez** (données de santé, hébergement HDS, forte contrainte réglementaire), collectivités, et surtout **les infogéreurs aveyronnais** qui hébergent aujourd'hui à Toulouse — ceux-là ont déjà le besoin et paient déjà.

> **Ordre de grandeur à ne pas perdre de vue :** aucun de ces acteurs ne consomme 2 MW. Chacun pèse **50 à 300 kW**. Le modèle n'est donc pas « un client », mais **un client-ancre plus de la colocation**, avec un remplissage progressif.

---

## 5. Ce qui est acquis — à ne pas re-démontrer

1. **Le site est techniquement bon.** Puissance, fibre, zone d'activités, terrain déjà artificialisé, altitude favorable au free cooling. Le risque n'est pas là.
2. **Le marché du foncier data center ne descend pas naturellement à 2 MW.** Les fonds de *powered land* travaillent sur 10 à 150 hectares et des dizaines de MW.
3. **Les opérateurs edge grandissent par rachat d'actifs en exploitation, pas par achat de terrain.** nLighten, Etix, UltraEdge : même schéma. Leur avantage compétitif est précisément de ne pas construire.
4. **La survaleur d'un terrain raccordé se calcule par le coût évité, pas par un multiple.** Ordre de grandeur : **+150 000 à +400 000 €** en valeur absolue. Sur une base de 650 000 €, cela donne un multiple de 1,23 à 1,6 — **pas un doublement**.
5. **L'angle le plus fort de Rodez : site de repli et de reprise d'activité pour Toulouse.** 150 km, au-delà du seuil de 50-100 km qu'exigent les plans de continuité, et 2 à 3 ms — compatible avec de la réplication synchrone.
6. **Le meilleur montage identifié à ce jour : la marge de développement via une promesse unilatérale de vente** au prix demandé par le père, revendue ensuite — sans capital mobilisé.

---

## 6. Ce qu'on ne sait toujours pas

| Question ouverte | Pourquoi c'est important |
|---|---|
| **Qui finance le raccordement ?** | **LA question du projet.** Si l'exploitant paie, le montage tient. Si Charles doit avancer 100 à 300 k€ pour un gain médian de 165 k€, il ne tient pas |
| Combien coûte réellement le raccordement 2 MW ? | Le chiffrage Enedis arrive. Risque principal : un renforcement de ligne |
| Le raccordement est-il **transférable** à un repreneur ? | Si non, tout le modèle de revente s'effondre. À confirmer par écrit |
| Combien vaut un MW raccordé, en euros ? | Aucune référence obtenue à ce jour |
| Le bâtiment est-il **convertible** en data center ? | Question ouverte depuis mi-août. Les bureaux et sanitaires existants sont un atout ; la toiture amiantée un passif |
| Quel est le montant de l'offre du BTP ? | La seule référence à battre, toujours inconnue |
| Y a-t-il une demande locale réelle ? | **Nouveau chemin critique depuis l'appel Datalok** |

---

## 7. Les actions en cours

### Cette semaine
- E-mail de suivi à Jules Martin, pour récupérer gratuitement les questions restées sans réponse
- **Appeler la CCI Aveyron** et **Rodez Agglomération** — nouveau chemin critique
- Envoyer les e-mails à **DATALLIANCE** et **CBRE**, qui apportent justement la référence en euros que Datalok refuse de donner
- Récupérer la facture d'électricité auprès de Frédéric Legrux (entreprise occupante) pour obtenir le **numéro de PRM**

### Dans les deux semaines
- **Visite Enedis sur site** — questions clés : à partir de quand la capacité est-elle réservée, quel acompte, le raccordement est-il transférable, existe-t-il un palier de puissance sans renforcement
- Appels à **APL Data Center** et **Cap Ingelec** — ce sont eux qui savent dire si le bâtiment est convertible
- Premiers contacts avec RAGT, Bosch Rodez, le Centre Hospitalier
- Devis fibre FTTO auprès de trois opérateurs

### À ne pas faire
- Payer les 4 000 € avant le chiffrage Enedis
- Acheter ou faire chiffrer un transformateur : il est en aval du point de livraison, c'est le budget de l'exploitant, pas celui du porteur de foncier
- Accepter la proposition de raccordement Enedis tant que la question « qui paie » est sans réponse
- Parler à Tenergie avant d'avoir déclaré le conflit d'intérêts par écrit

---

## 8. Sujets à explorer — le cœur de la conversation

Voici les huit sujets sur lesquels Charles veut avancer. **Prends-en un seul à la fois**, pose-lui une question d'ouverture, et challenge ses réponses.

### 8.1 Comment démontrer une demande locale sans budget et sans mandat ?

C'est devenu la question numéro un. Tension : Charles ne possède pas le terrain, n'a pas de mandat de commercialisation, ne peut rien promettre à un client, et n'a pas de budget d'étude. **Quel est l'artefact minimum qui prouve une demande ?** Une lettre d'intention non engageante ? Un sondage via la CCI ? Un atelier avec Rodez Agglomération ?

### 8.2 Quel pitch pour un client local qui n'a jamais envisagé la question ?

RAGT, Bosch ou l'hôpital hébergent aujourd'hui en interne ou à Toulouse. Ils n'ont rien demandé. **Quelle est la vraie douleur ?** Piste la plus prometteuse : leur salle serveur interne vieillit et ils ne la reconstruiront pas. La souveraineté et le plan de reprise sont d'autres angles. Le prix, en revanche, est probablement un mauvais argument.

### 8.3 Quel montage juridique permet d'avancer sans capital ?

Promesse unilatérale de vente, bail emphytéotique, société de projet, simple mandat ? Tension : le père veut vendre vite, Charles n'a pas d'argent, et il faut que le père soit protégé si le projet échoue. **Le modèle EDF — appel à manifestation d'intérêt puis bail emphytéotique de longue durée — est-il transposable à cette échelle ?**

### 8.4 Que faire si le raccordement coûte 300 000 € ?

C'est le scénario défavorable. Options : redescendre à un palier de puissance inférieur qui éviterait un renforcement, faire porter le coût par l'exploitant, basculer vers la location, ou arrêter. **Comment décider, et à quel moment ?**

### 8.5 Que vend-on exactement : du foncier, du délai, ou un service ?

Le positionnement détermine qui paie et combien. Un terrain se vend une fois. Un délai se valorise auprès de qui est pressé. Un service — un site opéré — génère un revenu récurrent mais suppose un métier que Charles n'a pas. **Où est la bonne place sur ce curseur ?**

### 8.6 Comment gérer le calendrier du père ?

Il commercialise maintenant, avec des prospects BTP identifiés. Charles a besoin de six mois. Son père veut avant tout **la tranquillité**, pas le rendement. **Que peut-on lui offrir qui ne lui coûte rien** — par exemple une promesse à son prix, qui le sécurise pendant que Charles cherche mieux ?

### 8.7 Tenergie : opportunité ou conflit d'intérêts ?

Charles envisage de proposer le projet à son employeur comme investisseur. C'est légitime, mais son employeur investirait dans un actif détenu par sa famille, sur un dossier qu'il a monté lui-même. **L'ordre compte** : déclaration écrite à la hiérarchie d'abord, aucune ressource de l'entreprise utilisée côté personnel, retrait de l'instruction si le dossier y est examiné. Fait dans cet ordre, c'est une opportunité. Dans l'autre, c'est un problème professionnel sérieux.

### 8.8 Quels seraient les critères honnêtes d'arrêt ?

Un projet familial est difficile à arrêter. **Quels signaux devraient conduire Charles à renoncer sans regret ?** Définir ces critères maintenant, à froid, vaut mieux que de les découvrir dans six mois.

---

## 9. Pièges à éviter — erreurs déjà commises

Ces erreurs ont déjà été faites et corrigées. Ne les reproduis pas.

| Erreur | La réalité |
|---|---|
| Sous-estimer la valeur du bien | Le bâtiment avait été valorisé à 200-400 €/m². Le marché de l'entrepôt à Rodez tourne autour de **855 €/m²**, ce qui explique les 400-650 k€ du notaire |
| Sur-corriger sur l'amiante | Après avoir sur-estimé le passif, il a été **sous-estimé à tort**. Vérité : classement liste B, aucun retrait exigé aujourd'hui, **mais toute la toiture est amiantée** et le retrait coûte environ 33 000 € HT |
| Annoncer un multiple de 2 au père | Aucune analyse ne le soutient. La méthode du coût évité donne **1,23 à 1,6** |
| Viser UltraEdge comme acheteur | Leur modèle consiste précisément à **ne pas** acheter de foncier |
| Confondre le poste de livraison et le transformateur | Le transformateur est en aval du point de livraison : **c'est le budget de l'exploitant** |

> **La leçon transversale : ne jamais donner un chiffre de valorisation sans l'ancrer sur une référence de marché vérifiée.** Charles transmet ces chiffres à son père. Une erreur coûte de la crédibilité familiale, qui est l'actif le plus précieux du projet.

### Trois contraintes permanentes

1. **Ne jamais impliquer Tenergie** dans un contact extérieur, ni laisser croire que l'entreprise porte le dossier. Le conflit d'intérêts n'est pas encore traité.
2. **Le père n'est pas un adversaire de négociation.** Toute formulation qui ressemble à « faisons du business ensemble » est contre-productive. Son moteur est la tranquillité.
3. **Ne jamais surestimer publiquement la capacité électrique.** Les 2,5 MW indiqués sur la carte Enedis sont **indicatifs, hors file d'attente, et non réservés**. Le dire autrement décrédibilise immédiatement face à un professionnel.
"""
