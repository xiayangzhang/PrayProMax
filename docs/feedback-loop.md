# PrayProMax — Feedback Loop

> **Status: v0.1 has the local primitives (pray-all.py + propose-pr.py); GitHub Actions PR-review pipeline, auto-merge gating, and self-healing scans are PLANNED, not yet implemented.**

## The core insight

Search is expensive. If every user has to search the web for every tradition
for every wish, the system never amortizes its cost. **Community contribution
is the amortization**: one user's search becomes everyone's cache hit.

This document describes the loop.

## The loop

```
   user wish
       │
       ▼
   pray-all.py (3-tier resolve)
       │
       ├─ L1/L2 hits → cheap draft
       └─ L3 miss → grok --search → draft + STAGE enrichment
       │
       ▼
   .session/<wish>/enrichments/<tid>.md
       │   (per-tradition discoveries: new mantra found,
       │    new case_index entry proposed, sources cited)
       │
       ▼
   propose-pr.py  (T6 — to be built)
       │   bundles enrichments into:
       │   ├─ Type 1: case_index addition to existing tradition sub-md
       │   ├─ Type 2: new prayers/ skeleton entry
       │   └─ Type 3: new tradition / new officiant card (rare)
       │
       ▼
   gh pr create (branch per session, descriptive title + body)
       │
       ▼
   GitHub Actions review pipeline
       │   ├─ schema gate (must pass)
       │   ├─ lineage gate (must pass — see CONTRIBUTING)
       │   ├─ 3-worker review (claude/codex/grok mirror seed pipeline)
       │   ├─ sensitivity check (no slurs, no attacks)
       │   └─ trust score
       │
       ▼
   auto-merge gates:
       ├─ 2/3 agent approval + schema pass → auto-merge (low-risk: additions)
       └─ corrections to existing classical content → human review required
       │
       ▼
   upstream INDEX / case_index / prayers/ enriched
       │
       ▼
   future users' L1/L2 cache HIT (no search needed)
```

## Two PR streams, different cadences

**Maintainer PR stream** (slow, bulky)
- Phase E cold-start, periodic re-audits, schema migrations
- Bundle many changes per PR
- Human (maintainer) reviews bigger diffs

**Community PR stream** (fast, narrow)
- One user's session contributes 0-5 enrichments at a time
- Single-change PR ok
- 3-agent CI review → auto-merge if all gates pass

## Two PR types, different gates

**Additive PRs**
- New case_index entry for existing tradition
- New prayers/ skeleton
- New officiant card
- Gates: 2/3 agent approval + schema valid → **auto-merge**

**Corrective PRs**
- Modify existing case_index / mitigation / taboos
- Modify classical-source-cited content
- Gates: 3/3 agent + **human (maintainer)** review
- Especially: changes to entries marked `source: classical` cannot be downgraded

## PII isolation across the loop

The PR pipeline carries **only placeholder-preserved content**. User anchors
(name, dob, address) never make it past the local render step. The
`.session/<wish>/` work dir and `outputs/<wish>/sections/` (with anchors
rendered) are `.gitignore`d. Only `enrichments/` (anchor-placeholder versions)
become PR material.

## Anti-vandalism gates (proposed for community-PR pipeline)

- **Delete-content PR** → human review required
- **Add-content PR with empty verification field** → auto-reject
- **PR touching >N files** → split or auto-reject
- **Sensitivity-flag content** (slurs, tradition attacks) → auto-reject
- **Submission rate-limit** per contributor (basic abuse guard)

## Self-healing scans (orthogonal to user-triggered loop)

A periodic GH Action should:
- Verify `verification:` URLs (404 detection)
- Detect schema drift (added fields → old entries missing)
- Find cross-entry contradictions (A says X, B says ¬X)
- Re-examine borderline entries (`status: skipped` with reason `no-lineage` should
  be revisited if newer sources surface)
- Detect orphaned officiant cards / dangling required_officiants references

Each finding opens its own small PR.

## Schema evolution (planned)

When the schema changes:
1. Bump `version:` in INDEX header
2. Old entries auto-grandfathered with `_schema_version: 1`
3. Migration script written + tested
4. PR includes the migration as a single coherent change

## Trust scoring (deferred)

Per `entry.correction_history`:
```yaml
correction_history:
  - { at: 2026-05-18, by_pr: 42, what: "...", agent_review: "3/3" }
  - { at: ..., by_pr: 51, what: "...", agent_review: "2/3" }
trust_score: 0.87
```

Used by:
- Review agents (weight existing content against proposed changes)
- Pray dispatcher (prefer high-trust content when multiple options)

## "Inbred drift" mitigation

If the system always uses its own output to train future output, it drifts
from real-world tradition. Counters:

- Periodic codex/grok scan for new academic / contemporary practice (external
  data injection)
- Real-practitioner feedback channel: GH issue template "I'm a practitioner of
  X, entry Y is wrong because Z"
- `source: classical` content is **immutable** (cannot be downgraded; AI-
  synthesized content cannot promote to `classical` without human + citation)
