# 20 — Benchmark du foncier : le bien de la SCI vs le marché de la zone

> **Source des données du bien** : Pappers Immobilier, relevé le 02/08/2026 (captures
> fournies). **Ces données remplacent les estimations approximatives** des docs 06 et 13,
> qui reposaient sur une mesure Google Maps et une lecture de vue aérienne.

---

> 🔴 **CORRIGÉ PAR LE DOC 27** — les valorisations notariales obtenues auprès du
> propriétaire donnent **400 000 à 650 000 €**, contre 215-380 k€ estimés ici. L'erreur
> venait de la valorisation du bâtiment (200-400 €/m² retenus, alors que l'entrepôt à Rodez
> se négocie ~855 €/m²). **Utiliser les chiffres du doc 27.** Le multiple RTB s'en trouve
> réduit à **×1,23-1,6** sur une base de 650 k€.

## 1. Le bien — données exactes (enfin)

| Élément | Valeur | Commentaire |
|---|---|---|
| **Adresse** | 35 rue de la Ferronnerie, **12000 Rodez** | |
| **Parcelle** | **12202000BH0187** → **section BH n° 187** | Le code INSEE **12202 = Rodez** ✅ **confirme définitivement la commune** (le doute Rodez/Onet-le-Château du doc 06 est levé) |
| **Surface parcelle** | **2 631 m²** | |
| **Surface disponible (libre)** | **2 144 m²** | = 2 631 − 487 |
| **Bâtiment — emprise au sol** | **487 m²** | ⚠️ **bien plus petit que mon estimation antérieure** (900-1 100 m² à vue d'œil) |
| Hauteur du bâti | 4 m / 6 m | plain-pied |
| **Altitude** | **586 m** | ✅ confirme l'hypothèse free cooling du doc 17 |
| Usage déclaré | Tertiaire & Autres / **Industriel** | cohérent avec un zonage d'activités |
| **Acquisition** | **275 000 €** le **19/07/2018** | par la SCI |
| Propriétaire | 1 · Occupants : 2 · Personnes liées : 1 | |

> ⚠️ **Anomalie de donnée** : l'acte mentionne un lot de **2 786 m²** (« local industriel,
> commercial ou assimilé »), incompatible avec un bâtiment de 487 m² d'emprise en
> plain-pied sur une parcelle de 2 631 m². Le « 99 €/m² » affiché par Pappers est calculé
> sur cette base douteuse. **Ne pas utiliser ce ratio** — voir §3 pour les bons calculs.

### Corrections à reporter dans les autres documents

| Doc | Ancienne valeur | Valeur exacte |
|---|---|---|
| 06, 13, `site.yml` | surface 2 522 m² (mesure Maps) | **2 631 m²** |
| 06 | bâti ~900-1 100 m² | **487 m²** |
| 06 | commune « à confirmer » | **Rodez confirmé** (INSEE 12202) |
| 06 | parcelle « à confirmer » | **BH 187** |

---

## 2. Le benchmark de la zone

### 2.1 Terrain nu viabilisé — la référence la plus directe

| Zone | Prix | Remarque |
|---|---|---|
| **ZA Bel-Air** (la zone du bien) | **55 à 90 € HT/m²** | 133 ha au total, **2 ha encore disponibles**, vocation industrielle |
| ZA Les Cazals (Luc-la-Primaube / Olemps) | 65 à 135 €/m² | 54 lots, 931 à 3 600 m² |

→ **La référence à retenir pour ce bien est 55-90 €/m²** (sa propre zone), et non la
fourchette plus large de 65-135 €/m² que j'utilisais au doc 13.

### 2.2 Bâti industriel

| Référence | Valeur |
|---|---|
| Prix moyen d'un entrepôt à Rodez (2023) | **~855 €/m²** |
| Loyer entrepôt / local d'activité à Rodez | **~63 €/m²/an** (surface moyenne 547 m²) |
| Annonce comparable (ensemble bureaux + logement + entrepôt, 7 km du centre) | 211 500 € |

Le prix de 855 €/m² correspond à un entrepôt **en bon état**. Un hangar ancien à **toiture
amiantée** se négocie très en dessous : retenons **200 à 400 €/m²**.

### 2.3 💡 Trouvaille : le statut fiscal de la zone

**La ZA de Bel-Air bénéficie des statuts AFR (Aide à Finalité Régionale) et ZRR (Zone de
Revitalisation Rurale)**, ouvrant droit à des **aides régionales** et à des **exonérations
fiscales sous conditions** pour les entreprises qui s'y implantent.

> 🎯 **À vérifier en priorité pour le business plan** : si un projet de data center est
> éligible, cela peut alléger le CAPEX (subvention) et/ou l'IS et la CFE des premières
> années. **Question à poser à Rodez Agglomération en même temps que le CU** (doc 07).
> *(Réserve : la source rattache Bel-Air à Onet-le-Château ; la parcelle étant sur Rodez,
> l'éligibilité doit être confirmée commune par commune.)*

---

## 3. Le prix de 2018 était-il dans le marché ?

### Décomposition du prix payé

**275 000 € pour 2 631 m² de terrain + 487 m² de bâti.**

| Méthode | Calcul | Résultat |
|---|---|---|
| Prix rapporté au **terrain** | 275 000 / 2 631 | **104,5 €/m²** |
| Prix rapporté au **bâti** | 275 000 / 487 | 565 €/m² |
| *(Ratio Pappers, base douteuse)* | *275 000 / 2 786* | *99 €/m² — à ignorer* |

### Reconstitution à prix de marché 2018

*(Les prix 2018 sont estimés en dessous des prix 2026 actuels.)*

| Composante | Hypothèse 2018 | Valeur |
|---|---|---|
| Terrain 2 631 m² | 45 – 75 €/m² | 118 – 197 k€ |
| Bâti 487 m² (hangar) | 250 – 450 €/m² | 122 – 219 k€ |
| **Total reconstitué** | | **240 – 416 k€** |

### ✅ Verdict : achat dans le marché, plutôt bien négocié

**275 000 € se situe dans la partie basse-médiane de la fourchette reconstituée
(240-416 k€).** Il n'y a **pas de surpaiement** — l'acquisition de 2018 apparaît correcte,
voire légèrement avantageuse.

C'est une bonne nouvelle pour la discussion : le point de départ n'est pas biaisé par un
achat trop cher qu'il faudrait « rattraper ».

---

## 4. La valeur aujourd'hui (2026)

| Composante | Fourchette | Valeur |
|---|---|---|
| Terrain 2 631 m² (prix Bel-Air actuels) | 55 – 90 €/m² | **145 – 237 k€** |
| Bâti 487 m², hangar ancien, toiture amiantée | 200 – 400 €/m² | **97 – 195 k€** |
| **Sous-total** | | **242 – 432 k€** |
| **− Passif amiante** (désamiantage, doc 06) | | **− 25 à − 55 k€** |
| **= Valeur de marché estimée** | | **~215 – 380 k€** |
| **Point médian** | | **≈ 300 k€** |

> 📌 **C'est la valeur à confronter à l'offre réelle de l'acheteur BTP** — le chiffre qui
> manque toujours au dossier. Si l'offre est nettement au-dessus de 380 k€, elle est
> généreuse ; nettement en dessous de 215 k€, elle est faible.

**Évolution depuis 2018** : 275 k€ → ~300 k€, soit **+9 % en 8 ans** (~+1,1 %/an). Modeste,
mais cohérent avec un marché d'activité de ville moyenne, et **freiné par le passif
amiante** qui s'est alourdi (réglementation) depuis l'achat.

---

## 5. Le multiple RTB — l'analyse honnête

### 5.1 La mécanique

Passer en RTB implique de **démolir le bâti** (toiture amiantée). On **détruit donc une
valeur** (le hangar) pour en **créer une autre** (un terrain propre, électrifié, autorisé).

| | Valeur actuelle (avec bâti) | Valeur RTB (terrain nu dé-risqué) |
|---|---|---|
| Terrain | 145 – 237 k€ | 145 – 237 k€ |
| Bâti | +97 à +195 k€ | **0** (démoli) |
| Passif amiante | −25 à −55 k€ | **0** (traité) |
| **Survaleur de dé-risquage** *(doc 14 : raccordement 100-300 k€ + autorisations 20-50 k€ + désamiantage 25-55 k€ + temps)* | — | **+150 à +400 k€** |
| **TOTAL** | **215 – 380 k€** | **295 – 637 k€** |
| **Médian** | **≈ 300 k€** | **≈ 465 k€** |

### 5.2 Le multiple réaliste

| Comparaison | Multiple |
|---|---|
| **Valeur RTB médiane / valeur actuelle médiane** | **≈ × 1,55** |
| Fourchette basse | × 1,37 |
| Fourchette haute | × 1,68 |
| **Vs prix d'acquisition 2018 (275 k€)** | **≈ × 1,7** |
| **Gain net absolu** | **+ 80 k€ à + 260 k€** *(médian ≈ +165 k€)* |

### 5.3 Ce que ça veut dire — et il faut le dire clairement

**Le multiple RTB réaliste est de l'ordre de ×1,4 à ×1,7, pas de ×2 à ×4.**

Deux raisons, spécifiques à ce bien :

1. **Le bâti a de la valeur** (97-195 k€). Le démolir en détruit une partie, qu'il faut
   d'abord reconstituer avant de créer du gain net. Un terrain **nu** au départ aurait un
   multiple mécaniquement plus élevé.
2. **La survaleur RTB est bornée** par le coût de ce qu'on fait économiser à l'acheteur
   (méthode du doc 14), pas par un multiple de marché importé.

**Ce n'est pas décevant, c'est réaliste** : +165 k€ de gain médian pour un investissement
de dé-risquage de l'ordre de 150-400 k€ (raccordement, permis, désamiantage)… ce qui
signifie que **le gain net après dépenses est faible, voire nul, si l'on doit tout payer
soi-même**.

### 5.4 🔴 L'enseignement stratégique

Ce calcul révèle quelque chose d'important, qui n'apparaissait pas avant d'avoir les
chiffres exacts :

> **Si le porteur du projet finance lui-même la totalité du dé-risquage (raccordement,
> permis, désamiantage), la survaleur créée couvre à peine la dépense engagée.**

La rentabilité du montage RTB ne vient donc **pas** de la revente du foncier dé-risqué à
elle seule. Elle suppose l'un des trois leviers suivants :

1. **Faire porter une partie du coût par l'acquéreur/exploitant** (ex. : il paie le
   raccordement, on lui vend un terrain autorisé) ;
2. **Conserver le foncier en bail** plutôt que le vendre — le revenu récurrent capitalisé
   dépasse le gain de cession (doc 13, levier 2) ;
3. **Exploiter soi-même** (scénario Policloud / Next Compute, docs 09 et 16), où la
   valeur vient de l'exploitation et non du foncier.

→ Cela **renforce la recommandation du doc 14** : tester le marché **avant** de dépenser,
et **ne pas engager les frais de dé-risquage sans savoir qui paiera quoi**.

---

## 6. Synthèse pour la discussion avec le propriétaire

| Question | Réponse |
|---|---|
| Le bien a-t-il été payé au bon prix en 2018 ? | ✅ **Oui** — 275 k€ dans la partie basse-médiane du marché de l'époque |
| Combien vaut-il aujourd'hui ? | **~215 à 380 k€**, médian **~300 k€** (net du passif amiante) |
| Combien vaudrait-il en RTB ? | **~295 à 637 k€**, médian **~465 k€** |
| Quel multiple ? | **× 1,4 à × 1,7** — et non × 2 à × 4 |
| Gain net potentiel | **+ 80 à + 260 k€** (médian **+165 k€**) |
| Mais… | ce gain **couvre à peine** le coût du dé-risquage si l'on paie tout soi-même (§5.4) |
| Ce qu'il manque toujours | **le montant réel de l'offre BTP** — seule vraie référence à battre |
| Piste bonus à instruire | **statut AFR / ZRR** de la zone → aides et exonérations possibles |

## Sources

- Pappers Immobilier — fiche 35 rue de la Ferronnerie, 12000 Rodez (captures du 02/08/2026)
- [ZA Bel-Air : terrains à 55-90 € HT/m², statuts AFR et ZRR — Immo-Hub / Rodez Agglomération](https://immo-hub.org/parcs-d-activites/zone-dactivites-bel-air-agglomeration-de-rodez)
- [ZA Les Cazals : 65-135 €/m² — Immo-Hub](https://immo-hub.org/parcs-d-activites/1891-zone-dactivites-les-cazals-agglomeration-de-rodez)
- [Vente entrepôt / local d'activité à Rodez (prix moyen entrepôt ~855 €/m²) — Unemplacement](https://unemplacement.com/entrepots-vente/aveyron-12/rodez-12000)
- [Location entrepôt / local d'activité Rodez (~63 €/m²/an) — Unemplacement](https://unemplacement.com/entrepots/aveyron-12/rodez-12000)
- [Locaux d'activité / entrepôts à vendre à Rodez — SeLoger Bureaux & Commerces](https://www.seloger-bureaux-commerces.com/achat/local-d-activites-entrepot/midi-pyrenees/aveyron/rodez-12000)
- [Marché logistique et locaux d'activité France 2025 — CBRE](https://immobilier.cbre.fr/blog/entrepots/t4-2025-entrepot-logistique-en-france-un-m2-combien-deuros/) · [Knight Frank T3 2025 (PDF)](https://www.knightfrank.fr/fichiers/publications2020/file//kf-france-logistique-t3-2025-6904dd5537006400338202.pdf)
- Méthode de survaleur par coût de remplacement : `docs/14-etude-marche-powered-land-france.md`
