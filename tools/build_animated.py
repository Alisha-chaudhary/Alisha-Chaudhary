#!/usr/bin/env python3
"""Animated and pseudo-3D versions of the EMBER ARCHIVE assets.

Run after build_assets.py, from the repository root:
    python tools/build_assets.py && python tools/build_animated.py

GitHub plays SMIL animation inside <img> SVGs. JavaScript is not allowed, so the
3D sphere is computed here in Python and baked into frame-by-frame animation values.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_assets as ba
from build_assets import (ASH, COPPER, EMBER, OBS, WINE, WINE_LIGHT, SERIF, MONO, t, svg, box, arrow)

random.seed(7)


def anim(attr, vals, dur, begin="0s", extra=""):
    v = ";".join(vals) if isinstance(vals, (list, tuple)) else vals
    return f'<animate attributeName="{attr}" values="{v}" dur="{dur}" begin="{begin}" repeatCount="indefinite" {extra}/>'


def f1(x):
    return f"{x:.1f}"


def embers(n, x0, x1, y_bottom, y_top, color=EMBER, seed=1):
    r = random.Random(seed)
    out = []
    for _ in range(n):
        x = r.uniform(x0, x1)
        dur = r.uniform(5, 9)
        beg = r.uniform(0, 6)
        rad = r.uniform(0.9, 2.2)
        drift = r.uniform(-18, 18)
        out.append(
            f'<circle cx="{x:.1f}" cy="{y_bottom}" r="{rad:.1f}" fill="{color if r.random() < .7 else COPPER}" opacity="0">'
            f'<animate attributeName="cy" values="{y_bottom};{y_top}" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="cx" values="{x:.1f};{x+drift:.1f}" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;0.9;0.7;0" keyTimes="0;.15;.7;1" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/>'
            f'</circle>')
    return "".join(out)


# ------------------------------------------------------------------ hero
def hero():
    W, H = 1000, 420
    cx, cy, R, D = 800, 188, 108, 460
    N, F, TILT = 34, 48, 0.42
    DUR = 28

    pts = []
    ga = math.pi * (3 - math.sqrt(5))
    for i in range(N):
        y = 1 - 2 * (i + .5) / N
        r = math.sqrt(1 - y * y)
        a = i * ga
        pts.append((r * math.cos(a), y, r * math.sin(a)))

    def project(p, th):
        x, y, z = p
        x2 = x * math.cos(th) + z * math.sin(th)
        z2 = -x * math.sin(th) + z * math.cos(th)
        y3 = y * math.cos(TILT) - z2 * math.sin(TILT)
        z3 = y * math.sin(TILT) + z2 * math.cos(TILT)
        s = D / (D - z3 * R)
        return cx + x2 * R * s, cy + y3 * R * s, z3, s

    frames = [[project(p, 2 * math.pi * k / F) for p in pts] for k in range(F + 1)]

    # edges: 3 nearest neighbours
    edges = set()
    for i, p in enumerate(pts):
        d = sorted(range(N), key=lambda j: sum((p[a] - pts[j][a]) ** 2 for a in range(3)))[1:4]
        for j in d:
            edges.add((min(i, j), max(i, j)))
    edges = sorted(edges)

    def op(z, lo=.12, hi=1.0):
        return lo + (hi - lo) * (z + 1) / 2

    defs = (f'<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">'
            f'<path d="M32 0H0V32" fill="none" stroke="{WINE}" stroke-width=".6" opacity=".5"/></pattern>'
            f'<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{EMBER}" stop-opacity=".5"/>'
            f'<stop offset=".5" stop-color="{WINE}" stop-opacity=".28"/><stop offset="1" stop-color="{OBS}" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{OBS}"/>'
            f'<stop offset=".58" stop-color="{OBS}" stop-opacity=".55"/><stop offset="1" stop-color="{OBS}" stop-opacity="0"/></linearGradient>'
            f'<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{EMBER}" stop-opacity="0"/>'
            f'<stop offset=".5" stop-color="{COPPER}" stop-opacity=".55"/><stop offset="1" stop-color="{EMBER}" stop-opacity="0"/></linearGradient>'
            f'<clipPath id="floor"><rect x="520" y="318" width="480" height="102"/></clipPath>'
            f'<clipPath id="card"><rect width="{W}" height="{H}" rx="14"/></clipPath>')

    b = [f'<g clip-path="url(#card)">',
         f'<rect width="{W}" height="{H}" fill="{OBS}"/><rect width="{W}" height="{H}" fill="url(#grid)"/>',
         f'<circle cx="{cx}" cy="{cy}" r="220" fill="url(#glow)">'
         + anim("opacity", "0.75;1;0.75", "5s") + '</circle>']

    # perspective floor
    vp = (cx, 300)
    fl = ['<g clip-path="url(#floor)">']
    for k in range(-9, 10):
        x_end = cx + k * 62
        fl.append(f'<line x1="{vp[0]}" y1="{vp[1]}" x2="{x_end}" y2="430" stroke="{COPPER}" stroke-opacity="{.38 - abs(k) * .02:.2f}" stroke-width="1"/>')
    n = 7

    def yy(tt):
        return 318 + 112 * tt ** 2

    for i in range(n + 1):
        tt0, tt1 = i / n, (i + 1) / n
        y0, y1 = yy(tt0), yy(tt1)
        fl.append(f'<line x1="500" x2="1000" y1="{y0:.1f}" y2="{y0:.1f}" stroke="{EMBER}" stroke-width="1.2" stroke-opacity=".55">'
                  + anim("y1", [f1(y0), f1(y1)], "3.5s") + anim("y2", [f1(y0), f1(y1)], "3.5s")
                  + (anim("stroke-opacity", ["0", ".55"], "3.5s") if i == 0 else "") + '</line>')
    fl.append("</g>")
    b.append("".join(fl))
    b.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')

    # orbit rings (tilted ellipses with travelling dashes)
    for rx, ry, rot, d, col in [(150, 34, -14, "3 9", COPPER), (176, 46, 18, "2 12", EMBER)]:
        b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{col}" stroke-opacity=".55" '
                 f'stroke-dasharray="{d}" transform="rotate({rot} {cx} {cy})">'
                 + anim("stroke-dashoffset", ["0", "-120"], "9s") + '</ellipse>')

    # edges
    for (i, j) in edges:
        xs1 = [f1(frames[k][i][0]) for k in range(F + 1)]
        ys1 = [f1(frames[k][i][1]) for k in range(F + 1)]
        xs2 = [f1(frames[k][j][0]) for k in range(F + 1)]
        ys2 = [f1(frames[k][j][1]) for k in range(F + 1)]
        os_ = [f"{op((frames[k][i][2] + frames[k][j][2]) / 2, .04, .5):.2f}" for k in range(F + 1)]
        b.append(f'<line x1="{xs1[0]}" y1="{ys1[0]}" x2="{xs2[0]}" y2="{ys2[0]}" stroke="{COPPER}" stroke-width="1">'
                 + anim("x1", xs1, f"{DUR}s") + anim("y1", ys1, f"{DUR}s") + anim("x2", xs2, f"{DUR}s")
                 + anim("y2", ys2, f"{DUR}s") + anim("stroke-opacity", os_, f"{DUR}s") + '</line>')

    # nodes and labels
    labels = {2: "IAM", 9: "CVE", 15: "IOC", 22: "TTP", 28: "LOG"}
    for i in range(N):
        xs = [f1(frames[k][i][0]) for k in range(F + 1)]
        ys = [f1(frames[k][i][1]) for k in range(F + 1)]
        rs = [f"{(1.8 + 2.6 * (frames[k][i][2] + 1) / 2) * frames[k][i][3]:.1f}" for k in range(F + 1)]
        os_ = [f"{op(frames[k][i][2], .2, 1):.2f}" for k in range(F + 1)]
        hot = i in labels
        b.append(f'<circle cx="{xs[0]}" cy="{ys[0]}" r="{rs[0]}" fill="{COPPER if hot else OBS}" stroke="{COPPER}" stroke-width="1.2">'
                 + anim("cx", xs, f"{DUR}s") + anim("cy", ys, f"{DUR}s")
                 + anim("r", [f"{float(r) * (1.6 if hot else 1):.1f}" for r in rs], f"{DUR}s")
                 + anim("opacity", os_, f"{DUR}s") + '</circle>')
        if hot:
            lx = [f1(frames[k][i][0] + 11) for k in range(F + 1)]
            ly = [f1(frames[k][i][1] + 4) for k in range(F + 1)]
            lo = [f"{op(frames[k][i][2], 0, 1) ** 1.6:.2f}" for k in range(F + 1)]
            b.append(f'<text x="{lx[0]}" y="{ly[0]}" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{ASH}">{labels[i]}'
                     + anim("x", lx, f"{DUR}s") + anim("y", ly, f"{DUR}s") + anim("opacity", lo, f"{DUR}s") + '</text>')

    # ember core
    b.append(f'<circle cx="{cx}" cy="{cy}" r="30" fill="none" stroke="{EMBER}" stroke-opacity=".5">'
             + anim("r", ["22", "46", "22"], "4s") + anim("stroke-opacity", [".7", "0", ".7"], "4s") + '</circle>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{EMBER}">' + anim("r", ["11", "15", "11"], "2.4s") + '</circle>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{COPPER}"/>')

    # scan sweep
    b.append(f'<rect x="560" y="0" width="440" height="26" fill="url(#scan)" opacity=".35">'
             + anim("y", ["20", "380"], "7s") + '</rect>')

    # embers
    b.append(embers(18, 540, 980, 410, 40, seed=3))

    # corner brackets
    L = 22
    for (x, y, sx, sy) in [(16, 16, 1, 1), (W - 16, 16, -1, 1), (16, H - 16, 1, -1), (W - 16, H - 16, -1, -1)]:
        b.append(f'<path d="M{x} {y + sy*L}V{y}H{x + sx*L}" fill="none" stroke="{EMBER}" stroke-width="1.5"/>')

    # text, fading in once
    def reveal(el, delay):
        return (f'<g opacity="1">{el}<animate attributeName="opacity" values="0;0;1" keyTimes="0;.001;1" '
                f'dur="{delay + .7}s" begin="0s" fill="freeze" calcMode="linear"/></g>') if False else el

    b.append(t(56, 74, "EMBER ARCHIVE  /  ANALYST FILE", size=12, fill=COPPER, spacing=5))
    b.append(t(56, 170, "Alisha Chaudhary", size=58, fill=ASH, family=SERIF))
    b.append(f'<rect x="56" y="192" width="72" height="3" rx="1.5" fill="{COPPER}">'
             + anim("width", ["24", "72", "72", "24"], "6s", extra='keyTimes="0;.2;.8;1"') + '</rect>')
    b.append(t(56, 236, "Cybersecurity Analyst", size=18, fill=COPPER, weight="bold"))
    b.append(t(56, 262, "IAM & Access Governance  |  Vulnerability Intelligence", size=13, fill=ASH))
    b.append(t(56, 312, "\u201cEvidence first. Understand the system.", size=19, family=SERIF, style="italic"))
    b.append(t(56, 338, "Make the finding actionable.\u201d", size=19, family=SERIF, style="italic"))
    b.append(t(56, 384, "HYDERABAD, INDIA", size=12, fill=ASH, spacing=3))
    b.append(t(280, 384, "17.3850\u00b0 N, 78.4867\u00b0 E", size=12, fill=COPPER, spacing=2))
    b.append("</g>")
    svg("hero.svg", W, H, "".join(b), "Alisha Chaudhary, Cybersecurity Analyst",
        "Animated hero banner with a rotating three-dimensional evidence network. Cybersecurity Analyst focused on IAM and access governance and vulnerability intelligence, based in Hyderabad, India. Evidence first. Understand the system. Make the finding actionable.",
        defs)


# ------------------------------------------------------------------ section headers
def section(name, num, label, heading):
    W, H = 1000, 88
    b = [f'<rect width="{W}" height="{H}" rx="10" fill="{OBS}"/>',
         t(18, 60, num, size=46, fill=EMBER, family=SERIF),
         t(100, 34, f"{num} / {label}", size=12, fill=COPPER, spacing=4),
         t(100, 64, heading, size=27, fill=ASH, family=SERIF),
         f'<rect x="100" y="76" width="40" height="2" fill="{EMBER}"/>',
         f'<rect x="140" y="76.5" width="{W-158}" height="1" fill="{WINE_LIGHT}"/>',
         f'<rect x="100" y="75.5" width="70" height="3" rx="1.5" fill="{COPPER}" opacity=".9">'
         + anim("x", ["100", str(W - 90)], "5s") + anim("opacity", ["0", ".95", ".95", "0"], "5s", extra='keyTimes="0;.1;.85;1"') + '</rect>',
         f'<circle cx="38" cy="30" r="3" fill="{EMBER}">' + anim("opacity", [".2", "1", ".2"], "2.4s") + '</circle>']
    svg(name, W, H, "".join(b), f"{num} / {label}", heading)


# ------------------------------------------------------------------ terminal (typed reveal)
def terminal():
    W = 1000
    lines = [
        ("p", "cat about.txt"),
        ("o", "I build practical security tools, investigate published vulnerabilities through"),
        ("o", "controlled experimentation, and translate technical findings into actionable"),
        ("o", "defensive intelligence."),
        ("g", ""),
        ("p", "ls focus/"),
        ("c", ("evidence-led-analysis", "security-assessment", "identity-governance")),
        ("c", ("vulnerability-research", "risk-documentation", "python-security-automation")),
        ("g", ""),
        ("p", "cat method.txt"),
        ("o", "Published claims get tested, not trusted. Every result ships with its method,"),
        ("o", "its measurements, and enough detail for someone else to reproduce it."),
        ("g", ""),
        ("p", "status"),
        ("k", ("location", "Hyderabad, India")),
        ("k", ("background", "B.Sc. Computer Applications")),
        ("k", ("exploring", "detection engineering, threat hunting, cloud security")),
    ]
    top, lh = 62, 24
    H = top + len(lines) * lh + 28
    TOTAL = 16.0           # seconds for one cycle
    step = 0.42
    b = [f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="{OBS}" stroke="{WINE_LIGHT}"/>',
         f'<path d="M1 12a11 11 0 0 1 11-11h{W-24}a11 11 0 0 1 11 11V40H1Z" fill="{WINE}"/>',
         f'<circle cx="26" cy="21" r="5.5" fill="{EMBER}"/><circle cx="46" cy="21" r="5.5" fill="{COPPER}"/>'
         f'<circle cx="66" cy="21" r="5.5" fill="{ASH}" fill-opacity=".55"/>',
         t(W / 2, 25, "alisha@archive  ~/profile", size=12, fill=ASH, anchor="middle", spacing=1.5, opacity=.9)]
    y, k = top, 0

    def wrapg(inner, k):
        t0 = (k * step) / TOTAL
        t1 = min(t0 + 0.03, 0.98)
        return (f'<g>{inner}<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{t0:.4f};{t1:.4f};0.97;1" '
                f'dur="{TOTAL}s" repeatCount="indefinite"/></g>')

    for kind, val in lines:
        if kind == "p":
            b.append(wrapg(t(32, y, "$", size=14, fill=COPPER, weight="bold") + t(52, y, val, size=14, weight="bold"), k))
        elif kind == "o":
            b.append(wrapg(t(52, y, val, size=14, opacity=.9), k))
        elif kind == "c":
            b.append(wrapg("".join(t(52 + i * 290, y, c, size=14, opacity=.9) for i, c in enumerate(val)), k))
        elif kind == "k":
            b.append(wrapg(t(52, y, val[0], size=14, fill=COPPER) + t(190, y, val[1], size=14, opacity=.9), k))
        if kind != "g":
            k += 1
        y += lh
    b.append(t(32, y - 2, "$", size=14, fill=COPPER, weight="bold"))
    b.append(f'<rect x="52" y="{y-15}" width="9" height="17" fill="{EMBER}">'
             + anim("opacity", ["1", "1", "0", "0"], "1.1s", extra='keyTimes="0;.5;.5;1"') + '</rect>')
    svg("terminal-profile.svg", W, H + 8, "".join(b), "Profile terminal",
        "Terminal-style profile. I build practical security tools, investigate published vulnerabilities through controlled experimentation, and translate technical findings into actionable defensive intelligence. Focus areas are evidence-led analysis, security assessment, identity governance, vulnerability research, risk documentation and Python security automation. Based in Hyderabad, India, with a B.Sc. in Computer Applications. Currently exploring detection engineering, threat hunting and cloud security.")


# ------------------------------------------------------------------ pipeline (travelling pulse)
def pipeline():
    W, H = 1000, 200
    steps = [("ASSESS", "Scope the system and its exposure"),
             ("VALIDATE", "Test the claim and reproduce the result"),
             ("CORRELATE", "Link CVEs, indicators and telemetry"),
             ("PRIORITISE", "Rank by impact and by evidence"),
             ("DOCUMENT", "Write findings others can act on")]
    x0, step, T = 100, 190, 7
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="url(#pg)" stroke="{WINE}"/>']
    b.append(f'<line x1="{x0}" y1="62" x2="{x0 + step*4}" y2="62" stroke="{EMBER}" stroke-width="1.6" stroke-dasharray="6 6">'
             + anim("stroke-dashoffset", ["0", "-24"], "1.2s") + '</line>')
    for i, (n, d) in enumerate(steps):
        cx = x0 + i * step
        last = i == 4
        beg = f"{i * T / 4 - 0.15:.2f}s" if i else "0s"
        b.append(f'<circle cx="{cx}" cy="62" r="19" fill="none" stroke="{EMBER}" stroke-width="1.5" opacity="0">'
                 + anim("r", ["19", "34"], f"{T}s", begin=beg if i else "0s") + anim("opacity", [".9", "0"], f"{T}s", begin=beg if i else "0s") + '</circle>')
        b.append(f'<circle cx="{cx}" cy="62" r="19" fill="{OBS}" stroke="{COPPER}" stroke-width="1.5"/>')
        b.append(f'<circle cx="{cx}" cy="62" r="{9 if last else 6}" fill="{EMBER if not last else COPPER}"/>')
        b.append(t(cx, 112, n, size=13, fill=COPPER, anchor="middle", spacing=2.5, weight="bold"))
        for j, ln in enumerate(ba.wrap(d, 22)):
            b.append(t(cx, 136 + j * 17, ln, size=11, anchor="middle", opacity=.88))
        if i < 4:
            mx = cx + step / 2
            b.append(f'<path d="M{mx-4} 56L{mx+4} 62L{mx-4} 68" fill="none" stroke="{COPPER}" stroke-width="1.5"/>')
    b.append(f'<circle r="6" fill="{COPPER}"><animateMotion dur="{T}s" repeatCount="indefinite" path="M{x0} 62H{x0 + step*4}" keyPoints="0;1;1" keyTimes="0;.86;1" calcMode="linear"/>'
             + anim("opacity", ["1", "1", "0"], f"{T}s", extra='keyTimes="0;.86;1"') + '</circle>')
    svg("pipeline.svg", W, H, "".join(b), "Engineering approach",
        "Assess, validate, correlate, prioritise, document. " + " ".join(f"{n.title()}: {d}." for n, d in steps))


# ------------------------------------------------------------------ footer
def footer():
    W, H = 1000, 150
    defs = (f'<radialGradient id="fg" cx=".5" cy="0" r=".7"><stop offset="0" stop-color="{EMBER}" stop-opacity=".4"/>'
            f'<stop offset="1" stop-color="{OBS}" stop-opacity="0"/></radialGradient>'
            f'<clipPath id="fc"><rect width="{W}" height="{H}" rx="14"/></clipPath>')
    b = [f'<g clip-path="url(#fc)"><rect width="{W}" height="{H}" fill="{OBS}"/>',
         f'<rect width="{W}" height="{H}" fill="url(#fg)">' + anim("opacity", [".7", "1", ".7"], "5s") + '</rect>',
         embers(22, 40, 960, 150, 20, seed=11),
         f'<rect x="460" y="34" width="80" height="2" rx="1" fill="{EMBER}">' + anim("width", ["40", "120", "40"], "5s")
         + anim("x", ["480", "440", "480"], "5s") + '</rect>',
         t(W / 2, 70, "EMBER ARCHIVE", size=13, fill=COPPER, anchor="middle", spacing=8),
         t(W / 2, 108, "Security through evidence, clarity, and careful engineering.", size=21, family=SERIF, style="italic", anchor="middle"),
         '</g>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{WINE}"/>']
    svg("footer.svg", W, H, "".join(b), "EMBER ARCHIVE", "Security through evidence, clarity, and careful engineering.", defs)


# ------------------------------------------------------------------ animated project diagrams
def packet(path, dur, begin, color=EMBER, r=3):
    return (f'<circle r="{r}" fill="{color}" opacity="0"><animateMotion path="{path}" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>'
            + anim("opacity", ["0", "1", "1", "0"], f"{dur}s", begin=f"{begin}s", extra='keyTimes="0;.1;.85;1"') + '</circle>')


_orig = {k: getattr(ba, k) for k in ("diag_threatlens", "diag_identity", "diag_phish", "diag_ssh")}


def diag_threatlens():
    ox = 668
    extra = "".join(packet(f"M{ox+92+(c*100)} {73+r*40}L{ox+228} 118", 2.4, round((r * 2 + c) * 0.4, 1))
                    for r in range(3) for c in range(2))
    return _orig["diag_threatlens"]() + extra + (
        f'<rect x="{ox+228}" y="92" width="66" height="52" rx="4" fill="none" stroke="{EMBER}" stroke-width="1.5">'
        + anim("stroke-opacity", [".3", "1", ".3"], "2.4s") + '</rect>')


def diag_identity():
    ox = 656
    pk = packet(f"M{ox+2} 75H{ox+216}", 3.2, 0, COPPER, 3.5)
    chain = "".join(
        f'<rect x="{ox+6+i*62}" y="156" width="48" height="28" rx="4" fill="none" stroke="{EMBER}" stroke-width="1.6" opacity="0">'
        + anim("opacity", ["0", "1", "1", "0"], "5s", begin=f"{i*.8:.1f}s", extra='keyTimes="0;.1;.4;.6"') + '</rect>' for i in range(5))
    return _orig["diag_identity"]() + pk + chain


def diag_phish():
    ox = 646
    pk = "".join(packet(f"M{ox+54} 117L{ox+70} {79+i*46}L{ox+160} {79+i*46}L{ox+182} 117", 2.8, i * 0.9) for i in range(3))
    return _orig["diag_phish"]() + pk


def diag_ssh():
    s = _orig["diag_ssh"]()
    return s + (f'<circle cx="806" cy="92" r="3" fill="{COPPER}">' + anim("opacity", ["1", ".2", "1"], "2s") + '</circle>')


if __name__ == "__main__":
    hero()
    for n, num, lab, head in [
        ("sec-01-profile.svg", "01", "PROFILE", "Who I am and how I work"),
        ("sec-02-domains.svg", "02", "SECURITY DOMAINS", "Where the work sits"),
        ("sec-03-projects.svg", "03", "FEATURED PROJECTS", "Evidence in the repositories"),
        ("sec-04-approach.svg", "04", "ENGINEERING APPROACH", "From claim to finding"),
        ("sec-05-toolkit.svg", "05", "TECHNICAL TOOLKIT", "What I work with"),
        ("sec-06-record.svg", "06", "RECORD", "Experience, research and education"),
        ("sec-07-activity.svg", "07", "ACTIVITY", "Public contribution record"),
    ]:
        section(n, num, lab, head)
    terminal()
    pipeline()
    footer()
    ba.diag_threatlens, ba.diag_identity, ba.diag_phish, ba.diag_ssh = diag_threatlens, diag_identity, diag_phish, diag_ssh
    ba.projects()
    print("animated assets written")
