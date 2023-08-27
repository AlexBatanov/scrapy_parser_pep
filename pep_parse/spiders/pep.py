import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        """
        Парсим ссылки всех PEP

        Возвращает:
        - генератор, который возвращает объекты Response для каждой ссылки PEP
        """
        for link in response.css('td > a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """
        Парсим информацию о PEP 'название, номер, статус'

        Возвращает:
        - генератор, который возвращает объекты PepParseItem с данными о PEP
        """
        status = response.css(
            'dt:contains("Status") + dd > abbr::text'
        ).get().strip()
        number, name = response.css(
            '#pep-content > h1 ::text'
        ).get().split(' – ', 1)

        yield PepParseItem(
            {'status': status, 'name': name, 'number': number}
        )
