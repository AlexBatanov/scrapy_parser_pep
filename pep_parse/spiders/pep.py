from itertools import chain
import scrapy

from pep_parse.items import PepParseItem

SECTIONS = [
    'index-by-category',
    'numerical-index',
    'reserved-pep-numbers'
]

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        sections = [
            section for section in response.css('section')
            if section.attrib['id'] in SECTIONS
        ]
        all_tbody = [section.css('tbody') for section in sections]
        tr_tags = chain.from_iterable(tbody.css('tr') for tbody in all_tbody)
        links = []
        for tr in tr_tags:
            link = tr.css('a.pep.reference.internal::attr(href)').get()
            yield response.follow(link, callback=self.pep_parse)
    
    def pep_parse(self, response):
        status = response.css('dt:contains("Status") + dd > abbr::text').get().strip()
        name = response.css('#pep-content > h1::text').get().strip()
        number = name.split()[1]
        yield {
            'status': status,
            'name': name,
            'nummber': number
        }
