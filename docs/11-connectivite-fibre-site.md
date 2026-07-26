# 11 — Connectivité fibre du site (ZA Bel-Air, Rodez)

> Vérification demandée : y a-t-il de la fibre au point GPS (44.372954, 2.544455), et
> est-ce un facteur bloquant ? Analyse documentaire (sources publiques). Les points de
> niveau « data center » (routes diversifiées, FTTO/fibre noire) demandent confirmation
> par devis opérateur — signalés **[À CONFIRMER]**.

---

## 1. Verdict en une phrase

**La fibre n'est pas un problème pour un projet edge / data center de 1 à 2,5 MW ici.**
La zone est très bien couverte en fibre, un réseau public structurant dessert le
territoire, et la fibre dédiée entreprise y est livrable. La **seule** limite réelle est
que Rodez n'est **pas un carrefour de dorsales nationales** — ce qui compte pour un
hyperscaler, mais **pas** pour ta cible (edge / colo régional). Ce constat **améliore**
la réserve « maillon faible fibre » que j'avais posée dans le doc 10.

---

## 2. Ce qu'on sait de la couverture au point GPS

| Niveau de fibre | Situation à Bel-Air / Onet-le-Château / Rodez | Pour un data center |
|---|---|---|
| **FTTH** (fibre mutualisée grand public/petit pro) | **Présente** : Orange déploie le FTTH **dans la ZA de Bel-Air** ; Onet-le-Château 98 % des locaux raccordables (19 armoires), Rodez 96 % (58 armoires) | base présente, mais **pas** le bon produit pour un DC (mutualisé, pas de GTR) |
| **RIP** (réseau d'initiative publique) | **ALL'Fibre / Alliance Très Haut Débit** (Orange Concession) couvre Aveyron-Lot-Lozère, DSP 25 ans, déploiement achevé en 2023, **91 %+ d'éligibilité en Aveyron** | **très favorable** : infrastructure publique récente + collecte structurée |
| **FTTO** (fibre dédiée entreprise, point-à-point, GTR 4 h) | Livrable nationalement via Orange, SFR Business, Bouygues, Ielo, Axione, Covage, Koesio… ; là où FTTH + RIP existent, la **FTTO/FTTE est généralement réalisable** en zone d'activités (sur devis + délai de construction) | **le bon produit** pour un DC — **[À CONFIRMER par devis]** |
| **Dorsale / backbone national** | Rodez dispose de nœuds opérateurs (NRO) et d'une collecte vers les hubs régionaux (**Toulouse ~150 km**), mais **n'est pas un carrefour de transit majeur** (contrairement à Toulouse, Montpellier, Marseille) | limite **seulement** pour l'hyperscale / la latence ultra-basse |

**Traduction concrète** : brancher le site en fibre professionnelle est **faisable et
banal** ; ce n'est ni cher ni long à l'échelle d'un projet edge. Ce qui manque, c'est la
**densité de dorsales** d'une métropole — non pertinent pour ta cible.

---

## 3. Ce que veut un data center (et où on en est)

Un data center n'a pas les mêmes besoins qu'un bureau. Par ordre d'importance :

1. **Fibre dédiée (FTTO) avec GTR** plutôt que FTTH mutualisée → **livrable ici** (à
   chiffrer). ✅ *a priori*
2. **Diversité de routes / redondance** (2 arrivées physiquement distinctes, pour éviter
   la coupure unique) → **[À CONFIRMER]** : c'est LE point à instruire sur site. En ZA
   desservie par un RIP, une seconde adduction est souvent possible mais pas garantie.
3. **Plusieurs opérateurs (carrier-neutral)** pour que les clients aient le choix → au
   moins 6 opérateurs commercialisent la fibre sur la commune ; côté FTTO, viser **2-3
   devis** (Orange, SFR Business, + un opérateur du RIP). ✅ *plausible*
4. **Proximité d'un point de peering / PoP majeur** (capacité, latence) → **Toulouse
   ~150 km** (~1,5-2 ms de latence aller-retour environ). Suffisant pour de l'edge/colo,
   faible pour de l'hyperscale. ⚠️ *acceptable pour ta cible*

---

## 4. Est-ce une problématique ? — mise en perspective

| Type de projet | La fibre à Rodez est-elle un frein ? |
|---|---|
| **Edge / conteneur (P100), 0,1–0,3 MW** | **Non.** FTTO standard suffit largement. |
| **Modulaire / colo régional, 1–2,5 MW** (ta cible) | **Non bloquant.** FTTO + une 2ᵉ route à sécuriser ; carrier-neutralité à organiser. |
| **RTB / powered land** (doc 10) | **Plutôt favorable** : la fibre était le 3ᵉ pilier du « powered land » et il est présent — ça **renforce** l'attractivité du site pour un acheteur edge/colo. |
| **Hyperscale (>50 MW)** | Oui, ce serait un frein — mais ce n'est pas ton marché (échelle + localisation). |

**Conclusion** : la connectivité **ne remet pas en cause** le projet ni la stratégie RTB.
Elle passe du statut de « maillon faible potentiel » (mon hypothèse prudente du doc 10) à
celui de « point **globalement favorable**, avec deux vérifications de terrain » (route
secondaire diversifiée + devis FTTO).

---

## 5. Actions de confirmation (rapides, avant tout engagement)

- [ ] **Tests d'éligibilité pro** à l'adresse exacte chez 2-3 opérateurs FTTO
  (Orange Business, SFR Business, opérateur du RIP ALL'Fibre) → prix + délai + débit.
- [ ] Demander à **Alliance Très Haut Débit (ALL'Fibre)** la présence d'un **NRO / point
  de collecte** proche de Bel-Air et la possibilité d'une **2ᵉ adduction diversifiée**.
- [ ] Vérifier la présence de **fibre noire / offres activées** mobilisables (Axione,
  Covage/Altitude, Ielo) pour un usage data center.
- [ ] Estimer la **latence vers Toulouse/Marseille** (PoP de peering) pour le dossier
  commercial.

---

## 6. Impact sur le dossier

- Le doc 10 (RTB) peut retirer la fibre de ses « risques majeurs » : elle devient un
  **atout** à mettre en avant auprès d'un acheteur (site électrifié **ET** connecté).
- Reste donc, comme **vrai** facteur discriminant de la stratégie RTB : **la demande /
  la localisation** (trouver l'acheteur edge/colo), pas l'infrastructure physique.

## Sources

- [Fibre à Onet-le-Château (12) : éligibilité, opérateurs, déploiement — Ariase](https://www.ariase.com/couverture/aveyron-12/onet-le-chateau)
- [Fibre à Rodez (12) : éligibilité, opérateurs, déploiement — Ariase](https://www.ariase.com/couverture/aveyron-12/rodez)
- [Alliance Très Haut Débit — RIP Aveyron / Lot / Lozère (ALL'Fibre)](https://fibre.guide/deploiement/rip/alliance-tres-haut-debit)
- [Développement du Très Haut Débit en Aveyron — Département de l'Aveyron](https://aveyron.fr/pages/numerique-innovation-energie/developpement-du-tres-haut-debit-par-le-deploiement-de-la-fibre-optique)
- [FTTO : la fibre dédiée aux entreprises (définition, GTR) — CDX Telecom](https://cdxtelecom.com/blog/reseaux/ftto/)
- [Fibre dédiée FTTO, débit garanti & GTR 4 h — SFR Business](https://www.sfrbusiness.fr/internet/tres-haut-debit/connect-integral/)
