from pep_parse.items import PepParseItem
import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.css(
            'table.pep-zero-table tbody tr td:nth-child(2) a::attr(href)'
        )

        for link in links:
            yield response.follow(
                link,
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        title = response.css('').get()
        status = response.css('').get()

        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
