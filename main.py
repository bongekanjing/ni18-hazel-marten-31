#!/usr/bin/env python3
"""make.fun entry point — The Daily World, 18 November 2026.

Copies the pre-rendered front page to the output directory after checking that
the file is a complete, valid PNG within the competition's size limits. Standard
library only, no network, no clock, deterministic output.
"""

import os
import shutil
import struct
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "page.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
MAX_SIDE = 1024
MAX_BYTES = 1024 * 1024
PNG_SIG = b"\x89PNG\r\n\x1a\n"


def fail(msg):
    sys.stderr.write("error: %s\n" % msg)
    raise SystemExit(3)


def check_png(path):
    """Validate signature, IHDR geometry, chunk CRCs and the IEND terminator."""
    if not os.path.isfile(path):
        fail("missing %s" % path)
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        fail("image is %d bytes, over the 1 MiB limit" % size)

    with open(path, "rb") as fh:
        blob = fh.read()
    if not blob.startswith(PNG_SIG):
        fail("not a PNG (bad signature)")
    if blob[-8:] != b"IEND\xaeB`\x82":
        fail("PNG is truncated (no IEND)")

    width, height = struct.unpack(">II", blob[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        fail("image is %dx%d, over the %dpx limit" % (width, height, MAX_SIDE))

    # Walk every chunk so a corrupt CRC or a bad length fails here, not at judging.
    pos, n = 8, 0
    while pos < len(blob):
        (length,) = struct.unpack(">I", blob[pos:pos + 4])
        ctype = blob[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(blob):
            fail("chunk %r runs past the end of the file" % ctype)
        (crc,) = struct.unpack(">I", blob[end - 4:end])
        calc = _crc32(blob[pos + 4:end - 4])
        if crc != calc:
            fail("chunk %r has a bad CRC" % ctype)
        n += 1
        pos = end
        if ctype == b"IEND":
            break
    if pos != len(blob):
        fail("trailing bytes after IEND")
    return width, height, size, n


def _crc32(data):
    import zlib
    return zlib.crc32(data) & 0xFFFFFFFF


def main():
    w, h, size, chunks = check_png(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    dest = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(SRC, dest)
    sys.stdout.write(
        "wrote %s (page.png %dx%d, %d bytes, %d chunks)\n" % (dest, w, h, size, chunks)
    )


if __name__ == "__main__":
    main()
