# Diplom_2
# Автоматизированное тестирование API «Яндекс Самокат»

## API-тесты для https://stellarburgers.nomoreparties.site/api на requests + pytest с отчётами Allure
Документация: [Документация API](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89)


- Allure: настроен вывод результатов в папку allure_results/ (очищается перед каждым прогоном).
- Makefile: 
make all — запустить все тесты, сгенерировать и открыть отчёт.
make one file=tests/test_xxx.py — прогнать один файл и открыть отчёт


## Проверяем ключевые сценарии:

- Курьер: создание, авторизация, защита от дубликатов, валидация обязательных полей;

- Заказ: создание (варианты color), список заказов, получение по треку, отмена;


## Структура:

- data/
    - urls.py
    - helpers.py (генерация данных)
- tests/
    - test_add_order.py
    - test_git.py
    - test_negativ_create_courier.py
    - test_negativ_login.py
    - test_order_list.py
    - test_positiv_create_courier.py
    - test_positiv_login.py
- requirements.txt - зависимости
- pytest.ini — конфиг pytest/Allure.
- Makefile - 
- conftest.py — фикстуры создания курьера и заказа