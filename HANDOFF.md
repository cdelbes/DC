# HAND-OFF — Projet « Data center Rodez » (parcelle ZA Bel-Air, Aveyron)

> **Document de transfert autonome.** Il est écrit pour être lu par un **nouvel assistant
> qui ne connaît rien du dossier**, sur un autre compte Claude. Il contient tout le
> contexte, les données maîtresses, les conclusions, **les erreurs déjà commises et
> corrigées**, les contraintes à respecter et les prochaines actions.
>
> **Date de rédaction : 17 août 2026.** Dépôt : `cdelbes/dc`, branche
> `claude/data-center-aveyron-feasibility-atkkuu`.

---

## 0. Message d'amorçage pour le nouvel assistant

*Copier-coller ceci dans la première conversation du nouveau compte, avec le dépôt (ou
l'archive) attaché :*

> Je reprends un projet personnel en cours : évaluer la faisabilité d'un data center sur une
> parcelle familiale à Rodez (Aveyron), détenue par la SCI de mon père, qu'il s'apprête à
> vendre à une entreprise du BTP. Tout l'historique est dans le dépôt joint. **Lis d'abord
> `HANDOFF.md`, puis `docs/21`, `docs/27` et `docs/28`** — ce sont les trois documents les
> plus à jour. Les docs 01 à 20 sont antérieurs et partiellement corrigés par les suivants :
> en cas de contradiction, **le document au numéro le plus élevé fait foi**.
> Ne reproduis pas les erreurs listées au §7 du hand-off.

---

## 1. Qui, quoi, pourquoi

| | |
|---|---|
| **Porteur** | Charles DELBÈS — charles@delbes.co |
| **Métier** | Développeur de projets EnR chez **Tenergie** (le projet Rodez est un **side project personnel**, hors Tenergie) |
| **Propriétaire du foncier** | **SCI JIDÉ**, gérée par **Jacques DELBÈS** (son père) |
| **Objet** | Déterminer si la parcelle vaut plus en « foncier data center » qu'en vente au BTP, et à quelles conditions |
| **Contrainte de temps** | Le père **commercialise la parcelle sous un mois** (à compter de mi-août 2026), prospects BTP déjà identifiés |
| **Référence méthodologique** | Projet **Next Compute** (mini data centers Policloud sur sites PV) — JV envisagée avec Tenergie |

### L'enjeu en une phrase

Obtenir du propriétaire **du temps** (≈ 6 mois) pour tester si un acteur du data center
paierait le foncier plus cher qu'un acheteur BTP — sans immobiliser de capital et sans
mettre en risque la relation familiale.

---

## 2. ⛔ Contraintes permanentes à respecter

1. **Le document interne Tenergie sur Next Compute ne doit JAMAIS être versionné** dans le
   dépôt. L'utilisateur a explicitement refusé sa copie (deux fois). Toutes les références
   dans les docs le mentionnent comme « document interne Tenergie, non versionné ». **Ne pas
   revenir dessus.**
2. **Conflit d'intérêts potentiel avec Tenergie** : le sujet n'est pas tranché. Ne rien
   publier, ni contacter d'acteur, en laissant croire que le projet est porté par Tenergie.
3. **Le père est le point de fragilité du projet, pas un adversaire de négociation.** Son
   moteur est la **tranquillité**, pas le rendement (voir doc 25). Toute formulation qui
   ressemble à « faisons du business ensemble » est contre-productive.
4. Le fichier `roi_calculator.xlsx` de Policloud et le BP Next Compute
   (`Next_Compute_P100_BP_v14.4.xlsx`) **ne sont pas dans le dépôt** — seules leurs analyses
   le sont (docs 09 et 16).

---

## 3. Données maîtresses du site

*(source de vérité machine : `data/site.yml`)*

### Localisation

| | |
|---|---|
| Adresse | **35 rue de la Ferronnerie, ZA de Bel-Air, 12000 Rodez** |
| GPS | **44.37295358345457, 2.5444548605206823** |
| Parcelle cadastrale | **12202000BH0187** (section **BH n° 187**, INSEE 12202) |
| Surface parcelle | **2 631 m²** — dont **2 144 m² libres** |
| Altitude | **586 m** (favorable au free cooling) |
| Zone PLU | attendue **UX** — PLUi Rodez Agglomération `DU_241200187` — **à confirmer au GPU** |
| Statut fiscal | **AFR + ZRR** à confirmer pour la partie Rodez |

### Bâtiment existant ⭐

**Ce n'est PAS un simple hangar** — point crucial, source d'une erreur initiale.

| | |
|---|---|
| Type | **bâtiment industriel avec étage de bureaux aménagés** |
| Emprise au sol | **487 m²** · hauteur 4-6 m |
| Année de construction | **1989 – 2000** |
| Surface chauffée (bureaux) | **154 m²** · DPE 192 kWhEP/m².an · 6 kg éqCO₂/m².an |
| Étage | entrée, accueil, 3 bureaux, archives, salle de réunion, réserve |
| RDC | WC, magasin, stockage, dépôt |
| **Amiante** | Couverture plaques fibres-ciment. **Liste B, classement EP — aucun retrait obligatoire *aujourd'hui*.** ⚠️ Mais le devis DELBES SAS chiffre **518,50 m² à déposer = toute la toiture** : **32,8 k€ HT** le retrait seul, **97 140 € TTC** avec couverture neuve isolée. Retrait **obligatoire dès qu'on touche au toit**. *(doc 30 — corrige le doc 28)* |
| Termites | absence |
| Démolition | **non prévue** — la **piste réhabilitation est l'hypothèse de tête** |

### Risques (ERP du 18/06/2026)

Aucun PPR · sismicité 2 (faible) · **pas de secteur d'information sur les sols** · radon
niveau 3 (à traiter en ventilation, enjeu faible pour un DC) · pas de débroussaillement.
**Aucun risque bloquant.**

### Réseau électrique (relevé cartographie Enedis)

| Tronçon HTA | Distance | Capacité conso indicative |
|---|---|---|
| GPS 44.3741348133494, 2.5473038346853905 | **260 m** | **2,5 MW** |
| — | **800 m** | **3,4 MW** |

**Puissance cible retenue : 1 MW** (~50 % de la capacité du départ le plus proche —
hypothèse prudente). ⚠️ Ces capacités sont **indicatives** (carte mensuelle, hors file
d'attente) et **non réservées**.

- **PRM/PDL : toujours inconnu.** 🎯 **Meilleure piste : DELBES SAS**, l'entreprise de
  couverture/étanchéité **occupante du bâtiment** (SIRET 427 280 508 00024) — c'est elle qui
  détient le contrat d'électricité. **05 65 42 53 50 · contact@delbes-aveyron.fr ·
  LEGRUX Frédéric**. Piste secondaire : le diagnostiqueur Lilian GAU, Cabinet AGENDA,
  06 88 94 97 77.
- Consommation actuelle du site : **15 595 kWh en 2025**, abonnement 144 € → site en **BT**.
- **Caparéseau ne sert à rien ici** : il ne cartographie que l'**injection**, pas le
  soutirage.

### Fibre

FTTH présente dans la ZA (RIP **ALL'Fibre**), **FTTO livrable**. Statut 🟢 — ce n'est pas un
point bloquant (doc 11).

---

## 4. Le propriétaire et la SCI

| | |
|---|---|
| Dénomination | **SCI JIDÉ** |
| SIREN / SIRET | **839 361 771** / **839 361 771 00026** |
| RCS | Rodez, immatriculée le **04/05/2018** · capital **1 000 €** |
| Siège | **9 rue Paraire, Le Grand Balcon, 12000 Rodez** *(le 35 rue de la Ferronnerie est un bien LOUÉ, pas un établissement — corrigé par le Kbis 2026)* |
| Gérant | **DELBÈS Jacques, Gérard, Pierre-Marie**, né le 15/08/1961 à Rodez |
| Objet social | acquisition, administration et **exploitation par bail, location ou autrement** → *la SCI est statutairement outillée pour louer, aucun changement d'objet nécessaire* |
| Kbis | ✅ **à jour au 16/08/2026** (`documents/Kbis-SCI-JIDE-2026-08-16.pdf`), code de vérification `kjVyFadFxT` |

### Chiffres financiers connus

| | |
|---|---|
| **Acquisition** | **275 000 €** le 19/07/2018 (≈ 104,5 €/m² de terrain — dans le marché de l'époque) |
| **Valorisation notariale 2026** | **400 000 à 650 000 €** — il demandera vraisemblablement **650 000 €** |
| Prix de transaction probable | **450-550 k€** (650 k€ est un prix d'affichage) |
| **Ancien loyer** | **3 500 €/mois** (42 000 €/an), qualifié par lui de « très bas » |
| Offre BTP | ⚠️ **TOUJOURS INCONNUE — c'est la seule vraie référence à battre** |
| **Assainissement** | 🔴 **OBLIGATOIRE** — contrôle Veolia/Rodez Agglo du 25/06/2026 : **NON CONFORME**, délai de mise en conformité **immédiat**. Devis PUECHOULTRES **18 076 € HT / 21 691 € TTC** |
| **Passif documenté total** | **61 000 à 118 800 € TTC** (assainissement + amiante) → le prix de transaction réaliste tombe à **530-555 k€** |

### Mandat Enedis ✅

**Signé par les deux parties le 13/08/2026 à Rodez.** Mandat **simple** de représentation
(aucun pouvoir de signature ni de paiement). Mandant : SCI JIDÉ représentée par Jacques
DELBÈS. Mandataire : Charles DELBÈS, 33 avenue Henri Malacrida, 13100 Aix-en-Provence.
Fichier prêt à joindre : **`documents/Mandat-Enedis-SIGNE-COMPLET.pdf`** (6 pages, champs
aplatis, page 5 = page signée scannée).

---

## 5. Les conclusions stratégiques du dossier

*(à ne pas re-démontrer — elles sont acquises)*

1. **Le site est techniquement bon.** Puissance, fibre, zone d'activités, terrain déjà
   artificialisé, altitude. **Le risque n'est pas là.**

2. **Le marché du « powered land » existe en France, mais pas à 1-2 MW.** Les acteurs
   (Hadès Patrimoine, Datalok, EDF, Altarea, les 35 sites de l'État) travaillent sur
   18-150 ha. Les acteurs edge (UltraEdge) grandissent **par rachat d'actifs en
   exploitation, pas par achat de terrain** — leur avantage compétitif est précisément de
   **ne pas acheter de foncier** (doc 19). *(doc 14 ⭐, révise les docs 10 et 13)*

3. **La survaleur RTB se calcule par le coût de remplacement, pas par un multiple.**
   Ordre de grandeur : **+150 à +400 k€** en valeur **absolue**. Sur une base de 650 k€,
   cela donne **×1,23 à ×1,6** — **pas ×2**.

4. **🔴 Le point décisif : QUI PAIE LE RACCORDEMENT ?**
   Si l'acquéreur/exploitant le finance, le montage tient. Si Charles doit avancer
   100-300 k€ pour un gain médian de ~165 k€, **le RTB pur ne vaut pas la peine** → il faut
   basculer vers le bail ou l'exploitation. *(doc 21 ⭐)*

5. **Le bâtiment est un actif pour un acheteur BTP (+244 à +416 k€) et un passif pour un
   data center greenfield (démolition).** D'où le basculement vers la **réhabilitation**.
   ⭐ **Question n° 1 à poser aux professionnels** : *« un bâtiment industriel de 487 m² au
   sol, 1989-2000, avec 154 m² de bureaux à l'étage, est-il convertible en data center de
   500 kW-1 MW, ou faut-il systématiquement du neuf ? »*

6. **Meilleur montage identifié : la marge de développement via une promesse unilatérale de
   vente** au prix demandé par le père, revendue ensuite — **aucun capital mobilisé**.

7. **Le meilleur angle commercial de Rodez : site de PRA / DR pour Toulouse.** 150 km
   (au-delà de la règle des 50-100 km), 2-3 ms de latence → **compatible réplication
   synchrone** (< 10 ms). La latence n'est **pas** un obstacle ; les 6 vraies barrières sont
   ailleurs (doc 22).

8. **Argument carbone solide et vérifié** : 19,6 gCO₂/kWh en France 2025 contre ~420 g en
   Virginie = **×21,4 exactement**. La France a exporté 92,3 TWh en 2025 (doc 17).

9. **Marché français** : 0,7-1,1 GW aujourd'hui → **2,3 GW en 2030**, avec **18 GW déjà
   réservés au RTE**. La croissance est **centralisée en puissance** mais **déconcentrée
   géographiquement** (doc 18).

10. **BP Next Compute (JV Tenergie) — critique** : Next Compute apporte 67 € pour 67 % et
    perçoit 255 974 € de dev fee ; Tenergie apporte 957 275 € pour 33 %. La couverture
    affiche 34,1 % de TRI mais **le TRI réel de Tenergie est de 25,3 %**. La ligne « IS
    total payé » pointe sur le résultat net. Le RPM n'a **aucun plancher**. Sensibilités
    jusqu'à 13,6 % (doc 16).

---

## 6. Index des 28 documents

> **Règle de lecture : en cas de contradiction, le numéro le plus élevé fait foi.**

| # | Fichier | Conclusion en une ligne |
|---|---|---|
| 01 | `contexte-projet` | Contexte, parties prenantes, 3 postures (acheter / louer / partager) |
| 02 | `raccordement-enedis` | Méthode Enedis ; Caparéseau = injection seulement |
| 03 | `typologie-data-centers` | Scénarios A (edge 100-300 kW) à D (HPC/IA) |
| 04 | `urbanisme-reglementaire` | Seuils DP/PC, ICPE 2925/2910/F-gaz |
| 05 | `business-plan-trame` | Structure du BP |
| 06 | `etude-urbanistique-site` | Étude du site — verdict 🟢 |
| 07 | `certificat-urbanisme-guide` | Guide CUb, Cerfa 13410*13, note descriptive modèle |
| 08 | `preetude-raccordement-enedis` | Guide pré-étude + 7 questions à poser à Enedis |
| 09 | `analyse-roi-policloud` | Décryptage du calculateur Policloud ; ⚠️ électricité = 0 € et 45 kW sous-évalués |
| 10 | `strategie-rtb-powered-land` | Concept RTB — **corrigé par le doc 14** |
| 11 | `connectivite-fibre-site` | Fibre OK 🟢 |
| 12 | `acheteurs-partenaires-clients` | 3 familles A/B/C — **UltraEdge déclassé par le doc 19** |
| 13 | `etude-valeur-fonciere-btp-vs-datacenter` | **Corrigé deux fois** (docs 14 et 20) |
| 14 | ⭐ `etude-marche-powered-land-france` | Le marché existe mais **pas à 1-2 MW** ; méthode du coût de remplacement (+150-400 k€) |
| 15 | `pitch-contact-marche` | Pitchs de contact |
| 16 | `evaluation-bp-next-compute` | Critique de la JV — TRI Tenergie réel 25,3 % |
| 17 | `argument-carbone-localisation` | Fact-check du post Gorintin — ×21,4 exact |
| 18 | `etude-marche-deploiement-datacenters-france` | 2,3 GW en 2030 ; centralisé en puissance, déconcentré en géographie |
| 19 | `fiche-ultraedge` | EV 764 M€, ~29× EBITDA, 250 sites/51 MW — **évite explicitement le greenfield** |
| 20 | `benchmark-valeur-foncier-rodez` | **Corrigé par le doc 27** (valeur sous-estimée) |
| 21 | ⭐ `plan-lancement-test-rapide` | Tester en 6-8 semaines pour ~0 € ; **« QUI PAIE LE RACCORDEMENT ? »** |
| 22 | `pourquoi-la-localisation-compte` | Latence non-sujet ; **Rodez = site PRA idéal pour Toulouse** |
| 23 | `emails-hades-fullsave` | E-mails prêts + contacts + préparation appel Datalok |
| 24 | ⭐ `guide-pratique-demande-enedis` | Accord du propriétaire = prérequis ; §3bis cadrage « augmentation de puissance » |
| 25 | ⭐ `preparation-conversation-pere` | Reframe **tranquillité** ; ne jamais dire « faisons du business ensemble » |
| 26 | `mandat-enedis-et-option-location` | Mode d'emploi du mandat + analyse de l'option location |
| 27 | ⭐ `apres-conversation-pere-recalage` | Recalage post-déjeuner : 400-650 k€, « ×2 » à corriger, piste réhabilitation |
| 28 | ⭐ `analyse-documents-proprietaire` | Amiante limité, pas de PPRi, bâtiment avec bureaux |
| 29 | ⭐ `apres-appel-enedis-preparation-rdv` | Préparation du RDV Enedis (12 questions) ; le transfo n'est PAS ton périmètre ; cibles marché 2 MW (nLighten, PRA toulousain) |
| 30 | ⭐ `passif-chiffre-kbis-assainissement-amiante` | Kbis OK ; assainissement **non conforme, délai immédiat** ; toiture amiantée sur 518 m² ; passif 61-119 k€ |

### Autres livrables

| Chemin | Contenu |
|---|---|
| `deck/Deck-Foncier-Bel-Air.pptx` | Deck de négociation (14 slides) — généré par `deck/build_deck.js` (pptxgenjs) |
| `documents/Mandat-Enedis-SIGNE-COMPLET.pdf` | ✅ Mandat signé fusionné, prêt pour Enedis |
| `documents/Mandat-Enedis-PRE-REMPLI.pdf` | Version pré-remplie non signée (archive) |
| `analyse/nc_model_sensibilites.py` | Reconstruction Python du modèle Next Compute — **reproduit le fichier à l'euro près** |
| `scripts/fill_mandat.py` | Remplissage du PDF Cerfa Enedis (PyMuPDF) |
| `scripts/get_parcelle.py`, `scripts/fetch_maps.py` | Récupération cadastre / cartes |
| `data/site.yml` | **Fiche site machine-readable — source de vérité** |
| `data/vertiv-megamod-specs.md` | Specs modulaire Vertiv |

---

## 7. ⚠️ Erreurs déjà commises et corrigées — à NE PAS reproduire

| # | Erreur | Réalité | Corrigé dans |
|---|---|---|---|
| 1 | Bâtiment valorisé à **200-400 €/m²** → valeur totale 215-380 k€ | L'entrepôt à Rodez tourne à **~855 €/m²** → **400-650 k€** confirmés par notaire | doc 27 |
| 2 | Amiante estimé à **25-55 k€**, toute la toiture — puis **révisé à la baisse à tort** au doc 28 | **L'estimation initiale était bonne** : devis réel **32,8 k€ HT / 39,4 k€ TTC** pour le retrait seul, sur **518,50 m² = toute la toiture**. Le classement EP (aucun retrait exigé aujourd'hui) reste juste. ⚠️ **Ne pas sur-corriger dans un sens ni dans l'autre.** | doc 30 |
| 3 | Supposé un **hangar nu de 900-1 100 m²** | **487 m² d'emprise**, bâtiment industriel **avec étage de bureaux** | doc 28 |
| 4 | **UltraEdge** présenté comme cible n° 1 | Leur modèle **évite délibérément le greenfield** — mauvaise cible pour vendre du terrain | doc 19 |
| 5 | Multiple RTB **×2** annoncé au père | **×1,23 à ×1,6** sur une base de 650 k€ (méthode coût de remplacement) | docs 14, 27 |
| 6 | Facteur carbone ×20 qualifié de « haut de fourchette » avant lecture du post | Le chiffre était **exact** (420/19,6 = 21,4) | doc 17 |

**Leçon transversale : ne pas donner de chiffre de valorisation sans l'ancrer sur une
référence de marché locale vérifiée.** Le porteur transmet ces chiffres à son père — une
erreur coûte de la crédibilité familiale, qui est l'actif le plus précieux du projet.

### Contraintes techniques d'environnement rencontrées

- Proxy en **403** sur : `data.enedis.fr`, GPU / apicarto, LinkedIn, `hades-patrimoine.com`,
  `fullsave.com` → contourner par **WebSearch**.
- **LibreOffice indisponible** → impossible de rendre le `.pptx` pour un contrôle visuel.
  Le signaler honnêtement plutôt que d'affirmer que le deck est correct.
- PDF Cerfa Enedis : boutons radio malformés (états « on » dupliqués) → écrire
  `w.field_value` **widget par widget**, puis `doc.bake()` pour aplatir.

---

## 8. État d'avancement au 17/08/2026

### ✅ Fait

- Mandat Enedis **signé** (13/08/2026) et fusionné en PDF prêt à déposer
- Conversation avec le père tenue : accord pour étudier, mandat obtenu, valorisation
  notariale connue
- Documents du propriétaire récupérés et analysés (diagnostics, ERP, Kbis, devis
  assainissement, plan de masse)
- Brouillons Gmail créés pour **Hadès Patrimoine** et **FullSave**
- Appel **Datalok** calé au **26 août 2026**
- 28 documents d'analyse + deck de négociation + modèle financier Next Compute reconstruit

### 🔜 Actions immédiates

1. ~~Kbis récent~~ ✅ **fait** (16/08/2026).
2. **Déposer la demande Enedis** via l'entrée **« Un site industriel en HTA »** sur
   `raccordement-entreprise-enedis.fr`.
   - La pré-étude gratuite **n'apparaît pas** sur le parcours consommateur HTA — c'est
     normal, c'est surtout un produit producteur. **Appeler Enedis avant de valider** pour
     confirmer si l'étude est facturée.
   - **Déposer n'engage à rien** : seule l'acceptation de la PTF engage (original signé +
     acompte 5-10 %, 3 mois de validité).
   - Demander **deux paliers : 1 MW et 2 MW**.
   - Pièces : mandat signé, Kbis récent, plan de masse.
3. **Récupérer le PRM** → appeler **DELBES SAS, 05 65 42 53 50**, l'occupant du bâtiment.
4. **Envoyer les e-mails** Hadès Patrimoine et FullSave — ⚠️ adresses **non vérifiées**,
   numéro de téléphone en **placeholder** à compléter. Relance prévue **25-28 août**.
5. **Appel Datalok le 26 août** — question n° 1 : **convertibilité du bâtiment** ;
   question n° 2 : **qui paie le raccordement**.
6. **Recalibrer auprès du père** : le « ×2 » **et** le poids du passif amiante (les deux ont
   été présentés de façon erronée).
7. **Obtenir le montant de l'offre BTP** — sans ce chiffre, aucun comparatif n'est possible.

### ❓ Questions ouvertes

- ~~Assainissement obligatoire ?~~ ✅ **tranché : obligatoire, délai immédiat**
- Les **518,50 m²** du devis amiante couvrent-ils toute la toiture ? *(incohérence avec le diagnostic — doc 30 §3)*
- Quel est le **lien exact entre Jacques DELBÈS et DELBES SAS** (l'occupant) ?
- La **redevance d'assainissement** a-t-elle déjà été majorée ?
- Le bâtiment est-il **convertible** en data center, ou faut-il du neuf ?
- **Qui paie le raccordement** dans un montage réaliste ?
- Zonage PLU exact et statut **AFR/ZRR** → contacter **Rodez Agglomération**
- **RAGT** (agro-semencier rodézien) comme client d'ancrage potentiel — non contacté
- Position vis-à-vis de **Tenergie** (conflit d'intérêts) — non tranchée
- Quel est le **montant de l'offre BTP** ?

---

## 9. Comment reprendre le projet sur un autre compte

1. Cloner ou dézipper le projet, puis vérifier la branche :
   `git checkout claude/data-center-aveyron-feasibility-atkkuu`
2. Lire dans l'ordre : **`HANDOFF.md` → `docs/21` → `docs/27` → `docs/28` → `docs/24`**.
   Le reste à la demande.
3. Charger `data/site.yml` comme source de vérité pour toute donnée chiffrée du site.
4. Respecter les contraintes du **§2** (non-versionnement du document Tenergie, conflit
   d'intérêts, posture vis-à-vis du père).
5. Relire le **§7** avant de produire toute nouvelle estimation de valeur.

### Pièces à re-fournir manuellement au nouvel assistant (non versionnées)

- `roi_calculator.xlsx` (Policloud) — si une analyse plus fine est souhaitée
- `Next_Compute_P100_BP_v14.4.xlsx` — **⚠️ document interne Tenergie, ne pas versionner**
- Dossier de diagnostics n° 0626-022 (Cabinet AGENDA, 18/06/2026)
- Devis assainissement PUECHOULTRES n° 26070129
- Plan de masse du géomètre
- Kbis SCI JIDÉ (à renouveler de toute façon)

---

*Fin du hand-off. Toutes les analyses détaillées sont dans `docs/`.*
