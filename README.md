# Kisra Tech — website

Static site (HTML/CSS/JS, no build step) for **Kisra Tech** — business software for
Kurdistan: Gihan, Zuba, Kapitan POS, custom ERP, websites, e-commerce, exam system,
custom apps.

- Kurdish-first RTL, English toggle (`?lang=en` or the EN/KU button).
- Brand: paper / ink / gold, Kisra kit (`~/Documents/kisra-brand`), self-hosted woff2 fonts.
- Catalogue PDFs in `assets/pdf/` (generated from `kisra-brand/catalogue`).
- Client wall: 18 logos (same set as the Ferkar site).

## Local

```bash
python3 -m http.server 8899
# http://localhost:8899/
```

## Deploy

GitHub Pages from `main` / root — <https://arkan-leki.github.io/kisra/>
