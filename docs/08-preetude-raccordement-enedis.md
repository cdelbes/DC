# 08 — Guide : pré-étude et raccordement Enedis (HTA)

> Objectif : transformer l'indication de la cartographie Enedis (2,5 MW de capacité
> « consommation » disponible, tronçon HTA à ~250 m) en une **offre chiffrée et
> engageante** (PTF), pour alimenter le business plan et fixer la puissance cible.

## 1. Ce que dit déjà la cartographie — et ses limites

**Relevé du porteur** (cartographie des capacités réseau, mon-compte-entreprise.enedis.fr) :
- Tronçon **HTA** arrivant jusqu'au point **44.3741348, 2.5473038**, soit **~250 m** de la
  parcelle (44.372954, 2.544455).
- **Capacité disponible « consommation » ≈ 2,5 MW** sur ce secteur.

**Bonne nouvelle — pourquoi :**
- 2,5 MW couvre **toute la trajectoire du projet** : MegaMod 1 MW, puis extension à 2 MW.
  La puissance n'est pas le facteur limitant, ce qui est rare et lève le risque n°1.
- Un départ HTA **déjà présent à 250 m** limite a priori l'ampleur (donc le coût et le
  délai) de l'extension de réseau — bien mieux qu'un raccordement à créer depuis un poste
  source lointain.

### Que signifie exactement « capacité disponible » ?

Question soulevée : le point à 250 m est **l'extrémité du tronçon HTA** portant
l'étiquette « Capacité disponible : 2,5 MW ». Est-ce 2,5 MW *restants* ou le
*dimensionnement* du câble (potentiellement déjà saturé) ?

**Réponse** : sur la cartographie Enedis, « **capacité disponible** » = capacité **encore
libre pour accueillir un nouveau raccordement sans renforcement** du réseau. Ce n'est
**pas** la capacité nominale du câble. C'est l'objet même de l'outil : montrer la
**marge** résiduelle. Un tronçon saturé afficherait une capacité disponible faible ou
nulle. Donc les 2,5 MW sont bien du **soutirable résiduel** à cet endroit (au mois de la
mise à jour). L'hypothèse « dimensionné 2,5 MW mais plus rien de libre » ne correspond
pas à ce que l'étiquette indique.

**Limites à garder en tête (à confirmer par Enedis, ne pas surinterpréter la carte) :**
1. **File d'attente non prise en compte.** La donnée est actualisée **mensuellement** et
   **n'intègre pas les demandes de raccordement en cours**. Un projet concurrent déjà
   déposé peut avoir consommé une partie des 2,5 MW sans apparaître. La capacité **n'est
   pas réservée** tant qu'il n'y a pas de **PTF acceptée + acompte** (règle du « premier
   arrivé »).
2. **Contrainte possiblement en amont.** Les 2,5 MW peuvent être bornés non par ce
   tronçon mais par le **poste source** (transfo HTB/HTA) qui l'alimente. La carte intègre
   les contraintes réseau, mais seule la **pré-étude** identifie l'élément limitant et
   confirme que 2,5 MW sont délivrables **jusqu'à la parcelle**.
3. **Point = extrémité du départ HTA.** Deux conséquences :
   - il faut **prolonger le HTA de ~250 m** (tranchée, câble, éventuel poste) → coût à la
     charge du demandeur (consommateur → pas de réfaction), l'un des postes majeurs du
     CAPEX ; et **chute de tension** à vérifier pour une forte puissance en bout de ligne ;
   - une extrémité de départ = alimentation **radiale (en antenne)**, sans bouclage. Pour
     la **résilience** d'un data center (secours N-1), une **seconde alimentation /
     bouclage** peut être souhaitable → coût supplémentaire à évaluer.
4. Le **poste de livraison HTA** (local + comptage) et son génie civil sont à la charge
   du projet, sur la parcelle.

## 2. Les niveaux d'étude Enedis (du moins au plus engageant)

| Niveau | Ce que ça donne | Engagement | Quand |
|---|---|---|---|
| Cartographie capacités | ordre de grandeur (fait ✅) | aucun | déjà fait |
| **Pré-étude** (facultative, portail entreprise) | estimation coût + délai + faisabilité pour une puissance donnée | aucun | **maintenant** |
| Demande de raccordement → **PTF** | offre technique et financière ferme, réserve la capacité | acompte à l'acceptation | scénario + foncier arrêtés |
| Convention de raccordement + travaux | réalisation | solde | après PC et décision d'investir |

**Stratégie recommandée** : lancer d'abord une **pré-étude** (gratuite, sans engagement)
pour 2 paliers — **1 MW** et **2 MW** — afin de comparer coût/délai et de caler le
business plan, puis ne demander la **PTF** que sur le palier retenu, une fois le CUb
obtenu et le foncier sécurisé.

## 3. Comment déposer la pré-étude / la demande

- **Portail** : `raccordement-entreprise-enedis.fr` (espace pro raccordement). Créer un
  compte, choisir **« Raccordement de locaux professionnels / entreprise »**, puissance
  **> 250 kVA → HTA**, motif « construction neuve ».
- La pré-étude est une **option proposée avant le dépôt du dossier complet** : elle
  estime coûts et délais sans engager.
- Alternative : contacter directement l'**Accueil Raccordement Électrique (ARE) Enedis**
  de la région Sud / Aveyron, ou passer par le **fournisseur d'électricité** (qui peut
  porter la demande d'accès au réseau).

### Informations à fournir (à préparer)

- [ ] Localisation précise : point GPS **44.372954, 2.544455** + référence cadastrale
- [ ] **Puissance de raccordement souhaitée** : demander **1 MW** et **2 MW** (2 scénarios)
- [ ] Usage : data center, fonctionnement **24/7, profil de charge plat** (~facteur de
      charge élevé — utile pour le tarif d'acheminement et la négociation fourniture)
- [ ] Type : construction neuve, alimentation **HTA**, poste de livraison privé prévu
- [ ] Date de mise en service visée (cohérente avec PC + travaux : viser T+18-24 mois)
- [ ] Existence éventuelle d'un **PDL/PRM** sur le site (compteur du dépôt actuel — à
      relever sur une facture ; un raccordement C4 existant peut servir de base)

### Questions à poser explicitement à Enedis

1. Le **départ HTA à ~250 m** peut-il acheminer 1 MW ? 2 MW ? Sinon, quel renforcement ?
2. **Coût** estimé du raccordement (extension HTA ~250 m + poste de livraison) par palier.
3. **Délai** de réalisation par palier (référence secteur : 4-6 mois si capacité dispo,
   6-9 mois + si renforcement).
4. La capacité de 2,5 MW est-elle **réservable**, et à quelles conditions
   (PTF + acompte) ? Y a-t-il des **demandes concurrentes en file d'attente** sur ce
   départ (non visibles sur la carte) ?
5. Les 2,5 MW affichés sont-ils limités par **ce départ HTA** ou par le **poste source**
   en amont ? La capacité tient-elle **jusqu'à la parcelle** après extension de ~250 m
   (chute de tension) ?
6. Le raccordement en **bout de départ (antenne)** est-il acceptable pour la puissance
   visée, ou faut-il un **bouclage / une 2ᵉ alimentation** (résilience) — et à quel coût ?
7. Quote-part éventuelle au titre d'un **S3REnR** (a priori non pour de la consommation).

## 4. Ce que la pré-étude alimente dans le business plan

- **CAPEX raccordement** = extension HTA (~250 m) + poste de livraison + comptage + génie
  civil. Ordre de grandeur à confirmer : de quelques dizaines de k€ (si simple extension)
  à plusieurs centaines de k€ (si renforcement/poste). ← **la pré-étude tranche.**
- **Délai raccordement** = jalon critique du planning (souvent le chemin le plus long
  avec le PC).
- **OPEX électricité** : la puissance souscrite (1 → 2 MW) et le profil 24/7 dimensionnent
  le TURPE (composante puissance) et le prix de fourniture à négocier en parallèle.

## 5. Enchaînement recommandé

```
Cartographie (fait : 2,5 MW dispo, HTA à 250 m)
   │
   ├─► Pré-étude Enedis 1 MW et 2 MW      (sans engagement)   ─┐
   │                                                            │ en parallèle
   └─► CUb (doc 07) + relevé cadastral/zonage                 ─┘
            │
            ▼
   Choix du scénario (1 MW ferme + réserve 2 MW ?)  → Business plan chiffré
            │
            ▼
   Demande de raccordement → PTF (réserve la capacité)   ── après décision d'investir
            │
            ▼
   Permis de construire → Convention de raccordement → Travaux → Mise en service
```

## Sources

- [Portail raccordement entreprise Enedis](https://www.raccordement-entreprise-enedis.fr/)
- [Fiches de collecte / formulaire pré-étude — Enedis](https://www.raccordement-entreprise-enedis.fr/Asset/Documents/DOC_21_pre-etude_et_formulaire_injection_plus_36_PV.pdf)
- [Procédure de traitement des demandes de raccordement — Enedis](https://www.enedis.fr/media/2173/download)
- [Raccordement électrique professionnel : guide 2026 — Acieb Énergie](https://www.aciebenergie.fr/guides/raccordement-electrique-professionnel-guide-2026/)
- Cartographie des capacités d'accueil : mon-compte-entreprise.enedis.fr (relevé du porteur).
