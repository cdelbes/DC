# 02 — Raccordement Enedis (chemin critique)

> Objectif : déterminer la **puissance de soutirage** mobilisable sur la parcelle,
> son **coût** et son **délai**. C'est la variable qui dimensionne tout le projet
> (type de data center, CAPEX, revenus).

## 1. Ce qu'il faut savoir

### Soutirage ≠ injection

- **Caparéseau** (RTE + Enedis) publie les capacités d'accueil des postes sources,
  mais pour l'**injection** (production EnR, cadre S3REnR). C'est un indicateur
  de l'état du réseau local, **pas** une réponse sur la capacité de **soutirage**
  (consommation) d'un data center.
- Pour le soutirage, la seule réponse fiable est une **étude Enedis** (pré-étude
  puis Proposition Technique et Financière — PTF) pour une puissance et un point
  de livraison donnés.

### Paliers de raccordement consommateur

| Puissance | Domaine | Raccordement | Ordre de grandeur data center |
|---|---|---|---|
| ≤ 36 kVA | BT (C5) | branchement standard | trop faible |
| 36 – 250 kVA | BT > 36 (C4) | BT forte puissance | 1 conteneur edge type P100 (100 kW) |
| 250 kVA – ~17 MW | **HTA (C3)** | poste de livraison HTA privé sur la parcelle | edge / modulaire 0,25 – 5 MW ← **cible probable** |
| > ~17 MW | HTB (RTE) | poste 63/225 kV | hyperscale — hors périmètre |

- Au-delà de 250 kVA, le raccordement se fait en **HTA 20 kV** avec un **poste de
  livraison** (local ou préfabriqué) sur la parcelle, génie civil à la charge du client.
- Coûts indicatifs relevés (2026) : à partir de ~3 200 € TTC au-delà de 36 kVA pour un
  raccordement simple, et **20 000 – 30 000 € et plus** si travaux lourds (extension de
  réseau, création poste HTA/BT). Un raccordement HTA de plusieurs MW avec extension
  peut coûter **plusieurs centaines de k€** — c'est la pré-étude qui tranche.
- Délais indicatifs : **4 à 6 mois** de travaux si la puissance est disponible,
  **6 à 9 mois minimum** sinon (renforcement réseau) ; ajouter l'instruction du dossier.
- La **réfaction** (prise en charge partielle par le TURPE) s'applique aux producteurs,
  pas aux consommateurs : un consommateur paie l'essentiel de son raccordement.

### Contexte réseau local (Aveyron / Rodez)

- Le secteur de Rodez est desservi en HTB par l'axe RTE nord-Occitanie ; RTE a lancé le
  projet de **poste électrique Sud-Aveyron** pour renforcer la zone (signal d'un réseau
  régional en cours de renforcement, plutôt favorable à moyen terme).
- Postes sources Enedis existants autour de Rodez (agglomération ~60 000 hab. +
  zones d'activités) : à identifier précisément via Caparéseau une fois le GPS connu —
  la **distance au poste source** et la présence d'un départ HTA à proximité de la
  parcelle sont les deux facteurs de coût principaux.
- Point positif : une parcelle en zone d'activités (usage actuel : dépôt BTP) est
  normalement déjà desservie par un départ HTA à proximité immédiate.

## 2. Démarche concrète (dans l'ordre)

1. **[Dès GPS connu]** Repérer sur Caparéseau (https://www.capareseau.fr) le(s) poste(s)
   source(s) les plus proches, leur taux de charge et les projets S3REnR — lecture
   « état de santé » du réseau local. *(Consultation manuelle : le site et les API
   open data Enedis/ODRE ne sont pas accessibles depuis cet environnement.)*
2. Relever la **puissance actuellement souscrite** sur la parcelle (factures du dépôt,
   n° PDL/PRM sur la facture) : un site C4 existant (ex. 100–250 kVA) donne un point de
   départ et parfois un raccordement réutilisable.
3. **Pré-étude Enedis** (demande via le portail raccordement Enedis, projet
   « consommateur > 36 kVA ») pour 2 ou 3 paliers de puissance, par ex. **250 kVA,
   1 MW, 3 MW** → obtenir pour chaque palier : faisabilité, coût, délai.
4. Sur la base des réponses, choisir le palier retenu et demander la **PTF** (validité
   3 mois) — sans engagement d'achat du foncier à ce stade.
5. En parallèle : contrat de fourniture (le prix de l'électron, C3/C4, représente
   50–70 % de l'OPEX d'un data center) — consulter des fournisseurs sur un profil de
   charge plat 24/7, qui obtient de bons prix.

## 3. Données à obtenir (checklist)

- [ ] Point GPS et référence de la parcelle
- [ ] N° PRM / puissance souscrite actuelle du dépôt
- [ ] Poste source de rattachement + distance (Caparéseau / pré-étude)
- [ ] Coût et délai de raccordement pour 250 kVA / 1 MW / 3 MW
- [ ] Prix de fourniture indicatif €/MWh profil 24/7 (2027–2030)

## Sources

- [Capacités d'accueil du réseau — data.gouv.fr](https://www.data.gouv.fr/datasets/capacites-daccueil-du-reseau)
- [Consulter les capacités d'accueil du réseau (Caparéseau) — RTE](https://www.services-rte.com/en/learn-more-about-our-services/consult-the-reception-capacity-of-the-grid.html)
- [Raccordement électrique professionnel : guide 2026 — Acieb Énergie](https://www.aciebenergie.fr/guides/raccordement-electrique-professionnel-guide-2026/)
- [Enedis raccordement : démarches, tarifs et contacts — Opéra Énergie](https://opera-energie.com/enedis-raccordement/)
- [Combien coûte un raccordement au réseau Enedis — Lab Énergies](https://www.lab-energies.fr/articles/cout-raccordement-enedis)
- [Raccordement électrique entreprise : demande, prix et délais — Selectra](https://entreprises.selectra.info/energie/electricite/raccordement)
- [Procédure de traitement des demandes de raccordement — Enedis](https://www.enedis.fr/media/2173/download)
- [Projet poste électrique Sud-Aveyron — RTE](https://www.rte-france.com/projets/nos-projets/sud-aveyron-un-nouveau-poste-electrique-pour-securiser-lalimentation-du-nord-de-loccitanie)
