# 14 — Étude de marché : le « powered land » en France existe-t-il pour un site de 1-2 MW ?

> **Question posée** : existe-t-il en France des foncières qui vendent des parcelles
> « powered land » (foncier électrifié, prêt à bâtir) pour des data centers modulaires de
> 500 kW à 2 MW ? Quelle est la valeur du foncier ? Y a-t-il vraiment une survaleur ?
>
> **Méthode** : recherche documentaire sur les acteurs français nommés, les transactions
> publiques, les critères d'implantation des opérateurs, et les références de valeur.
> Ce document sépare volontairement **ce qui est vérifié** de **ce qui est déduit**.
>
> ⚠️ **Ce document est écrit pour te convaincre toi-même avant de convaincre ton père.**
> Il contient donc autant les mauvaises nouvelles que les bonnes.

---

## 0. Verdict en trois phrases

1. **Oui, le marché du powered land existe en France** — il est structuré, avec des
   acteurs nommés (Hadès Patrimoine, Datalok, EDF, Altarea, l'État), ce n'est pas une
   mode importée des États-Unis.
2. **Non, ton site de 1-2 MW n'est pas dans ce marché-là.** Le powered land français se
   négocie sur des terrains de **18 à 150+ hectares** pour **50 MW à 1 GW**. Tu as
   **0,25 hectare** et 2,5 MW — soit 70 à 600 fois plus petit.
3. **Une survaleur existe quand même, mais elle n'est pas « ×2 à 4 »** : elle est
   **bornée par ce que tu fais économiser à l'acheteur** (raccordement + autorisations +
   temps), soit un ordre de grandeur de **+150 à +400 k€**, pas un multiple spectaculaire.

---

## 1. Le marché existe : les acteurs français vérifiés

C'est la bonne nouvelle, et elle est solide. Le « powered land » n'est pas un concept
théorique en France — il y a des sociétés dont c'est le métier.

| Acteur | Nature | Ce qu'il fait exactement | Échelle |
|---|---|---|---|
| **Hadès Patrimoine / Hadès Data Center** | Family office, Paris 8e, créé 2017, membre de France Datacenter | **Le plus proche de ton idée.** Portefeuille exclusif de sites « Powered Land » sur le territoire. Obtient permis + ICPE **purgés de recours**, livre en clé en main soit en *powered land* (terrain + poste), soit en *powered shell* (bâtiment clos prêt à équiper) | non publiée |
| **Datalok** | Place de marché + conseil immobilier data center | Marketplace de vente/achat de data centers et terrains, **activité de conseil dédiée aux acquisitions foncières** avec potentiel de raccordement ; accompagne des investisseurs avec des LOI | annonces de 1,6 MW à 150 MW |
| **EDF** | Énergéticien | Ouvre son foncier industriel (ex-centrales) aux data centers via des **AMI**, précisément pour le raccordement déjà en place. Objectif ~2 GW | 100+ MW/site |
| **Altarea** | Promoteur immobilier coté | Détient près de Bordeaux un terrain avec **400 MW sécurisés**, apporté à Vantage Data Centers | 400 MW |
| **L'État français** | Politique publique | **35 sites « clés en main »** annoncés au Sommet de l'IA (fév. 2025), dont 26 déjà sécurisés par des développeurs | **18 à 150+ ha**, jusqu'à 1 GW |

**Ce que ça prouve** : ton intuition de départ était juste. Le métier « sécuriser du
foncier + de la puissance + des autorisations, puis le vendre » **est un vrai métier en
France**, exercé par des professionnels, avec des transactions réelles.

**Ce que ça ne prouve pas** : que ce marché descend jusqu'à 1 MW sur 2 500 m².

---

## 2. Le problème de segmentation : où est le marché, où es-tu

C'est le cœur de l'étude, et le point qu'il faut regarder en face.

### Là où se fait le powered land français

| Référence | Surface | Puissance |
|---|---|---|
| Sites « clés en main » de l'État | **18 à 150+ ha** | jusqu'à 1 GW ; 15 sites raccordables à 750 MW |
| Terrain Altarea (Bordeaux) | plusieurs ha | 400 MW |
| Sites EDF (Montereau, La Maxe, Richemont) | ex-sites industriels | ~2 GW cumulés |
| Standard international greenfield | **50-500 acres** (20-200 ha) | multi-MW à GW |
| Annonce Datalok (France centrale) | **12 ha** | **150 MW** |

### Ton site

| | Ton site | Ratio |
|---|---|---|
| Surface | **0,25 ha** | **70 à 600× plus petit** |
| Puissance | **2,5 MW** max | **60 à 400× plus petit** |

**Conclusion sans détour** : quand la presse et les rapports parlent de « la ruée sur le
powered land », **ils ne parlent pas de ton segment**. Les multiples spectaculaires
(Peterson : 32 M$ → 302 M$ en Virginie) viennent de ce marché-là, pas du tien. Il faut
retirer cet argument du dossier — ou l'utiliser seulement comme preuve que *le concept*
fonctionne, jamais comme référence de prix.

---

## 3. Le segment 1-2 MW existe-t-il ? Oui — mais il fonctionne autrement

Bonne nouvelle : **les data centers de 0,5 à 2 MW sont une catégorie reconnue** (« edge »),
et ils sont même majoritaires en nombre en France.

- La France compte **~285 à 350 data centers** en service pour **~1 100 MW IT** — soit une
  **moyenne de ~3-4 MW par site**. La majorité correspond à des « installations plus
  modestes », de « quelques mégawatts ».
- Les edge data centers sont définis précisément dans la fourchette **0,5 à 2 MW**.
- Des opérateurs edge sont actifs en France : **nLighten** (8 sites en France, 30+ en
  Europe), **Etix Everywhere**, **UltraEdge**, **Adista**, **FullSave**.

### Mais — et c'est décisif — voici comment ils grandissent

**Ils rachètent des data centers existants qui tournent, pas du terrain nu.**

Exemples vérifiés pour nLighten, le plus actif :
- rachat d'**Euclyde** (6 sites : Sophia Antipolis, Lyon, Strasbourg, Besançon, Paris) ;
- rachat de **7 edge data centers à EXA Infrastructure** ;
- rachat du site d'**oXya** à Émerainville (fév. 2026).

C'est un marché de **consolidation d'actifs en exploitation** — avec des clients, du
chiffre d'affaires, des baies remplies. Pas un marché d'achat de parcelles à équiper.

**Traduction pour toi** : l'acheteur naturel d'un site edge n'achète pas *du potentiel*,
il achète *un business*. C'est une différence de nature, pas de degré.

---

## 4. Le critère qui coince : la localisation

Les critères d'implantation edge sont documentés et convergents :

- Être **dans le rayon de latence** de la population servie : typiquement **20-50 km des
  grands centres d'emploi**, dans l'anneau métropolitain.
- Être proche de zones **suffisamment denses en PME et grandes entreprises** pour
  justifier la viabilité de la demande edge.
- Les stratégies edge procèdent par **criblage de 20 à 50 métropoles cibles**.
- Constat explicite du marché français : pour l'edge, « la seule solution financièrement
  viable est de **transformer des sites existants** » situés **dans les aires
  métropolitaines**.

**Rodez Agglomération, c'est ~60 000 habitants.** Ce n'est pas une métropole cible. Sur
les grilles de criblage edge standard, le site ne passe pas le premier filtre.

### La contre-hypothèse : l'IA/HPC ne dépend pas de la latence

C'est vrai, et c'est ton meilleur contre-argument : pour **entraîner** des modèles, « il
n'est plus nécessaire d'être proche des grandes villes », et on voit arriver des projets
en zone rurale ou péri-urbaine. Le Bosquel (Somme, commune rurale) accueillera un centre
de calcul IA majeur.

**Mais** : ces projets ruraux se font « de **plusieurs centaines de mégawatts** sur des
sites de **plusieurs dizaines d'hectares** ». La ruralité est acceptée **à condition d'une
échelle massive**. Le rural + petit, c'est le croisement le moins couvert du marché.

### Où va la capacité, en France

Les régions qui captent les projets grâce à des réseaux disponibles sont les
**Hauts-de-France, le Grand Est et la vallée du Rhône**. L'Occitanie n'apparaît pas dans
les dynamiques citées ; Rodez encore moins.

---

## 5. La valeur : ce qu'on sait vraiment

### Le constat méthodologique d'abord

**Il n'existe pas de référentiel public €/MW pour le powered land français.** Le marché
est de gré à gré, opaque, sans base de comparables accessible. Toute personne qui te
donne un prix « au MW » en France sans transaction à l'appui extrapole.

### Les points de repère disponibles

| Référence | Valeur | Ce que ça dit |
|---|---|---|
| Foncier ZA agglo de Rodez | **65-135 €/m²** | ta base : ~164-340 k€ pour 2 522 m² |
| Data center Tier III **1,6 MW** en exploitation, France centrale (annonce Datalok) | **3,5 M€** (2 450 m², 730 m² de salle IT) | **le comparable le plus proche de ton échelle** — mais c'est un actif **en exploitation**, pas du terrain |
| Cession SFR → UltraEdge : **45 MW** | **764 M€** (70 %) | ~**17 M€/MW** pour des data centers **avec clients** |
| Coût de construction | **~11,3 M$/MW** (2026) | ce que coûte *construire*, pas ce que vaut le terrain |
| Prime powered land (Europe) | **×2 à 4** | documenté — mais **sur des sites à l'échelle**, pas 1 MW |

### La bonne façon de calculer TA survaleur (analyse par coût de remplacement)

Plutôt que d'emprunter un multiple américain, raisonnons comme le ferait l'acheteur.
Il paiera une prime **au maximum égale à ce que le site lui fait économiser** :

| Ce que tu lui évites | Valeur pour lui |
|---|---|
| Coût du raccordement (extension HTA ~250 m + poste de livraison) | **~100-300 k€** *(à confirmer par la pré-étude Enedis)* |
| Autorisations obtenues et purgées de recours (PC, ICPE) | **~20-50 k€** de frais + suppression de l'aléa |
| Désamiantage + démolition déjà faits | **~25-55 k€** |
| **Le temps gagné** : 3-4 ans de délai de raccordement évités | difficile à chiffrer, mais c'est **le vrai moteur** du marché |

**Fourchette de survaleur défendable : +150 à +400 k€** au-dessus de la valeur foncière
de base.

| | Valeur |
|---|---|
| Foncier nu (base marché) | 164 000 – 340 000 € |
| **Foncier RTB (base + survaleur par coût de remplacement)** | **~320 000 – 700 000 €** |

C'est **moins flatteur** que le « ×2 à 4 » du doc 10, mais c'est **défendable devant ton
père, un banquier ou un acheteur** — parce que chaque euro est justifié par un coût évité.
Je recommande de retenir cette méthode et d'abandonner le multiple.

> ⚠️ **Réserve majeure** : cette survaleur ne se matérialise **que s'il existe un
> acheteur**. Une survaleur théorique sur un marché sans acheteur vaut zéro. C'est le
> point n°1 à tester (§7).

---

## 6. Réponses directes à tes questions

**« Est-ce que ça existe ? »**
→ **Oui** pour le concept et le métier en France (Hadès Patrimoine fait exactement ça).
→ **Pas de façon documentée** pour des parcelles de 1-2 MW vendues comme powered land :
aucune foncière identifiée ne cible publiquement ce segment. Datalok n'avait **aucune
annonce active** au moment de l'étude — signal d'un marché **peu liquide**.

**« Quelle est la valeur du foncier ? »**
→ Base : **164-340 k€**. Avec dé-risquage : **~320-700 k€** (méthode coût de remplacement).
→ Aucun référentiel public €/MW n'existe en France pour valider mieux que ça.

**« Y a-t-il vraiment une survaleur ? »**
→ **Oui, mais modérée et conditionnelle.** Réelle en logique économique (tu supprimes un
coût et 3-4 ans d'attente). Conditionnelle car elle suppose un acheteur, et le vivier
d'acheteurs pour ton profil (petit + hors métropole) est **étroit**.

---

## 7. Ce qui devrait être vrai pour que ça marche

C'est la partie la plus utile : au lieu de conclure oui/non, voici les **conditions
falsifiables**. Si elles se vérifient, fonce. Sinon, il faut renoncer.

| # | Condition à vérifier | Comment | Si NON |
|---|---|---|---|
| 1 | **Au moins un acheteur/exploitant se déclare intéressé** par un site 1-2 MW à Rodez | Contacter Hadès Patrimoine, Datalok (conseil), UltraEdge, Adista, Etix, FullSave, nLighten | ⛔ le RTB pur n'a pas de sortie → revenir à l'exploitation ou à la vente BTP |
| 2 | **Le coût de raccordement est bas** (extension courte, pas de renforcement) | Pré-étude Enedis (doc 08) | 🔻 la survaleur s'effondre : si raccorder coûte 400 k€, tu ne fais économiser à personne |
| 3 | **Un client-ancre local existe** (RAGT, CH Rodez, collectivité) | Sondage direct (doc 12) | 🔻 sans demande locale, seul l'angle « site pour opérateur » subsiste |
| 4 | **La capacité 2,5 MW est réservable et transférable** | Question à Enedis (doc 08) | ⛔ tu ne vends pas de la puissance, juste un terrain |

**La condition n°1 est éliminatoire.** Elle se teste en quelques appels et quelques
semaines, pour un coût quasi nul. **C'est ce qu'il faut faire avant toute autre chose** —
avant même le CU, avant la PTF.

---

## 8. Mon avis honnête

**Ce qui tient debout :**
- Le concept est validé et pratiqué en France. Tu n'inventes rien de farfelu.
- Ta puissance disponible (2,5 MW immédiats) est objectivement rare et a de la valeur.
- La logique économique de la survaleur est saine (coûts et délais évités).
- Le désamiantage crée une valeur réelle, indépendante du marché data center.
- Le risque pour ton père reste faible, et l'argument « donne-moi le temps de tester »
  reste **entièrement valable**.

**Ce qui ne tient pas :**
- L'argument « le powered land vaut ×2 à 4, regarde la Virginie » : **à retirer**. Ce
  n'est pas ton marché, et un interlocuteur averti te le fera remarquer.
- L'idée qu'une foncière spécialisée viendrait acheter ton terrain : **non documentée**
  à cette échelle. Il n'y a pas de guichet.
- L'hypothèse implicite d'un marché liquide : **il ne l'est pas** à 1-2 MW hors métropole.

**Ce que ça change concrètement :**
Le projet ne meurt pas — il **change d'ordre**. La séquence « je sécurise, puis je
vendrai » devient risquée, parce que tu investirais (PTF, permis, désamiantage) sans
savoir s'il y a une sortie. La bonne séquence est **inversée** :

> **D'abord trouver l'intérêt d'un acheteur/exploitant. Ensuite seulement, dépenser
> pour dé-risquer.**

C'est aussi une meilleure histoire à raconter à ton père : « je ne te demande pas de
parier sur un marché, je te demande **quelques semaines pour vérifier s'il existe** ».
La demande d'exclusivité devient plus modeste, donc plus facile à accorder — et si le
test est positif, tu reviens avec une preuve, pas une théorie.

---

## 9. Recommandation opérationnelle

1. **Test de marché d'abord (2-4 semaines, coût ~0)** : appeler **Hadès Patrimoine** et
   **Datalok** (ce sont les deux qui connaissent la valeur réelle d'un tel actif — ils
   te diront en un appel si ton site les intéresse ou non, et à quel prix), puis les
   opérateurs edge/colo régionaux (doc 12).
2. **Obtenir l'offre BTP réelle** de ton père — c'est le seuil à battre.
3. **Ne demander qu'une exclusivité courte** (3-6 mois) pour ce test, pas 18 mois.
   Tu réserveras la demande longue pour la phase de dé-risquage, une fois l'intérêt prouvé.
4. **Puis seulement** : pré-étude Enedis, CU, devis désamiantage.

> 📌 **Conséquence pour le deck** : la slide 11 (« ~250 k€ – 1 M€ ») doit être recalée sur
> la fourchette **~320-700 k€** issue de la méthode coût de remplacement, et l'ask de la
> slide 13 ramené à une **exclusivité courte de test**. C'est moins spectaculaire, mais
> beaucoup plus solide — et ton père, qui connaît la valeur de son terrain, le sentira.

## Sources

- [Hadès Data Center — powered land / powered shell, permis et ICPE purgés](https://www.hades-patrimoine.com/data-center) · [site dédié](https://www.hades-datacenter.com/) · [fiche société (créée 2017, Paris 8e)](https://www.pappers.fr/entreprise/hades-patrimoine-828982934)
- [Datalok — annonces datacenter achat & vente](https://www.datalok.io/fr/annonces-datacenter.html) · [Datacenter Land: Why Grid Connection Changes Everything](https://www.datalok.io/en/blog/datacenter-land-grid-connection.html) · [annonce 12 ha / 150 MW France centrale](https://www.datalok.io/en/classified/VT-2025-001.html)
- [Sommet de l'IA : 35 sites « clés en main » (18 à 150+ ha) — Silicon](https://www.silicon.fr/Thematique/data-ia-1372/Breves/sommet-l-ia-l-aube-d-planification-nouvelle-467454.htm) · [26 sites sécurisés — L'Usine Digitale](https://www.usine-digitale.fr/intelligence-artificielle/souverainete-numerique-26-sites-ont-ete-securises-pour-la-construction-de-data-centers-ia-en-france.CEWDRJNI4NGRTHKKTBXSQ4EVMA.html) · [carte régionale des 35 sites — DCmag](https://dcmag.fr/la-carte-regionale-des-35-sites-de-data-centers-dedies-a-lia-identifies-par-le-gouvernement/)
- [nLighten : acquisition Euclyde (6 sites) — DCD](https://www.datacenterdynamics.com/en/news/nlighten-acquires-euclyde-data-centers/) · [7 edge data centers rachetés à EXA Infrastructure](https://exainfra.net/media-centre/press-releases/nlighten-strengthens-european-presence-with-strategic-acquisition-of-seven-edge-data-centers-from-exa-infrastructure/) · [acquisition site oXya Émerainville](https://www.nlighten.com/en/nlighten-expands-french-data-center-footprint-through-paris-site-acquisition/)
- [Edge Data Center Development 2026 : critères de site, 20-50 km des centres d'emploi — Build.inc](https://build.inc/insights/edge-data-center-development-2026)
- [Les tendances autour des datacenters EDGE en France — EY](https://www.ey.com/fr_fr/insights/tmt/les-tendances-autour-des-datacenters-edge-en-france)
- [Nombre de data centers en France : ~350 sites, 714 MW — Mission Open Data](https://www.mission-open-data.fr/nombre-data-centers-france-2026-chiffres/)
- [Le marché des data centers croît et s'élargit à de nouvelles régions (Hauts-de-France, Grand Est, vallée du Rhône) — Batirama](https://www.batirama.com/article/96970-le-marche-des-data-centers-en-france-croit-rapidement-et-s-elargit-a-de-nouvelles-regions.html)
- [Cession des data centers SFR : 764 M€ pour 45 MW — Univers Freebox](https://www.universfreebox.com/article/567396/sfr-annonce-la-cession-de-ses-data-centers-pour-700-millions-deuros-la-vente-lui-rapporte-plus-que-prevu)
- [Data centers : un immobilier mesuré en mégawatts — Carte Financement](https://cartefinancement.com/data-centers-immobilier-megawatts-infrastructure/)
- [Le marché du Data Center en plein boom — CBRE France](https://www.cbre.fr/insights/articles/le-marche-du-data-center-en-plein-boom)
- [Data center IA en zone rurale : Le Bosquel (Somme) — France 3](https://france3-regions.franceinfo.fr/hauts-de-france/somme/amiens/un-veritable-enjeu-de-souverainete-technologique-un-data-center-titanesque-dedie-a-l-intelligence-artificielle-bientot-installe-dans-la-somme-3370168.html)
- [Powered Land Full Report 2025 — Hines](https://www.hines.com/powered-land/power-play-full-report)
