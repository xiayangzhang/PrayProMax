#!/usr/bin/env python3
"""backfill-prayers.py — run writeback over existing .session/ dirs.

The L1 writeback step is now part of pray-all.py, but the 8 committed
examples predate that change. This script reuses pray-all.py's
writeback_to_prayers() on each given session to seed prayers/ from the
existing work without re-running full dispatches.

Order matters: first-wins per (wish_type, tradition) pair, so the more
universal wishes should be processed first within each wish_type bucket.

Usage:
    python3 scripts/backfill-prayers.py                # all 8 examples in default order
    python3 scripts/backfill-prayers.py SESSION_DIR... # specific sessions
"""
import asyncio
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

# Late-import after sys.path setup so pray-all module-level state resolves correctly.
import importlib.util
spec = importlib.util.spec_from_file_location('pray_all', ROOT / 'scripts' / 'pray-all.py')
pray_all = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pray_all)

# Default backfill order: protection → wisdom → event (job-interview first for universality)
DEFAULT_ORDER = [
    'example-safe-travel-20260519-220849',
    'example-wisdom-study-20260519-220849',
    'example-job-interview-20260519-220849',
    'example-github-flourish-20260519-220849',
    'example-merge-pr-20260519-232810',
    'example-ship-clean-20260519-234418',
    'example-yc-app-20260520-000029',
    'example-hackathon-win-20260520-001628',
]


async def backfill_one(session_name):
    session_dir = ROOT / '.session' / session_name
    state_path = session_dir / 'state.json'
    if not state_path.exists():
        print(f'  ❌ no state.json in {session_name}')
        return None
    state = json.loads(state_path.read_text())
    print(f'  → {session_name}  (wish_type={state["wish_type"]}, matched={sum(1 for r in state["results"] if r["status"]=="match")})')
    wb = await pray_all.writeback_to_prayers(state, session_dir)
    print(f'      wrote={wb["written"]}, skipped-existing={wb["skipped"]}, extraction-failed={wb["failed"]}')
    return wb


async def main():
    sessions = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT_ORDER
    print(f'📚 backfilling {len(sessions)} sessions → prayers/')
    print()
    totals = {'written': 0, 'skipped': 0, 'failed': 0}
    for s in sessions:
        wb = await backfill_one(s)
        if wb:
            for k in totals:
                totals[k] += wb[k]
        print()
    print('=== totals ===')
    print(f'  written: {totals["written"]}')
    print(f'  skipped-existing: {totals["skipped"]}')
    print(f'  extraction-failed: {totals["failed"]}')


if __name__ == '__main__':
    asyncio.run(main())
