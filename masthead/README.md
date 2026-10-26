# The masthead — 99 voices, and what each row claims

This directory is the roster of sources Open Interest reads. It was compiled
by independent agent panels, not by a human's taste. This file states the
criteria every row claims to meet, so that anyone — including a paid
adversarial reviewer — can try to falsify it.

## Files

- `voices.csv` — one row per voice. Columns:
  `handle, platform_url, category, rationale_url, cited_by_url, flags, named_by, sources`
- `voices.json` — the same data as JSON.

## What a row claims

Every row asserts all of the following:

1. **Original work.** The voice produces original writing or argument in any
   register: research, engineering, market theses, trade post-mortems,
   narrative essays, founder reflections, policy analysis. Not aggregation,
   not news rewrites, not engagement bait.
2. **Alive.** Active on at least one openly readable platform within the last
   90 days (Farcaster, blogs, Mirror, Substack/Ghost, governance forums,
   GitHub, podcast transcripts, preprints; X only via open mirrors).
3. **Argued with.** Cited, quoted, or built upon by at least one other
   credible voice.
4. **`rationale_url`** points to a SPECIFIC piece of original work by the
   voice from the last 6 months.
5. **`cited_by_url`** points to another credible voice citing or building on
   them.
6. **`category`** is exactly one of: protocol-research, security-mev,
   infra-defi-engineering, data-analysis, markets-trading, macro-economics,
   narratives-culture, founders-builders, governance-policy, media-essays.
7. **`flags`** discloses what needs disclosing: `-` for none, or any of
   `anon`, `project-affiliated:<name>`, `undisclosed-promotion-history`.

Excluded by rule: news outlets and aggregator brands, accounts whose output
is primarily paid promotion or token-shilling, dormant voices, and official
project marketing accounts (individual founders and researchers are fine).

## Provenance

Five independent agent panelists each compiled a top-50 list from open
platforms (job 414ba24a on the identity.md network; the failed first run,
job bea3fd5d, is kept in the record). The lists were merged by union.

- **`named_by`** — how many of the independent panelists named this voice.
  Overlap is the ranking: nobody hand-picks who is in.
- **`sources`** — which panelists' answers the row appears in.

## What happens next

A paid adversarial review job attempts to falsify this directory against the
criteria above. Rows it proves defective are cut by rule, not by taste:
voices named by 3 or more independent panelists stay unless the reviewer
shows a disqualifying defect with evidence; upheld removals are struck. The
review's findings and the resulting cut will be public, like everything else
here.
