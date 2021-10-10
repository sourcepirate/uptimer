from os import getcwd
from os.path import join
from typing import Any, List, Dict
from collections import defaultdict
from bisect import insort_right
from json import dumps


def indexing_range(index_list: List[Any], start: int, end: int, key=lambda x: x):
    """return the slices between the given range

    Assuming the index_list is sorted this function  is going to return a slice of (start, end)
    pointers

    points between (start, end) where lo >= start and high <= end
    """
    lo, hi = 0, len(index_list) - 1
    while not key(index_list[lo]) >= start:
        lo += 1

    while not key(index_list[hi]) <= end:
        hi -= 1

    return index_list[lo:hi]


class InmemoryDB(object):
    def __init__(self):
        self.domain_latency = defaultdict(list)
        self.domain_health = defaultdict(list)
        self.outfd = open(join(getcwd(), "data.json"), "w")

    def put(self, domain: str, timestamp: int, response_dict: Dict[Any, Any]):
        insort_right(
            self.domain_latency[domain],
            (timestamp, response_dict["latency"]),
        )
        insort_right(
            self.domain_health[domain],
            (timestamp, int(response_dict["healthy"])),
        )

    def points(
        self, domain: str, start_timestamp: int, end_timestamp: int
    ) -> List[Any]:
        return indexing_range(
            self.domain_latency[domain],
            start_timestamp,
            end_timestamp,
            key=lambda x: x[0],
        )

    def flush(self):
        """flush the data regularly"""
        data = {"health": self.domain_health, "latency": self.domain_latency}
        self.outfd.write(dumps(data))
        self.outfd.seek(0)
        self.outfd.flush()
        
        
