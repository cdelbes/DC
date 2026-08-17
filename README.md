# DC Rodez — Étude de faisabilité d'un data center (Aveyron)

Étude de faisabilité pour l'installation et la construction d'un data center sur une
parcelle située à **Rodez (Aveyron, 12)**, menée en side project adossé à l'expérience
du projet **Next Compute** (mini data centers Policloud sur sites photovoltaïques).

## Contexte

- La parcelle accueille aujourd'hui le **dépôt d'une entreprise de couverture / étanchéité**.
- Le propriétaire actuel (le père du porteur de projet) prévoit de **vendre la parcelle à une
  entreprise du BTP**.
- Objectif de l'étude : produire un **business plan** du projet de data center sur cette
  parcelle, afin d'en discuter avec le propriétaire **avant** la vente — et éventuellement de
  proposer une alternative (ou un complément) à la cession au BTP.

## Objectif final

Un **business plan chiffré** couvrant :

1. La **puissance de raccordement disponible** côté Enedis (soutirage) et son coût/délai.
2. Le **type de data center** adapté au terrain (surface, zone PLU, puissance) : edge
   conteneurisé, modulaire, colocation, HPC/IA.
3. Le cadre **urbanisme / réglementaire** (DP ou permis de construire, ICPE, SDIS).
4. Le **modèle économique** : CAPEX, OPEX, revenus, TRI/VAN/payback par scénario.

## Structure du dépôt

| Dossier / fichier | Contenu |
|---|---|
| `HANDOFF.md` | ⭐ **Document de transfert** — tout le projet en un seul fichier autonome (contexte, données, conclusions, erreurs corrigées, prochaines actions). À lire en premier pour reprendre le dossier. |
| `docs/01-contexte-projet.md` | Contexte, parties prenantes, question à trancher |
| `docs/02-raccordement-enedis.md` | Méthode et état des connaissances raccordement (chemin critique) |
| `docs/03-typologie-data-centers.md` | Types de data centers possibles selon terrain et puissance |
| `docs/04-urbanisme-reglementaire.md` | DP / PC, PLUi, ICPE — adapté de la méthode Next Compute |
| `docs/05-business-plan-trame.md` | Trame du business plan et hypothèses à renseigner |
| `docs/06-etude-urbanistique-site.md` | **Étude urbanistique du site** (ZA Bel-Air, Rodez) + amiante |
| `docs/07-certificat-urbanisme-guide.md` | **Guide CUb** : formulaire, pièces, note descriptive, délais |
| `docs/08-preetude-raccordement-enedis.md` | **Guide pré-étude / raccordement Enedis HTA** |
| `docs/09-analyse-roi-policloud.md` | **Décryptage pédagogique du ROI Calculator Policloud** (business du calcul GPU en chiffres) |
| `docs/10-strategie-rtb-powered-land.md` | **Stratégie RTB / “powered land”** : valoriser le foncier prêt-à-bâtir sans exploiter |
| `docs/11-connectivite-fibre-site.md` | **Vérification fibre du site** (FTTH/FTTO, RIP ALL'Fibre, backbone) |
| `docs/12-acheteurs-partenaires-clients.md` | **Liste acheteurs / partenaires / clients** pour un DC ~1 MW à Rodez |
| `docs/13-etude-valeur-fonciere-btp-vs-datacenter.md` | **Étude de valeur foncière** : vente BTP vs voie data center |
| `docs/14-etude-marche-powered-land-france.md` | **Étude de marché powered land France** ⭐ — le marché existe-t-il à 1-2 MW ? (révise les docs 10 et 13) |
| `docs/15-pitch-contact-marche.md` | **Pitchs de contact** Hadès Patrimoine & Datalok + questions à poser |
| `docs/16-evaluation-bp-next-compute.md` | **Évaluation critique du BP Next Compute** (JV Tenergie) — répartition de la valeur, erreurs, sensibilités |
| `docs/17-argument-carbone-localisation.md` | **Argument carbone & localisation** — fact-check du post Gorintin, fuite carbone, 92 TWh d'exports, formulations prêtes |
| `docs/18-etude-marche-deploiement-datacenters-france.md` | **Étude de marché : déploiement des data centers en France à 3/5/10 ans** — puissances, croissance, centralisé vs décentralisé |
| `docs/19-fiche-ultraedge.md` | **Fiche approfondie UltraEdge** — M&A (EV 764 M€, ~29× EBITDA), portefeuille, datapoles, Occitanie, angle d'approche |
| `docs/20-benchmark-valeur-foncier-rodez.md` | **Benchmark valeur du foncier** — données cadastrales réelles, prix 2018 vs marché, multiple RTB |
| `docs/21-plan-lancement-test-rapide.md` | ⭐ **PLAN D'ACTION** — tester le projet en 6-8 semaines pour ~0 € : qui contacter, dans quel ordre, avec quels arguments |
| `docs/22-pourquoi-la-localisation-compte.md` | **Pourquoi la localisation compte (ou non)** — latence réelle, les 6 vraies barrières, l'angle PRA où Rodez gagne |
| `docs/23-emails-hades-fullsave.md` | **E-mails prêts à envoyer** Hadès Patrimoine & FullSave + coordonnées + préparation de l'appel Datalok |
| `docs/24-guide-pratique-demande-enedis.md` | ⭐ **Guide pas à pas de la demande Enedis** — qui doit être demandeur, mandat SCI, quel compte, pièges à éviter |
| `docs/25-preparation-conversation-pere.md` | ⭐ **Préparation de la conversation avec le propriétaire** — reframe « tranquillité », échelle des demandes, objections |
| `docs/26-mandat-enedis-et-option-location.md` | **Mandat Enedis pré-rempli** (mode d'emploi) + analyse de l'option location |
| `documents/Mandat-Enedis-PRE-REMPLI.pdf` | ⭐ **Mandat Enedis prêt à signer** — champs pré-remplis, cases cochées |
| `docs/27-apres-conversation-pere-recalage.md` | ⭐ **Recalage après la conversation** — valorisation notariale 400-650 k€, le « ×2 » à corriger, piste réhabilitation |
| `docs/28-analyse-documents-proprietaire.md` | ⭐ **Analyse des documents du propriétaire** — amiante limité, pas de PPRi, bâtiment avec bureaux |
| `documents/Mandat-Enedis-SIGNE-COMPLET.pdf` | ✅ **Mandat signé** (13/08/2026) — fusionné, prêt pour Enedis |
| `analyse/nc_model_sensibilites.py` | Reconstruction du modèle Next Compute + tests de sensibilité (reproduit le fichier à l'euro près) |
| `deck/Deck-Foncier-Bel-Air.pptx` | **Deck de négociation** (présentation au propriétaire) |
| `data/site.yml` | Fiche site (GPS, parcelle, zone PLU, réseau HTA…) |
| `data/vertiv-megamod-specs.md` | Synthèse brochure Vertiv MegaMod (0,5–2 MW modulaire) |
| `scripts/` | Pipeline automatisé : cartes IGN, parcelle cadastrale, zonage PLU depuis un point GPS |

> La méthode s'appuie sur le dossier de reprise **Next Compute** (document interne
> Tenergie, non versionné dans ce dépôt).

## État d'avancement

- [x] Cadre méthodologique et structure de l'étude
- [x] Recherche préliminaire raccordement Enedis (procédure, coûts, délais, Caparéseau)
- [x] Typologie des data centers envisageables
- [x] Scripts d'analyse parcellaire prêts (cartes IGN, cadastre, zone PLU)
- [x] Point GPS de la parcelle : 44.372954, 2.544455 — ZA Bel-Air, Rodez
- [x] Étude urbanistique du site (doc 06) — verdict provisoire 🟢, foncier ≈ 2 522 m²
- [x] Candidat technique identifié : Vertiv MegaMod 0,5–2 MW (`data/vertiv-megamod-specs.md`)
- [x] Réseau HTA : ~2,5 MW dispo (conso) et tronçon HTA à ~250 m (cartographie Enedis) — 🟢
- [x] Guide certificat d'urbanisme opérationnel (doc 07)
- [x] Guide pré-étude / raccordement Enedis (doc 08)
- [x] Analyse du modèle économique Policloud (doc 09) — business du calcul GPU expliqué
- [x] Analyse stratégique RTB / powered land (doc 10) — posture recommandée en Phase 1
- [x] Vérification fibre (doc 11) — 🟢 favorable (FTTH présent, RIP ALL'Fibre, FTTO livrable)
- [x] Liste acheteurs / partenaires / clients (doc 12)
- [x] Étude de valeur foncière BTP vs data center (doc 13)
- [x] **Deck de négociation propriétaire** (`deck/Deck-Foncier-Bel-Air.pptx`)
- [x] Étude de marché powered land France (doc 14) — marché réel mais **pas à l'échelle 1-2 MW** ;
      survaleur révisée à **+150-400 k€** (méthode coût de remplacement)
- [x] Pitchs de contact rédigés (doc 15)
- [x] **Plan de lancement (doc 21)** — la question décisive n'est pas « un acheteur existe-t-il ? »
      mais « **qui finance le raccordement ?** » (la survaleur couvre à peine le dé-risquage)
- [x] ✅ **Conversation avec le père faite** — **mandat Enedis accordé**, accord pour étudier.
      Valorisation notariale **400-650 k€** (il demandera 650 k€), ancien loyer **3 500 €/mois**,
      ⚠️ **commercialisation sous 1 mois** avec prospects déjà identifiés
- [x] ✅ **Mandat Enedis SIGNÉ** le 13/08/2026 par Jacques et Charles DELBÈS — fusionné et prêt
- [x] ✅ **Documents reçus et analysés** (doc 28) : amiante **limité à une partie de couverture,
      classement EP sans retrait obligatoire** · **aucun PPRi** · pas de pollution · pas de termites ·
      ⭐ **le bâti est un bâtiment industriel 1989-2000 avec étage de bureaux**, pas un hangar
- [ ] ⚠️ **Obtenir un Kbis récent** (celui fourni date de 2019) avant de déposer chez Enedis
- [ ] 🚀 **Déposer la pré-étude Enedis** (1 MW et 2 MW)
- [ ] 📄 Récupérer les **études amiante et assainissement** déjà réalisées par le père
- [ ] ❓ **Instruire la piste réhabilitation** (ne pas démolir le bâtiment de 487 m²) — doc 27 §4
- [ ] 🗣️ **Recalibrer le « ×2 »** annoncé au père (réalité : ×1,3 à ×1,6)
- [ ] Puis déposer la **pré-étude Enedis** (1 MW et 2 MW) avec un compte au **SIRET de la SCI**
- [ ] Vérifier le zonage PLU ; clarifier la position vis-à-vis de Tenergie
- [x] 📅 **Appel Datalok calé au 26 août 2026**
- [ ] 📞 Envoyer les e-mails **Hadès Patrimoine** et **FullSave** (doc 23) + relance le 25-28 août
- [ ] 📞 Puis Adista / Etix si besoin
- [ ] 🏛️ **SEMAINES 3-4** — Rodez Agglomération (zonage + AFR/ZRR) et RAGT (client-ancre)
- [x] Analyse localisation (doc 22) — la latence n'est **pas** le sujet (2-3 ms vers Toulouse) ; le vrai
      frein est la **granularité de la demande**. Angle fort identifié : **site de secours (PRA) de Toulouse**
- [x] Évaluation du BP Next Compute (doc 16) — JV : TRI réel Tenergie **25,3 %** (et non 34,1 %),
      Next Compute capte ~65 % de la valeur pour 67 € de capital ; 3 erreurs et 10 questions listées
- [x] Argument carbone / localisation (doc 17) — post lu et **fact-check validé** (×20 exact : 420 g
      Virginie vs 19,6 g France). Non discriminant entre sites français, mais deux apports clés :
      **fuite carbone** (acceptabilité locale) et **92 TWh exportés** (réponse à « le réseau ne tiendra pas »)
- [x] Étude de marché déploiement France 3/5/10 ans (doc 18) — 0,7-1,1 GW aujourd'hui → ~2,3 GW en 2030 ;
      croissance **centralisée en puissance, déconcentrée en géographie** ; 18 GW réservés chez RTE pour 2,3 GW construits
- [x] Fiche approfondie UltraEdge (doc 19) — ⚠️ **cible révisée à la baisse** : leur modèle évite le
      greenfield ; angle restant = la puissance (leurs sites font ~200 kW en moyenne) et l'accueil de module
- [ ] Sonder RAGT / CH Rodez / Rodez Agglo (client-ancre)
- [x] **Parcelle confirmée** : BH 187, Rodez (INSEE 12202) — 2 631 m², bâti 487 m², altitude 586 m
- [x] Benchmark valeur foncière (doc 20) — achat 2018 (275 k€) **dans le marché** ; valeur actuelle
      ~300 k€ médian, RTB ~465 k€ → multiple réaliste **×1,4 à ×1,7** (et non ×2-4)
- [ ] Vérifier l'éligibilité **AFR / ZRR** de la ZA Bel-Air (aides + exonérations)
- [ ] Confirmation zone PLUi sur le Géoportail de l'Urbanisme
- [ ] Dépôt du CUb (Cerfa 13410*13)
- [ ] Pré-étude Enedis (1 MW / 2 MW)
- [ ] Devis désamiantage + démolition du hangar
- [ ] Choix du scénario (type et taille de data center)
- [ ] Business plan chiffré
- [ ] Dossier de présentation au propriétaire

## Démarrage rapide (dès que le GPS est connu)

```bash
pip install Pillow requests
python scripts/get_parcelle.py <lon> <lat>      # parcelle + surface + zone PLU
python scripts/fetch_maps.py <lon> <lat> rodez_ # cartes situation / cadastre / ortho
```

Puis reporter les résultats dans `data/site.yml`.
