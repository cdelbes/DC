# 07 — Guide : certificat d'urbanisme opérationnel (CUb)

> Objectif : obtenir une **réponse écrite et opposable** de l'administration sur la
> constructibilité d'un data center sur la parcelle, **avant** d'engager la moindre
> dépense lourde ou la discussion foncière avec le propriétaire. Sans risque et peu
> coûteux (gratuit, hors temps).

## 1. Pourquoi le CUb (et pas le CUa)

| | CU d'information (CUa) | **CU opérationnel (CUb)** ← à demander |
|---|---|---|
| Question posée | quelles règles s'appliquent au terrain ? | **mon opération précise est-elle réalisable ?** |
| Contenu de la réponse | zonage, règles, servitudes, taxes | + faisabilité de l'opération décrite + état/desserte des **équipements publics** (voirie, eau, électricité, assainissement) |
| Intérêt ici | faible | **fort** : la mairie doit se prononcer sur « data center modulaire » et sur la desserte électrique/réseaux |

**Effet juridique clé** : le CU **cristallise pendant 18 mois** les règles d'urbanisme,
la fiscalité et les servitudes applicables (art. L.410-1 CU). Si le PLUi évolue ensuite,
le projet reste jugé sur les règles du jour du CU. C'est une **sécurité juridique** avant
d'acheter/louer le terrain.

> ⚠️ Le CUb n'est **pas** une autorisation de construire : il ne dispense pas du permis
> de construire. Il fiabilise, il n'autorise pas.

## 2. Formulaire et pièces

- **Formulaire** : Cerfa **13410\*13** (version en vigueur depuis le 01/01/2026 — les
  versions antérieures sont rejetées par les guichets dématérialisés). Cocher
  **« b) certificat d'urbanisme opérationnel »**.
- **Pièces à joindre** (dossier CUb) :
  1. **Plan de situation** du terrain (repérage dans la commune) — généré par
     `scripts/fetch_maps.py` (couche `map_situation`).
  2. **Note descriptive succincte de l'opération** : c'est la pièce décisive — voir le
     modèle §4 ci-dessous.
  3. **Plan du terrain** avec, s'ils existent, les bâtiments (le hangar à démolir) et la
     localisation de l'implantation projetée (couche `map_cadastre` / `map_ortho`).
  4. Le cas échéant, un croquis d'implantation du/des modules.
- **Nombre d'exemplaires** : dépôt **dématérialisé obligatoire** (commune > 3 500 hab.,
  Rodez est concernée) via la **téléprocédure / guichet numérique des autorisations
  d'urbanisme (GNAU)** de Rodez Agglomération (SVE). Le dépôt papier en mairie (2 ex.,
  4 pour le CUb) reste possible mais la voie électronique est la règle.

## 3. Délai, silence, validité

- **Délai d'instruction : 2 mois** (CUb).
- **Silence de l'administration à 2 mois = CU tacite** : les règles sont cristallisées,
  mais un CU tacite ne porte que sur les informations, pas sur un accord exprès de
  faisabilité → **viser une réponse expresse** (relancer le service à 6-7 semaines).
- **Validité : 18 mois**, prolongeable par périodes d'un an tant que les règles n'ont
  pas changé (demande de prolongation ≥ 2 mois avant l'échéance).

## 4. Note descriptive de l'opération — trame à remplir

> À adapter, à joindre au Cerfa. Décrire assez pour que l'instructeur qualifie
> destination + faisabilité, sans figer au point de se contraindre.

```
Objet : construction d'un centre de données (data center) modulaire

1. Terrain
   - Adresse : rue de la Ferronnerie / av. des Compagnons, ZA de Bel-Air, 12000 Rodez
   - Références cadastrales : [SECTION N°]  — surface ≈ 2 522 m²
   - Zonage PLUi : [zone UX / à confirmer]
   - État actuel : terrain bâti (hangar-dépôt à toiture amiantée) + cour de stockage

2. Opération projetée
   - Démolition du hangar existant (toiture amiantée — désamiantage préalable réglementaire)
   - Construction d'un data center modulaire préfabriqué, destination « industrie »
   - Emprise au sol projetée : ≈ 640 m² (module ~26,5 × 24 m), hauteur ≈ 5 m
   - Puissance électrique : raccordement HTA, ~1 MW (extensible ~2 MW)
   - Équipements techniques associés : poste de livraison HTA, groupes de froid,
     dispositif de sécurité incendie, clôture périmétrique

3. Desserte par les équipements publics (questions posées à l'administration)
   - Voirie : accès poids lourds existant depuis la rue de la Ferronnerie
   - Électricité : présence d'un réseau HTA à proximité (~250 m) — capacité de
     raccordement à confirmer auprès d'Enedis
   - Eau / assainissement / télécom : desserte de la zone d'activités à confirmer

4. Demande
   Le pétitionnaire sollicite la confirmation que le terrain peut être utilisé pour
   l'opération décrite, et l'indication de l'état des équipements publics existants
   ou prévus.
```

## 5. Étapes concrètes

1. Récupérer la **référence cadastrale** exacte (cadastre.gouv.fr au point GPS) et le
   **zonage** (Géoportail de l'Urbanisme) → renseigner `data/site.yml`.
2. Générer plan de situation + plan du terrain (`scripts/fetch_maps.py 2.5444548605206823 44.37295358345457 rodez_`).
3. Remplir le **Cerfa 13410\*13** (CUb) + la note descriptive (§4).
4. Déposer via le **GNAU de Rodez Agglomération** (rechercher « guichet numérique
   urbanisme Rodez agglomération »). Conserver le récépissé (n° de dossier CU).
5. **Appeler le service urbanisme en amont** (Rodez Agglo, 05 65 73 83 44 / mairie de
   Rodez) : un rendez-vous de pré-dépôt fait gagner un temps précieux et signale le
   projet — utile aussi pour la question de la destination « data center ».
6. À réception du CU : archiver, il sécurise 18 mois et devient une pièce forte du
   dossier de décision présenté au propriétaire.

## 6. Articulation avec le permis de construire

Le CUb est l'**étape 1**. Le **permis de construire** (obligatoire ici, emprise > 20 m²,
Cerfa 13409) viendra ensuite, une fois le scénario et le foncier arrêtés, en intégrant :
la démolition du hangar (ou permis de démolir dédié — à vérifier si exigé à Rodez), le
plan de masse coté, l'étude d'implantation, le volet ICPE et la notice SDIS. Instruction
PC de droit commun : 3 mois (+ éventuelles majorations).

## Sources

- [Certificat d'urbanisme (CUa, CUb) — service-public / guides](https://construireenfrance.fr/guides/certificat-urbanisme)
- [Cerfa 13410\*13 — certificat d'urbanisme (version 2026)](https://www.construires.fr/formulaires-cerfa/certificat-urbanisme/)
- [Certificat d'urbanisme : guide complet — Urbanista](https://www.urbanista-avocat.com/certificat-durbanisme/)
- Article L.410-1 et R.410-1 et s. du Code de l'urbanisme (cristallisation 18 mois).
