import csv
from collections import Counter
from datetime import datetime

from pep_parse.settings import (
    DATETIME_FORMAT,
    RESULTS_DIR,
    STATUS_SUMMARY_FILENAME,
)


class PepParsePipeline:
    def __init__(self):
        self.statuses = Counter()
        RESULTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item
