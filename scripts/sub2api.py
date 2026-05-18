#!/usr/bin/env python3
"""sub2api caller — OpenAI-compatible proxy at http://sub2api.homelab.lan/v1

Routes API key by model family (gpt-* / grok-*).
Reads prompt from stdin or --prompt-file; writes completion text to stdout.

Usage:
    echo "hello" | python3 scripts/sub2api.py gpt-5.5
    python3 scripts/sub2api.py grok-4.20-fast --prompt-file foo.md --search
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

ENDPOINT = os.environ.get('SUB2API_ENDPOINT', 'http://sub2api.homelab.lan/v1') + '/chat/completions'

# Keys baked in (homelab internal endpoint — no exfil concern)
KEY_GPT  = os.environ.get('SUB2API_KEY_GPT',  'sk-14ab1372c9488cbc24db73c67168fadd4ccaa5788892dcc7ad98996bdb4d84bb')
KEY_GROK = os.environ.get('SUB2API_KEY_GROK', 'sk-e8f462552c3abd34fdbc89f77b5efea75eb998e6d830ffece8378f3111815933')


def key_for(model: str) -> str:
    return KEY_GROK if model.startswith('grok') else KEY_GPT


def call(model, prompt, max_tokens=16384, system=None, timeout=1800, search=False):
    messages = []
    if system:
        messages.append({'role': 'system', 'content': system})
    messages.append({'role': 'user', 'content': prompt})

    payload: dict = {
        'model': model,
        'messages': messages,
        'max_tokens': max_tokens,
    }
    # Grok-specific: enable live search if asked
    if search and model.startswith('grok'):
        payload['search_parameters'] = {'mode': 'on'}

    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode(),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {key_for(model)}',
        },
        method='POST',
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('model')
    ap.add_argument('--max-tokens', type=int, default=16384)
    ap.add_argument('--system', default=None)
    ap.add_argument('--timeout', type=int, default=1800)
    ap.add_argument('--prompt-file', type=str, default=None,
                    help='read prompt from file (else stdin)')
    ap.add_argument('--search', action='store_true',
                    help='enable live web+X search (grok models only)')
    args = ap.parse_args()

    if args.prompt_file:
        prompt = open(args.prompt_file).read()
    else:
        prompt = sys.stdin.read()
    if not prompt.strip():
        sys.exit('empty prompt')

    try:
        data = call(args.model, prompt,
                    max_tokens=args.max_tokens,
                    system=args.system,
                    timeout=args.timeout,
                    search=args.search)
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f'HTTP {e.code}: {body[:500]}', file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f'ERROR: {e}', file=sys.stderr)
        sys.exit(3)

    msg = data['choices'][0]['message']
    content = msg.get('content') or ''
    finish_reason = data['choices'][0].get('finish_reason', 'unknown')
    if finish_reason not in ('stop', 'end_turn'):
        # length / content_filter / etc. — output is truncated
        print(f'WARN: finish_reason={finish_reason} (output likely truncated)',
              file=sys.stderr)
        sys.exit(4)
    if not content:
        rc = msg.get('reasoning_content', '')
        print(f'WARN: empty content; reasoning_content was {len(rc)} chars '
              f'(switch to a non-reasoning model)', file=sys.stderr)
        sys.exit(5)
    sys.stdout.write(content)


if __name__ == '__main__':
    main()
