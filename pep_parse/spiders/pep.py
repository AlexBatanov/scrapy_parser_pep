from itertools import chain

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.constants import SECTIONS, PEP_NUMBER


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """
        Парсим ссылки всех PEP

        Возвращает:
        - генератор, который возвращает объекты Response для каждой ссылки PEP
        """
        sections = [
            section for section in response.css('section')
            if section.attrib['id'] in SECTIONS
        ]
        all_tbody = [section.css('tbody') for section in sections]
        tr_tags = chain.from_iterable(tbody.css('tr') for tbody in all_tbody)
        for tr in tr_tags:
            link = tr.css('a.pep.reference.internal::attr(href)').get()
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
        name = ' '.join(response.css('#pep-content > h1 ::text').getall())
        number = name.split()[PEP_NUMBER]

        data = {
            'status': status,
            'name': name,
            'number': number
        }
        yield PepParseItem(data)
