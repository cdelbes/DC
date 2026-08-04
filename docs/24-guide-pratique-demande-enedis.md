# 24 — Guide pratique : faire la demande Enedis, pas à pas

> Suite opérationnelle du doc 08 (méthode) et du doc 21 (plan). Ce document décrit
> **exactement quoi faire**, dans quel ordre, avec quel compte.

---

## ⚠️ 0. Le blocage à connaître avant de créer un compte

**Tu n'es pas propriétaire de la parcelle.** Elle appartient à la **SCI de ton père**. Or
Enedis exige, pour toute demande de raccordement :

> « L'**attestation d'information ou d'accord formalisé** est nécessaire **du propriétaire
> de l'unité foncière** sur lequel l'installation à raccorder est ou sera implantée **si le
> demandeur n'est pas propriétaire** de l'unité foncière. »

**Conséquence : tu ne peux pas déposer de demande ferme sans l'accord écrit de la SCI.**

Ce n'est pas une mauvaise nouvelle — c'est même une clarification utile : **la conversation
avec ton père est un prérequis, pas une étape parallèle.** Et comme tu dois de toute façon
lui demander le montant de l'offre BTP (doc 21), **fais les deux dans la même
conversation**. C'est elle qui débloque tout le reste.

---

## 1. Les deux niveaux de demande — ne pas les confondre

| | **Pré-étude** | **Demande de raccordement → PTF** |
|---|---|---|
| Nature | estimation de coût, délai, faisabilité | **offre technique et financière ferme** |
| Coût | **gratuite** | gratuite, mais **engage** dès acceptation (acompte) |
| Engagement | **aucun** | réserve la capacité réseau |
| Autorisation d'urbanisme requise | **non** | **oui** (permis de construire, à confirmer) |
| Accord du propriétaire | allégé (voir §2) | **obligatoire** |
| Validité | — | **3 mois** |
| Délai de réponse | quelques semaines | 2 à 6 semaines selon extension |

**Ce que tu veux aujourd'hui, c'est la PRÉ-ÉTUDE.** Elle répond à ta question — *combien ça
coûte, combien de temps* — sans rien engager et sans permis.

> ⚠️ Ne demande **pas** la PTF maintenant : elle suppose un permis de construire et
> l'accord formel du propriétaire, et son acceptation déclenche un acompte.

---

## 2. Qui doit être le « demandeur » ? — trois options

| Option | Qui dépose | Ce qu'il faut | Verdict |
|---|---|---|---|
| **A. La SCI dépose** | ton père (gérant) | KBIS de la SCI, compte Enedis au SIRET de la SCI | ✅ **le plus propre** — la SCI est propriétaire, aucun justificatif tiers |
| **B. Toi, mandaté par la SCI** ⭐ | toi | **mandat de représentation Enedis** signé par la SCI + KBIS | ✅ **le plus pratique** — tu pilotes, la SCI reste le demandeur |
| **C. Toi en ton nom propre** | toi | attestation d'accord du propriétaire | 🟡 possible mais bancal : tu n'as aucun droit sur le terrain |

### ⭐ La bonne solution : le mandat de représentation

Enedis publie un **formulaire type de « mandat de représentation pour le raccordement »**,
conçu exactement pour ce cas. Le **mandat simple** permet à un tiers d'exprimer la demande
de raccordement auprès d'Enedis **et de recevoir les informations confidentielles** qui s'y
rapportent.

**Concrètement** : ton père signe un mandat d'une page, tu deviens l'interlocuteur d'Enedis,
la SCI reste juridiquement le demandeur. Il ne s'engage à rien — un mandat n'est ni une
promesse de vente ni une autorisation de travaux.

📄 Formulaire : `enedis.fr/media/1926/download` (« Mandat de représentation pour le
raccordement »).

---

## 3. La question du compte — ne surtout pas utiliser celui de Tenergie

**Ton réflexe est le bon.** Trois raisons de ne pas mélanger :

1. **Conflit d'intérêts** : une demande personnelle déposée sous le SIRET de ton employeur
   est difficile à justifier a posteriori (doc 21 §7).
2. **Confusion sur le porteur** : le dossier resterait rattaché à Tenergie ; si le projet
   avance, démêler qui en est propriétaire serait pénible.
3. **Traçabilité** : les échanges Enedis sont archivés au nom du titulaire du compte.

### Quel compte créer, alors ?

Le portail `raccordement-entreprise-enedis.fr` rattache un compte à un **SIRET**.

- **Si option B (mandat)** → crée le compte avec le **SIRET de la SCI**, en te déclarant
  mandataire. C'est le chemin le plus simple : **tu n'as aucune structure à créer.**
- **Si tu tiens à une entité personnelle** → il faudrait créer une société (SASU…). **C'est
  prématuré** : ne monte pas une structure avant de savoir si le projet tient.

> 💡 **Ne crée pas de société pour faire une pré-étude.** Le mandat de la SCI suffit et
> coûte zéro euro.

---

## 4. Étapes, dans l'ordre

### Étape 1 — La conversation avec ton père *(le déblocage)*

Trois choses à obtenir en une fois :
1. le **montant de l'offre BTP** (doc 21) ;
2. son **accord de principe** pour une pré-étude au nom de la SCI ;
3. sa **signature du mandat de représentation** Enedis.

**Argumentaire** : *« C'est gratuit, ça n'engage à rien, ça ne bloque pas la vente, et ça
me donne le seul chiffre qui manque pour savoir si mon idée tient. Si la réponse est
mauvaise, j'arrête et tu vends. »*

### Étape 2 — Rassembler les informations

À préparer avant de remplir le formulaire :

| Élément | Valeur (déjà connue) |
|---|---|
| Adresse | 35 rue de la Ferronnerie, 12000 Rodez |
| **Parcelle cadastrale** | **12202000BH0187** (section BH n° 187) |
| Coordonnées GPS | 44.372954, 2.544455 |
| Surface parcelle | 2 631 m² |
| **Type de raccordement** | **consommation** (soutirage) — *surtout pas production* |
| **Puissances demandées** | **1 MW** et **2 MW** (deux scénarios) |
| Domaine de tension | **HTA** (> 250 kVA) |
| Nature du projet | construction neuve — data center modulaire, poste de livraison HTA privé |
| Profil de charge | **24/7, quasi constant** (facteur de charge élevé) |
| Date de mise en service visée | horizon **2028** (réaliste : 18-24 mois après décision) |
| PDL/PRM existant | à relever sur une facture d'électricité du dépôt |

📎 **Utile à joindre** : plan de situation et plan cadastral — tu peux les générer avec le
script du dépôt :
```bash
python scripts/fetch_maps.py 2.5444548605206823 44.37295358345457 rodez_
```

### Étape 3 — Créer le compte et déposer

1. Aller sur **`raccordement-entreprise-enedis.fr`**
2. Créer un compte avec le **SIRET de la SCI** (KBIS sous la main)
3. Choisir : **raccordement de locaux professionnels** → **consommation** → **> 250 kVA**
4. Sélectionner l'option **pré-étude** (proposée avant le dépôt du dossier complet)
5. Renseigner les informations de l'étape 2, **pour les deux paliers**
6. Joindre le **mandat signé** et le **KBIS de la SCI**

### Étape 4 — Poser les bonnes questions

À écrire explicitement dans le champ « commentaires » ou lors de l'échange avec le
conseiller (extrait du doc 08) :

1. Le **départ HTA situé à ~260 m** peut-il acheminer 1 MW ? 2 MW ? Sinon, quel renforcement ?
2. Quel est le **coût estimé** (extension HTA + poste de livraison) pour chaque palier ?
3. Quel **délai** de réalisation pour chaque palier ?
4. La capacité affichée sur la cartographie (2,5 MW) est-elle **réservable**, et **y a-t-il
   des demandes concurrentes en file d'attente** sur ce départ ?
5. La limite vient-elle **du départ** ou du **poste source amont** ? La capacité tient-elle
   **jusqu'à la parcelle** après extension (chute de tension) ?
6. Un raccordement **en bout de départ (antenne)** est-il acceptable, ou faut-il un
   **bouclage** pour la résilience — et à quel coût ?

---

## 5. Le raccourci si tu veux avancer avant la conversation

Si tu préfères tester le terrain avant d'impliquer ton père : **appelle Enedis**.

- Portail **`raccordement-entreprise-enedis.fr`** (formulaire de contact) ou l'**Accueil
  Raccordement Électrique** de la région.
- Présente-toi comme **développeur étudiant la faisabilité d'un projet** sur une parcelle
  dont tu n'es pas encore propriétaire, et demande **ce qu'il est possible d'obtenir à ce
  stade**.

C'est une question légitime et courante — les développeurs la posent en permanence. Tu
sauras en un appel si une estimation informelle est possible sans mandat, ce qui te fera
gagner du temps.

> ⚠️ **Mais ne fais pas ça depuis ton adresse professionnelle Tenergie.** Utilise une
> adresse personnelle.

---

## 6. Les pièges à éviter

| Piège | Pourquoi | À faire |
|---|---|---|
| Utiliser le compte **Tenergie** | conflit d'intérêts + dossier rattaché à l'employeur | compte au SIRET de la **SCI** |
| Demander la **PTF** au lieu de la pré-étude | suppose un permis, et l'acceptation engage financièrement | **pré-étude** d'abord |
| Cocher **« production »** | c'est le réflexe d'un développeur EnR — mais ici tu **consommes** | **consommation / soutirage** |
| Créer une **société** pour l'occasion | coût et complexité inutiles à ce stade | **mandat** de la SCI |
| Ne demander **qu'une seule puissance** | tu perds la comparaison | **1 MW *et* 2 MW** |
| Annoncer « **2,5 MW sécurisés** » | faux : la carte est indicative | « capacité indiquée, non réservée » |

---

## 7. Après la pré-étude — ce qui suivra

La pré-étude est **le déclencheur du reste** :

1. **Si le raccordement est peu coûteux** (extension simple, pas de renforcement) → le
   montage RTB devient viable, on enchaîne sur le CU puis la PTF.
2. **Si le raccordement est coûteux** (200-400 k€) → la survaleur ne couvre plus la dépense
   (doc 20 §5.4) → il faut soit **faire payer l'exploitant**, soit basculer sur le **bail**
   ou l'**exploitation**.
3. **Si la capacité n'est pas au rendez-vous** → le projet s'arrête, pour un coût de zéro
   euro.

Dans les trois cas, tu auras **la réponse la plus structurante du projet**, gratuitement.

---

## 8. Récapitulatif — la checklist

- [ ] **Conversation avec ton père** : offre BTP + accord de principe + signature du mandat
- [ ] Télécharger et faire signer le **mandat de représentation Enedis**
- [ ] Récupérer le **KBIS de la SCI**
- [ ] Relever le **PRM** sur une facture d'électricité du dépôt
- [ ] Générer les **cartes** (`scripts/fetch_maps.py`)
- [ ] Créer le compte sur **raccordement-entreprise-enedis.fr** (SIRET de la SCI)
- [ ] Déposer la **pré-étude** pour **1 MW et 2 MW**
- [ ] Joindre les **6 questions** du §4
- [ ] Relancer à **3 semaines** si pas de retour

## Sources

- [Mandat de représentation pour le raccordement — Enedis (formulaire)](https://www.enedis.fr/media/1926/download)
- [Demande de raccordement au réseau public de distribution — Enedis (pièces justificatives)](https://www.enedis.fr/media/2141/download) · [note externe demande de raccordement](https://www.enedis.fr/media/1947/download)
- [Je raccorde mon projet de bâtiment ou d'équipement — Enedis](https://www.enedis.fr/raccordement-batiment-professionnel-entreprise) · [Se raccorder ou modifier une installation](https://www.enedis.fr/se-raccorder-ou-modifier-une-installation)
- [Portail raccordement entreprise Enedis](https://www.raccordement-entreprise-enedis.fr/) · [base questions-réponses (PDF)](https://www.raccordement-entreprise-enedis.fr/Asset/Documents/Communication/Base%20Question-R%C3%A9ponse%20VF.pdf)
- [Raccordement Enedis : portail, prix, délais et procédure pas à pas — Selectra](https://selectra.info/energie/guides/demarches/enedis/raccordement)
- [Segments C1 à C5 (C3 = HTA, C4 = BT > 36 kVA) — Enedis](https://www.enedis.fr/faq/glossaire/quoi-correspondent-les-points-de-connexion-c1-c5)
- Méthode et questions à poser : `docs/08-preetude-raccordement-enedis.md`
