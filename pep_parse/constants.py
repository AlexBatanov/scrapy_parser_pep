from pathlib import Path


# PathConstants:
BASE_DIR = Path(__file__).parents[1]
FILE_NAME_STATUS = 'status_summary_'
PATH_NAME_RESULTS = 'results/'
FILE_NAME_PEP = 'pep_%(time)s.csv'

# FormatConstants:
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# PEPConstants:
STATUS_PEP = 'status'

# OutputConstants:
COLUMS_NAME_STATUS_AND_COUNT = 'Статус,Количество'
FIELDS_NAMES = ['number', 'name', 'status']
