from .constants import PATH_NAME_RESULTS, FILE_NAME_PEP, FIELDS_NAMES


BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True

FEEDS = {
    f'{PATH_NAME_RESULTS}{FILE_NAME_PEP}': {
        'format': 'csv',
        'fields': FIELDS_NAMES,
        'overwrite': True
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
