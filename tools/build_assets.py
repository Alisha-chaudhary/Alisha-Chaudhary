#!/usr/bin/env python3
"""Generates every SVG in assets/ for the EMBER ARCHIVE profile.

Run from the repository root:  python tools/build_assets.py
Only the Python standard library is needed.
"""
import math
import os
import textwrap
from html import escape

OBS, WINE, EMBER, COPPER, ASH = "#0B0B0E", "#391521", "#A83B32", "#C58A63", "#D9D2CB"
WINE_LIGHT = "#4A1B2A"   # slightly lighter wine surface
WINE_DEEP = "#1A0C12"    # darkened wine for gradients

SERIF = "Georgia, 'Times New Roman', 'Noto Serif', serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
CHAR = 0.6  # monospace advance, as a fraction of font size

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)


def t(x, y, s, size=14, fill=ASH, family=MONO, weight="normal", style="normal",
      anchor="start", spacing=0, opacity=1):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" font-style="{style}" text-anchor="{anchor}" '
            f'letter-spacing="{spacing}" opacity="{opacity}">{escape(s)}</text>')


def svg(name, w, h, body, title, desc, defs=""):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
           f'role="img" aria-labelledby="t d"><title id="t">{escape(title)}</title>'
           f'<desc id="d">{escape(desc)}</desc><defs>{defs}'
           f'<linearGradient id="pg" x1="0" y1="0" x2="1" y2="1">'
           f'<stop offset="0" stop-color="{WINE}" stop-opacity=".62"/>'
           f'<stop offset="1" stop-color="{OBS}" stop-opacity="1"/></linearGradient>'
           f'</defs>{body}</svg>')
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(doc)


def chips(items, x0, y0, max_x, size=12, h=26, gap=8, fill=OBS, stroke=WINE_LIGHT, color=ASH):
    out, x, y = [], x0, y0
    for s in items:
        w = round(len(s) * size * CHAR + 24)
        if x + w > max_x:
            x, y = x0, y + h + gap
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" '
                   f'stroke="{stroke}" stroke-width="1"/>')
        out.append(t(x + 12, y + h / 2 + size * 0.34, s, size=size, fill=color))
        x += w + gap
    return "".join(out), y + h


def panel(w, h, accent=True):
    s = f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" fill="url(#pg)" stroke="{WINE}" stroke-width="1"/>'
    if accent:
        s += f'<rect x="0" y="18" width="3" height="{h-36}" rx="1.5" fill="{EMBER}"/>'
    return s


# ---------------------------------------------------------------- hero
def hero():
    W, H = 1000, 420
    defs = (f'<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">'
            f'<path d="M32 0H0V32" fill="none" stroke="{WINE}" stroke-width=".6" opacity=".55"/></pattern>'
            f'<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">'
            f'<stop offset="0" stop-color="{EMBER}" stop-opacity=".42"/>'
            f'<stop offset=".55" stop-color="{WINE}" stop-opacity=".25"/>'
            f'<stop offset="1" stop-color="{OBS}" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{OBS}" stop-opacity="1"/>'
            f'<stop offset=".6" stop-color="{OBS}" stop-opacity=".6"/>'
            f'<stop offset="1" stop-color="{OBS}" stop-opacity="0"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" rx="14" fill="{OBS}"/>',
         f'<rect width="{W}" height="{H}" rx="14" fill="url(#grid)"/>',
         f'<circle cx="820" cy="210" r="210" fill="url(#glow)"/>',
         f'<rect width="{W}" height="{H}" rx="14" fill="url(#fade)"/>']
    # network
    focal = (820, 210)
    nodes = {"IAM": (700, 118), "CVE": (934, 120), "IOC": (944, 302), "TTP": (726, 322), "LOG": (656, 222)}
    extra = [(780, 70), (880, 60), (905, 205), (860, 350), (780, 270), (700, 215), (950, 210), (640, 340)]
    edges = [(focal, p) for p in nodes.values()]
    edges += [(focal, extra[2]), (focal, extra[4]), (focal, extra[5]),
              (nodes["IAM"], extra[0]), (extra[0], extra[1]), (extra[1], nodes["CVE"]),
              (nodes["CVE"], extra[2]), (extra[2], extra[6]), (nodes["IOC"], extra[3]),
              (extra[3], nodes["TTP"]), (nodes["TTP"], extra[7]), (nodes["LOG"], extra[5]),
              (extra[4], nodes["TTP"])]
    for (x1, y1), (x2, y2) in edges:
        b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{COPPER}" stroke-opacity=".32" stroke-width="1"/>')
    # evidence trail (dashed)
    trail = [nodes["LOG"], extra[5], focal, extra[2], nodes["CVE"]]
    pts = " ".join(f"{x},{y}" for x, y in trail)
    b.append(f'<polyline points="{pts}" fill="none" stroke="{EMBER}" stroke-width="1.6" stroke-dasharray="5 6" opacity=".9"/>')
    for p in extra:
        b.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="3" fill="{OBS}" stroke="{COPPER}" stroke-opacity=".7"/>')
    for label, (x, y) in nodes.items():
        b.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{OBS}" stroke="{COPPER}" stroke-width="1.5"/>')
        b.append(f'<circle cx="{x}" cy="{y}" r="2" fill="{COPPER}"/>')
        dx = 12 if x < 900 else -12
        b.append(t(x + dx, y + 4, label, size=11, fill=COPPER, spacing=2, anchor="start" if dx > 0 else "end"))
    # focal ember
    b.append(f'<circle cx="{focal[0]}" cy="{focal[1]}" r="46" fill="none" stroke="{EMBER}" stroke-opacity=".28"/>')
    b.append(f'<circle cx="{focal[0]}" cy="{focal[1]}" r="28" fill="none" stroke="{EMBER}" stroke-opacity=".55"/>')
    b.append(f'<circle cx="{focal[0]}" cy="{focal[1]}" r="13" fill="{EMBER}"/>')
    b.append(f'<circle cx="{focal[0]}" cy="{focal[1]}" r="5" fill="{COPPER}"/>')
    b.append(t(focal[0], focal[1] + 70, "FINDING", size=11, fill=ASH, spacing=3, anchor="middle", opacity=.85))
    # crosshair marks
    for cx, cy in [(610, 60), (968, 380), (968, 40)]:
        b.append(f'<path d="M{cx-6} {cy}H{cx+6}M{cx} {cy-6}V{cy+6}" stroke="{COPPER}" stroke-opacity=".6"/>')
    # corner brackets
    L = 22
    for (x, y, sx, sy) in [(16, 16, 1, 1), (W - 16, 16, -1, 1), (16, H - 16, 1, -1), (W - 16, H - 16, -1, -1)]:
        b.append(f'<path d="M{x} {y + sy*L}V{y}H{x + sx*L}" fill="none" stroke="{EMBER}" stroke-width="1.5"/>')
    # text block
    b.append(t(56, 74, "EMBER ARCHIVE  /  ANALYST FILE", size=12, fill=COPPER, spacing=5))
    b.append(t(56, 170, "Alisha Chaudhary", size=58, fill=ASH, family=SERIF, weight="normal"))
    b.append(f'<rect x="56" y="192" width="72" height="3" rx="1.5" fill="{COPPER}"/>')
    b.append(t(56, 236, "Cybersecurity Analyst", size=18, fill=COPPER, weight="bold"))
    b.append(t(56, 262, "IAM & Access Governance  |  Vulnerability Intelligence", size=13, fill=ASH))
    b.append(t(56, 312, "\u201cEvidence first. Understand the system.", size=19, family=SERIF, style="italic"))
    b.append(t(56, 338, "Make the finding actionable.\u201d", size=19, family=SERIF, style="italic"))
    b.append(t(56, 384, "HYDERABAD, INDIA", size=12, fill=ASH, spacing=3))
    b.append(t(280, 384, "17.3850\u00b0 N, 78.4867\u00b0 E", size=12, fill=COPPER, spacing=2))
    svg("hero.svg", W, H, "".join(b),
        "Alisha Chaudhary, Cybersecurity Analyst",
        "Hero banner. Cybersecurity Analyst focused on IAM and access governance and vulnerability intelligence, based in Hyderabad, India. Motto: Evidence first. Understand the system. Make the finding actionable.",
        defs)


# ---------------------------------------------------------------- link pills
def pill(name, label):
    w = round(len(label) * 13 * CHAR + 48)
    b = (f'<rect x=".5" y=".5" width="{w-1}" height="35" rx="18" fill="{WINE}" stroke="{COPPER}" stroke-opacity=".6"/>'
         f'<circle cx="20" cy="18" r="4" fill="{EMBER}"/>' + t(34, 22.5, label, size=13, fill=ASH, spacing=1.5))
    svg(name, w, 36, b, label, f"Link button, {label}")
    return w


# ---------------------------------------------------------------- section header
def section(name, num, label, heading, head_size=29):
    W, H = 1000, 88
    b = [f'<rect width="{W}" height="{H}" rx="10" fill="{OBS}"/>',
         t(18, 60, num, size=46, fill=EMBER, family=SERIF),
         t(100, 34, f"{num} / {label}", size=12, fill=COPPER, spacing=4),
         t(100, 64, heading, size=head_size, fill=ASH, family=SERIF),
         f'<rect x="100" y="76" width="40" height="2" fill="{EMBER}"/>',
         f'<rect x="140" y="76.5" width="{W-158}" height="1" fill="{WINE_LIGHT}"/>']
    svg(name, W, H, "".join(b), f"{num} / {label}", heading)


# ---------------------------------------------------------------- terminal
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
    b = [f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="{OBS}" stroke="{WINE_LIGHT}"/>',
         f'<path d="M1 12a11 11 0 0 1 11-11h{W-24}a11 11 0 0 1 11 11V40H1Z" fill="{WINE}"/>',
         f'<circle cx="26" cy="21" r="5.5" fill="{EMBER}"/><circle cx="46" cy="21" r="5.5" fill="{COPPER}"/>'
         f'<circle cx="66" cy="21" r="5.5" fill="{ASH}" fill-opacity=".55"/>',
         t(W / 2, 25, "alisha@archive  ~/profile", size=12, fill=ASH, anchor="middle", spacing=1.5, opacity=.9)]
    y = top
    for kind, val in lines:
        if kind == "p":
            b.append(t(32, y, "$", size=14, fill=COPPER, weight="bold"))
            b.append(t(52, y, val, size=14, fill=ASH, weight="bold"))
        elif kind == "o":
            b.append(t(52, y, val, size=14, fill=ASH, opacity=.9))
        elif kind == "c":
            for i, cell in enumerate(val):
                b.append(t(52 + i * 290, y, cell, size=14, fill=ASH, opacity=.9))
        elif kind == "k":
            b.append(t(52, y, val[0], size=14, fill=COPPER))
            b.append(t(190, y, val[1], size=14, fill=ASH, opacity=.9))
        y += lh
    b.append(t(32, y - 2, "$", size=14, fill=COPPER, weight="bold"))
    b.append(f'<rect x="52" y="{y-15}" width="9" height="17" fill="{EMBER}"/>')
    svg("terminal-profile.svg", W, H + 8, "".join(b),
        "Profile terminal",
        "Terminal-style profile. I build practical security tools, investigate published vulnerabilities through controlled experimentation, and translate technical findings into actionable defensive intelligence. Focus areas are evidence-led analysis, security assessment, identity governance, vulnerability research, risk documentation and Python security automation. Based in Hyderabad, India, with a B.Sc. in Computer Applications. Currently exploring detection engineering, threat hunting and cloud security.")


# ---------------------------------------------------------------- domain panels
DOMAINS = [
    ("domain-iam.svg", "Identity & Access Management", "IdentityGuard, local lab",
     ["RBAC", "Least privilege", "Access reviews", "Joiner-mover-leaver", "Segregation of duties",
      "Authorisation policies", "Simulated PAM"]),
    ("domain-vuln.svg", "Vulnerability Management", "ThreatLens, ssh-enum, internship",
     ["CVE research", "CVSS v3.1", "NVD API", "Severity assessment", "Risk prioritisation", "Remediation guidance"]),
    ("domain-intel.svg", "Threat Intelligence & Investigation", "PhishMind, synthetic samples",
     ["Phishing analysis", "BEC analysis", "SPF / DKIM / DMARC", "Indicator enrichment", "Source validation",
      "MITRE ATT&CK mapping"]),
    ("domain-eng.svg", "Security Engineering", "ThreatLens, IdentityGuard, CyberSec",
     ["Python automation", "API integration", "FastAPI", "Pytest", "Audit logging", "Structured reporting", "SQL"]),
    ("domain-detect.svg", "Detection & Telemetry", "SOC Detection Lab, documented",
     ["Windows event analysis", "Sysmon", "Splunk SPL", "ATT&CK-mapped detections", "Telemetry troubleshooting"]),
]


def domains():
    W, H = 1000, 132
    for name, title, ev, items in DOMAINS:
        b = [panel(W, H)]
        b.append(t(36, 56, title, size=21, fill=ASH, family=SERIF))
        b.append(t(36, 88, "EVIDENCE", size=10, fill=COPPER, spacing=3))
        b.append(t(36, 106, ev, size=12, fill=ASH, opacity=.85))
        c, _ = chips(items, 440, 28, W - 28)
        b.append(c)
        svg(name, W, H, "".join(b), title, f"{title}. Evidence from {ev}. Skills include {', '.join(items)}.")


# ---------------------------------------------------------------- project cards
def wrap(text, width):
    return textwrap.wrap(text, width)


def project_card(name, idx, title, status, desc, stack, repo, diagram):
    W, H = 1000, 300
    b = [panel(W, H, accent=False),
         f'<rect x="0" y="0" width="1000" height="3" rx="1.5" fill="{EMBER}" opacity=".9"/>',
         t(36, 46, f"FEATURED PROJECT {idx:02d}", size=11, fill=COPPER, spacing=3.5)]
    sw = round(len(status) * 11 * CHAR + 22)
    b.append(f'<rect x="{596-sw}" y="30" width="{sw}" height="22" rx="11" fill="none" stroke="{COPPER}" stroke-opacity=".7"/>')
    b.append(t(596 - sw / 2, 45, status, size=11, fill=ASH, anchor="middle"))
    b.append(t(36, 96, title, size=36, fill=ASH, family=SERIF))
    y = 134
    for ln in wrap(desc, 70):
        b.append(t(36, y, ln, size=15, fill=ASH, family=SERIF, opacity=.93))
        y += 23
    c, _ = chips(stack, 36, 250, 600, size=11, h=24, gap=6)
    b.append(c)
    b.append(f'<line x1="640" y1="30" x2="640" y2="{H-30}" stroke="{WINE_LIGHT}"/>')
    b.append(diagram)
    b.append(t(964, H - 26, repo, size=12, fill=COPPER, anchor="end"))
    svg(name, W, H, "".join(b), f"{title}", f"{title}. {desc} Repository {repo}.")


def box(x, y, w, h, label, size=10, fill=OBS, stroke=COPPER, color=ASH, sw=1):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{stroke}" stroke-opacity=".75" stroke-width="{sw}"/>'
            + t(x + w / 2, y + h / 2 + size * 0.35, label, size=size, fill=color, anchor="middle", spacing=1))


def arrow(x1, y1, x2, y2, color=COPPER):
    ang = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 6 * math.cos(ang), y2 - 6 * math.sin(ang)
    px, py = -math.sin(ang) * 3.5, math.cos(ang) * 3.5
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-opacity=".8"/>'
            f'<path d="M{x2} {y2}L{hx+px} {hy+py}L{hx-px} {hy-py}Z" fill="{color}" fill-opacity=".85"/>')


def diag_threatlens():
    ox, g = 668, []
    names = [["DNS", "TLS"], ["HEADERS", "TECH ID"], ["OSINT", "CVE LOOKUP"]]
    for r, row in enumerate(names):
        for c, n in enumerate(row):
            g.append(box(ox + c * 100, 58 + r * 40, 90, 30, n))
    for r in range(3):
        g.append(arrow(ox + 192, 73 + r * 40, ox + 226, 118))
    g.append(box(ox + 228, 92, 66, 52, "", 10, fill=WINE, stroke=EMBER))
    g.append(t(ox + 261, 114, "SCORE", size=10, anchor="middle", spacing=1))
    g.append(t(ox + 261, 128, "REPORT", size=10, anchor="middle", spacing=1))
    g.append(t(ox + 148, 40, "SIX ANALYSIS MODULES", size=10, fill=COPPER, anchor="middle", spacing=2.5))
    g.append(t(ox + 148, 198, "HTML / PDF / JSON", size=10, fill=ASH, anchor="middle", spacing=2, opacity=.8))
    return "".join(g)


def diag_identity():
    ox, g = 656, []
    g.append(t(ox + 154, 40, "ACCESS WORKFLOW", size=10, fill=COPPER, anchor="middle", spacing=2.5))
    g.append(box(ox, 58, 84, 34, "REQUEST"))
    g.append(arrow(ox + 86, 75, ox + 106, 75))
    g.append(box(ox + 108, 58, 84, 34, "APPROVAL"))
    g.append(arrow(ox + 194, 75, ox + 214, 75))
    g.append(box(ox + 216, 58, 92, 34, "JIT ACCESS", fill=WINE, stroke=EMBER))
    g.append(t(ox + 262, 108, "simulated", size=10, anchor="middle", fill=ASH, opacity=.75))
    g.append(t(ox + 154, 142, "TAMPER-EVIDENT AUDIT CHAIN", size=10, fill=COPPER, anchor="middle", spacing=2.5))
    for i in range(5):
        x = ox + 6 + i * 62
        g.append(box(x, 156, 48, 28, f"#{i+1}", size=10))
        if i < 4:
            g.append(f'<line x1="{x+48}" y1="170" x2="{x+62}" y2="170" stroke="{EMBER}" stroke-width="1.6"/>')
    return "".join(g)


def diag_phish():
    ox, g = 646, []
    g.append(t(ox + 150, 40, "INVESTIGATION FLOW", size=10, fill=COPPER, anchor="middle", spacing=2.5))
    g.append(box(ox, 100, 52, 34, ".EML"))
    for i, n in enumerate(["EMAIL", "IOC", "URL"]):
        y = 62 + i * 46
        g.append(box(ox + 70, y, 90, 34, n + " AGENT", size=9))
        g.append(arrow(ox + 54, 117, ox + 70, y + 17))
        g.append(arrow(ox + 162, y + 17, ox + 180, 117))
    g.append(box(ox + 182, 90, 62, 54, "", fill=WINE, stroke=EMBER))
    g.append(t(ox + 213, 114, "RISK", size=10, anchor="middle", spacing=1))
    g.append(t(ox + 213, 128, "AGENT", size=10, anchor="middle", spacing=1))
    for i, v in enumerate(["BENIGN", "SUSPICIOUS", "INCONCLUSIVE", "MALICIOUS"]):
        g.append(t(ox + 256, 92 + i * 16, v, size=8.5, fill=ASH, opacity=.85))
    g.append(arrow(ox + 246, 117, ox + 254, 117))
    return "".join(g)


def diag_ssh():
    ox, g = 656, []
    g.append(t(ox + 154, 40, "AUTH TIMING, ILLUSTRATIVE", size=10, fill=COPPER, anchor="middle", spacing=2.5))

    def curve(mu, sd, color, dash):
        pts = []
        for i in range(0, 309, 4):
            x = i
            y = math.exp(-((x - mu) ** 2) / (2 * sd * sd))
            pts.append(f"{ox + x:.1f},{176 - y * 96:.1f}")
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="2" {dash}/>'

    g.append(curve(150, 40, COPPER, ""))
    g.append(curve(156, 40, EMBER, 'stroke-dasharray="5 4"'))
    g.append(f'<line x1="{ox}" y1="178" x2="{ox+308}" y2="178" stroke="{WINE_LIGHT}"/>')
    g.append(t(ox + 154, 198, "Welch's t-test, Cohen's d", size=10, fill=ASH, anchor="middle", spacing=1, opacity=.8))
    g.append(t(ox + 154, 60, "no significant difference", size=11, fill=ASH, anchor="middle", family=SERIF, style="italic"))
    return "".join(g)


def projects():
    project_card(
        "project-threatlens.svg", 1, "ThreatLens", "Python framework",
        "Modular framework that combines DNS, TLS, HTTP header, technology fingerprinting and OSINT checks with "
        "CVE correlation through the NVD API. Findings are scored with CVSS v3.1 and written to HTML, PDF and JSON reports.",
        ["Python", "AsyncIO", "NVD API", "Shodan"], "github.com/Alisha-chaudhary/ThreatLens", diag_threatlens())
    project_card(
        "project-identityguard.svg", 2, "IdentityGuard", "In active development",
        "Local IAM and access-governance lab covering role-based access control, joiner-mover-leaver workflows, "
        "access requests and approvals, segregation-of-duties checks and access review cycles. Privileged access is "
        "simulated with just-in-time grants, and actions are recorded in a tamper-evident audit chain.",
        ["Python", "FastAPI", "SQLAlchemy", "SQLite", "Pytest"], "github.com/Alisha-chaudhary/IdentityGuard", diag_identity())
    project_card(
        "project-phishmind.svg", 3, "PhishMind", "v1.0",
        "Phishing and business email compromise investigation platform. It parses .eml files, checks SPF, DKIM and "
        "DMARC, extracts indicators and uses cooperating agents to produce a structured verdict with confidence and "
        "MITRE ATT&CK mapping. It recommends response actions and never applies them. Validated on synthetic samples.",
        ["Python", "Email analysis", "Threat intel enrichment", "MITRE ATT&CK"],
        "github.com/Alisha-chaudhary/PhishMind", diag_phish())
    project_card(
        "project-ssh-enum.svg", 4, "ssh-enum", "Research study",
        "Re-investigates CVE-2016-6210, an OpenSSH username enumeration timing side-channel, on a default Ubuntu "
        "Server configuration. Timing measurements were tested with Welch's t-test and Cohen's d. No significant "
        "difference was found, documented as a reproducible negative result.",
        ["Python", "OpenSSH", "Hydra", "Metasploit", "Kali Linux"], "github.com/Alisha-chaudhary/ssh-enum", diag_ssh())


# ---------------------------------------------------------------- pipeline
def pipeline():
    W, H = 1000, 200
    steps = [("ASSESS", "Scope the system and its exposure"),
             ("VALIDATE", "Test the claim and reproduce the result"),
             ("CORRELATE", "Link CVEs, indicators and telemetry"),
             ("PRIORITISE", "Rank by impact and by evidence"),
             ("DOCUMENT", "Write findings others can act on")]
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="url(#pg)" stroke="{WINE}"/>']
    step = 190
    x0 = 100
    b.append(f'<line x1="{x0}" y1="62" x2="{x0 + step*4}" y2="62" stroke="{EMBER}" stroke-width="1.6" stroke-dasharray="6 6"/>')
    for i, (n, d) in enumerate(steps):
        cx = x0 + i * step
        last = i == len(steps) - 1
        b.append(f'<circle cx="{cx}" cy="62" r="19" fill="{OBS}" stroke="{COPPER}" stroke-width="1.5"/>')
        b.append(f'<circle cx="{cx}" cy="62" r="{9 if last else 6}" fill="{EMBER if not last else COPPER}"/>')
        b.append(t(cx, 112, n, size=13, fill=COPPER, anchor="middle", spacing=2.5, weight="bold"))
        for j, ln in enumerate(wrap(d, 22)):
            b.append(t(cx, 136 + j * 17, ln, size=11, fill=ASH, anchor="middle", opacity=.88))
        if i < 4:
            mx = cx + step / 2
            b.append(f'<path d="M{mx-4} 56L{mx+4} 62L{mx-4} 68" fill="none" stroke="{COPPER}" stroke-width="1.5"/>')
    svg("pipeline.svg", W, H, "".join(b), "Engineering approach",
        "Assess, validate, correlate, prioritise, document. " + " ".join(f"{n.title()}: {d}." for n, d in steps))


# ---------------------------------------------------------------- toolkit
def toolkit():
    W = 1000
    rows = [
        ("Languages", ["Python", "SQL", "Bash"]),
        ("Frameworks and standards", ["MITRE ATT&CK", "NIST CSF", "OWASP Top 10", "CIS Controls"]),
        ("Vulnerability and intelligence", ["CVE analysis", "CVSS v3.1", "NVD API", "Shodan", "VirusTotal", "AbuseIPDB", "urlscan.io"]),
        ("Detection and telemetry", ["Sysmon", "Splunk", "SPL", "Windows event logs"]),
        ("Security tools", ["Nmap", "Wireshark", "Burp Suite", "Hydra", "Metasploit", "Kali Linux"]),
        ("Engineering", ["FastAPI", "SQLAlchemy", "SQLite", "Pytest", "Git", "Linux", "Windows"]),
        ("Working knowledge", ["Tenable Nessus", "Qualys VMDR", "Microsoft Defender VM"]),
    ]
    y = 22
    body, desc = [], []
    for label, items in rows:
        c, bottom = chips(items, 290, y, W - 24, size=12, h=26, gap=8)
        body.append(t(32, y + 18, label, size=12, fill=COPPER, spacing=1))
        body.append(c)
        y = bottom + 14
        body.append(f'<line x1="32" y1="{y-7}" x2="{W-32}" y2="{y-7}" stroke="{WINE_LIGHT}" stroke-opacity=".7"/>')
        desc.append(f"{label}. {', '.join(items)}.")
    H = y + 8
    b = [f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="url(#pg)" stroke="{WINE}"/>'] + body
    svg("toolkit.svg", W, H, "".join(b), "Technical toolkit", " ".join(desc))


# ---------------------------------------------------------------- footer
def footer():
    W, H = 1000, 150
    defs = (f'<radialGradient id="fg" cx=".5" cy="0" r=".7"><stop offset="0" stop-color="{EMBER}" stop-opacity=".35"/>'
            f'<stop offset="1" stop-color="{OBS}" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" rx="14" fill="{OBS}"/>',
         f'<rect width="{W}" height="{H}" rx="14" fill="url(#fg)"/>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{WINE}"/>',
         f'<rect x="460" y="34" width="80" height="2" rx="1" fill="{EMBER}"/>',
         t(W / 2, 70, "EMBER ARCHIVE", size=13, fill=COPPER, anchor="middle", spacing=8),
         t(W / 2, 108, "Security through evidence, clarity, and careful engineering.", size=21, fill=ASH,
           family=SERIF, style="italic", anchor="middle")]
    svg("footer.svg", W, H, "".join(b), "EMBER ARCHIVE",
        "Security through evidence, clarity, and careful engineering.", defs)


# ---------------------------------------------------------------- snake placeholder
def snake_placeholder():
    W, H = 880, 192
    b = [f'<rect width="{W}" height="{H}" rx="10" fill="{OBS}"/>']
    for c in range(53):
        for r in range(7):
            b.append(f'<rect x="{16 + c*16}" y="{32 + r*16}" width="12" height="12" rx="2" fill="{WINE}" fill-opacity=".45"/>')
    b.append(f'<rect x="240" y="68" width="400" height="56" rx="8" fill="{OBS}" stroke="{WINE_LIGHT}"/>')
    b.append(t(W / 2, 92, "PLACEHOLDER", size=11, fill=COPPER, anchor="middle", spacing=4))
    b.append(t(W / 2, 112, "The snake replaces this file after the first workflow run", size=12, fill=ASH, anchor="middle"))
    path = os.path.join(OUT, "..", "output", "github-contribution-grid-snake.svg")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">'
                f'<title>Contribution snake placeholder</title>{"".join(b)}</svg>')


if __name__ == "__main__":
    hero()
    for n, l in [("pill-linkedin.svg", "LINKEDIN"), ("pill-github.svg", "GITHUB"), ("pill-repos.svg", "REPOSITORIES")]:
        pill(n, l)
    for n, num, lab, head in [
        ("sec-01-profile.svg", "01", "PROFILE", "Who I am and how I work"),
        ("sec-02-domains.svg", "02", "SECURITY DOMAINS", "Where the work sits"),
        ("sec-03-projects.svg", "03", "FEATURED PROJECTS", "Evidence in the repositories"),
        ("sec-04-approach.svg", "04", "ENGINEERING APPROACH", "From claim to finding"),
        ("sec-05-toolkit.svg", "05", "TECHNICAL TOOLKIT", "What I work with"),
        ("sec-06-record.svg", "06", "RECORD", "Experience, research and education"),
        ("sec-07-activity.svg", "07", "ACTIVITY", "Public contribution record"),
    ]:
        section(n, num, lab, head)   # all sections: obsidian bg + size 29 heading (match sec-02)
    terminal()
    domains()
    projects()
    pipeline()
    toolkit()
    footer()
    snake_placeholder()
    print("assets written to", os.path.abspath(OUT))
