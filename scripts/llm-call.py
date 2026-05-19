#!/usr/bin/env python3
"""OpenAI-compatible chat completions caller.

Reads prompt from stdin (or --prompt-file); writes completion text to stdout.
Defaults to the official OpenAI API. Override OPENAI_ENDPOINT to point at any
compatible proxy (Azure OpenAI, LiteLLM, OpenRouter, your own gateway, etc.).

For Grok models (model name starts with `grok-`), reads XAI_API_KEY and
XAI_ENDPOINT (or falls back to OPENAI_API_KEY / OPENAI_ENDPOINT).

Env vars:
  OPENAI_API_KEY     required (or XAI_API_KEY for grok-* models)
  OPENAI_ENDPOINT    optional, default: https://api.openai.com/v1
  XAI_ENDPOINT       optional, default: https://api.x.ai/v1

Usage:
    echo "hello" | python3 scripts/llm-call.py gpt-5.5
    python3 scripts/llm-call.py grok-4.3 --prompt-file foo.md --search
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error


def endpoint_for(model):
    if model.startswith('grok'):
        base = os.environ.get('XAI_ENDPOINT', 'https://api.x.ai/v1')
    else:
        base = os.environ.get('OPENAI_ENDPOINT', 'https://api.openai.com/v1')
    return base.rstrip('/') + '/chat/completions'


def key_for(model):
    if model.startswith('grok'):
        return os.environ.get('XAI_API_KEY') or os.environ.get('OPENAI_API_KEY', '')
    return os.environ.get('OPENAI_API_KEY', '')


def call(model, prompt, max_tokens=16384, system=None, timeout=1800, search=False):
    messages = []
    if system:
        messages.append({'role': 'system', 'content': system})
    messages.append({'role': 'user', 'content': prompt})

    payload = {
        'model': model,
        'messages': messages,
        'max_tokens': max_tokens,
    }
    # Grok-specific live search (xAI native param)
    if search and model.startswith('grok'):
        payload['search_parameters'] = {'mode': 'on'}

    key = key_for(model)
    if not key:
        print('ERROR: no API key (set OPENAI_API_KEY or XAI_API_KEY)', file=sys.stderr)
        sys.exit(2)

    req = urllib.request.Request(
        endpoint_for(model),
        data=json.dumps(payload).encode(),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {key}',
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
                    help='enable live web/X search (grok models only)')
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
