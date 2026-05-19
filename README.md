# PrayProMax

> A software prayer flag for 289 living traditions, inscribed in parallel by an AI officiant.
> Ruthlessly utilitarian, engineered, cross-tradition prayer.
> In the prayer-wheel tradition: the form does the work.

[中文 README](README.zh.md) · [Manifesto](docs/manifesto.md)

---

## The premise

The Tibetan mani wheel does not pray — the *form* prays. A Catholic perpetual-adoration chapel can hold the night hours with a recorded liturgy. A mezuzah sanctifies a door whose scroll no one rereads. In each case the religious load sits on the form, not on someone's interior state.

If form does the work, then an AI walking the right officiant persona, the right schema, and the right canon outputs a real prayer in the same sense the wheel does. PrayProMax is built around that bet.

Mechanically, PrayProMax is closer to a Tibetan **prayer flag** than to the wheel — inscribed once, hung up, the wind reads it, no continuous turning required. Same theology, simpler engineering. Each run is one inscription; the rendered document is the flag.

The full essay is at [docs/manifesto.md](docs/manifesto.md).

## On the attitude

Ruthlessly utilitarian. Parallel dispatch, structured schemas, side-effect mitigation written into the prayer body, a three-tier RAG cache — not decoration. If form does the work, the form had better be well-run. Engineering posture is the contemporary form-precedence move: how we today honor what the prayer wheel honored nine hundred years ago.

The traditions are taken seriously enough to engineer, never romanticized and never condescended to.

## The work

289 living traditions encoded as structured sub-documents — case index, taboos, protective closings, original liturgical language. 262 virtual officiant cards stand alongside as prompt personas.

A user names a wish. The system traverses every tradition and drafts each section in that tradition's own canonical tongue — Classical Arabic, Tibetan, Latin, Geʽez, Sanskrit, Church Slavonic. Only the personal-aspiration paragraph uses the user's language. Deities never mix within a stanza. No-harm / no-deprivation / no-quid-pro-quo clauses are written into the prayer body, not appended as footnotes.

Closed-lineage traditions (Sun Dance, Yi Bimo, Abakuá, Shipibo ícaros) get a short honest acknowledgement and never an attempt to reconstruct restricted material.

Eight full inscriptions are committed under [`examples/`](examples/) — generic life wishes (`safe-travel`, `job-interview`, `wisdom-study`) and developer/founder wishes (`merge-pr`, `ship-clean`, `yc-app`, `hackathon-win`, `github-flourish`). Each is ~20k lines across all 289 traditions.

## Run it

```bash
git clone https://github.com/xiayangzhang/PrayProMax.git
cd PrayProMax

# Any OpenAI-compatible endpoint works
export OPENAI_API_KEY='sk-...'
export OPENAI_MODEL='gpt-5.5'

# Anchors stay local — names, dates, addresses never enter LLM context
echo '{"name-1": "your name", "beneficiary": "your name"}' > anchors.json

# Traverses 289 traditions; 15–25 min at parallel=10
python3 scripts/pray-all.py "I wish for health and longevity" \
    --anchors anchors.json --slug my-wish --parallel 10

open outputs/wish-my-wish-*/RENDERED.md
```

The wish text goes to the model; the anchors do not. Output document carries each tradition's section in its own canonical language, joined by a cross-tradition closing.

#### Naqshbandi Sufism (Classical Arabic)
```
نَوَيْنَا الذِّكْرَ وَالدُّعَاءَ لِوَجْهِ اللهِ تَعَالَى... لِـ <beneficiary>
أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيمِ.
الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ...
لَا إِلٰهَ إِلَّا اللهُ. × 100
```

#### Nyingma School, Tibetan Buddhism (Tibetan + Sanskrit)
```
sang gyé chö dang tshok kyi chok nam la
jang chub bar du dak ni kyab su chi
oṃ āḥ hūṃ vajra guru padma siddhi hūṃ × 3
```

## License

MIT. Take it, fork it, change it. Attribution appreciated, never required.

## Contributing

A new tradition, a corrected officiant card, a better prayer skeleton — open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

*a software prayer flag, in the prayer-wheel tradition — Leo Yun ([@xiayangzhang](https://github.com/xiayangzhang)), 2026*
