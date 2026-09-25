import csv
from collections import Counter
from datetime import datetime

from pep_parse.constants import DATETIME_FORMAT
from pep_parse.settings import RESULTS_DIR, STATUS_SUMMARY_FILENAME


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = Counter()
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime(DATETIME_FORMAT)
        filename = (
            RESULTS_DIR
            / STATUS_SUMMARY_FILENAME.format(timestamp)
        )

        with open(
            filename,
            mode='w',
            encoding='utf-8',
            newline=''
        ) as file:
            writer = csv.writer(file, dialect=csv.excel)

            rows = [
                ['Статус', 'Количество'],
                *self.statuses.items(),
                ['Total', sum(self.statuses.values())],
            ]

            writer.writerows(rows)
