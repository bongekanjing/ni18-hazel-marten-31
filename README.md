# The Daily World — 18 November 2026

![competition](https://img.shields.io/badge/make.fun-news--image--20261118-1f6feb)
![entry](https://img.shields.io/badge/entry-bongekanjing%2Fni18--hazel--marten--31-2ea043)
![license](https://img.shields.io/badge/license-MIT-8957e5)

A single front page that sums up Wednesday 18 November 2026: 18 headlines
(3 illustrated leads and 15 briefs across seven regions), a six-figure number
strip, a region index and a closing-levels tape, drawn to 1024x1024.

## What it does

`main.py` validates the shipped `page.png` — signature, IHDR geometry, every
chunk CRC, the IEND terminator, and the 1 MiB ceiling — then writes
`entry.png` to `$MAKEFUN_OUTPUT_DIR`. It is standard library only, needs no
network, reads no clock, and is byte-for-byte deterministic: two runs produce
the same SHA-256.

    MAKEFUN_OUTPUT_DIR=out python3 main.py

## Rebuilding the page

`render.py` draws the page with Pillow and the three bundled OFL fonts. It is
reproducible and offline; it is not part of the graded run, only the source of
`page.png`.

    python3 render.py
    python3 verify_layout.py    # deterministic layout audit

`verify_layout.py` instruments `ImageDraw` to capture every text box and then
reports pairwise overlaps and margin violations. The current page reports zero
of both.

## Content

The three leads are the European Commission's 45bn euro loan for Ukraine, the
Board of Peace's verdict on the Gaza ceasefire, and the Federal Reserve's
October minutes. Every figure on the page was taken from a report published on
18 November; where a source gave a move without a closing level, the page shows
only the move rather than inventing a number.

## License

MIT. The fonts are Playfair Display, Libre Franklin and Libre Baskerville,
all under the SIL Open Font License.
