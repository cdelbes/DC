# 06 — Étude urbanistique du site (ZA Bel-Air, Rodez)

> **Point GPS** : 44.372954 N, 2.544455 E — secteur rue de la Ferronnerie /
> avenue des Compagnons, **zone d'activités de Bel-Air**, 12000 Rodez (en limite
> d'Onet-le-Château).
> Étude documentaire réalisée sur sources publiques ; les points marqués **[À CONFIRMER]**
> doivent être vérifiés sur le Géoportail de l'Urbanisme et auprès du service instructeur
> de Rodez Agglomération (05 65 73 83 44). Ce document n'est pas un avis juridique.

## 1. Identification du site

| Élément | Valeur | Source |
|---|---|---|
| Coordonnées | 44.372954, 2.544455 | fourni |
| Localisation | ZA de Bel-Air, rue de la Ferronnerie / av. des Compagnons | vue aérienne + annuaires (Ets Castes : av. des Compagnons, 12000 Rodez ; Orexad : 389 rue Ferronnerie, 12000 Rodez) |
| Commune | **Rodez (12000)** — ✅ **confirmé** : code INSEE **12202** dans la référence cadastrale | Pappers Immobilier |
| Foncier disponible | **2 631 m²** de parcelle, dont **2 144 m² libres** | ✅ Pappers Immobilier (doc 20) |
| Bâti existant | hangar-dépôt, **487 m² d'emprise au sol** (h. 4-6 m) + cour de stockage | ✅ Pappers/BDNB (doc 20) — nettement plus petit que l'estimation initiale à vue |
| Références cadastrales | **12202000BH0187** → **section BH n° 187**, Rodez | ✅ Pappers Immobilier (doc 20) |
| Environnement immédiat | tissu 100 % activités : Orexad, Veolia Eau, RMA 12, Couvoir Ruthénois (Ets Castes), centre technique municipal de Rodez au nord | vue aérienne |
| Desserte | voirie de ZA (rue de la Ferronnerie), av. des Compagnons avec arrêts de bus ; accès poids lourds existant (dépôt matériaux) | vue aérienne |
| Altitude | **586 m** (plateau de Bel-Air) | ✅ Pappers/BDNB |

**Lecture d'ensemble** : un site d'activités mature et banalisé — le contexte le plus
favorable possible pour un data center au regard de la grille Next Compute (équivalent
des sites 🟢 « zone d'activités » du criblage).

## 2. Document d'urbanisme et zonage

- Document applicable : **PLUi de Rodez Agglomération** (document consolidé publié au
  GPU, dernières procédures 2024–2025 ; identifiant GPU du document : `DU_241200187`).
- La ZA de Bel-Air (~133 ha, vocation industrielle et artisanale d'après Rodez
  Agglomération) relève d'un zonage **urbain à vocation économique — type UX**
  **[À CONFIRMER]** : libellé exact de la zone et éventuel secteur (UXa…) à lire sur le
  GPU au point GPS.
- Conséquence attendue : les destinations **industrie / entrepôt / bureau** y sont
  admises de droit → un data center y est en principe **constructible**, sans STECAL ni
  évolution du document (contrairement aux zones A/N du criblage Next Compute).

### Qualification de la destination « data center »

Dans la nomenclature des destinations (R.151-27/28 CU), un data center est
généralement rattaché à la sous-destination **« industrie »** (doctrine et pratique
des services instructeurs) ; certains instructeurs retiennent « entrepôt ».
**[À CONFIRMER]** avec l'instructeur — dans une zone UX qui admet les deux, le débat
est sans enjeu, c'est précisément l'intérêt de ce site.

### Règles de zone à relever au règlement **[À CONFIRMER]**

| Règle | Enjeu pour le projet MegaMod |
|---|---|
| Hauteur maximale | modules 4–5 m → très en deçà des plafonds usuels de ZA (9–15 m) : a priori sans objet |
| Implantation / reculs (voies, limites séparatives) | dimensionne la position des modules sur les 2 522 m² |
| Emprise au sol maximale / coefficient | MegaMod 1 MW ≈ 640 m² soit **~25 %** du foncier : marge importante |
| Aspect extérieur | modules métalliques — bardage/teinte à caler sur le règlement (RAL sobre) |
| Stationnement | faible besoin (site quasi inoccupé en exploitation) |
| Espaces verts / pleine terre | à vérifier, la cour est déjà imperméabilisée (argument ZAN favorable) |
| Clôtures | hauteur max usuelle 2 m — compatible sécurisation périmétrique |

## 3. Risques, servitudes, protections

| Sujet | Analyse | Statut |
|---|---|---|
| **PPRi « Aveyron amont »** (Aveyron + ruisseau de l'Auterne, communes de Rodez et Onet-le-Château couvertes) | le site est sur le **plateau** de Bel-Air, en dehors des fonds de vallée de l'Aveyron et de l'Auterne → a priori **hors zone inondable** | **[À CONFIRMER]** sur la carte du PPRi (aveyron.gouv.fr) |
| Retrait-gonflement des argiles | aléa à consulter (Géorisques) — dimensionne les fondations/longrines des modules (11–30 t par module) | **[À CONFIRMER]** |
| Sismicité | Aveyron en zone 1 (très faible) → sans contrainte notable | acquis |
| Radon | Aveyron largement en zone 3 (potentiel significatif) → enjeu pour locaux de travail permanents, faible pour un DC (présence humaine ponctuelle) | à noter |
| Monuments historiques / ABF | centre ancien de Rodez à ~2,5 km, château d'Onet à ~2 km : un périmètre de 500 m est **improbable** en ZA Bel-Air | **[À CONFIRMER]** (atlas des patrimoines) |
| Servitudes aéronautiques (aéroport Rodez-Aveyron, ~8 km NO) | hauteur projet ≤ 5 m → sans objet sauf servitude radioélectrique particulière | **[À CONFIRMER]** dans les annexes du PLUi |
| Lignes électriques / canalisations | à vérifier dans les annexes servitudes (I4…) du PLUi | **[À CONFIRMER]** |
| ZAN / artificialisation | parcelle **déjà artificialisée** (dépôt + cour) → aucune consommation d'espace naturel : dossier favorable | acquis |

## 3 bis. Démolition du hangar et amiante (point structurant)

Le projet prévoit la **démolition du hangar existant**, dont la **toiture est amiantée**
(fibrociment probable — plaques ondulées, très courant sur ce type de dépôt). C'est à la
fois une contrainte réglementaire et **un levier de valeur** dans la négociation foncière.

**Obligations avant démolition :**

1. **Repérage amiante avant démolition (RAAT)** obligatoire (Code du travail R.4412-97 et s.,
   norme NF X46-020) par un diagnostiqueur certifié → localise et quantifie tous les
   matériaux amiantés (toiture, mais aussi joints, colles, conduits éventuels).
2. **Désamiantage par une entreprise certifiée** (certification amiante SS3 / Qualibat
   1552) : **plan de retrait** transmis à la **DREETS (inspection du travail)** et à la
   Carsat **au moins 1 mois avant** le début des travaux.
3. **Traçabilité des déchets** : bordereaux de suivi (BSDA), évacuation en filière agréée
   (ISDD/ISDND selon nature) — l'amiante-ciment est un déchet dangereux.
4. **Permis de démolir** : à vérifier s'il est exigé sur ce secteur de Rodez (les communes
   peuvent l'instaurer) ; sinon la démolition est intégrée au **permis de construire**.

**Impact business plan** (à chiffrer au stade devis) :
- Désamiantage toiture fibrociment : ordre de grandeur **20 à 50 €/m²** (selon accès,
  hauteur, dépose soignée) → pour ~900-1 100 m² de toiture, **~25 à 55 k€**, hors
  démolition de la structure et évacuation des gravats.
- Démolition de la structure (charpente/murs, dalle conservée si réutilisable) : poste
  séparé à chiffrer.

**Levier de négociation** : un hangar à toiture amiantée est un **passif** pour le
propriétaire (coût de désamiantage à sa charge tôt ou tard, décote à la revente). Le
projet data center, en prenant en charge la dépollution, **retire ce passif** — argument
à valoriser face à l'offre de l'acheteur BTP (qui, lui, héritera aussi de ce coût).

**Point ZAN / dalle** : après démolition, la parcelle reste **artificialisée** (pas de
consommation d'espace) ; si la dalle béton existante est saine, sa **réutilisation** comme
assise du data center réduit le génie civil — à vérifier (portance vs 11-30 t par module).

## 4. Régime d'autorisation pour un MegaMod

Le scénario Vertiv MegaMod (cf. `data/vertiv-megamod-specs.md`) change de catégorie
par rapport au P100 de Next Compute :

| Configuration | Emprise au sol | Régime |
|---|---|---|
| MegaMod 0,5 MW | ~26,5 × 14 m ≈ **371 m²** | **Permis de construire** |
| MegaMod 1 MW | ~26,5 × 24 m ≈ **636 m²** | **Permis de construire** |
| MegaMod Plus 1 MW | ~26,5 × 31 m ≈ **821 m²** | **Permis de construire** |

- **PC obligatoire** (> 20 m²) quelle que soit la variante — délai d'instruction de droit
  commun 3 mois (hors consultations), à sécuriser par une pré-rencontre avec
  l'instructeur.
- Démolition : a priori aucune (implantation sur la cour) ; si le hangar est démoli ou
  modifié, l'intégrer au PC.
- Si réutilisation du hangar existant en salle IT : **changement de destination** à
  instruire (dépôt/entrepôt → industrie), potentiellement dans le même PC.

### ICPE et sécurité (à instruire en parallèle du PC)

| Rubrique | Déclencheur MegaMod | Pré-analyse |
|---|---|---|
| 2925 (charge d'accumulateurs) | UPS Liebert EXL S1 + batteries VRLA — puissance de charge > 50 kW probable à 1 MW | **déclaration** probable |
| 2910 (combustion) | groupe électrogène de secours s'il est ajouté (non inclus dans le bloc de base) | selon puissance (≥ 1 MW th → déclaration) |
| F-gaz / 1185 | froid à détente directe (DX Liebert PDX + condenseurs) — charge de fluide importante à 1 MW | contrôle étanchéité, seuils à calculer |
| SDIS 12 | notice sécurité, accès engins, extinction | consultation dans le cadre du PC |

### Bruit

Condenseurs et groupes en toiture/périmètre : en ZA la contrainte est réduite, mais
l'arrêté du 26/08/2011 (bruit de voisinage) et les éventuelles prescriptions du
règlement de zone s'appliquent. Habitat le plus proche à localiser (lotissements au
sud de la ZA) → **étude acoustique recommandée** au stade PC.

## 5. Test d'implantation sur le foncier (2 522 m²)

```
Foncier ≈ 2 522 m²
├─ MegaMod 1 MW (26,5 × 24 m)             ≈ 636 m²   (25 %)
├─ Poste de livraison HTA + TGBT            ≈ 30 m²
├─ Groupe électrogène + cuve (option)       ≈ 60 m²
├─ Reculs, circulation PL, grutage, parking ≈ 600–800 m²
└─ Réserve d'extension (2e bloc 0,5–1 MW)   ≈ 400–800 m²  → jusqu'à 2 MW IT
```

- La variante **1 MW tient confortablement**, avec réserve pour doubler (extensibilité
  native MegaMod, y compris en empilage).
- Le montage nécessite une **grue lourde** : accès PL existant (dépôt matériaux) = atout.
- Point d'attention : la mesure de 2 522 m² correspond-elle à la parcelle entière ou à
  la partie disponible hors hangar ? **[À CONFIRMER]** — si le hangar reste exploité par
  ailleurs, l'implantation se fait sur la cour sud/ouest et reste faisable pour 1 bloc.

## 6. Conclusion de l'étude urbanistique

**Verdict provisoire : site 🟢 favorable.**

1. Zone d'activités mature, destinations industrielles admises de droit attendues,
   aucune des contraintes rédhibitoires du criblage Next Compute (zone A/N, PPRi).
2. Le foncier de 2 522 m² absorbe un MegaMod 1 MW avec réserve d'extension à 2 MW.
3. Le passage en **permis de construire** (au lieu d'une DP) allonge le calendrier
   administratif (~4–6 mois dépôt→autorisation purgée) mais reste standard en ZA.
4. Le vrai déterminant redevient le **raccordement Enedis** : 1 à 2 MW de soutirage en
   HTA — voir doc 02, pré-étude à lancer en priorité.

### Prochaines actions (ordre recommandé)

1. **Relever la référence cadastrale et la zone exacte** au point GPS (cadastre.gouv.fr
   + Géoportail de l'Urbanisme) et lire le règlement de la zone.
2. Vérifier PPRi / argiles / servitudes (Géorisques + annexes PLUi).
3. Déposer un **certificat d'urbanisme opérationnel (CUb)** décrivant « construction
   d'un data center modulaire ~640 m², 1 MW » : réponse opposable de l'administration
   sous 2 mois, sans engagement — c'est l'outil idéal avant toute discussion foncière
   avec le propriétaire.
4. Pré-rencontre service urbanisme Rodez Agglomération + SDIS 12.
5. Lancer la pré-étude Enedis (250 kVA / 1 MW / 2 MW) en parallèle.

## Sources

- [ZA Bel-Air — Rodez Agglomération (133 ha, vocation industrielle/artisanale)](https://immo-hub.org/parcs-d-activites/zone-dactivites-bel-air-agglomeration-de-rodez)
- [Le PLUi — Rodez Agglomération](https://www.rodezagglo.fr/agglo/amenagement/qu-est-ce-que-le-plui/)
- [PLUi — Ville de Rodez](https://www.ville-rodez.fr/demarches/urbanisme/plui/)
- [Règlement écrit du PLUi (GPU, DU_241200187)](https://data.geopf.fr/annexes/gpu/documents/DU_241200187/fb485a507bc36cbdb7352b29c4b1ad26/241200187_reglement_20240625.pdf)
- [Règlement du PPRi de Rodez — Préfecture de l'Aveyron](https://www.aveyron.gouv.fr/contenu/telechargement/6640/84630/file/rodez_reglement_ppri_cle71a897.pdf)
- [Ets Castes, avenue des Compagnons, 12000 Rodez — 118000.fr](https://www.118000.fr/e_C0000753963)
- Brochure Vertiv™ MegaMod™ (fournie) — synthèse dans `data/vertiv-megamod-specs.md`
