# 05 — Trame du business plan

> Objectif : un BP comparable entre scénarios (A edge / B modulaire, C/D en option)
> et opposable à l'alternative « vente de la parcelle au BTP ». Toutes les valeurs
> ci-dessous sont des **ordres de grandeur à remplacer** par les chiffres réels
> (pré-étude Enedis, devis, offre d'achat BTP).

## 1. Hypothèses de cadrage (à renseigner)

| Hypothèse | Valeur | Source / statut |
|---|---|---|
| Surface parcelle | *à compléter* | cadastre (script) |
| Valeur vénale parcelle (offre BTP) | *à compléter* | propriétaire |
| Puissance raccordable / coût / délai | *à compléter* | pré-étude Enedis |
| Prix électricité profil 24/7 (€/MWh) | ~90–120 | consultation fournisseurs |
| Zone PLUi + régime d'autorisation | *à compléter* | GPU + doc 04 |

## 2. Structure du modèle (par scénario)

### CAPEX
- Foncier : achat de la parcelle **ou** 0 si bail (le loyer passe en OPEX)
- Raccordement Enedis + poste de livraison HTA
- Infrastructure : conteneurs/modules ou réhabilitation bâtiment, dalle/VRD, clôture
- Électrique secondaire : TGBT, UPS, batteries, (groupe électrogène scén. B+)
- Froid : groupes, free cooling / free chilling
- Sécurité : incendie gaz, contrôle d'accès, vidéosurveillance
- Télécoms : adduction fibre (double si colo)
- Études, MOE, autorisations, aléas (10–15 %)

### OPEX annuel
- Électricité = puissance IT moyenne × 8 760 h × PUE × prix MWh ± TURPE
- Loyer foncier (si bail) — *c'est la ligne qui rémunère le propriétaire*
- Maintenance (2–4 % du CAPEX équipements), télécoms, assurance, taxes (TA, TF),
  supervision/astreinte, sécurité

### Revenus (selon modèle d'affaires)
1. **Location wholesale à un opérateur edge** (scén. A) : loyer fixe €/mois par site —
   revenu sûr, marge faible.
2. **Colocation retail** (scén. B/C) : €/kW IT/mois (ordres de grandeur marché
   France région : 120–250 €/kW/mois selon redondance et services) + frais d'accès.
3. **Hébergement HPC/GPU** (scén. D) : €/kW élevé mais contrats plus courts.
4. Options : revente chaleur fatale, services managés, autoconsommation PV en toiture
   du dépôt (synergie avec le métier énergie du porteur).

### Indicateurs de sortie
- TRI projet (cible > 10–12 % pour du B), VAN @ 6–8 %, payback, DSCR si dette.
- **Comparatif propriétaire** : loyer capitalisé vs prix de vente BTP ; TRI du scénario
  « achat » avec foncier payé au prix de l'offre BTP (test de robustesse).

## 3. Mini-modèle indicatif — scénario A (1× conteneur 100 kW, base P100)

*Illustratif, à recaler — ne pas diffuser en l'état.*

| Poste | Montant |
|---|---|
| CAPEX (conteneur équipé, dalle, raccordement C4, études) | ~700 k€ |
| OPEX hors élec (maintenance, assurance, télécom, taxes) | ~40 k€/an |
| Électricité (70 kW moyens × 8 760 h × PUE 1,3 × 100 €/MWh) | ~80 k€/an |
| Revenu location opérateur edge (hypothèse 180 k€/an) | 180 k€/an |
| EBITDA | ~60 k€/an → payback brut > 10 ans |

→ Enseignement attendu : le scénario A seul rentabilise difficilement un foncier cher ;
il prend son sens comme **phase 1** d'un scénario B (mutualisation raccordement et
autorisations) ou si l'opérateur edge finance lui-même le conteneur (le foncier ne
porte alors que dalle + raccordement, modèle « landlord »).

## 4. Étapes de construction du BP

1. Recevoir GPS → analyse parcellaire (surface, zone) → scénarios compatibles.
2. Pré-étude Enedis 250 kVA / 1 MW / 3 MW → coût-délai par palier.
3. Sonder la demande : 3–4 contacts (opérateur edge, intégrateur régional,
   CH/collectivités, courtier colo) pour calibrer les prix.
4. Modèle Excel multi-scénarios (à créer dans `business-plan/` une fois 1–3 faits).
5. Dossier de décision propriétaire (comparatif vente BTP / bail / achat).
