# 03 — Typologie : quel data center sur cette parcelle ?

> Le choix du type dépend de trois variables : **puissance raccordable** (doc 02),
> **surface / configuration du terrain** (analyse parcellaire, `data/site.yml`) et
> **demande solvable** localement. Quatre scénarios sont mis en concurrence dans le
> business plan.

## Scénario A — Edge conteneurisé (100 – 300 kW)

Le modèle éprouvé sur Next Compute (Policloud P100 : conteneur ISO 20', 14,4 m²
d'emprise, 100 kW, UPS + groupes froids, extinction gaz).

- **Terrain requis** : ~50–100 m² par conteneur (dalle + groupes froids + dégagements).
  Compatible avec la simple cour du dépôt, sans toucher au bâtiment.
- **Urbanisme** : **déclaration préalable** si emprise ≤ 20 m² (voir doc 04) → délai court.
- **Raccordement** : C4 (≤ 250 kVA) voire HTA léger. Souvent faisable sans renforcement.
- **CAPEX** : ~0,5 – 1 M€ par conteneur équipé (hors IT), raccordement et VRD compris.
- **Clients** : opérateurs edge (UltraEdge…), intégrateurs cloud souverain, collectivités.
- **Verdict** : ticket d'entrée minimal, déployable en < 12 mois, mais revenus plafonnés.

## Scénario B — Modulaire multi-conteneurs / bâtiment technique (0,5 – 2 MW)

Assemblage de modules préfabriqués (acteurs français : Modul Data Center à Gardanne,
Module-IT à Nantes — délais de fabrication 3 à 6 mois) ou réaménagement du bâtiment
existant du dépôt en salle IT.

- **Terrain requis** : 1 000 – 3 000 m² utiles (modules + poste HTA + groupes +
  éventuel groupe électrogène).
- **Urbanisme** : **permis de construire** (> 20 m² d'emprise), ICPE à examiner
  (rub. 2925 accumulateurs/chargeurs, 2910 groupe électrogène, fluides frigorigènes).
- **Raccordement** : HTA (C3), poste de livraison privé. Pré-étude Enedis indispensable.
- **CAPEX** : ordre de grandeur 4 – 8 M€/MW IT installé pour du modulaire (hors foncier).
- **Clients** : colocation régionale (baies à la baie/au kW), PME/ETI Occitanie nord,
  santé, collectivités (souveraineté et proximité), opérateurs télécoms.
- **Verdict** : le scénario « cœur de cible » si la pré-étude Enedis confirme ≥ 1 MW.

## Scénario C — Colocation régionale (2 – 5 MW)

Petit data center de colocation classique (bâtiment neuf, salles de 200–500 m²,
redondance N+1, certification HDS possible pour la santé).

- **Terrain requis** : ≥ 4 000 – 6 000 m² ; voirie poids lourds ; double adduction
  fibre souhaitable.
- **Raccordement** : HTA plusieurs MW — dépend entièrement de la capacité du poste source.
- **CAPEX** : 8 – 12 M€/MW IT tout compris. Financement de projet nécessaire.
- **Risque** : profondeur du marché aveyronnais à démontrer ; concurrence des sites
  de Toulouse/Montpellier à ~2 h.
- **Verdict** : à ne retenir que si un client ancre (ETI, santé, secteur public) signe
  un pré-engagement.

## Scénario D — HPC / IA (densité élevée, 1 – 5 MW)

Colocation haute densité pour calcul/IA (modèle Eclairion : modulaire haute densité,
refroidissement liquide direct — DLC), éventuellement couplée à la valorisation de
chaleur fatale.

- **Atout Rodez** : climat frais (~570–630 m d'altitude) → free cooling une grande
  partie de l'année, PUE bas, argument de coût pour du HPC.
- **Contrainte** : télécoms moins critiques (batch) mais **puissance élevée
  indispensable** ; clients nationaux à démarcher (labos, studios, fournisseurs GPU cloud).
- **Verdict** : opportuniste — pertinent seulement si le réseau local autorise ≥ 2–3 MW
  à coût raisonnable.

## Grille de décision

| Critère | A. Edge 100–300 kW | B. Modulaire 0,5–2 MW | C. Colo 2–5 MW | D. HPC/IA |
|---|---|---|---|---|
| Puissance Enedis requise | ≤ 250 kVA | 0,5–2 MW HTA | 2–5 MW HTA | 1–5 MW HTA |
| Surface utile | 50–100 m² | 1 000–3 000 m² | ≥ 4 000 m² | 1 500–4 000 m² |
| Urbanisme | DP (rapide) | PC + ICPE | PC + ICPE | PC + ICPE |
| CAPEX | 0,5–1 M€ | 2–16 M€ | 16–60 M€ | 5–40 M€ |
| Délai mise en service | 6–12 mois | 12–24 mois | 24–36 mois | 18–30 mois |
| Dépendance marché local | faible (opérateur national) | moyenne | forte | faible |
| Compatible vente partielle au BTP | ✅ | selon surface | ❌ | selon surface |

**Approche retenue pour le BP** : chiffrer A comme « coup d'essai » à faible risque et
B comme scénario principal ; C et D en options conditionnées aux réponses Enedis et à
un client ancre.

## Sources

- [Eclairion inaugure son data center modulaire — Usine Digitale](https://www.usine-digitale.fr/article/eclairion-inaugure-son-data-center-modulaire-pour-revolutionner-les-supercalculateurs.N2224546)
- [Modul Data Center (Gardanne)](https://moduldatacenter.com/)
- [UltraEdge — edge data centers en France](https://www.ultraedge.com/en)
- [The Containerized Data Center: Complete Guide 2026 — Datalok](https://www.datalok.io/en/blog/containerized-datacenter-guide-2026.html)
- [Edge Data Center Market — GM Insights](https://www.gminsights.com/industry-analysis/edge-data-center-market)
- Dossier Next Compute (document interne Tenergie, non versionné) pour les caractéristiques P100.
