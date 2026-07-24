# Scripts d'analyse parcellaire

Pipeline hérité de Next Compute : un point GPS suffit à produire l'essentiel de
l'analyse de site.

```bash
pip install Pillow

# 1) Parcelle + surface + zone PLU (APIs publiques IGN, sans clé)
python get_parcelle.py <lon> <lat>

# 2) Cartes (plan de situation, cadastre+ortho, ortho seule)
python fetch_maps.py <lon> <lat> rodez_
```

Attention à l'ordre des arguments : **longitude puis latitude** (ex. Rodez ≈ `2.575 44.351`).

Résultats à reporter dans `../data/site.yml`.

## Notes

- Réseau : si vous passez par un proxy d'entreprise, exporter
  `REQUESTS_CA_BUNDLE=/chemin/vers/ca-bundle.crt` (les scripts le prennent en compte).
- Si l'API GPU ne renvoie rien : la commune est peut-être au RNU ou le document n'est
  pas numérisé → vérifier manuellement sur https://www.geoportail-urbanisme.gouv.fr/.
- La capacité de **soutirage** Enedis ne s'obtient pas par API : voir la démarche du
  document `../docs/02-raccordement-enedis.md` (Caparéseau en lecture d'ambiance,
  puis pré-étude Enedis).
