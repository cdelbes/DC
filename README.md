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
| `docs/29-apres-appel-enedis-preparation-rdv.md` | ⭐ **Après l'appel Enedis** : préparation du RDV sur site (12 questions), périmètre du poste de livraison vs transfo, cibles marché 2 MW |
| `docs/30-passif-chiffre-kbis-assainissement-amiante.md` | ⭐ **Le passif chiffré** : Kbis à jour, assainissement NON CONFORME (21,7 k€ dus), toiture amiantée 518 m² (97 k€ TTC) |
| `docs/31-benchmark-developpeurs-amont-powered-land.md` | ⭐ **Benchmark des acteurs de l'amont** : powered land, contractants généraux, modulaire, AMO, opérateurs edge, marketplaces — qui achète vraiment, qui informe |
| `docs/32-brief-appel-datalok.md` | ⭐ **Brief d'appel Datalok (26/08)** : ouverture, fiche site, questions par priorité, objections, ce qu'il ne faut pas dire |
| `docs/33-compte-rendu-datalok-26-08.md` | ⭐ **CR Datalok** : 2 MW « petit mais faisable », Aveyron non bloquant, ⭐ **la demande doit être LOCALE** ; analyse de la prestation à 4 000 € |
