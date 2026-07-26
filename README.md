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
- [x] Liste acheteurs / partenaires / clients (doc 12) — cible n°1 UltraEdge (Datapoles)
- [ ] Test de marché : sonder RAGT / CH Rodez / Rodez Agglo (client-ancre) + UltraEdge
- [ ] Teaser 1 page pour démarchage
- [ ] Confirmation parcelle + zone PLUi sur cadastre.gouv.fr / Géoportail de l'Urbanisme
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
