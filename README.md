# Next Partitions proposal (September 2026)

Source for the proposal published at **https://np-proposal-2026.vercel.app/**

Prepared by Rank Friendly (Joseph Green) for Next Partitions (Abe Gold).
Proposed start date: September 15, 2026.

## Files

| Path | What it is |
|---|---|
| `index.html` | The whole proposal — 13 pages, all content and all styling in one file. This is the only file you edit for text changes. |
| `images/` | The 7 screenshots used as evidence on pages 2 and 3. |
| `build-single-file.py` | Rebuilds `proposal-single-file.html`, one self-contained file for emailing or printing. Not needed for the website. |

The page is plain HTML and CSS. There is no build step, no framework and no
JavaScript — open `index.html` in a browser and what you see is what ships.

## What is in the proposal

| Page | Section |
|---|---|
| 1 | Cover, and **01** — the market is open: $21.74 average cost per click, difficulty 23, 170 unclaimed city searches |
| 2 | **02** — site audit of all 48 pages: 18 strong, 25 thin, 3 broken |
| 3 | The four conflicting quote-time promises, and what a buyer can and cannot verify |
| 4 | What the market leaves open, and **03** — four jobs, starting with proof you are real |
| 5 | Jobs 2–4: installer directory, one product list, customer service — plus the Shabbat and holiday notice |
| 6 | **04** — how a facilities manager finds you; what every industry page carries |
| 7 | **05** — month one, itemised to 260 credits |
| 8 | Months two to six, and **06** — the 30 / 90 / 180 day checkpoints |
| 9 | **07** — pricing: $6,500 (recommended) or $8,500 a month, and how credits work |
| 10 | **08** — optional 90-day Google Ads test, and **09** — what is not covered |
| 11 | **10** — what we need from you, and **11** — the agreement and signature block |
| 12 | **12** — how to pay (Square link and bank transfer details) |
| 13 | Supplement — pay in advance, get extra months free, and the 12-business-hour guarantee |

### Figures that appear in more than one place

Change one of these and search the file for the others, so the document stays
consistent:

- **$6,500 / 260 credits** — pages 4, 7, 9, 13
- **$8,500 / 340 credits** — pages 9, 13
- **Seven manufacturers** (Bobrick, Bradley, Metpar, Scranton, ASI Global, Ammco, Hadrian) — pages 4, 7, 8
- **48 pages / 18 strong / 25 thin / 3 broken** — pages 2, 6, 8
- **$34,000 competitor ad spend** — pages 9, 10
- **September 15, 2026 start date** — pages 1, 11, 13
- **Page N of 13** footers — every page

Two placeholders are still open, both marked `class="fill"` in the HTML:
the ad-test budget figure, and the plan and payment terms in the agreement
block on page 11.

## Editing

Ask Claude for the change you want, or edit `index.html` directly. Useful
markers when searching the file:

- `<div class="page">` starts each printed page
- `<div class="sec"><span class="n">07</span>` is the numbered section heading
- `<div class="panel p-gold">` etc. are the coloured callout boxes
  (`p-blue`, `p-green`, `p-amber`, `p-red`, `p-purple`, `p-gold`)
- `<div class="card c-g">` are the three-across cards
- `<span class="fill">` marks a blank still to be filled in

Colours, fonts and page size are the `:root` variables at the top of the
`<style>` block. Page size is A4 (210mm × 297mm) and the document is designed
to print — check any layout change with your browser's print preview, not just
on screen.

If you add a page, update the `Page N of 13` footer on every page.

## Publishing a change

The Vercel project `np-proposal-2026` is connected to this repository, so every
push to `claude/dazzling-rubin-ip5o5a` builds automatically. That branch is the
one and only working branch: edit it, push it, and the site rebuilds in about a
minute.

**One setting to check once.** Vercel has to treat this branch as the production
branch, or pushes build as previews instead of going live. In Vercel, open
`np-proposal-2026` → Settings → Git → Production Branch and set it to
`claude/dazzling-rubin-ip5o5a`. After that, every push updates
https://np-proposal-2026.vercel.app/ directly.

Until that setting is changed, a push builds a preview at
`np-proposal-2026-git-claude-dazzling-rubin-ip5o5a-rmbh.vercel.app`, which needs
a Vercel login to open, and the live URL keeps serving the last production
deployment.

**Edits are public as soon as they are pushed.** There is no promote step and no
review gate, and the live URL is the one the client reads, so treat a push as
publishing. If you want to see a change before it goes out, ask for a preview
deployment first. If something lands wrong, Vercel keeps every previous
deployment: open the project's Deployments tab and roll back to the one before.

## Sending it as a single file

    python3 build-single-file.py

Writes `proposal-single-file.html` with the screenshots embedded, so it works
as an email attachment or a file on a USB stick with no folder around it. It is
gitignored, because it is rebuilt from `index.html` whenever you need it.
