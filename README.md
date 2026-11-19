# The Daily World — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/bongekanjing/ni18-hazel-marten-31/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/bongekanjing/ni18-hazel-marten-31/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

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

Bounty page: [make.fun/bounty/news-image-20261118](https://make.fun/bounty/news-image-20261118)

## License

MIT. The fonts are Playfair Display, Libre Franklin and Libre Baskerville,
all under the SIL Open Font License.
