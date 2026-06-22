# DISCOVERY — organvm/life-betterment-simulation

**Date:** 2026-06-22 · **Verdict:** PROMOTE (real latent value) · **Tier:** ranked (value-repos.json)

## Value Thesis

The README brands this repo `DESIGN_ONLY`, but that label undersells it: the repo
already contains a **fully working, LLM-powered interactive product**. The crown
jewel is `friend-zone_contagion_v1.8.html` — a self-contained "Social Influence
Simulator" (583 lines, zero build step) that renders a draggable force-directed
social-network graph and wires it to the Gemini API (`gemini-2.0-flash`) for three
genuinely useful capabilities: (1) generating personality nodes from free-text
persona descriptions, (2) propagating life-event trait changes through the network
weighted by per-node influence, and (3) producing an AI "social-dynamics coach"
analysis of an inner circle's strengths, blind spots, and actionable advice.
Alongside it sit two working Three.js (r180) WebGL apps — interactive 3D Buddhist
cosmology gameplay maps (`easterncosmos-v.html`, `easterncosmos-vv.html`) — a spiral
growth-animation design, a pitch deck (`docs/pitch/index.html`), and a substantial
research corpus (Cialdini "Beyond the Five," social-contagion theory, Human Design
scheduling, a Siddhartha-arc journal). The highest latent value is therefore a
**deployable consumer/coaching web product** plus two **reusable estate assets**: an
"AI social-dynamics coach + network-contagion engine" that ORGAN-III (Commerce) could
productize as a self-improvement SaaS, and a drop-in Three.js network/cosmology
visualization layer other ORGAN-II (Art) repos can reuse. None of this is archival —
the interactive artifacts run today; they are simply unpromoted and undeployed.

## What's actually here (verified)

- `friend-zone_contagion_v1.8.html` — working LLM social-influence simulator (Gemini).
- `easterncosmos-v.html` / `easterncosmos-vv.html` — working Three.js 3D cosmology maps.
- `animating-a-spiral-shape-for-web-2.md` — growth-spiral animation design + code.
- `docs/source-materials/` — theory, research PDFs/DOCX, prototypes, PROVENANCE.yaml.
- `docs/pitch/index.html` — investor/explainer pitch page.
- `src/life_betterment_simulation/core.py` — Python stub (`main()` prints a version);
  the real value lives in the HTML/JS artifacts, not the Python package.

## Single best concrete first task

**Promote the Social Influence Simulator to a deployable demo.** Copy
`friend-zone_contagion_v1.8.html` to a top-level `index.html` entrypoint, replace the
empty inline `apiKey` with a documented runtime config path (env-injected key or a
"paste your Gemini key" field) so it runs outside the original sandbox, and ship it as
a static site (the repo already targets static hosting; no build step needed). This
turns an unrunnable-as-shipped prototype into a live, shareable product in one PR and
unblocks the ORGAN-III productization path named in the README.

## Build status

Green. `pip install -e . && pytest` → 1 passed (mirrors `.github/workflows/ci.yml`).
