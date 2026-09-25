import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

from pep_parse.constants import (
    CSV_DIALECT,
    DATETIME_FORMAT,
    FEEDS_SETTING,
    STATUS_SUMMARY_FILENAME,
)


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = Counter()

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        feeds = spider.crawler.settings.getdict(FEEDS_SETTING)
        results_dir = Path(next(iter(feeds))).parent

        timestamp = datetime.now().strftime(DATETIME_FORMAT)
        filename = results_dir / STATUS_SUMMARY_FILENAME.format(timestamp)

        total = sum(self.statuses.values())

        with open(
            filename,
            mode='w',
            encoding='utf-8',
            newline=''
        ) as file:
            writer = csv.writer(file, dialect=CSV_DIALECT)

            rows = [
                ['Статус', 'Количество'],
                *self.statuses.items(),
                ['Total', total],
            ]

            writer.writerows(rows)
