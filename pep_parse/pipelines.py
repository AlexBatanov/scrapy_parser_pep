from collections import defaultdict
from datetime import datetime as dt
import os

from .constants import (
    BASE_DIR, DATETIME_FORMAT, FILE_NAME_STATUS,
    PATH_NAME_RESULTS, STATUS_PEP, COLUMS_NAME_STATUS_AND_COUNT
)


class PepParsePipeline:
    def __init__(self):
        os.makedirs(BASE_DIR / PATH_NAME_RESULTS, exist_ok=True)

    def open_spider(self, spider):
        self.counter_pep = defaultdict(int)

    def process_item(self, item, spider):
        """Считает количество статусов"""
        self.counter_pep[item[STATUS_PEP]] += 1
        return item

    def close_spider(self, spider):
        """Записывает статусы и их количество в csv"""
        date = dt.today().strftime(DATETIME_FORMAT)
        file = BASE_DIR / f'{PATH_NAME_RESULTS}{FILE_NAME_STATUS}{date}.csv'

        with open(file, mode='w', encoding='utf-8') as f:
            rows = [COLUMS_NAME_STATUS_AND_COUNT]
            rows.extend([
                f'{status},{count}'
                for status, count in self.counter_pep.items()
            ])
            rows.append(f'Total,{sum(self.counter_pep.values())}\n')
            f.write('\n'.join(rows))
