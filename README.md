# scrapy_parser_pep
Данный проект использует фреймворк Scrapy для парсинга информации о PEP (Python Enhancement Proposals) с официального сайта Python. Он извлекает данные, такие как название, статус и номер PEP, и сохраняет их в формате CSV. Также проект подсчитывает количество PEP с каждым статусом и записывает эту информацию в отдельный файл.

## Установка и использование

1. Склонируйте репозиторий на свой компьютер:
    ```
   git clone git@github.com:AlexBatanov/scrapy_parser_pep.git
    ``` 

2. Установите необходимые зависимости:
   ```
   pip install -r requirements.txt
   ```
   

3. Запуск парсера:
   ```
   scrapy crawl pep
   ```

После выполнения парсинга в папке results будут два файла с результатом.
   
### Автор
[Batanov Alexandr](https://github.com/AlexBatanov)
