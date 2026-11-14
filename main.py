"""ai-happy-01 entry: copy the bundled happy image to the output path.

The program is deterministic: it copies entry.png byte-for-byte, so every
run writes exactly the same bytes to /output/entry.png.

The bundled file is JPEG data (told apart by its first bytes, as the
competition rules allow) kept under the name entry.png.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
