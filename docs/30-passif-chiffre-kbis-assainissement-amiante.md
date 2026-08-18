# 30 — Les trois documents du 17/08 : le passif enfin chiffré

> Documents reçus le 17/08/2026 : **Kbis à jour**, **contrôle de raccordement assainissement
> (Veolia / Rodez Agglomération)**, **devis de désamiantage + couverture neuve (DELBES SAS)**.
>
> **Deux verrous sautent, un passif de ~119 k€ TTC se documente, et une conclusion du doc 28
> doit être re-corrigée — dans l'autre sens.**

---

## 1. ✅ Le Kbis : verrou levé

| | |
|---|---|
| Émis le | **17/08/2026**, à jour au **16/08/2026** |
| Greffe | Tribunal de Commerce de **Rodez** · n° de gestion 2018D00141 |
| Code de vérification | `kjVyFadFxT` — contrôlable sur `controle.infogreffe.fr` |

**Moins de 3 mois : le dossier Enedis est complet de ce côté.** C'était le dernier point
bloquant identifié au doc 28 §5.

### ⚠️ Une donnée à corriger : le siège social

Le Kbis 2019 indiquait le siège au **35 rue de la Ferronnerie**. Le Kbis à jour dit autre
chose :

| | Kbis 2019 *(périmé)* | **Kbis 2026** |
|---|---|---|
| Siège | 35 rue de la Ferronnerie | **9 rue Paraire, Chez M. Delbès, Le Grand Balcon, 12000 Rodez** |
| Établissement principal | — | **9 rue Paraire** (idem) |
| Domicile du gérant | — | 9 rue Paraire, Le Grand Balcon, 12000 Rodez |

**Conséquence : le 35 rue de la Ferronnerie n'est pas un établissement de la SCI — c'est un
bien qu'elle donne à bail.** C'est cohérent avec l'objet social (*« exploitation par bail,
location ou autrement »*) et **cohérent avec ce que tu as déclaré à Enedis** (tu as bien
saisi « rue Paraire / Le Grand Balcon » comme siège, et la Ferronnerie comme adresse de
chantier). ✅ Rien à rectifier côté Enedis.

`data/site.yml` est corrigé en conséquence.

---

## 2. 🔴 L'assainissement : **NON CONFORME**, mise en conformité **immédiate**

C'est la réponse à la question laissée ouverte au doc 28 §4 — et **la réponse est la plus
défavorable des deux possibles**.

**Contrôle Veolia pour le service d'assainissement collectif de Rodez Agglomération,
réalisé le 25/06/2026, méthode : test de coloration.**

| Point contrôlé | Constat |
|---|---|
| **Conformité du raccordement** | 🔴 **NON CONFORME** |
| Réseau public | **Séparatif** (EU et EP distincts) |
| Constat 1 | *« Raccordé en **unitaire** sur le réseau public EU »* — les eaux pluviales partent dans le réseau d'eaux usées |
| Constat 2 | *« Manque les **regards de branchements** EU et EP, ou non accessibles lors du passage »* |
| Délai de raccordement de l'art. **L. 1331-1** du code de la santé publique | **Expiré : oui** |
| **Délai de mise en conformité** | 🔴 **Immédiat** |
| Validité du rapport | **5 ans** — mais **caduc en cas d'aménagement ou de modification** |

### Préconisations imposées

1. **Séparer les eaux pluviales des eaux usées**
2. **Poser les regards de branchement** ou les rendre accessibles

→ **C'est mot pour mot l'objet du devis PUECHOULTRES** (réseaux périphériques EP + EU,
regards avec tampons fonte) : **18 076 € HT / 21 691 € TTC**.

### Ce que ça change

| Avant | Maintenant |
|---|---|
| « devis en attente, caractère obligatoire à clarifier » *(doc 28)* | ✅ **obligatoire, constaté par le délégataire du service public, délai immédiat** |
| Argument de négociation hypothétique | 🎯 **argument documenté par un tiers, opposable, que tout notaire verra** |

**Trois conséquences pratiques :**

- **Pour la vente au BTP** : ce rapport sera au dossier de vente. Tout acquéreur déduira les
  21,7 k€ — ou exigera les travaux avant signature. Le contrôle a d'ailleurs été commandé
  **un mois avant la mise en vente**, donc vraisemblablement *pour* la vente.
- **Pour ton projet** : tu hérites du même passif. Ce n'est **pas** un différenciateur entre
  BTP et data center — c'est une déduction sur le prix, quel que soit l'acheteur.
- ⚠️ **La validité tombe si le bâtiment est modifié.** Une réhabilitation en data center
  imposera une **contre-visite**. À intégrer au planning, pas au budget (la contre-visite
  est peu coûteuse ; ce sont les travaux qui comptent).

> 💡 **Pression réglementaire réelle** : l'article L. 1331-1 du CSP impose le raccordement
> conforme, et le délai est **expiré**. La collectivité peut majorer la redevance
> d'assainissement (jusqu'au doublement) tant que la non-conformité persiste, voire faire
> exécuter les travaux d'office aux frais du propriétaire. Ce n'est pas théorique : c'est le
> levier habituel des agglomérations. **Question à poser à ton père : la redevance a-t-elle
> déjà été majorée ?**

---

## 3. 🔴 Le devis de désamiantage : je dois re-corriger le doc 28

**Et cette fois, c'est ma correction du doc 28 qui était fausse, pas mon estimation
initiale.**

**Devis DELBES SAS n° D-260258 du 03/05/2026** — *« Réfection couverture dépôt / bureaux
SAS DELBÈS »*. Validité expirée le **02/07/2026**.

### Le chiffrage

| Poste | Quantité | Montant HT |
|---|---|---|
| Plan de retrait amiante | forfait | **1 700,00 €** |
| Cabane de décontamination | forfait | **240,00 €** |
| **Démolition couverture amiantée** | **518,50 m²** × 41,00 € | **21 258,50 €** |
| **Évacuation + traitement** de la couverture | **518,50 m²** × 10,00 € | **5 185,00 €** |
| Empoussièrement / eau / déplacement | forfait | **4 420,00 €** |
| **➜ Sous-total strictement amiante** | | **≈ 32 803 € HT** *(≈ 39 400 € TTC)* |
| Couverture neuve **Ondatherm 40 mm** (panneau sandwich isolé) | 518,50 m² × 59,10 € | **30 643,35 €** |
| Gouttières, bavettes, closoirs, rives, faîtage, dépose, sécurité, bâchage | | le solde |
| **TOTAL DEVIS** | | **80 949,85 € HT** |
| TVA 20 % | | 16 189,97 € |
| **TOTAL TTC** | | **97 139,82 €** |
| Acompte à la commande (30 % TTC) | | **29 141,95 €** |

### 🔻 Ce que je dois corriger

Au doc 28 §1, j'écrivais que le passif amiante était *« nettement plus faible que
présenté »* et ne concernait *« qu'une partie de la couverture »*. **Le devis dit le
contraire sur la surface.**

| Sujet | Doc 28 | Réalité du devis | Verdict |
|---|---|---|---|
| Surface amiantée | « une partie seulement » | **518,50 m²** — soit **plus que l'emprise au sol (487 m²)** | ❌ **doc 28 faux** |
| Obligation réglementaire | liste B, **EP**, aucun retrait exigé | inchangé — le devis est **volontaire** | ✅ doc 28 juste |
| Coût du retrait | « bien plus faible que 25-55 k€ » | **≈ 32,8 k€ HT / 39,4 k€ TTC** | ✅ **mon estimation initiale de 25-55 k€ était bonne** ; c'est ma correction qui était fausse |

**La lecture juste, désormais :** la **totalité de la couverture** est en fibres-ciment
amianté ; **rien n'oblige à la retirer aujourd'hui** (liste B, évaluation périodique) ; mais
**dès qu'on y touche — démolition, réfection, ou percement pour des équipements techniques —
le retrait devient obligatoire et coûte ~33 k€ HT**, plus ~31 k€ HT si l'on remet une
couverture neuve isolée.

### ⚠️ Une incohérence à faire trancher

**518,50 m² de couverture amiantée > 487 m² d'emprise au sol.** C'est arithmétiquement
possible (une toiture en pente développe plus de surface que l'emprise), mais **incompatible
avec la lecture du diagnostic** retenue au doc 28, selon laquelle la zone « Stockage » serait
couverte en **bacs acier non amiantés**.

**Question à poser à ton père ou à DELBES SAS** :

> *« Les 518,50 m² du devis couvrent-ils l'intégralité de la toiture, ou seulement la partie
> fibres-ciment ? Et que devient la zone en bacs acier mentionnée au diagnostic ? »*

Tant que ce n'est pas tranché, **retiens l'hypothèse haute** (toute la toiture amiantée) :
c'est celle du devis, et c'est celle qu'un acquéreur retiendra.

### 📌 Trois observations qui comptent

**a) Le devis émane de DELBES SAS — l'occupant du bâtiment, et une entreprise du même nom.**
En-tête : *DELBES SAS, 35 rue de la Ferronnerie, ZA de Bel-Air — Couverture / Étanchéité*,
SIRET 427 280 508 00024, capital 150 000 €, qualifiée RGE Qualibat. Le devis est adressé à
*« Mr DELBÈS Jacques »* et décrit *« la couverture dépôt/bureaux SAS DELBÈS »*.

> C'est donc **l'entreprise locataire qui a chiffré la réfection du toit de son propre
> dépôt**, pour le compte du propriétaire. Un acquéreur tiers pourra considérer ce devis
> comme **un prix entre parties liées** et demander une contre-offre. **À faire confirmer :
> quel est exactement le lien entre ton père et DELBES SAS ?**

**b) 🎯 C'est la piste la plus directe pour le PRM.** DELBES SAS occupe le bâtiment : c'est
donc **elle qui détient le contrat d'électricité du dépôt**. Plutôt que d'attendre le retour
du diagnostiqueur, demande une facture d'électricité :
- **Tél. 05 65 42 53 50** · **contact@delbes-aveyron.fr**
- Interlocuteur cité sur le devis : **LEGRUX Frédéric**
- Ou, plus simple : **demande-la directement à ton père.**

**c) Le doc 28 posait la question « a-t-il déjà fait faire un devis de désamiantage ? »
→ Oui, en mai 2026. La réponse est là.**

---

## 4. Le passif total, et ce qu'il fait au prix

| Poste | Montant TTC | Statut |
|---|---|---|
| **Mise en conformité assainissement** | **21 692 €** | 🔴 **Obligatoire**, délai immédiat, constaté par un tiers |
| **Retrait amiante seul** | **≈ 39 400 €** | 🟡 Non obligatoire aujourd'hui — **obligatoire dès qu'on touche à la toiture** |
| **Retrait + couverture neuve isolée** | **97 140 €** | 🟡 Devis complet, validité expirée |
| **Fourchette de passif documenté** | **≈ 61 000 à 118 800 €** | |

### Effet sur le prix affiché

Ton père vise **650 000 €** (doc 27). Face à un acquéreur informé :

| Profil d'acquéreur | Ce qu'il déduit | Prix net probable |
|---|---|---|
| **BTP qui conserve le bâtiment** | assainissement + toiture complète | **≈ 530 – 555 k€** |
| **BTP qui démolit** | assainissement + retrait amiante *(obligatoire avant démolition)* | **≈ 590 k€** |
| **Toi, en réhabilitation data center** | les deux, plus l'adaptation technique | **≈ 530 k€** |

> ✅ **Cela confirme l'estimation du doc 27** : *« 650 k€ est un prix d'affichage ; la
> transaction se fera plutôt entre 450 et 550 k€. »* Le passif documenté explique
> précisément l'écart.

### 🎯 Ce que ça change pour ta négociation

C'est **beaucoup plus solide** que ce que tu avais avant, et surtout **ce n'est pas toi qui
le dis** :

- le **délégataire du service public** a écrit « non conforme, délai immédiat » ;
- **l'entreprise de couverture** a chiffré 97 140 € TTC.

**Formulation à privilégier auprès de ton père** — ne pas transformer ça en marchandage,
mais en information utile (doc 25 : son moteur est la **tranquillité**) :

> *« Les deux documents que tu m'as envoyés vont peser sur la vente, quel que soit
> l'acheteur. L'assainissement est déclaré non conforme avec mise en conformité immédiate :
> 21 700 €. Et la toiture est amiantée sur toute sa surface, avec ton devis à 97 000 €.
> Un acquéreur va déduire ça du prix. Ça veut dire que les 650 000 € vont être difficiles à
> tenir — ce n'est pas moi qui le dis, c'est le rapport de Rodez Agglo. »*

C'est le bon moment pour **recalibrer le « ×2 »** en même temps (doc 27 §3) : tu apportes
une mauvaise nouvelle qui ne vient pas de toi, et une correction qui vient de toi. Les deux
ensemble passent mieux.

### ⚠️ Et pour ton propre montage

Attention à l'effet ciseau : si tu prends une **promesse de vente à 650 k€**, tu hérites de
~119 k€ de travaux **en plus** du raccordement. La survaleur RTB (**+150 à +400 k€**,
doc 14) doit alors couvrir *le raccordement **et** le passif bâtiment*. **Le montage ne tient
que si la promesse est signée à un prix qui intègre le passif — autour de 530-550 k€, pas
650 k€.** Ce n'est pas de la négociation agressive : c'est le prix qu'un tiers paierait.

---

## 5. Actions

### Immédiat
- [x] ✅ **Kbis à jour** — obtenu, joignable au dossier Enedis
- [ ] 🎯 **PRM** : appeler **DELBES SAS (05 65 42 53 50)** ou demander la facture à ton père
- [ ] Faire trancher l'**incohérence des 518,50 m²** (devis) vs la lecture du diagnostic
- [ ] Demander à ton père si la **redevance d'assainissement a été majorée**

### Avant / pendant le RDV Enedis
- [ ] Signaler la **non-conformité assainissement** : les travaux de raccordement électrique
      et ceux d'assainissement ouvrent tous deux des tranchées — **il y a une mutualisation
      possible**, et donc une économie à chercher
- [ ] Les 12 questions du **doc 29 §4** restent la priorité

### Conversation avec ton père
- [ ] Le passif documenté (§4) — **en même temps** que le recalibrage du « ×2 »
- [ ] Le lien exact avec **DELBES SAS**
- [ ] Toujours en attente : **le montant de l'offre BTP**

---

## 6. Synthèse

| Sujet | Avant | Après ces trois documents |
|---|---|---|
| **Kbis** | ⚠️ périmé, bloquant | ✅ **à jour au 16/08/2026** |
| **Siège de la SCI** | 35 rue de la Ferronnerie | ✅ **9 rue Paraire** — la Ferronnerie est un bien loué |
| **Assainissement** | « obligatoire ? à clarifier » | 🔴 **NON CONFORME, délai immédiat — 21 692 € TTC dus** |
| **Surface amiantée** | « une partie seulement » *(doc 28)* | 🔴 **518,50 m² — toute la toiture** *(à faire confirmer)* |
| **Coût du désamiantage** | « bien plus faible que 25-55 k€ » | 🔴 **32,8 k€ HT — mon estimation initiale était juste** |
| **Devis désamiantage existant ?** | question ouverte | ✅ **oui, 97 140 € TTC, mai 2026** |
| **Piste PRM** | diagnostiqueur | 🎯 **DELBES SAS, occupant du bâtiment** |
| **Passif documenté total** | inconnu | **61 000 à 118 800 € TTC** |
