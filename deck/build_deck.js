const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE";           // 13.3 x 7.5
const W = 13.33, H = 7.5;

// ---- Palette (écho charte Tenergie) ----
const NAVY = "1B4355";   // bleu nuit (primaire sombre)
const TEAL = "00A19A";   // turquoise (accent)
const GREEN = "56B576";  // vert (go / sécurisé)
const CORAL = "EC5F65";  // corail (BTP / attention)
const YELLOW = "FFDD00";
const INK = "1A2A31";    // texte sur clair
const MUTE = "5E7076";   // texte secondaire
const PAPER = "F1F5F6";  // fond carte clair
const CARD = "FFFFFF";
const LINE = "D8E2E4";

const HEAD = "Cambria";
const BODY = "Calibri";

const NOTE = "Document de travail — chiffres indicatifs à confirmer (offre BTP, pré-étude Enedis, devis).";

function bg(s, color){ s.background = { color }; }
function pageNum(s, n){
  s.addText(String(n).padStart(2,"0"), { x: W-0.9, y: H-0.5, w:0.5, h:0.3, fontFace:BODY, fontSize:10, color:MUTE, align:"right" });
}
function kicker(s, txt, color){
  s.addText(txt.toUpperCase(), { x:0.7, y:0.55, w:11, h:0.35, fontFace:BODY, fontSize:12, bold:true, color, charSpacing:2 });
}
function title(s, txt, color){
  s.addText(txt, { x:0.7, y:0.9, w:12, h:1.0, fontFace:HEAD, fontSize:32, bold:true, color });
}
function chip(s, x, y, w, txt, fill, tcolor){
  s.addShape(p.ShapeType.roundRect, { x, y, w, h:0.42, fill:{color:fill}, rectRadius:0.21, line:{type:"none"} });
  s.addText(txt, { x, y, w, h:0.42, align:"center", fontFace:BODY, fontSize:12, bold:true, color:tcolor });
}
function circle(s, x, y, d, fill, txt, tcolor, fs){
  s.addShape(p.ShapeType.ellipse, { x, y, w:d, h:d, fill:{color:fill}, line:{type:"none"} });
  if(txt) s.addText(txt, { x, y, w:d, h:d, align:"center", valign:"middle", fontFace:HEAD, fontSize:fs||20, bold:true, color:tcolor });
}

// =========================================================
// 1 — COUVERTURE
// =========================================================
let s = p.addSlide(); bg(s, NAVY);
s.addShape(p.ShapeType.ellipse, { x:9.7, y:-2.2, w:6.5, h:6.5, fill:{color:"22515F"}, line:{type:"none"} });
s.addShape(p.ShapeType.ellipse, { x:11.2, y:3.8, w:4.5, h:4.5, fill:{color:"163541"}, line:{type:"none"} });
s.addText("PROPOSITION — FONCIER DE BEL-AIR", { x:0.8, y:1.5, w:10, h:0.4, fontFace:BODY, fontSize:14, bold:true, color:TEAL, charSpacing:3 });
s.addText("Et si ton terrain\nvalait bien plus qu'un dépôt ?", { x:0.8, y:2.05, w:11.5, h:2.2, fontFace:HEAD, fontSize:44, bold:true, color:"FFFFFF", lineSpacingMultiple:1.0 });
s.addText("Étudier un projet de data center sur la parcelle avant de la vendre.", { x:0.82, y:4.35, w:11, h:0.5, fontFace:BODY, fontSize:18, color:"CFE0E3" });
s.addShape(p.ShapeType.line, { x:0.85, y:5.15, w:3.2, h:0, line:{color:TEAL, width:2} });
s.addText("Une proposition de Charles — juillet 2026", { x:0.8, y:5.35, w:9, h:0.4, fontFace:BODY, fontSize:14, italic:true, color:"9FB6BB" });

// =========================================================
// 2 — LA DÉCISION DU MOMENT
// =========================================================
s = p.addSlide(); bg(s, "FFFFFF");
kicker(s, "La décision du moment", TEAL);
title(s, "Aujourd'hui, une seule option est sur la table", INK);
// left: BTP now
s.addShape(p.ShapeType.roundRect, { x:0.7, y:2.15, w:5.6, h:4.4, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.1 });
circle(s, 1.05, 2.5, 0.7, CORAL, "!", "FFFFFF", 26);
s.addText("Vendre maintenant à l'acheteur BTP", { x:1.95, y:2.5, w:4.2, h:0.7, fontFace:HEAD, fontSize:17, bold:true, color:INK, valign:"middle" });
s.addText([
  {text:"Encaissement unique et définitif", options:{bullet:true, breakLine:true}},
  {text:"Tu te sépares du terrain pour de bon", options:{bullet:true, breakLine:true}},
  {text:"Le passif de la toiture amiantée est déduit de l'offre", options:{bullet:true, breakLine:true}},
  {text:"La valeur « data center » du terrain n'est jamais testée", options:{bullet:true}},
], { x:1.1, y:3.5, w:5.0, h:2.9, fontFace:BODY, fontSize:15, color:INK, paraSpaceAfter:10 });
// right: the message
s.addShape(p.ShapeType.roundRect, { x:6.7, y:2.15, w:5.9, h:4.4, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Ma proposition tient en une phrase :", { x:7.1, y:2.55, w:5.1, h:0.5, fontFace:BODY, fontSize:15, color:TEAL, bold:true });
s.addText("Ne vendons pas tout de suite.\nDonne-moi le temps d'étudier le projet — le risque pour toi est faible.", { x:7.1, y:3.15, w:5.2, h:2.4, fontFace:HEAD, fontSize:22, bold:true, color:"FFFFFF", lineSpacingMultiple:1.05 });
pageNum(s,2);

// =========================================================
// 3 — CE QUE JE TE DEMANDE
// =========================================================
s = p.addSlide(); bg(s,"FFFFFF");
kicker(s,"Ce que je te demande",TEAL);
title(s,"Trois choses simples — et ta sortie reste garantie", INK);
const asks = [
  ["1","Du temps — 3 à 6 mois","Le temps de vérifier qu'il existe vraiment un acheteur. Pas plus, pour commencer."],
  ["2","Une exclusivité courte","Une promesse de vente sous conditions, ou une option : tu ne t'engages à rien de définitif."],
  ["3","Ta confiance","On avance ensemble, en transparence. On refait le point avec les réponses en main."],
];
asks.forEach((a,i)=>{
  const x = 0.7 + i*4.05;
  s.addShape(p.ShapeType.roundRect, { x, y:2.35, w:3.75, h:3.5, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.1 });
  circle(s, x+0.35, y=2.7, 0.85, TEAL, a[0], "FFFFFF", 30);
  s.addText(a[1], { x:x+0.35, y:3.75, w:3.1, h:0.5, fontFace:HEAD, fontSize:19, bold:true, color:INK });
  s.addText(a[2], { x:x+0.35, y:4.3, w:3.1, h:1.4, fontFace:BODY, fontSize:14.5, color:MUTE });
});
s.addShape(p.ShapeType.roundRect, { x:0.7, y:6.15, w:11.9, h:0.7, fill:{color:"EAF6F5"}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Si le projet n'aboutit pas, la vente à l'acheteur BTP reste possible : tu ne perds rien.", { x:0.9, y:6.15, w:11.5, h:0.7, valign:"middle", fontFace:BODY, fontSize:15, bold:true, color:NAVY });
pageNum(s,3);

// =========================================================
// 4 — LE PROJET EN UNE IMAGE
// =========================================================
s = p.addSlide(); bg(s, NAVY);
kicker(s,"Le projet, simplement", TEAL);
s.addText("Transformer un dépôt en foncier prêt à recevoir un data center", { x:0.7, y:0.9, w:12, h:1.0, fontFace:HEAD, fontSize:30, bold:true, color:"FFFFFF" });
const flow = [
  ["Le terrain aujourd'hui","Dépôt de couverture, hangar à toiture amiantée. ~2 522 m² en zone d'activités."],
  ["Ce qu'on prépare","Puissance électrique, autorisations, fibre, terrain propre : un site « prêt à construire »."],
  ["La valeur créée","Un foncier électrifié et dé-risqué — l'actif le plus recherché du secteur data center."],
];
flow.forEach((f,i)=>{
  const x=0.7+i*4.15;
  s.addShape(p.ShapeType.roundRect, { x, y:2.5, w:3.7, h:3.4, fill:{color:"143743"}, line:{color:"2C5866",width:1}, rectRadius:0.1 });
  s.addText("0"+(i+1), { x:x+0.3, y:2.75, w:1.4, h:0.7, fontFace:HEAD, fontSize:30, bold:true, color:TEAL });
  s.addText(f[0], { x:x+0.3, y:3.55, w:3.1, h:0.7, fontFace:HEAD, fontSize:17, bold:true, color:"FFFFFF" });
  s.addText(f[1], { x:x+0.3, y:4.25, w:3.15, h:1.5, fontFace:BODY, fontSize:14, color:"CFE0E3" });
  if(i<2) s.addText("→", { x:x+3.62, y:3.7, w:0.6, h:0.8, align:"center", fontFace:BODY, fontSize:30, bold:true, color:TEAL });
});
pageNum(s,4);

// =========================================================
// 5 — POURQUOI MAINTENANT (marché)
// =========================================================
s = p.addSlide(); bg(s,"FFFFFF");
kicker(s,"Pourquoi maintenant", TEAL);
title(s,"Le marché n'a jamais autant cherché des terrains électrifiés", INK);
const stats = [
  ["+109 Md€","annoncés en France pour les data centers d'ici 2030"],
  ["3 à 4 ans","de délai pour obtenir un raccordement électrique aujourd'hui"],
  ["N°1","la puissance disponible est devenue le premier critère de choix d'un site"],
];
stats.forEach((st,i)=>{
  const x=0.7+i*4.05;
  s.addShape(p.ShapeType.roundRect, { x, y:2.3, w:3.75, h:2.0, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
  s.addText(st[0], { x:x+0.15, y:2.5, w:3.45, h:0.95, align:"center", fontFace:HEAD, fontSize:34, bold:true, color:YELLOW });
  s.addText(st[1], { x:x+0.3, y:3.45, w:3.15, h:0.7, align:"center", fontFace:BODY, fontSize:13, color:"CFE0E3" });
});
s.addShape(p.ShapeType.roundRect, { x:0.7, y:4.65, w:11.9, h:1.95, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.1 });
s.addText("Ce métier existe déjà en France — je ne l'invente pas", { x:1.0, y:4.85, w:11, h:0.5, fontFace:HEAD, fontSize:17, bold:true, color:INK });
s.addText([
  {text:"Hadès Patrimoine (Paris) a fait métier de préparer des terrains « prêts à bâtir » pour data centers : permis, autorisations, poste électrique.", options:{bullet:true, breakLine:true}},
  {text:"EDF ouvre ses anciens sites industriels ; l'État a identifié 35 terrains « clés en main » pour accueillir ces projets.", options:{bullet:true}},
], { x:1.0, y:5.4, w:11.3, h:1.15, fontFace:BODY, fontSize:14, color:INK, paraSpaceAfter:6 });
pageNum(s,5);

// =========================================================
// 6 — POURQUOI CE TERRAIN
// =========================================================
s = p.addSlide(); bg(s,"FFFFFF");
kicker(s,"Pourquoi ce terrain précisément", TEAL);
title(s,"Bel-Air coche les cases que d'autres n'ont pas", INK);
const atouts = [
  ["Puissance rare, à portée","~2,5 MW disponibles et une ligne haute tension à seulement 250 m. C'est ce qui manque partout ailleurs."],
  ["Bon usage, bonne zone","Zone d'activités : un data center y est constructible. Terrain déjà artificialisé (pas de « béton neuf » à justifier)."],
  ["Connecté et bien placé","Très haut débit présent. Climat frais de Rodez (~590 m) = refroidissement moins cher."],
];
atouts.forEach((a,i)=>{
  const y=2.25+i*1.45;
  s.addShape(p.ShapeType.roundRect, { x:0.7, y, w:11.9, h:1.25, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.08 });
  circle(s, 1.0, y+0.28, 0.68, TEAL, String(i+1), "FFFFFF", 22);
  s.addText(a[0], { x:1.95, y:y+0.14, w:3.7, h:1.0, valign:"middle", fontFace:HEAD, fontSize:17, bold:true, color:INK });
  s.addText(a[1], { x:5.8, y:y+0.1, w:6.6, h:1.05, valign:"middle", fontFace:BODY, fontSize:14, color:MUTE });
});
pageNum(s,6);

// =========================================================
// 7 — LES 3 VERROUS ET OÙ ON EN EST
// =========================================================
s = p.addSlide(); bg(s, NAVY);
kicker(s,"Là où j'en suis déjà", TEAL);
s.addText("Les 3 verrous d'un data center — et le plus dur est déjà là", { x:0.7, y:0.9, w:12.2, h:1.0, fontFace:HEAD, fontSize:28, bold:true, color:"FFFFFF" });
const verrous = [
  ["Électricité","~2,5 MW disponibles, ligne HTA à 250 m","Cartographie Enedis","SÉCURISÉ"],
  ["Urbanisme","Zone d'activités = constructible","À confirmer avec la mairie","FAVORABLE"],
  ["Fibre","Très haut débit présent, fibre pro livrable","Réseau public ALL'Fibre","FAVORABLE"],
];
verrous.forEach((v,i)=>{
  const x=0.7+i*4.15;
  s.addShape(p.ShapeType.roundRect, { x, y:2.4, w:3.7, h:3.5, fill:{color:"143743"}, line:{color:"2C5866",width:1}, rectRadius:0.1 });
  circle(s, x+1.35, 2.75, 1.0, GREEN, "✓", "FFFFFF", 34);
  s.addText(v[0], { x, y:3.95, w:3.7, h:0.5, align:"center", fontFace:HEAD, fontSize:19, bold:true, color:"FFFFFF" });
  s.addText(v[1], { x:x+0.3, y:4.5, w:3.1, h:0.85, align:"center", fontFace:BODY, fontSize:13.5, color:"CFE0E3" });
  chip(s, x+0.85, 5.45, 2.0, v[3], GREEN, "FFFFFF");
});
s.addText("La puissance électrique — d'habitude le point qui tue les projets — est déjà disponible ici.", { x:0.7, y:6.55, w:12, h:0.5, align:"center", fontFace:BODY, fontSize:15, italic:true, color:YELLOW });
pageNum(s,7);

// =========================================================
// 8 — POURQUOI JE PEUX Y ARRIVER
// =========================================================
s = p.addSlide(); bg(s,"FFFFFF");
kicker(s,"Pourquoi je peux y arriver", TEAL);
title(s,"C'est très exactement mon métier", INK);
s.addShape(p.ShapeType.roundRect, { x:0.7, y:2.2, w:5.5, h:4.4, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Développeur de projets d'énergie", { x:1.0, y:2.55, w:5.0, h:0.6, fontFace:HEAD, fontSize:19, bold:true, color:"FFFFFF" });
s.addText("Mon quotidien : sécuriser du foncier, obtenir des raccordements électriques et des autorisations d'urbanisme, monter des projets et les mener jusqu'à la construction ou la revente.", { x:1.0, y:3.25, w:5.0, h:2.0, fontFace:BODY, fontSize:15, color:"CFE0E3" });
s.addText("Le data center reprend les mêmes briques.", { x:1.0, y:5.5, w:5.0, h:0.8, fontFace:HEAD, fontSize:16, italic:true, bold:true, color:TEAL });
const skills = [
  ["Raccordement électrique","Je sais dialoguer avec Enedis et lire une capacité réseau."],
  ["Urbanisme","Permis, zonage, relation avec les mairies : c'est ma routine."],
  ["Next Compute","J'ai déjà déployé des mini data centers sur nos centrales solaires."],
  ["Réseau d'acteurs","Enedis, fournisseurs de modules, opérateurs data center."],
];
skills.forEach((k,i)=>{
  const y=2.2+i*1.12;
  s.addShape(p.ShapeType.roundRect, { x:6.5, y, w:6.1, h:0.98, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.08 });
  circle(s, 6.75, y+0.24, 0.5, GREEN, "✓", "FFFFFF", 16);
  s.addText(k[0], { x:7.45, y:y+0.1, w:5.0, h:0.4, fontFace:HEAD, fontSize:15, bold:true, color:INK });
  s.addText(k[1], { x:7.45, y:y+0.48, w:5.0, h:0.42, fontFace:BODY, fontSize:12.5, color:MUTE });
});
pageNum(s,8);

// =========================================================
// 9 — LA STRATÉGIE : DÉRISQUER PUIS ARBITRER
// =========================================================
s = p.addSlide(); bg(s,"FFFFFF");
kicker(s,"Ma stratégie", TEAL);
title(s,"Vérifier d'abord, investir ensuite, décider en dernier", INK);
// phase 1 block
s.addShape(p.ShapeType.roundRect, { x:0.7, y:2.2, w:5.3, h:4.4, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
s.addText("ÉTAPE 1 — VÉRIFIER  (3-6 mois, sans dépense)", { x:1.0, y:2.45, w:4.8, h:0.5, fontFace:BODY, fontSize:12.5, bold:true, color:TEAL, charSpacing:1 });
s.addText([
  {text:"Contacter les spécialistes du foncier data center", options:{bullet:true, breakLine:true}},
  {text:"Sonder les opérateurs : ce site les intéresse-t-il ?", options:{bullet:true}},
], { x:1.0, y:3.0, w:4.8, h:1.3, fontFace:BODY, fontSize:14, color:"E6EFF0", paraSpaceAfter:10 });
s.addText("ÉTAPE 2 — SÉCURISER  (si l'étape 1 est positive)", { x:1.0, y:4.35, w:4.8, h:0.5, fontFace:BODY, fontSize:12.5, bold:true, color:TEAL, charSpacing:1 });
s.addText([
  {text:"Réserver la puissance électrique auprès d'Enedis", options:{bullet:true, breakLine:true}},
  {text:"Obtenir le permis avec la mairie de Rodez", options:{bullet:true, breakLine:true}},
  {text:"Traiter l'amiante et démolir", options:{bullet:true}},
], { x:1.0, y:4.9, w:4.8, h:1.6, fontFace:BODY, fontSize:14, color:"E6EFF0", paraSpaceAfter:8 });
// arrow
s.addText("→", { x:6.05, y:4.0, w:0.7, h:0.8, align:"center", fontFace:BODY, fontSize:34, bold:true, color:TEAL });
// decision -> 3 options
s.addText("ÉTAPE 3 — TU CHOISIS", { x:6.8, y:2.3, w:5.8, h:0.4, fontFace:BODY, fontSize:13, bold:true, color:CORAL, charSpacing:1 });
const opts = [
  ["A","Vendre le foncier « prêt à construire »","Encaisser la survaleur, une fois le site dé-risqué.", GREEN],
  ["B","Le louer à un exploitant","Un loyer récurrent sur 20-40 ans : tu gardes le terrain.", TEAL],
  ["C","Vendre au BTP (repli)","Toujours possible si le projet n'aboutit pas.", MUTE],
];
opts.forEach((o,i)=>{
  const y=2.75+i*1.28;
  s.addShape(p.ShapeType.roundRect, { x:6.8, y, w:5.8, h:1.12, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.08 });
  circle(s, 7.05, y+0.28, 0.56, o[3], o[0], "FFFFFF", 20);
  s.addText(o[1], { x:7.8, y:y+0.12, w:4.6, h:0.42, fontFace:HEAD, fontSize:15, bold:true, color:INK });
  s.addText(o[2], { x:7.8, y:y+0.55, w:4.6, h:0.45, fontFace:BODY, fontSize:12.5, color:MUTE });
});
pageNum(s,9);

// =========================================================
// 10 — AMIANTE
// =========================================================
s = p.addSlide(); bg(s,"FFFFFF");
kicker(s,"Un bonus pour toi", TEAL);
title(s,"Le projet règle le problème de l'amiante", INK);
s.addShape(p.ShapeType.roundRect, { x:0.7, y:2.3, w:5.75, h:3.9, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.1 });
circle(s, 1.05, 2.65, 0.7, CORAL, "!", "FFFFFF", 26);
s.addText("Aujourd'hui : un passif", { x:1.95, y:2.65, w:4.3, h:0.7, valign:"middle", fontFace:HEAD, fontSize:17, bold:true, color:INK });
s.addText([
  {text:"La toiture du hangar est amiantée.", options:{bullet:true, breakLine:true}},
  {text:"Le désamiantage coûte ~25 000 à 55 000 €.", options:{bullet:true, breakLine:true}},
  {text:"Un acheteur BTP le déduira de son offre — ou tu le porteras un jour.", options:{bullet:true}},
], { x:1.1, y:3.6, w:5.1, h:2.5, fontFace:BODY, fontSize:15, color:INK, paraSpaceAfter:10 });
s.addShape(p.ShapeType.roundRect, { x:6.85, y:2.3, w:5.75, h:3.9, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
circle(s, 7.2, 2.65, 0.7, GREEN, "✓", "FFFFFF", 26);
s.addText("Avec le projet : réglé", { x:8.1, y:2.65, w:4.3, h:0.7, valign:"middle", fontFace:HEAD, fontSize:17, bold:true, color:"FFFFFF" });
s.addText([
  {text:"Le désamiantage et la démolition sont intégrés au montage.", options:{bullet:true, breakLine:true}},
  {text:"Le passif disparaît sans que tu aies à le financer.", options:{bullet:true, breakLine:true}},
  {text:"Le terrain ressort propre et valorisé.", options:{bullet:true}},
], { x:7.25, y:3.6, w:5.1, h:2.5, fontFace:BODY, fontSize:15, color:"E6EFF0", paraSpaceAfter:10 });
pageNum(s,10);

// =========================================================
// 11 — COMBIEN ÇA PEUT VALOIR (la slide argent)
// =========================================================
s = p.addSlide(); bg(s,"FFFFFF");
kicker(s,"Ce que ça change pour toi", CORAL);
title(s,"Vente BTP maintenant  vs  voie data center", INK);
// BTP
s.addShape(p.ShapeType.roundRect, { x:0.7, y:2.05, w:5.6, h:1.95, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.1 });
s.addText("VENTE BTP — MAINTENANT", { x:1.0, y:2.22, w:5.0, h:0.4, fontFace:BODY, fontSize:12.5, bold:true, color:CORAL, charSpacing:1 });
s.addText("~164 000 – 340 000 €", { x:1.0, y:2.62, w:5.1, h:0.7, fontFace:HEAD, fontSize:26, bold:true, color:INK });
s.addText("valeur de marché du terrain, passif amiante déduit", { x:1.0, y:3.32, w:5.1, h:0.5, fontFace:BODY, fontSize:12.5, italic:true, color:MUTE });
// Data center
s.addShape(p.ShapeType.roundRect, { x:6.55, y:2.05, w:6.05, h:1.95, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
s.addText("TERRAIN PRÊT À BÂTIR — APRÈS PRÉPARATION", { x:6.9, y:2.22, w:5.5, h:0.4, fontFace:BODY, fontSize:12.5, bold:true, color:TEAL, charSpacing:1 });
s.addText("~320 000 – 700 000 €", { x:6.9, y:2.62, w:5.5, h:0.7, fontFace:HEAD, fontSize:26, bold:true, color:YELLOW });
s.addText("ou un loyer récurrent, si tu préfères garder le terrain", { x:6.9, y:3.32, w:5.5, h:0.5, fontFace:BODY, fontSize:12.5, italic:true, color:"CFE0E3" });
// pont explicatif
s.addText("D'où vient la différence ? De ce que le terrain fait économiser à son acheteur.", { x:0.7, y:4.2, w:11.9, h:0.45, fontFace:HEAD, fontSize:16, bold:true, color:INK });
const bridge = [
  ["Raccordement","100 – 300 k€","le branchement électrique est déjà réglé"],
  ["Autorisations","20 – 50 k€","permis obtenu, plus aucun aléa"],
  ["Amiante traité","25 – 55 k€","terrain propre, prêt à construire"],
  ["Temps gagné","3 à 4 ans","le vrai moteur de la valeur"],
];
bridge.forEach((b,i)=>{
  const x=0.7+i*3.02;
  s.addShape(p.ShapeType.roundRect, { x, y:4.75, w:2.82, h:1.55, fill:{color:PAPER}, line:{color:LINE,width:1}, rectRadius:0.08 });
  s.addText(b[0], { x:x+0.2, y:4.9, w:2.45, h:0.35, fontFace:BODY, fontSize:12, bold:true, color:MUTE });
  s.addText(b[1], { x:x+0.2, y:5.24, w:2.45, h:0.45, fontFace:HEAD, fontSize:17, bold:true, color:TEAL });
  s.addText(b[2], { x:x+0.2, y:5.72, w:2.45, h:0.5, fontFace:BODY, fontSize:11.5, color:MUTE });
});
s.addText("Chaque euro de cette différence correspond à un coût réel que l'acheteur n'aura pas à payer.", { x:0.7, y:6.45, w:11.9, h:0.45, align:"center", fontFace:BODY, fontSize:13, italic:true, color:MUTE });
pageNum(s,11);

// =========================================================
// 12 — TON RISQUE EST FAIBLE
// =========================================================
s = p.addSlide(); bg(s, NAVY);
kicker(s,"L'essentiel pour toi", TEAL);
s.addText("Pour toi, le risque est faible — et l'upside réel", { x:0.7, y:0.9, w:12, h:1.0, fontFace:HEAD, fontSize:30, bold:true, color:"FFFFFF" });
const reassure = [
  ["Tu gardes le terrain","Rien n'est vendu tant que tu n'as pas décidé."],
  ["Ta sortie BTP reste ouverte","Si le projet échoue, la vente au BTP reprend son cours."],
  ["Le coût d'attendre est quasi nul","Le temps travaille pour toi : la demande data center monte."],
  ["Le passif amiante peut disparaître","Pris en charge par le projet, à ma charge d'organisation."],
];
reassure.forEach((r,i)=>{
  const x=0.7+(i%2)*6.1, y=2.4+Math.floor(i/2)*2.05;
  s.addShape(p.ShapeType.roundRect, { x, y, w:5.85, h:1.8, fill:{color:"143743"}, line:{color:"2C5866",width:1}, rectRadius:0.1 });
  circle(s, x+0.32, y+0.32, 0.6, GREEN, "✓", "FFFFFF", 20);
  s.addText(r[0], { x:x+1.1, y:y+0.28, w:4.5, h:0.55, fontFace:HEAD, fontSize:17, bold:true, color:"FFFFFF" });
  s.addText(r[1], { x:x+1.1, y:y+0.85, w:4.55, h:0.8, fontFace:BODY, fontSize:13.5, color:"CFE0E3" });
});
pageNum(s,12);

// =========================================================
// 13 — LE PLAN / L'ASK FINAL
// =========================================================
s = p.addSlide(); bg(s,"FFFFFF");
kicker(s,"Le plan", TEAL);
title(s,"Ce que je ferai — et ce que je te demande", INK);
// left: my commitments timeline
s.addText("Mes engagements (jalons)", { x:0.7, y:2.05, w:5.5, h:0.4, fontFace:HEAD, fontSize:16, bold:true, color:INK });
const steps = [
  ["Mois 1-2","Contacter les spécialistes du foncier data center et les opérateurs"],
  ["Mois 2-4","Premier rendez-vous à la mairie + pré-étude Enedis (gratuite)"],
  ["Mois 4-6","Je te rapporte les réponses : y a-t-il un acheteur, à quel prix ?"],
  ["Point d'étape","On décide ensemble — continuer, ou vendre au BTP"],
];
steps.forEach((st,i)=>{
  const y=2.55+i*0.98;
  circle(s, 0.75, y+0.05, 0.4, TEAL, String(i+1), "FFFFFF", 15);
  if(i<3) s.addShape(p.ShapeType.line, { x:0.95, y:y+0.45, w:0, h:0.55, line:{color:LINE,width:2} });
  s.addText(st[0], { x:1.4, y:y-0.05, w:4.9, h:0.35, fontFace:HEAD, fontSize:14.5, bold:true, color:TEAL });
  s.addText(st[1], { x:1.4, y:y+0.28, w:4.9, h:0.55, fontFace:BODY, fontSize:13, color:MUTE });
});
// right: the ask
s.addShape(p.ShapeType.roundRect, { x:6.75, y:2.05, w:5.85, h:4.6, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Ce que je te demande", { x:7.1, y:2.35, w:5.2, h:0.5, fontFace:HEAD, fontSize:18, bold:true, color:"FFFFFF" });
s.addText([
  {text:"Ne pas signer la vente BTP tout de suite", options:{bullet:true, breakLine:true}},
  {text:"M'accorder 3 à 6 mois d'exclusivité, le temps de vérifier", options:{bullet:true, breakLine:true}},
  {text:"Refaire le point ensemble avec les réponses en main", options:{bullet:true}},
], { x:7.1, y:3.05, w:5.2, h:2.4, fontFace:BODY, fontSize:15.5, color:"E6EFF0", paraSpaceAfter:14 });
s.addShape(p.ShapeType.line, { x:7.1, y:5.5, w:5.15, h:0, line:{color:"2C5866",width:1} });
s.addText("Je ne te demande pas de parier sur ce projet.\nJuste quelques mois pour vérifier s'il tient debout.", { x:7.1, y:5.65, w:5.2, h:0.9, fontFace:BODY, fontSize:14, italic:true, color:TEAL });
pageNum(s,13);

// =========================================================
// 14 — CLÔTURE
// =========================================================
s = p.addSlide(); bg(s, NAVY);
s.addShape(p.ShapeType.ellipse, { x:-2.3, y:3.2, w:6.5, h:6.5, fill:{color:"163541"}, line:{type:"none"} });
s.addShape(p.ShapeType.ellipse, { x:10.5, y:-2.4, w:5.5, h:5.5, fill:{color:"22515F"}, line:{type:"none"} });
s.addText("Ne vendons pas juste un terrain.", { x:1.0, y:2.6, w:11.3, h:0.9, fontFace:HEAD, fontSize:36, bold:true, color:"FFFFFF" });
s.addText("Donnons-nous le temps d'en faire un actif.", { x:1.0, y:3.5, w:11.3, h:0.9, fontFace:HEAD, fontSize:36, bold:true, color:TEAL });
s.addText("Le risque est faible. La valeur potentielle, elle, est grande.", { x:1.02, y:4.6, w:11, h:0.5, fontFace:BODY, fontSize:17, color:"CFE0E3" });
s.addText("On en parle ?", { x:1.0, y:5.35, w:6, h:0.6, fontFace:HEAD, fontSize:22, italic:true, bold:true, color:YELLOW });

p.writeFile({ fileName: "/home/user/DC/deck/Deck-Foncier-Bel-Air.pptx" }).then(f=>console.log("OK", f));
