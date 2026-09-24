BOT_NAME = "pep_parse"

SPIDERS_MODULE = 'pep_parse.spiders'

SPIDER_MODULES = [SPIDERS_MODULE]
NEWSPIDER_MODULE = SPIDERS_MODULE

ADDONS = {}

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    "results/pep_%(time)s.csv": {
        "format": "csv",
        "fields": ["number", "name", "status"],
        "encoding": "utf-8",
        "overwrite": True,
    },
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
