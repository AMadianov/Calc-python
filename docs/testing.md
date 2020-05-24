# Тестирование

## UNIT тесты

Все прогоняемые тесты лежат в каталоге **[test](test)**. При добавлении нового **test case** его необходимо добавить в **test suite** файла **[unit.py](test/unit.py)**

Запуск всех тестов:

`$python unit.py -v`

## BDD тестирование

Основные [инструменты тут](https://wiki.python.org/moin/PythonTestingToolsTaxonomy#Web_Testing_Tools). На старте будем использовать **[selenium](https://pypi.python.org/pypi/selenium)** из фреймворка **[behave](https://pypi.python.org/pypi/behave)**. Дальше будет видно. Все фичи сохраняем в [test/features](test/features), логика тестов в папке [steps](test/features/steps)

Запуск BDD тестов:

`$behave -i first_test.feature`
 