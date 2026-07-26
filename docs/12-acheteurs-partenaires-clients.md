# 12 — Acheteurs, partenaires et clients potentiels (data center ~1 MW à Rodez)

> Cible : un data center de **~1 MW** sur la ZA de Bel-Air (Rodez). On distingue **trois
> familles** d'interlocuteurs, car elles n'achètent pas la même chose :
> - **(A) Exploitants / partenaires** : achètent ou opèrent le site (cible n°1 de la
>   stratégie RTB du doc 10) ;
> - **(B) Clients du service** : consomment de la colocation / de l'hébergement ;
> - **(C) Angle « client-ancre »** : un premier gros utilisateur qui sécurise le projet.
>
> ⚠️ Réalité de cadrage : **1 MW à Rodez ne se remplit pas avec un seul client local.**
> Le montage gagnant est presque toujours **un exploitant qui apporte son carnet de
> clients** (famille A), éventuellement sécurisé par **un client-ancre** (famille C).
> Les gros acteurs mondiaux (Equinix, Digital Realty, hyperscalers) sont **hors cible**
> à cette échelle. Les fiches ci-dessous mêlent faits vérifiés et **[hypothèses de fit à
> confirmer]**.

---

## A. Exploitants / partenaires — la cible prioritaire

Ceux qui pourraient **acheter le site RTB**, **le co-développer**, ou **l'opérer** en y
amenant leur demande.

### A1. UltraEdge — **le meilleur fit, à contacter en priorité** ⭐
- **Qui** : n°1 français de l'edge (a repris les data centers de SFR), **400 M€
  d'investissement d'ici 2028**, ~248 sites, 90 edge data centers.
- **Modèle « Datapole »** : un data center majeur au cœur d'une grande ville **+ des sites
  d'hébergement de proximité dans un rayon de ~100 km**. Datapoles prévus à **Toulouse et
  Montpellier**.
- **Pourquoi ce site** : Rodez est à ~150 km de Toulouse et de Montpellier — **exactement
  le type de site satellite** que leur modèle agrège autour d'un datapole métropolitain.
  Puissance 1 MW disponible + fibre + foncier propre = ce qu'ils cherchent.
- **Comment approcher** : les contacter **quand le datapole Toulouse/Montpellier se
  précise**, en présentant un **site RTB clé en main** (électrifié, permis, fibre). Angle :
  « point de régénération / edge de proximité déjà dé-risqué ».

### A2. Opérateurs de colocation régionaux d'Occitanie
Ils cherchent à **mailler le territoire** (proximité, souveraineté, plan de reprise). Un
site à Rodez peut être un **satellite / site de secours (Disaster Recovery)** de leur base
toulousaine.

| Opérateur | Base | Pourquoi ce site | Contact / angle |
|---|---|---|---|
| **Adista** | Labège + Pamiers (via rachat Equadex) | cloud/colo de proximité en Occitanie ; Rodez élargit leur couverture territoriale | site DR / edge pour leurs clients Aveyron |
| **Etix Everywhere** | Toulouse | hébergement souverain pour entreprises et **organisations publiques** du Sud-Ouest | site de proximité / redondance régionale |
| **FullSave** | Toulouse (TLS00, 2 MW) + **Auch (AUC00)** | déjà présent en **villes moyennes** (Auch) — Rodez est une extension logique | carrier-neutral, expansion secondaire |
| **Cyllene / Cofely-type MSP régionaux** | variable | hébergeurs/infogéreurs cherchant capacité de proximité | **[à confirmer]** |

### A3. Acteurs « calcul / cloud souverain » et modulaire
- **Policloud** (déjà dans ta boucle) : fournisseur de conteneurs GPU — pourrait **déployer
  et exploiter** sur ton site RTB (tu es alors le « landlord », eux l'IT). C'est le pont
  direct avec les docs 03 et 09.
- **Scaleway / Outscale (Dassault) / OVHcloud** : cloud souverains français — plutôt
  intéressés par de gros sites, mais **à surveiller** pour de l'edge/souveraineté.
  **[fit à confirmer, probablement trop grands]**.
- Fabricants de modulaire (**Vertiv/MegaMod**, Modul Data Center, Module-IT) : **pas des
  acheteurs**, mais des **partenaires industriels** pour construire — utiles pour crédibiliser
  un dossier RTB.

### A4. Foncières / fonds d'infrastructure (pour une vente RTB pure)
- Pour un site de 1 MW, les grands fonds « powered land » (Hines, Silver Lake…) sont
  **trop gros**. En revanche, une **foncière régionale** ou un **développeur data center**
  agrégateur de sites secondaires peut être le bon acheteur du foncier RTB.
- **Angle énergie (ton atout)** : ta propre entreprise (**Tenergie**) ou un producteur EnR
  peut co-porter un « **green data center** » (électricité verte + foncier), montage que
  des fonds infra apprécient.

---

## B. Clients du service (colocation / hébergement de proximité)

Ils ne rachètent pas le site : ils **louent des baies / de la puissance**. Utiles pour
**démontrer la demande** (précommandes) et pour l'exploitation si tu opères toi-même.

### B1. ETI et industriels de l'Aveyron (proximité + souveraineté des données)
| Entreprise | Profil | Besoin data center plausible |
|---|---|---|
| **RAGT** (Rodez) | semencier international, **1 500+ salariés, 50 pays** | R&D génomique = **gros volumes de calcul/stockage**, souveraineté → **meilleur prospect local** |
| **Bosch** (Rodez) | usine (systèmes injection) | edge industriel, sauvegarde, IoT usine |
| **Lactalis AOP & Terroirs** (970 sal.) | agroalimentaire multi-sites | hébergement/sauvegarde multi-sites |
| **Société des Caves (Roquefort)** | agroalimentaire AOP | idem, proximité |
| **SOFOP / aéronautique** (Onet-le-Château) | industrie/défense | souveraineté, hébergement sensible |

*Angle commun* : proximité (latence, intervention rapide), **données qui restent en
Aveyron** (souveraineté locale), plan de reprise d'activité.

### B2. Secteur public et santé (souvent le meilleur client-ancre)
| Cible | Pourquoi | Point clé |
|---|---|---|
| **Centre Hospitalier de Rodez** (H. Jacques Puel) | données de santé | nécessite hébergement **HDS** → besoin récurrent et réglementé |
| **Département de l'Aveyron** | collectivité, numérique territorial | souveraineté, sauvegarde, cofinancements possibles |
| **Rodez Agglomération** | collectivité, aménageur de Bel-Air | **double casquette** : client **et** facilitateur du projet |
| **Éducation / IUT de Rodez** | recherche/formation | calcul, stockage |
| **Établissements de santé privés, EHPAD, cliniques** | HDS, sauvegarde | mutualisable |

> La **certification HDS** (Hébergement de Données de Santé) est un **différenciateur fort**
> et un marché captif régional (hôpitaux, cliniques, éditeurs santé). À étudier comme
> positionnement.

### B3. Écosystème IT local (revendeurs de capacité)
- **Infogéreurs / MSP / ESN de Rodez et Aveyron** (voir annuaires Kompass) : ils
  **revendent** de l'hébergement à leurs clients PME → un data center local leur évite
  d'envoyer les données à Toulouse/Paris. **Multiplicateur de demande** intéressant.

---

## C. Le client-ancre (à décrocher en premier)

Un **pré-engagement** d'un seul gros utilisateur change tout : il **dé-risque** le projet,
crédibilise le dossier RTB et facilite le financement. Les 3 candidats les plus crédibles :

1. **RAGT** — besoin calcul/stockage réel, ancrage ruthénois, image de souveraineté. **#1.**
2. **CH de Rodez / santé** — besoin HDS récurrent, acheteur public solide.
3. **Rodez Agglomération / Département** — souveraineté territoriale + rôle d'aménageur.

Un LOI (lettre d'intention) même non engageante de l'un d'eux vaut de l'or face à un
exploitant (famille A) ou face à ton père.

---

## D. Qui NE PAS cibler (pour ne pas perdre de temps)

- **Hyperscalers** (Google, AWS, Microsoft, Meta) : cherchent 50-1 000 MW, hors sujet.
- **Equinix, Digital Realty, DATA4** : colocation « wholesale/hub » métropolitaine, 1 MW
  à Rodez ne les intéresse pas.
- Ce sont ces acteurs qui rendent le powered land célèbre, mais **pas à ton échelle** —
  d'où le recentrage sur edge + régional + local (familles A/B/C).

---

## E. Plan d'approche recommandé (ordre)

1. **Décrocher une marque d'intérêt côté demande** (famille C) : sonder **RAGT**, le
   **CH de Rodez** et **Rodez Agglomération** → obtenir 1 LOI si possible.
2. **En parallèle, ouvrir le dialogue avec UltraEdge** (famille A1) sur le calendrier de
   leurs datapoles Toulouse/Montpellier, en présentant un **site RTB**.
3. **Élargir aux colocateurs régionaux** (Adista, Etix, FullSave) comme exploitants/
   acheteurs alternatifs, angle **DR / edge de proximité**.
4. **Garder Policloud** comme option d'exploitation « landlord » (tu loues le site, ils
   posent l'IT) — cohérent avec les docs 03/09.
5. Structurer un **teaser d'une page** (puissance 1 MW sécurisable, fibre, foncier propre
   dé-amianté, permis en cours, climat froid/PUE bas, souveraineté Occitanie nord) à
   envoyer à ces cibles.

> Prochain livrable possible : ce **teaser 1 page** (ou 1 slide) prêt à envoyer, + un
> tableau de suivi des contacts (CRM léger).

## Sources

- [UltraEdge lance ses Datapoles (proximité ~100 km) — DCmag](https://dcmag.fr/ultraedge-lance-officiellement-ses-datapoles-des-ecosystemes-dhebergement-de-proximite-ultra-connectes/)
- [UltraEdge : 400 M€ pour 7 datapoles régionaux (Toulouse, Montpellier…) — L'Usine Nouvelle](https://www.usinenouvelle.com/electronique-informatique/cloud-computing/datacenters/ultraedge-qui-a-repris-les-datacenters-de-sfr-veut-investir-400-millions-deuros-dici-a-2028-pour-creer-sept-datapoles-regionaux-en-france.647LJJKWMNA5XGD5RORUAULBPQ.html)
- [Data centers Occitanie — UltraEdge](https://www.ultraedge.com/en/regions/occitanie)
- [Adista Labège / Pamiers (via Equadex) — DataCenterMap](https://www.datacentermap.com/france/toulouse/adista-labege/)
- [Etix Everywhere Toulouse (hébergement souverain SW France)](https://www.etixeverywhere.com/data-centers-in-toulouse/)
- [FullSave Toulouse (2 MW) et Auch — DataCenterMap](https://www.datacentermap.com/france/toulouse/tls001/)
- [Les 10 plus grosses entreprises de l'Aveyron (RAGT, Bosch…) — Ecomnews](https://ecomnews.fr/news/quelles-sont-les-10-plus-grosses-entreprises-de-laveyron/)
- [Les 15 plus gros employeurs de l'Aveyron — Emploi LR](https://www.emploilr.com/actualites/les-15-plus-gros-employeurs-de-l-aveyron-publics-et-prives_7270.php)
- [Groupe RAGT (Rodez, 1 500+ collaborateurs)](https://onrecrute.enaveyron.fr/fr/fiche/ils-recrutent/entreprises/groupe-ragt_TFOCompanies710/)
