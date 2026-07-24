#!/usr/bin/env python3
"""Parcelle cadastrale + zonage PLU à partir d'un point GPS (APIs publiques IGN).

Usage : python get_parcelle.py <lon> <lat>

Interroge :
  - apicarto cadastre  : https://apicarto.ign.fr/api/cadastre/parcelle
  - apicarto GPU       : https://apicarto.ign.fr/api/gpu/zone-urba (zonage PLU)

Affiche section/numéro de parcelle, surface, commune, zone PLU (libellé + type).
Reporter les valeurs dans data/site.yml.
"""
import json
import os
import ssl
import sys
import urllib.parse
import urllib.request


def ssl_context() -> ssl.SSLContext:
    bundle = os.environ.get("REQUESTS_CA_BUNDLE") or os.environ.get("SSL_CERT_FILE")
    if bundle and os.path.exists(bundle):
        return ssl.create_default_context(cafile=bundle)
    return ssl.create_default_context()


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60, context=ssl_context()) as r:
        return json.load(r)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    lon, lat = float(sys.argv[1]), float(sys.argv[2])
    geom = urllib.parse.quote(json.dumps(
        {"type": "Point", "coordinates": [lon, lat]}, separators=(",", ":")))

    print(f"# Point : lon={lon} lat={lat}\n")

    print("## Cadastre (apicarto)")
    data = get_json(
        f"https://apicarto.ign.fr/api/cadastre/parcelle?geom={geom}")
    feats = data.get("features", [])
    if not feats:
        print("Aucune parcelle trouvée — vérifier le point.")
    for f in feats:
        p = f["properties"]
        print(f"- Parcelle {p.get('section')} {p.get('numero')}"
              f" | commune {p.get('nom_com')} ({p.get('code_insee')})"
              f" | contenance {p.get('contenance')} m²")

    print("\n## Zonage PLU (Géoportail de l'Urbanisme via apicarto)")
    try:
        data = get_json(
            f"https://apicarto.ign.fr/api/gpu/zone-urba?geom={geom}")
        feats = data.get("features", [])
        if not feats:
            print("Pas de zonage renvoyé (RNU probable ou document non numérisé)"
                  " — vérifier sur https://www.geoportail-urbanisme.gouv.fr/")
        for f in feats:
            p = f["properties"]
            print(f"- Zone {p.get('libelle')} ({p.get('typezone')})"
                  f" | {p.get('libelong')}"
                  f" | document {p.get('idurba')}")
    except Exception as e:  # l'API GPU est parfois indisponible
        print(f"Erreur GPU ({e}) — consulter manuellement le Géoportail de l'Urbanisme.")


if __name__ == "__main__":
    main()
