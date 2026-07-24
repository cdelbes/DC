# 04 — Urbanisme & réglementaire

> Adapté de la méthode Next Compute (document interne, non versionné). Les
> qualifications (zone, seuils, ICPE) restent à valider par le service instructeur
> et un conseil en urbanisme — ce document n'est pas un avis juridique.

## 1. Régime d'autorisation selon l'emprise

| Emprise au sol / surface de plancher créée | Régime |
|---|---|
| ≤ 5 m² (H ≤ 12 m) | Dispense (sauf secteur protégé) |
| > 5 et ≤ 20 m² | **Déclaration préalable** (Cerfa 13404) → scénario A (1 conteneur) |
| > 20 m² | **Permis de construire** → scénarios B, C, D |
| Changement de destination du bâtiment existant (dépôt → data center) | DP a minima ; PC si travaux modifiant structure/façade. La destination « industrie » / « entrepôt » vs « bureau » est à qualifier avec l'instructeur |

Point de vigilance hérité de Next Compute : avec les groupes froids posés au sol,
l'emprise d'un P100 approche 20 m² — le mode de comptage est à trancher avec
l'instructeur pour rester en DP.

## 2. Le verrou n°1 : la zone du PLUi

- Rodez relève du **PLUi de Rodez Agglomération** — zonage à vérifier sur le
  [Géoportail de l'Urbanisme](https://www.geoportail-urbanisme.gouv.fr/) dès le GPS connu
  (script `scripts/get_parcelle.py`).
- Un dépôt d'entreprise BTP est très probablement en **zone urbaine à vocation
  économique (type UE/UX/UI)** → usage industriel/tertiaire autorisé **de droit** =
  configuration favorable, la même que les meilleurs sites du criblage Next Compute.
- À vérifier dans le règlement de zone : hauteurs, implantation par rapport aux
  limites, aspect extérieur, **nuisances sonores** (groupes froids — voisinage),
  stationnement, espaces verts / coefficient de pleine terre.
- Servitudes et risques : PPRi (l'Aveyron traverse Rodez), canalisations, monuments
  historiques (périmètre ABF en centre ancien), archéologie.

## 3. ICPE et sécurité

| Rubrique | Objet | Déclencheur probable |
|---|---|---|
| 2925 | Ateliers de charge d'accumulateurs | UPS/batteries lithium — seuil en kW de charge |
| 2910 | Combustion | Groupe électrogène de secours (scénarios B/C/D) |
| 1185 / F-gaz | Fluides frigorigènes | Groupes froids selon fluide et charge |
| 4735 et s. | Stockages spécifiques | Novec/FK-5-1-12 : notice sécurité, pas d'ICPE en général |

- **SDIS 12** : notice de sécurité incendie (extinction gaz, accès pompiers).
- **Bruit** : étude acoustique recommandée dès le scénario B (voisinage de la zone).
- **ZAN / artificialisation** : parcelle déjà artificialisée = argument favorable.
- **Évaluation environnementale** : a priori non requise aux tailles envisagées.

## 4. Fiscalité / divers

- Taxe d'aménagement sur les m² créés ; IFER data center non applicable aux petites
  tailles (à vérifier au-delà du MW).
- Chaleur fatale : depuis la loi REEN, les gros data centers doivent étudier la
  valorisation — ici c'est surtout une **opportunité** (réseau de chaleur, bâtiments
  voisins, serres).

## 5. Checklist par scénario

- [ ] Zone PLUi + règlement de la zone (GPU) — *bloqué par le GPS*
- [ ] Risques : PPRi, retrait-gonflement argiles, radon (Aveyron = zone à potentiel)
- [ ] Périmètre ABF / secteur protégé
- [ ] Qualification destination du bâtiment existant
- [ ] Pré-rencontre service urbanisme Rodez Agglomération (recommandée avant dépôt)
