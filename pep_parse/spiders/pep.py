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
        title = response.css('h1::text').getall()[1]

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

