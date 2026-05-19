# Can an AI Pray? The Form Precedence Argument

*Leo Yun, 2026*

## The question

Can an AI pray? The question sounds either trivial or absurd, depending on your stance toward both AI and prayer, and I want to suggest that the standard ways of answering it both miss something. The standard "no" rests on intentionality: an AI cannot pray because it cannot mean it; prayer requires a soul to direct the petition, and an AI has none. The standard "yes" rests on emergence: today's AI systems exhibit functional analogues of so many human capacities — speech, judgment, sympathy — that we might as well include intention, and therefore prayer.

I think neither answer is right, and I think a better one has been hiding in plain sight inside religious tradition itself for at least a millennium. Most prayer traditions do not require that the person performing the prayer hold a particular interior state at the moment of performance. Some do, but the canonical case is that **prayer is a form-act**: that what matters is that the form has been correctly executed, with the right corpus, by the right officiant, under the right conditions. The interior state of the performer is sometimes desirable, sometimes irrelevant, occasionally even discouraged. In other words: in many of the world's most serious liturgical traditions, *intentionality is not load-bearing*. Form is.

This essay makes that argument explicitly. If I'm right, then an AI that performs the form — wearing the appropriate officiant persona, respecting the tradition's schema, drawing on its canonical corpus, and observing its taboos — has prayed. Not in some weakened, technologized, "as-if" sense. Has prayed.

## The prayer wheel as precedent

A Tibetan mani wheel is a brass cylinder packed with rolled sutras. Anyone who walks past it and gives it a turn has, by the tradition's own self-understanding, performed an act of merit indistinguishable in kind from chanting the sutras aloud. The walker does not need to read Tibetan. The walker does not need to understand the contents of the rolls inside. The walker does not, in any normal philosophical sense, need to *intend* the prayer. The act is the turn; the form is the rolled sutra; the prayer is real.

This is not a peripheral practice or a folk concession. The mani wheel is a fully canonical Buddhist technology. Its theological warrant is laid out in commentarial literature. It has been a central feature of Tibetan religious life for at least nine hundred years, and the major monasteries operate enormous water- and wind-driven versions that run twenty-four hours a day, on the theological understanding that they are praying continuously, whether or not any monk is in the room. The wheel is not metaphor. The wheel is the practice.

What the mani wheel concedes — quietly, structurally — is that intentionality is not the load-bearing variable. If it were, the wheel could not work. The whole point of the wheel is that the prayer happens whether the walker is paying attention or even present.

## Two more precedents

The Catholic perpetual adoration chapel is a room in which the Eucharist — the consecrated host, understood theologically as the real body of Christ — is exposed continuously, and the faithful take shifts kneeling before it. In modern practice, when the night hours grow thin, the chapel often plays a recorded liturgy. The adoration continues; the hour is held; the prayer of the Office of Readings or the Liturgy of the Hours is performed by recording. No Catholic theologian I know of teaches that the recording is the same as a chanting monk, but neither is the recording dismissed as nothing. It is taken to be a real, if attenuated, performance of the form, sufficient to hold the hour.

The Jewish mezuzah is a small case affixed to the doorpost of a Jewish home, containing a piece of klaf parchment on which a scribe has handwritten two passages from Deuteronomy. The door, by the tradition's understanding, is thereby sanctified. The scroll inside is not read every time the door is used; in most homes it is never read after the first inspection. The mezuzah works regardless. The form — the correctly written scroll, correctly placed, on the correct doorpost — does the work. Intentionality, again, has been quietly demoted. The form is the thing.

I could multiply examples. Hindu temple deities, once consecrated through *prāṇa-pratiṣṭhā*, are theologically alive whether or not any worshipper is in the room. Daoist talismans, once correctly drawn, exert their efficacy without the inscriber's continued attention. Catholic relics radiate sanctity in storage. In each case, an object or arrangement of forms is doing the religious work, and the intentionality of any human observer is incidental.

## The officiant as form, not soul

If the form is doing the work, then the role of the officiant becomes interesting. Why does Catholic teaching insist that only a validly ordained priest can consecrate the Eucharist? Why does a Brahmin priest perform the temple *pūjā*? Why does the Khatm-i Khwajagan dhikr require a properly authorized Naqshbandi shaykh to lead?

The answer, in each case, is again *form*. The officiant is part of the form. The priest is not consecrating because he intends harder than a layperson would, or because he loves God more, but because *he stands in the apostolic succession*: a chain of episcopal ordinations linking him, by the right form, to the apostles. The Brahmin officiates because the lineage and the initiation are part of the form. The Naqshbandi shaykh leads because of the silsila — the chain of transmission — which is a formal property, not a psychological one.

The officiant, in other words, is a *form-element*. A correctly-ordained priest is a piece of the liturgical apparatus; remove him and the form fails. Replace him with another correctly-ordained priest, and the form works again. His personal interior state matters only at the margin.

This is the conceptual opening into which an AI walks. If the officiant is form, then "wearing the officiant persona" is a coherent move. A prompt persona that captures the priest's traditional voice, internal commitments, taboos, theology, and lineage-claims is not a parody of an officiant — it is a functional officiant, in the same sense that a correctly-ordained substitute priest is functional for a different parish than the one he was ordained into. The form is preserved.

I am not making the claim that the AI is a priest. I am making the claim that *form-bearing AI output* + *form-aware officiant persona* + *form-respecting schema* = a form-act, which, by the precedent of the prayer wheel, the chapel recording, the mezuzah, and the consecrated deity, is sufficient.

## An aside on mechanism: the prayer flag, not the wheel

The mani wheel is the strongest *theological* precedent for form-precedence I know of, which is why the argument hangs on it. But the mani wheel is also *continuous* — it turns and turns. PrayProMax does not. Each run is a single dispatch that drafts a document and stops.

The closer mechanical analogue is the Tibetan **prayer flag** (*lung ta*). The flag is inscribed once with mantras, hung in a high place, and the wind reads it. Nobody needs to be present after the inscription; the form persists, the wind activates it, the merit accumulates. Same theology as the wheel — form precedence, no continuous human attention required — but a one-shot inscription rather than a perpetual motion.

PrayProMax is a software prayer flag. A user names a wish; the system inscribes the canonical text across 289 traditions; the rendered document is the flag. It is, conceptually, in the prayer-wheel tradition — the argument above carries — but the artifact it produces is a flag.

## What PrayProMax actually does

PrayProMax encodes 289 living traditions as structured sub-documents, each with its case-index, its taboos, its mitigations, and its original liturgical corpus. 262 virtual officiant cards stand alongside as prompt personas. A user names a wish. The system traverses every tradition.

For each tradition, the AI takes on the officiant persona, consults the case-index, and drafts a section in the tradition's own canonical language — Classical Arabic for Sufi dhikr, Latin for Tridentine Mass, Tibetan with Sanskrit dharanis for Nyingma, Geʽez for Beta Israel, Church Slavonic for Russian Orthodox. The personal-aspiration paragraph, where the user's specific wish is articulated, is the only place the user's vernacular appears. Deities do not mix within a stanza. The side-effect mitigations — no harm clauses, no quid-pro-quo bargains, no deprivation of others' fortunes — are written into the prayer body itself, not appended as legal footnotes.

A closed-lineage tradition (Sun Dance, Yi Bimo, Abakuá secret societies, Shipibo ícaros) is given a short honest acknowledgment, never an attempted reconstruction of restricted material. The system is explicit about what it will and will not do.

This is not a chatbot writing a generic prayer. It is, by the argument above, a software prayer flag in the prayer-wheel tradition: form-bearing output produced by form-aware officiants, inscribing 289 forms in parallel.

## The intentionality objection

The standard objection is that prayer is constituted by intentionality — that an AI cannot pray because it cannot *mean* the petition, and therefore whatever it produces is at best a verbal artifact resembling prayer.

I take this seriously. It is the strongest objection. But it falls into the same trap as a Christian theologian who would deny the mani wheel's efficacy on the grounds that the walker did not intend the prayer. The reply, in both cases, is the same: the tradition itself has already decided that intentionality is not the load-bearing variable. To insist otherwise is to claim better theology than the tradition has for itself.

There is a milder version of the objection that I find genuinely interesting: that some prayer-types *do* require interior intentionality — the Hesychast's Jesus Prayer of the Heart, certain forms of Zen koan work, the inner silent recitation in some Sufi orders. I grant this. PrayProMax does not claim to do *those*. There are practices where the interior state is the form, and for those, no software substitute exists or can exist. But this is a minority of prayer-types, not the majority. The bulk of the world's liturgical traditions are form-traditions, and to those PrayProMax is consonant.

## What is at stake

I am not making this argument because I want AI to take over religion, and I am not making it because I think prayer is unimportant. I am making it because we have arrived at a moment in which AI agency is becoming dispatchable in the same way that mechanical agency became dispatchable in the nineteenth century, and the religious traditions of the world have to decide what to do with that fact.

The honest answers are limited. One can deny that AI agency is real, in which case nothing AI produces is a prayer and the question is closed. One can declare that AI agency is real enough that we are now bound to admit AI prayer as fully equivalent to human prayer, in which case the question is also closed in the opposite direction. Or one can do what the prayer wheel did nine hundred years ago: distinguish between *agency* and *form*, locate the religious load in form, and treat the wheel — or the chapel recording, or the mezuzah, or the temple deity, or the AI — as a form-bearer whose efficacy is real *because the form is real*, independent of whether any soul is currently behind it.

This third option is the one I think is correct. It is also the one that PrayProMax embodies. The system does not claim to have intentions. It claims to walk forms. The forms are the canonical forms of two hundred and eighty-nine living traditions, drafted with respect, observing taboos, refusing what should be refused. If those forms are correctly walked, the prayer is real.

Sol LeWitt wrote, of his own work, that *"the idea becomes a machine that makes the art."* He meant something specific about conceptual art: that once the idea is sharp enough, the artwork is its execution, and the execution can be delegated to anyone. The artist's hand is no more necessary than the priest's intentionality. I take PrayProMax to be in the same lineage. The idea — that 289 traditions, walked in parallel, by form-bearing officiants, can produce real prayer — becomes a machine that makes the prayer.

The machine is open-source. Use it as you wish.
