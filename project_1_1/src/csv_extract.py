"""
    Python Real-World Projects
    Project 1.1: Data Acquisition Base Application
"""
import csv
import logging
from abc import ABC, abstractmethod
from pathlib import Path

from model import RawData, XYPair

logger = logging.getLogger(__name__)

class PairBuilder(ABC):
    target_class: type[RawData]

    @abstractmethod
    def from_row(self, row: list[str]) -> RawData:
        ...


class Series1Pair(PairBuilder):
    logger.info('class that get the instances and make it a series1 pair')
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        logger.debug(
            f"from_row() called with a list of type tring which return raw data:{row}")
        try:            
            cls = self.target_class
            # the rest of the implementation...
            logger.debug(f"Series 1 Pair Successfully created : {cls(row[0], row[1])}")
            return cls(row[0], row[1])

        except Exception as e:
            logger.debug(f"Error in from_row():{e}")

class Series2Pair(PairBuilder):
    logger.info('class that get the instances and make it a series2 pair')
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        return cls(row[0], row[2])

class Series3Pair(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        return cls(row[0], row[3])

class Series4Pair(PairBuilder):
    target_class = XYPair

    def from_row(self, row: list[str]) -> RawData:
        cls = self.target_class
        return cls(row[4], row[5])

class Extract:
    def __init__(self, builders: list[PairBuilder]) -> None:
        self.builders = builders

    def build_pairs(self, row: list[str]) -> list[RawData]:
        return [bldr.from_row(row) for bldr in self.builders]

EXTRACT_CLASS: type[Extract] = Extract
BUILDER_CLASSES: list[type[PairBuilder]] = [Series1Pair,]

def test_series1pair() -> None:
    from unittest.mock import Mock, call, sentinel
    mock_raw_class = Mock()
    p1 = Series1Pair()
    p1.target_class = mock_raw_class
    xypair = p1.from_row([sentinel.X, sentinel.Y])
    assert mock_raw_class.mock_calls == [
        call(sentinel.X, sentinel.Y)
    ]
