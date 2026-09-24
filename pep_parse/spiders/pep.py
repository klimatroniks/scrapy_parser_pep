import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = list(map('https://{}/'.format, allowed_domains))

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
        title = response.xpath('string((//h1)[2])').get().strip()

        num, name = title.split(' – ')
        num = num.split()[1]

        status = response.xpath(
            '//dt[text()="Status"]/following-sibling::dd[1]//text()'
        ).get()

        yield PepParseItem(
            number=num,
            name=name,
            status=status
        )
