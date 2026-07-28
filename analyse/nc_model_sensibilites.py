#!/usr/bin/env python3
"""Reconstruction du BP Next Compute P100 v14.4 + tests de sensibilité.

Reproduit le fichier à l'euro près (FCFE 15 ans, FCFE an1/an5, parts actionnaires, TRI).
Usage : pip install numpy_financial && python nc_model_sensibilites.py
Voir docs/16-evaluation-bp-next-compute.md pour l'interprétation.
"""
import numpy_financial as npf


def irr(flows):
    try:
        v = npf.irr(flows)
        return None if v != v else v
    except Exception:
        return None


def run(cpu_price=None, cpu_use=None, gpu_price=0.8, gpu_use=0.9,
        elec=135.0, opex_infl=0.0, rev_decline=0.0, extra_opex=0.0):
    """Rejoue le modèle. Paramètres = leviers de sensibilité."""
    N, UP, GPU_N, VCPU = 15, 0.995, 104, 5616
    cpu_price = cpu_price or [0.04, 0.05] + [0.06] * 13
    cpu_use = cpu_use or [0.30, 0.35] + [0.40] * 13
    STOR = 184992.0
    MEZZ, MEZZ_R, MEZZ_N = 1858370.514, 0.12, 5
    AV, AV_R, AV_N = 957242.386, 0.07, 5
    infra_am, it_am, acc_am, re_am = 50600., 354200., 57142.58, 152000.
    carry = sweep = 0.0
    fcfe, ten, nc, dscr = [], [], [], []
    for y in range(1, N + 1):
        i, d = y - 1, (1 - rev_decline) ** (y - 1)
        gpu = GPU_N * gpu_price * gpu_use * 8760 * UP * d
        # note : facteur 9/12 en an 1 codé en dur dans le fichier (ligne 8 du BP)
        cpu = VCPU * cpu_price[i] * cpu_use[i] * 8760 * UP * d * (9 / 12 if y == 1 else 1)
        rev = gpu + cpu + STOR * d
        # RPM : tranches point mort / compensation / standard
        bep, fin = 63000 * 12, 80000 * 12
        z1 = min(rev, bep)
        z2 = min(max(rev - bep, 0), fin - bep)
        z3 = max(rev - fin, 0)
        cge = z1 * .95 + z2 * .20 + z3 * .70
        infl = (1 + opex_infl) ** (y - 1)
        loyer = 6000 * (2 if y in (6, 11) else 1)   # doublement an 6/11 : cf. §4.4
        opex = (906.833448 * elec * infl
                + (loyer + 8400 + 708 + 10000 + 99000 + extra_opex) * infl
                + rev * .025)
        mi = -npf.ipmt(MEZZ_R, y, MEZZ_N, MEZZ) if y <= MEZZ_N else 0.
        mp = -npf.ppmt(MEZZ_R, y, MEZZ_N, MEZZ) if y <= MEZZ_N else 0.
        ai = AV * AV_R if y <= AV_N else 0.
        ap = AV if y == AV_N else 0.
        reinv = 380000. if y in (6, 7, 11, 12) else 0.
        flux = cge - opex - (mi + mp + ai + ap + reinv)
        am = (infra_am + (it_am + acc_am if y <= 5 else 0.)
              + (re_am if 8 <= y <= 12 else 0.) + (re_am if y >= 13 else 0.))
        ebt = cge - opex - mi - am - ai
        base = max(0., ebt - carry)
        carry = max(0., carry - ebt)
        tax = min(42500, base) * .15 + max(0., base - 42500) * .25
        ebitda = cge - opex
        sw = min(ebitda * .05, max(0., flux - tax)) if (ebitda > 0 and y <= MEZZ_N) else 0.
        rel = min(sweep, mp) if mp > 0 else 0.
        f = flux - tax - sw + rel
        sweep += sw - rel
        fcfe.append(f)
        nc.append(f * .67)
        ten.append(f * .33 + ai + ap)          # Tenergie : 33% FCFE + intérêts + principal
        if y <= MEZZ_N:
            dscr.append((flux + mi + mp) / (mi + mp))
    return dict(tot=sum(fcfe), tri=irr([-957275.386] + ten),
                ten=sum(ten) - 957275.386, nc=sum(nc),
                f1=fcfe[0], f5=fcfe[4], dscr=dscr)


if __name__ == "__main__":
    b = run()
    print("=== VÉRIFICATION vs fichier ===")
    for lbl, got, exp in [("Total FCFE 15 ans", b['tot'], 8886728),
                          ("FCFE an 1", b['f1'], 85563),
                          ("FCFE an 5", b['f5'], -430376),
                          ("Gain net Tenergie", b['ten'], 3267622),
                          ("Part Next Compute", b['nc'], 5954041)]:
        print(f"  {lbl:22}{got:>13,.0f}   attendu {exp:>12,.0f}")
    print(f"  {'TRI Tenergie':22}{b['tri']:>13.1%}   attendu       25,3%")

    print("\n=== SENSIBILITÉS — TRI Tenergie ===")
    for lbl, kw in [
        ("BASE (hypothèses Next Compute)", {}),
        ("CPU usage 40%->25%", dict(cpu_use=[.30, .30] + [.25] * 13)),
        ("CPU prix reste 0,04 €/h", dict(cpu_price=[.04] * 15)),
        ("CPU prix 0,04 ET usage 25%", dict(cpu_price=[.04] * 15, cpu_use=[.30, .30] + [.25] * 13)),
        ("GPU prix 0,80->0,60 €/h", dict(gpu_price=.60)),
        ("GPU usage 90%->70%", dict(gpu_use=.70)),
        ("Élec 135->200 €/MWh", dict(elec=200.)),
        ("Inflation OPEX 2%/an", dict(opex_infl=.02)),
        ("Érosion prix -3%/an", dict(rev_decline=.03)),
        ("Charges omises +40 k€/an", dict(extra_opex=40000.)),
        ("COMBINÉ prudent", dict(cpu_price=[.04] * 15, cpu_use=[.30, .30] + [.30] * 13,
                                 gpu_price=.70, elec=170., opex_infl=.02, extra_opex=30000.)),
    ]:
        r = run(**kw)
        t = f"{r['tri']:.1%}" if r['tri'] is not None else "n/a"
        print(f"  {lbl:34} TRI {t:>7}   gain net Tenergie {r['ten']:>11,.0f} €")
    print("\nDSCR an 1-5 (base) :", " ".join(f"{d:.2f}" for d in b['dscr']))
