# 01 — Contexte du projet

## Situation

- **Lieu** : parcelle à Rodez (Aveyron, 12). Point GPS à confirmer *(en attente — voir `data/site.yml`)*.
  > ⚠️ L'énoncé initial mentionne « Rodès » ; il existe une commune Rodès dans les
  > Pyrénées-Orientales (66), mais le département indiqué étant l'Aveyron, on retient
  > **Rodez (12000)** ou sa périphérie (Rodez Agglomération). À confirmer avec le point GPS.
- **Usage actuel** : dépôt d'une entreprise de couverture / étanchéité (bâtiment(s)
  d'activité, probablement en zone d'activités ou zone urbaine à vocation économique).
- **Propriétaire** : le père du porteur de projet.
- **Projet du propriétaire** : vendre la parcelle à une autre entreprise du BTP.

## Pourquoi un data center ici ?

L'usage actuel (dépôt BTP) suggère une parcelle **déjà artificialisée, en zone à vocation
économique**, ce qui est exactement le profil recherché dans la méthode Next Compute
(document interne, non versionné) : les sites en zone U / zone d'activités sont constructibles **de droit**
pour un usage industriel/tertiaire, contrairement aux zones A/N.

Atouts potentiels à vérifier :

- **Foncier maîtrisé** (négociation intra-familiale possible avant mise en vente).
- **Bâtiment existant** : possibilité de réemploi (data center en bâtiment) ou de pose de
  conteneurs sur cour/parking → économie de gros œuvre.
- **Climat** : Rodez est en altitude (~570–630 m), climat frais → bon potentiel de
  **free cooling** (nombre d'heures/an où l'air extérieur suffit à refroidir), donc PUE bas.
- **Marché local** : peu d'offre de colocation / edge dans l'Aveyron ; clients potentiels =
  collectivités, santé (CH de Rodez), ETI locales, opérateurs télécoms, souveraineté des
  données départementale.

## Points de vigilance dès maintenant

1. **Le raccordement Enedis est le chemin critique** (comme identifié sur Next Compute) :
   la puissance de soutirage disponible déterminera la taille maximale du projet.
2. **La vente est en cours de préparation** : le calendrier de l'étude doit être court
   pour que le scénario data center soit sur la table avant signature avec un acheteur BTP.
3. **Trois postures possibles** vis-à-vis du propriétaire, à arbitrer avec le business plan :
   - a) **Achat** de la parcelle par la société projet (valorisation à comparer à l'offre BTP) ;
   - b) **Bail long terme** (bail commercial ou emphytéotique) — le père garde le foncier
     et perçoit un loyer, potentiellement supérieur au rendement de la vente ;
   - c) **Division parcellaire** : vente d'une partie au BTP, conservation de l'emprise
     nécessaire au data center.
4. **Conflit d'intérêts familial** : formaliser la discussion avec une évaluation
   indépendante du foncier pour que la comparaison vente BTP vs projet DC soit objective.

## Livrable cible

Un **dossier de décision** pour le propriétaire :

- valeur de la parcelle en vente BTP (référence marché),
- valeur du projet data center (business plan : TRI, loyer possible, prix d'achat soutenable),
- risques et délais de chaque option.
