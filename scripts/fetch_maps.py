#!/usr/bin/env python3
"""Cartes IGN (Géoplateforme WMS) à partir d'un point GPS.

Usage : python fetch_maps.py <lon> <lat> [prefixe]
Produit 3 PNG dans le dossier courant, marqueur au centre :
  - <pfx>map_situation.png  : plan IGN ~2,4 km (DP1.1 / localisation)
  - <pfx>map_cadastre.png   : ortho + parcellaire ~320 m (DP1.2)
  - <pfx>map_ortho.png      : ortho ~140 m (fond de plan de masse)

Dépendances : Pillow. WMS public IGN, sans clé.
"""
import math
import os
import ssl
import sys
import urllib.parse
import urllib.request

from PIL import Image, ImageDraw

WMS = "https://data.geopf.fr/wms-r/wms"
OUTDIR = os.environ.get("MAPS_OUTDIR", ".")


def mercator(lon: float, lat: float):
    x = lon * 20037508.34 / 180.0
    y = math.log(math.tan((90 + lat) * math.pi / 360.0)) / (math.pi / 180.0)
    return x, y * 20037508.34 / 180.0


def ssl_context() -> ssl.SSLContext:
    # Si un bundle CA d'entreprise est fourni (proxy), l'utiliser.
    bundle = os.environ.get("REQUESTS_CA_BUNDLE") or os.environ.get("SSL_CERT_FILE")
    if bundle and os.path.exists(bundle):
        return ssl.create_default_context(cafile=bundle)
    return ssl.create_default_context()


def fetch(cx, cy, layers, half_m, filename, w=1400, h=1050):
    bbox = f"{cx - half_m},{cy - half_m},{cx + half_m},{cy + half_m}"  # EPSG:3857
    params = {
        "SERVICE": "WMS", "VERSION": "1.3.0", "REQUEST": "GetMap",
        "LAYERS": layers, "STYLES": "", "CRS": "EPSG:3857", "BBOX": bbox,
        "WIDTH": str(w), "HEIGHT": str(h), "FORMAT": "image/png",
        "TRANSPARENT": "TRUE",
    }
    url = WMS + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=120, context=ssl_context()).read()
    path = os.path.join(OUTDIR, filename)
    with open(path, "wb") as f:
        f.write(data)
    return path


def add_marker(path, color=(236, 95, 101)):
    im = Image.open(path).convert("RGB")
    d = ImageDraw.Draw(im)
    w, h = im.size
    x, y, r = w // 2, h // 2, 13
    d.ellipse([x - r, y - r, x + r, y + r], outline=(255, 255, 255), width=4)
    d.ellipse([x - r, y - r, x + r, y + r], outline=color, width=3)
    im.save(path)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    lon, lat = float(sys.argv[1]), float(sys.argv[2])
    pfx = sys.argv[3] if len(sys.argv) > 3 else ""
    cx, cy = mercator(lon, lat)
    jobs = [
        ("GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2", 1200, pfx + "map_situation.png"),
        ("ORTHOIMAGERY.ORTHOPHOTOS,CADASTRALPARCELS.PARCELLAIRE_EXPRESS", 160,
         pfx + "map_cadastre.png"),
        ("ORTHOIMAGERY.ORTHOPHOTOS", 70, pfx + "map_ortho.png"),
    ]
    for layers, half, fn in jobs:
        p = fetch(cx, cy, layers, half, fn)
        add_marker(p)
        print("OK ->", p)


if __name__ == "__main__":
    main()
