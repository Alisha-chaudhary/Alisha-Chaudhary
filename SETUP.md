# EMBER ARCHIVE setup guide

## Directory structure

```
Alisha-Chaudhary/                  <- repository name must match your username (case-insensitive)
├── README.md                      <- the profile page
├── SETUP.md                       <- this file (delete it from the repo if you prefer a cleaner root)
├── assets/                        <- 24 SVG files, all generated
│   ├── hero.svg
│   ├── pill-*.svg                 <- link buttons
│   ├── sec-01 ... sec-07-*.svg    <- section headers
│   ├── terminal-profile.svg
│   ├── domain-*.svg               <- five security domain panels
│   ├── project-*.svg              <- four featured project cards
│   ├── pipeline.svg
│   ├── toolkit.svg
│   └── footer.svg
├── output/
│   └── github-contribution-grid-snake.svg   <- placeholder, replaced by the workflow
├── tools/
│   └── build_assets.py            <- regenerates everything in assets/
└── .github/
    ├── workflows/snake.yml
    └── scripts/style_snake.py
```

## Steps

1. Copy the folder contents into your existing profile repository, `Alisha-chaudhary/Alisha-Chaudhary`, on the `main` branch.
2. In the repository go to Settings, then Actions, then General. Under Workflow permissions choose **Read and write permissions** and save. The workflow also declares `contents: write`, but this repository setting must not block it.
3. Commit and push to `main`.
4. Open the Actions tab, choose **Generate contribution snake**, and press **Run workflow**.
5. When the run is green, open `output/github-contribution-grid-snake.svg` in the repository and confirm it now shows your real contribution graph instead of the placeholder.
6. Reload your profile. The snake runs again every 12 hours.

## Changing the artwork

Edit `tools/build_assets.py` (static panels) or `tools/build_animated.py` (animated hero, headers, terminal, pipeline, footer and project diagrams), then run `python tools/build_assets.py && python tools/build_animated.py` from the repository root and commit the changed SVGs.

## Known rendering limits

* GitHub shows SVGs inside `<img>`, so web fonts cannot load. The files use Georgia and system monospace fonts with fallbacks, so letter shapes differ slightly between Windows, macOS, Linux and Android.
* The snake SVG and the two statistics cards are external to your content. If they fail, the rest of the page still works.
* `github-readme-stats.vercel.app` is a public instance that is sometimes rate limited. If it keeps failing, delete those two images or self-host the service.

## Validation checklist

**Facts to confirm before publishing**

- [ ] LinkedIn URL. Your live GitHub profile points to `linkedin.com/in/alisha-chaudhary-/` and this README uses `linkedin.com/in/alishaachaudhary`. Keep whichever one opens your real profile.
- [ ] Internship dates read Jan 2026 to Jun 2026. Earlier material gave March to June. Use the correct one.
- [ ] The mitreattack-python pull request is still unmerged. If it has merged, change "Under maintainer review".
- [ ] IdentityGuard and PhishMind repositories exist, are public, and the names match the links.
- [ ] Each project description still matches its repository README. The cards say nothing about test counts, users, performance or deployment.
- [ ] Every skill in the toolkit is something you can discuss in an interview.

**Links and assets**

- [ ] All links in the README open the right page.
- [ ] Every `assets/` and `output/` path loads. A broken image shows its alt text.
- [ ] The snake workflow run is green and the SVG in `output/` is no longer the placeholder.

**Rendering**

- [ ] Check the profile on desktop in light mode and dark mode.
- [ ] Check it on a phone. Text inside the cards is smaller there, so look at the project cards in particular.
- [ ] Run the page through a screen reader or read the alt text. It carries the full content of each image.

## Animation notes

* The hero sphere is real 3D maths (Fibonacci sphere, rotation, perspective) baked into SVG animation frames. GitHub does not allow JavaScript, so this is the supported way to get 3D.
* Animation is SMIL and plays in GitHub's web view. Some mobile apps and email clients show only the first frame, which is still a complete image.
* The animated hero is about 170 KB. Everything else is under 12 KB.
