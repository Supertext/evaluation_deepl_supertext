import argparse
from pathlib import Path

from analysis.results import ABResult


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze AB test results")
    parser.add_argument("-i", "--input", type=Path, help="Input CSV file")
    parser.add_argument("-o", "--output_dir", type=Path, default="results", help="Output directory")
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    basename = args.input.name.rstrip(".csv")
    args.output_dir.mkdir(exist_ok=True)

    result = ABResult(args.input)
    result.analyze_by_segment(args.output_dir / f"{basename}_by_segment")
    result.analyze_by_document(args.output_dir / f"{basename}_by_document")


if __name__ == "__main__":
    args = parse_args()
    main(args)
