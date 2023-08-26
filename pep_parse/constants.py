from pathlib import Path


# PathConstants:
BASE_DIR = Path(__file__).parent
FILE_NAME_STATUS = 'status_summary_'
PATH_NAME_RESULTS = 'results/'
FILE_NAME_PEP = 'pep_%(time)s.csv'

# FormatConstants:
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# PEPConstants:
SECTIONS = [
    'index-by-category',
    'numerical-index',
    'reserved-pep-numbers'
]
STATUS_PEP = 'status'
PEP_NUMBER = 1

# OutputConstants:
COLUMS_NAME_STATUS_AND_COUNT = 'Статус,Количество\n'
FIELDS_NAMES = ['number', 'name', 'status']
