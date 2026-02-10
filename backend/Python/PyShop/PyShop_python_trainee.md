## Задание 1. Разработать функцию определения счета в игре

### Задача

В примере кода ниже генерируется список фиксаций состояния счета игры в течение матча.
Разработайте функцию get_score(game_stamps, offset), которая вернет счет на момент offset в списке game_stamps.
Нужно суметь понять суть написанного кода, заметить нюансы, разработать функцию вписывающуюся стилем в существующий код, желательно адекватной алгоритмической сложности.

```Python
from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
    Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
    Please pay attention to that for some offsets the game_stamps list may not contain     scores.
    '''
    # return home, away
```

### Результат

1. Ссылка на [gist](https://gist.github.com/) с исходным кодом функции.

## Задание 2. Разработать тесты для функции определения счета в игре

### Задача

Для разработанной в предыдущем задании функции get_score(game_stamps, offset) разработайте unit-тесты на фреймворке [unittest](https://docs.python.org/3/library/unittest.html).  
Тесты должны учитывать все возможные случаи использования функции, концентрироваться на проверке одного случая, не повторяться, название тестов должно отражать суть выполняемой проверки.

### Результат

1. Ссылка на [gist](https://gist.github.com/) с исходным кодом тестов.

## Задание 3. Разработать парсер смартфонов

### Задача

Разработать парсер, который будет собирать информацию о версиях операционных систем в топ-100 смартфонах с самым высоким рейтингом пользователей в каталоге [ozon.ru](http://ozon.ru/).

На сайте [ozon.ru](http://ozon.ru/) в категории “Электроника -> Телефоны и смарт-часы” с сортировкой “Высокий рейтинг” нужно собрать информацию о первых 100 смартфонах попавших в выборку. Перейти на страницу с каждым из них и забрать информацию о версии операционной системы из характеристик. По собранным данным построить распределение моделей по версиям операционных систем в порядке убывания, например:

```txt
Android 8 — 12
Android 10 — 9
iOS 14 — 8
…
```

Для парсинга следует использовать язык программирования Python, фреймворк Scrapy, для скачивания динамических частей сайта следует использовать Scrapy+Selenium. В выполнении задания может помочь scrapy proxy rotation middleware.

Для расчета распределения следует использовать фреймворк Pandas.

### Результат

1. Ссылка на [gist](https://gist.github.com/) с распределение моделей устройств по версиям операционных систем в plain-text формате.
2. Ссылка на [github-репозиторий](https://github.com/) с публичным доступом с исходными кодами решения.
