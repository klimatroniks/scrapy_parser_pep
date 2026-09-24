import csv
from collections import Counter
from datetime import datetime
from pathlib import Path


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = Counter()

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        feeds = spider.crawler.settings.getdict('FEEDS')
        results_dir = Path(next(iter(feeds))).parent

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = results_dir / (
            f'status_summary_{timestamp}.csv'
        )

        with open(
            filename,
            mode='w',
            encoding='utf-8',
            newline=''
        ) as file:
            writer = csv.writer(file, dialect='excel')

            rows = [
                ['Статус', 'Количество'],
                *self.statuses.items(),
                ['Всего', sum(self.statuses.values())]],

            writer.writerows(rows)
