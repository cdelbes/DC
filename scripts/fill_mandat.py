import fitz

SRC = "/root/.claude/uploads/8f74a3e6-026d-520d-82ba-90b8a5d4138b/ab9e752b-EnedisMOPRAC_046E.pdf"
OUT = "/home/user/DC/documents/Mandat-Enedis-PRE-REMPLI.pdf"

TODO = "……………………………"

VALUES = {
    # --- MANDANT : la Société (SCI propriétaire) ---
    "Nom et prénom bénéficiaire entreprise": f"SCI  {TODO}",
    "SIRET Bénéficaire": TODO,
    "Nom et prénom du représentant de la société  bénéficiaire": TODO,
    "fonciton représentant de la société bénéficiaire": "Gérant",
    # --- MANDATAIRE : le Particulier ---
    "Nom et prénom mandataire particulier": "Charles DELBES",
    "Adresse mandataire particulier": TODO,
    # --- LOCALISATION : site n°1 ---
    "Adresse Site 1": "35 rue de la Ferronnerie — parcelle cadastrale BH 187",
    "CP site 1": "RODEZ (12000)",
    "Déf site 1": "Raccordement de locaux professionnels — soutirage HTA (1 MW et 2 MW)",
    # --- SIGNATURES ---
    "Nom Prénom mandant signature": TODO,
    "Date et lieu mandant signature": "Rodez, le " + TODO,
    "Nom Prénom mandataire signature": "Charles DELBES",
    "Date et lieu mandataire signature": "Rodez, le " + TODO,
}

# Cases à marquer : (page index, rect du widget à cocher)
MARKS = [
    (1, [52, 281, 64, 291]),    # Mandant  -> la Société
    (1, [46, 428, 58, 438]),    # Mandataire -> le Particulier
    (1, [150, 445, 162, 455]),  # Mandataire -> Monsieur
    (2, [39, 116, 52, 129]),    # Mandat SIMPLE de représentation
]

doc = fitz.open(SRC)
filled = 0
for page in doc:
    for w in page.widgets() or []:
        if w.field_name in VALUES and w.field_type_string == "Text":
            w.field_value = VALUES[w.field_name]
            w.update()
            filled += 1

for pno, r in MARKS:
    rect = fitz.Rect(*r)
    doc[pno].insert_text(
        (rect.x0 + 1.5, rect.y1 - 1.5), "X",
        fontsize=10, fontname="hebo", color=(0, 0, 0.6),
    )

doc.save(OUT)
print(f"Champs texte remplis : {filled}/{len(VALUES)}")
print("Cases marquées :", len(MARKS))
print("->", OUT)
