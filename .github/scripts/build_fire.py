#!/usr/bin/env python3
"""Generate a fire-effect contribution grid SVG from GitHub contribution data.

Queries the GitHub GraphQL API for the repository owner's contribution calendar,
then renders an SVG where each day cell is coloured by intensity using a fire
gradient (dark red -> orange -> yellow) with animated flame particles rising
from active cells. No JavaScript; SMIL animation plays in GitHub's web view.
"""
import json
import os
import sys
import urllib.request
import urllib.error

GRAPHQL_URL = "https://api.github.com/graphql"
OUTPUT = "output/fire-contribution.svg"

# Repository owner / username whose contribution graph we render.
LOGIN = os.environ.get("GITHUB_REPOSITORY_OWNER", "Alisha-chaudhary")

# Fire gradient by contribution count.
def fire_color(count):
    if count == 0:
        return "#0B0B0E"  # background (invisible cell)
    if count <= 2:
        return "#1A0A0A"  # ember
    if count <= 5:
        return "#4A1212"  # dark red
    if count <= 10:
        return "#8A2222"  # red
    if count <= 15:
        return "#D94F1F"  # orange-red
    return "#FF8C1F"      # orange / hot

def query_contributions(token):
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """
    body = json.dumps({"query": query, "variables": {"login": LOGIN}}).encode("utf-8")
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Alisha-chaudhary/fire-contribution-grid",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        sys.exit(f"build_fire.py: GitHub API HTTP {exc.code}: {exc.read().decode('utf-8', 'ignore')[:500]}")
    except urllib.error.URLError as exc:
        sys.exit(f"build_fire.py: GitHub API request failed: {exc}")

def build_svg(weeks):
    """Render the fire contribution grid SVG."""
    CELL = 10
    GAP = 2
    PAD_X = 14
    PAD_Y = 14
    COLS = len(weeks)          # 52 weeks
    ROWS = 7                   # 7 days
    width = PAD_X * 2 + COLS * (CELL + GAP)
    height = PAD_Y * 2 + ROWS * (CELL + GAP)

    # Collect active cells (count > 0) with their week index, weekday index, count.
    active = []
    for wi, week in enumerate(weeks):
        for day in week.get("contributionDays", []):
            count = int(day.get("contributionCount", 0))
            if count > 0:
                # weekday 0 = Sunday ... 6 = Saturday. GitHub grids start week on Sunday.
                wd = int(day.get("weekday", 0)) if "weekday" in day else None
                active.append((wi, wd, count))

    # Map count to a color index for flame variation.
    def flame_hue(count):
        if count <= 2:
            return 0   # red flame
        if count <= 7:
            return 1   # orange flame
        return 2       # yellow/white hot flame

    # Flame particle definitions (teardrop paths) + SMIL animation.
    flames = []
    flame_id = 0
    for (wi, wd, count) in active:
        cx = PAD_X + wi * (CELL + GAP) + CELL / 2
        cy = PAD_Y + wd * (CELL + GAP) + CELL / 2
        # Number of flame particles scales with intensity (1-3).
        n_flames = 1 if count <= 5 else (2 if count <= 12 else 3)
        for k in range(n_flames):
            delay = k * 0.6
            dur = 1.6 + (k % 3) * 0.4
            rise = 6 + (k % 4) * 4
            fh = flame_hue(count)
            if fh == 0:
                fcol = "#FF4500"   # orange-red
            elif fh == 1:
                fcol = "#FFA500"   # orange
            else:
                fcol = "#FFFF00"   # yellow
            # Teardrop flame path pointing up.
            path = f"M {cx:.1f},{cy:.1f} Q {cx-2:.1f},{cy+3:.1f} {cx:.1f},{cy-8:.1f} Q {cx+2:.1f},{cy+3:.1f} {cx:.1f},{cy:.1f} Z"
            flames.append(
                f'<g data-flame="{flame_id}">'
                f'<path d="{path}" fill="{fcol}" opacity="0">'
                f'<animate attributeName="opacity" values="0;0.85;0.35;0.9;0" dur="{dur}s" repeatCount="indefinite" begin="{delay}s"/>'
                f'<animate attributeName="y" values="0;{-rise}" dur="{dur}s" repeatCount="indefinite" begin="{delay}s" additive="sum"/>'
                f'</path>'
                f'</g>'
            )
            flame_id += 1

    # Build cell rects.
    cells = []
    for wi, week in enumerate(weeks):
        for day in week.get("contributionDays", []):
            count = int(day.get("contributionCount", 0))
            x = PAD_X + wi * (CELL + GAP)
            y = PAD_Y + int(day.get("weekday", 0)) * (CELL + GAP)
            cells.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{fire_color(count)}"/>'
            )

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="180" role="img" aria-labelledby="fire-title fire-desc">
  <title id="fire-title">Alisha Chaudhary's GitHub contribution fire grid</title>
  <desc id="fire-desc">Animated fire-effect contribution grid. Each cell is a day, coloured by contribution count using a fire gradient, with animated flame particles over active days.</desc>
  <rect x="0" y="0" width="{width}" height="{height}" rx="10" fill="#0B0B0E"/>
  {''.join(cells)}
  {''.join(flames)}
</svg>
'''
    return svg

def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("build_fire.py: GITHUB_TOKEN is not set (needs contents: write + repo scope)")

    result = query_contributions(token)

    if "errors" in result:
        sys.exit(f"build_fire.py: GraphQL errors: {result['errors']}")

    user = (result.get("data") or {}).get("user")
    if not user:
        sys.exit("build_fire.py: no user data returned from GraphQL API")

    weeks = user.get("contributionsCollection", {}).get("contributionCalendar", {}).get("weeks", [])
    if not weeks:
        sys.exit("build_fire.py: no contribution weeks returned")

    svg = build_svg(weeks)
    os.makedirs("output", exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"build_fire.py: wrote {OUTPUT} ({len(weeks)} weeks, {sum(len(w.get('contributionDays', [])) for w in weeks)} days)")

if __name__ == "__main__":
    main()
