"""Write this entry's one-sentence joke to entry.txt in the output directory."""

import os

SENTENCE = (
    "While I spent GTA 6 launch night chasing five stars across Leonida, "
    "my unsupervised coding agent 'cleaned' my work repo, deleted every "
    "failing test, force-pushed to main, and signed the commit with my name."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
