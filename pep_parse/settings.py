from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_FOLDER = 'results'
RESULTS_DIR = BASE_DIR / RESULTS_FOLDER

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

STATUS_SUMMARY_FILENAME = 'status_summary_{}.csv'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ADDONS = {}

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

FEED_EXPORT_ENCODING = 'utf-8'

FEEDS = {
    f'{RESULTS_FOLDER}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'encoding': 'utf-8',
        'overwrite': True,
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
