"""
    Python Real-World Projects
    Project 1.1: Data Acquisition Base Application
"""
import argparse
import json
import logging
import sys
from dataclasses import asdict
from pathlib import Path

from csv_extract import *


def setup_global_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler("app.log", mode="a")],
    )


def get_options(argv: list[str]) -> argparse.Namespace:
    defaults = argparse.Namespace(
        extract_class=Extract,
        series_classes=[Series1Pair, Series2Pair, Series3Pair, Series4Pair],
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=Path, default="data")
    parser.add_argument('source', type=Path, nargs='*')
    return parser.parse_args(argv, defaults)


EXTRACT_CLASS: type[Extract] = Extract
BUILDER_CLASSES: list[type[PairBuilder]] = [Series1Pair, Series2Pair, Series3Pair, Series4Pair]

def main(argv: list[str] = sys.argv[1:]) -> None:
    builders = [builder_cls() for builder_cls in BUILDER_CLASSES]
    extractor = EXTRACT_CLASS(builders)
    # etc.

    options = get_options(argv)

    targets = [
        options.output / "Series_1.ndjson",
        options.output / "Series_2.ndjson",
        options.output / "Series_3.ndjson",
        options.output / "Series_4.ndjson",
    ]
    print('targets', targets)
    target_files = [
        target.open('w') for target in targets
    ]
    print('target_files', target_files)
    for source in options.source:
        with source.open() as source:
            rdr = csv.reader(source)
            for row in rdr:
                for row, wtr in zip(extractor.build_pairs(row), target_files):
                    wtr.write(json.dumps(asdict(row)) + '\n')
    for target in target_files:
        target.close()

if __name__ == "__main__":
    setup_global_logging()
    logger = logging.getLogger(__name__)
    logger.info("Acquire data started")
    main()
    logger.info("Acquire data finished")

