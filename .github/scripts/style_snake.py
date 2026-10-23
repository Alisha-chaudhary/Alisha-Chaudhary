#!/usr/bin/env python3
"""Adds a solid obsidian background to the generated snake SVG.

snk writes a transparent SVG, which looks wrong on GitHub's light theme.
This inserts one rounded rectangle behind everything else. Safe to run twice.
"""
import re
import sys

BG = "#0B0B0E"
path = sys.argv[1]
svg = open(path, encoding="utf-8").read()

if 'data-ember-bg="1"' in svg:
    sys.exit(0)

m_tag = re.search(r"<svg\b[^>]*>", svg)
m_vb = re.search(r'viewBox="\s*(-?[\d.]+)[ ,]+(-?[\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)\s*"', m_tag.group(0)) if m_tag else None
if not (m_tag and m_vb):
    sys.exit("style_snake.py: could not find an <svg> tag with a viewBox, leaving file unchanged")

x, y, w, h = m_vb.groups()
rect = f'<rect data-ember-bg="1" x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{BG}"/>'
svg = svg[: m_tag.end()] + rect + svg[m_tag.end():]
open(path, "w", encoding="utf-8").write(svg)
print("background added")
