import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(description="Copy and sort files.")
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Source directory path."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("dist"),
        help="Output directory path.",
    )
    return parser.parse_args()


def recursive_copy_and_sort(source: Path, output: Path):
    try:
        for el in source.iterdir():
            if el.is_dir():
                recursive_copy_and_sort(el, output)
            else:
                extension = el.suffix[1:]
                sub_dir = output / extension
                sub_dir.mkdir(exist_ok=True, parents=True)
                shutil.copy(el, sub_dir)
                print(f"File '{el.name}' copied to '{sub_dir}'")
    except Exception as e:
        print(f"Error: {e}")


def main():
    args = parse_argv()
    recursive_copy_and_sort(args.source, args.output)


if __name__ == "__main__":
    main()
