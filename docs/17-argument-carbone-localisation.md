# 17 — L'argument carbone de la localisation : ce que ça change pour le projet

> **Origine** : post LinkedIn de **Charles Gorintin** (cofondateur d'Alan et de Mistral AI),
> titré « *La même requête d'IA émet vingt fois moins…* ».
>
> ⚠️ **Avertissement de méthode** : le post **n'a pas pu être lu** (LinkedIn renvoie une
> erreur 403 aux accès automatisés, et le contenu n'est pas indexé). Ce document analyse
> donc **la thèse**, reconstituée et vérifiée à partir de sources publiques indépendantes —
> **pas le texte exact de l'auteur**. Les chiffres ci-dessous sont sourcés ; les nuances
> propres à son argumentation peuvent m'échapper.
> *(Colle le texte du post et je précise l'analyse.)*

---

## 1. La thèse, et sa solidité factuelle

**L'idée** : à requête d'IA identique, les émissions dépendent essentiellement du **mix
électrique du pays où tourne le data center**. Héberger en France plutôt qu'ailleurs
divise donc l'empreinte dans des proportions considérables.

### Les données vérifiées

| Pays | Intensité carbone de l'électricité |
|---|---|
| **France 2025** | **19,6 gCO₂e/kWh** — plus bas historique, 2ᵉ rang européen derrière la Norvège *(RTE, Bilan électrique 2025)* |
| France 2023 | 49 g |
| Allemagne 2023 | 366 g |
| Pologne 2023 | 636 g |

**Illustration concrète** : l'entraînement d'un même modèle type GPT-3 aurait émis
**93 t en France**, **485 t en Corée du Sud** et **858 t en Inde** — le seul mix
énergétique explique l'écart.

### Le facteur « 20× » est-il juste ?

Il est **plausible mais dépendant du couple choisi** :

| Comparaison | Rapport |
|---|---|
| France 2025 (19,6 g) vs Pologne (636 g) | **× 32** |
| France 2023 (49 g) vs Pologne | × 13 |
| France vs Allemagne | × 7,5 |
| France vs États-Unis (~370-400 g) | ≈ × 8 |
| GPT-3 : Inde vs France | × 9,2 |

→ « Vingt fois » se situe **dans la fourchette haute** : c'est vrai contre un réseau
très charbonné et en retenant le point bas français de 2025. Contre l'Allemagne ou les
États-Unis, l'ordre de grandeur réel est plutôt **×8**. **L'argument reste massivement
valable ; c'est le multiplicateur exact qui mérite prudence.**

### Précaution intellectuelle

Charles Gorintin est cofondateur de **Mistral AI**, acteur qui a un intérêt direct à
promouvoir l'hébergement de l'IA en France. Cela n'invalide en rien la thèse — **les
données publiques la confirment** — mais il faut citer RTE plutôt que le post quand on
s'en sert dans un dossier.

---

## 2. Le contexte : la France en fait un axe stratégique

Ce n'est pas un argument isolé, c'est une **politique et un mouvement de marché** :

- La France se positionne comme « **la première destination européenne pour l'infrastructure
  IA décarbonée** ».
- **Mistral AI** a sécurisé **96 MW à Fouju**, avec montée contractuelle à **200 MW**, et
  entraîne ses modèles à Bruyères-le-Châtel sur le mix bas carbone local (nucléaire + hydro).
- Un **mégacampus de 1,4 GW / 8,5 Md€** est en construction en Île-de-France.
- L'électricité ne pèse que **5 % du bilan carbone national** français, contre ~20 % en
  Allemagne, en Espagne et en moyenne UE.

---

## 3. Ce que ça change pour le projet de Rodez — l'analyse honnête

### 3.1 🟢 Un vent porteur au niveau national

L'argument valide le **marché** sur lequel le projet se place : la France est
structurellement le bon pays pour héberger du calcul. C'est un argument utile face à ton
père, face à un acheteur et face à un client.

### 3.2 🔴 Mais ce n'est **pas** un argument de site

**Attention au piège logique.** Si l'avantage vient du **mix électrique national**, alors
il est **identique partout en France** : Rodez n'est ni mieux ni moins bien loti que Fouju,
Marseille ou Bordeaux. Cet argument **ne différencie pas ton terrain** — il différencie
la France.

Pire : il est majoritairement mobilisé pour justifier des **campus à 100 MW – 1,4 GW en
Île-de-France**. Il crée de la demande pour l'infrastructure IA française en général, pas
pour un site de 1 MW en Aveyron. C'est cohérent avec la conclusion du **doc 14** : le vent
souffle fort, mais sur un autre segment que le tien.

### 3.3 🟢 En revanche, deux angles deviennent réellement différenciants

C'est ici que le sujet devient exploitable pour toi.

**a) Le PUE — l'altitude de Rodez est un multiplicateur du même argument**

L'empreinte d'une requête = *(énergie IT × PUE) × intensité carbone du réseau*.

Le mix français agit sur le **3ᵉ** facteur, identique partout. Mais le **PUE** dépend du
site : à ~590 m d'altitude, Rodez permet du **free cooling** une grande partie de l'année.

> Argument défendable : **mix français bas carbone × PUE bas grâce au climat** = l'un des
> plus faibles contenus carbone par unité de calcul accessibles en Europe. C'est cumulatif,
> et c'est **propre au site**.

**b) L'apport Tenergie — dépasser l'argument « réseau national »**

C'est ton avantage structurel, et il va **plus loin que le post** : produire ou contracter
de l'électricité renouvelable **locale** (PPA, autoconsommation, adossement à une centrale)
permet de revendiquer bien mieux qu'un mix national moyen — une **traçabilité de la
fourniture**. Cela renoue avec l'ADN du projet Next Compute (data centers sur sites PV).

C'est le seul angle qui transforme un argument macro (« la France est bas carbone ») en
un argument micro (« **ce site-ci** est bas carbone, et je peux le prouver »).

### 3.4 🟢 Un levier commercial concret : la contrainte réglementaire des clients

L'argument carbone cesse d'être du marketing quand il devient un **critère d'achat** :

- **CSRD** : les entreprises doivent reporter leurs émissions, y compris le **scope 3** —
  donc leur informatique hébergée.
- **Directive européenne sur l'efficacité énergétique** : reporting obligatoire pour les
  data centers **> 500 kW**.

→ Pour les cibles du **doc 12** (RAGT, CH de Rodez, collectivités, ETI aveyronnaises),
« hébergement local, bas carbone, données en Aveyron » devient un **argument de conformité**,
pas seulement de conviction. C'est ce qui rend un client-ancre plus facile à convaincre.

---

## 4. La contre-objection à préparer

Un interlocuteur averti dira :

> « Si c'est le mix national qui compte, et qu'il est bas carbone partout en France,
> pourquoi Rodez plutôt que la région parisienne, où sont la fibre et les clients ? »

**La réponse ne doit pas être le carbone** (il n'est pas discriminant), mais :

1. **La puissance disponible tout de suite** (2,5 MW à 260 m — la ressource rare, cf. doc 08) ;
2. **Le PUE** (climat d'altitude → coût d'exploitation réduit) ;
3. **Le foncier** disponible et bon marché, déjà artificialisé (argument ZAN) ;
4. **La proximité / souveraineté territoriale** pour des clients régionaux ;
5. **L'adossement possible à une production renouvelable** (Tenergie).

Le carbone est un **argument de renfort**, pas l'argument principal. L'utiliser comme
argument principal exposerait à cette objection.

---

## 5. À retenir pour le dossier

| Usage | Verdict |
|---|---|
| Prouver que le marché français du data center a un vent porteur | ✅ oui, solide et sourçable (RTE) |
| Différencier le site de Rodez d'un autre site français | ❌ non — le mix est national |
| Argument commercial auprès de clients soumis à CSRD | ✅ oui, combiné à la proximité |
| Argument **spécifique au site** | ✅ seulement via **PUE (altitude)** + **PPA renouvelable Tenergie** |
| Citer le post en source | ⚠️ préférer **RTE / Bilan électrique** — l'auteur est partie prenante (Mistral) |

**Action recommandée** : intégrer au futur teaser (doc 15) une ligne
« **électricité française bas carbone (19,6 gCO₂/kWh) + free cooling d'altitude + adossement
renouvelable possible** » — c'est la formulation qui capte l'argument **sans** s'exposer à
la contre-objection du §4.

## Sources

- [Bilan électrique 2025 — RTE (émissions)](https://analysesetdonnees.rte-france.com/en/annual-review-2025/ghg-emissions) · [chapitre Émissions 2024 (PDF)](https://assets.rte-france.com/analyse-et-donnees/2025-03/BE2024%20-%20Chapitre%20%C3%89missions.pdf)
- [Production d'électricité bas carbone en Europe — SFEN](https://www.sfen.org/rgn/production-delectricite-bas-carbone-en-europe-le-graphique-qui-souligne-la-singularite-francaise/)
- [Intensité carbone de l'électricité par pays — Selectra](https://selectra.info/energie/guides/environnement/intensite-carbone)
- [Empreinte carbone de l'IA (comparaison GPT-3 France / Corée / Inde) — Projet Celsius](https://projetcelsius.com/blog/empreinte-carbone-ia/)
- [France's energy advantage is its AI edge — The Next Web](https://thenextweb.com/news/france-energy-advantage-ai-data-centres)
- [Mistral : 96 MW à Fouju, montée à 200 MW — Global Data Center Hub](https://www.globaldatacenterhub.com/p/frances-85b-ai-campus-is-more-than)
- [The inside story of the French AI data center build-out — DCD](https://www.datacenterdynamics.com/en/analysis/france-ai-data-center-build-out-emmanuel-macron/)
- [Enquête annuelle Arcep sur l'empreinte du numérique (2026)](https://www.usine-digitale.fr/intelligence-artificielle/data-centers-la-consommation-electrique-explose-en-france-avec-lia-malgre-une-amelioration-de-lefficacite-energetique.XWCZSS5BL5FHDJ4I2FWOA3XY4A.html)
