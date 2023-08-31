# Автоматизация тестирования с помощью Selenium и Python
Финальный проект из курса для тестировщиков c онлайн платформы Stepik, который учит писать автоматизированные UI-тесты на языке программирования Python с помощью библиотеки Selenium WebDriver. 

Написаны UI автотесты на сайт: http://selenium1py.pythonanywhere.com.

Актуален с Chromedriver, Chrome версии 116.0.5845.96 

Контакты для связи: killzone15@yandex.ru
# Содержание проекта
Папка <code>pages</code> содержит файлы c расширением .py с описанием веб-страниц согласно паттерну **Page Object**:
* **base_page.py** — содержит класс **BasePage**, который содержит унивирсальные методы для всех страниц.
* **basket_page.py** — содержит класс **BasketPage** *(потомок от класса BasePage)*, в котором описаны методы проверки отсутствия товара в корзине.
* **locators.py** — содержит локаторы тестируемых веб-страниц.
* **login_page.py** — содержит класс **LoginPage** *(потомок от класса BasePage)*, который содержит методы проверки страницы «Войти или зарегистрироваться». Так же содержит функцию регистрации новых пользователей <code>register_new_user</code>
* **main_page.py** — содержит класс **MainPage** *(потомок от класса BasePage)*, содержи заглушку.
  > метод __init__ вызывается при создании объекта. Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage.
* **product_page.py** — содержит класс **ProductPage** *(потомок от класса BasePage)*, содержит метод добавление товара в корзину и методы проверки страницы с товаром.
## Конфигурация тестов
 * **Conftest.py** — конфигурация тестов.

   *language* - для запуска сайта на различных языках интерфейса.

   *browser* - создает экзампляр браузера, для тестирования.
 * **__init__.py** — это специальный файл, который используется в Python для обозначения каталога как пакета (package).
 * **pytest.ini** — содержит зарегистрированые метки для маркировки тестов.
   
## Тесты

### test_main_page.py 
* **test_guest_can_go_to_login_page** — гость может перейти на страницу «Войти или зарегистрироваться» с главной страницы.

* **test_guest_cant_see_product_in_basket_opened_from_main_page** — гость не может увидеть товар в корзине перейдя в корзину с главной страницы.
### test_product_page.py

* **test_guest_can_add_product_to_basket** — гость может добавить товар в корзину.

    Тест с параметризацией, проверят работоспособность страницы товара с промо-акцией. Промо-акция включается путем добавления параметра <code>?promo=offerN</code> к ссылке на товар от offer0 до offer9.

    Пример ссылки:
    ```
    http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0
    ```
    Параметризация теста:
    ```
    @pytest.mark.parametrize('link_num', [0, 1, 2, 3, 4, 5, 6,
                                    pytest.param(7, marks=pytest.mark.skip(reason="Название товара не соответствует "
                                                                                  "наименованию товара в сообщении "
                                                                                  "об успешном добавлении товара в "
                                                                                  "корзину")),
                                    8, 9])
    ```
    Баг был обнажурен на странице с промо-акцией, при параметре <code>?promo=offer7</code>, помечен маркером **xfail**.

* **test_guest_can_go_to_login_page_from_product_page** — гость может перейти на страницу «Войти или зарегистрироваться» со страницы товара.
* **test_guest_cant_see_success_message** — гость не может увидеть сообщениее об успешном добавлении товара в корзину на странице товара.
* **test_guest_should_see_login_link_on_product_page** — гость должен увидеть ссылку на страницу «Войти или зарегистрироваться» со страницы товара.
* **test_guest_can_go_to_login_page_from_product_page** — гость может перейти на страницу «Войти или зарегистрироваться» со страницы товара.
* **test_guest_cant_see_product_in_basket_opened_from_product_page** — гость не должен увидеть товар в корзине, перейдя на страницу «Корзина» со страницы товара.
* **setup** — фукстура, которая регистрирует новых пользователей. Проверят, то что пользователь вошел на сайт.
* **test_user_cant_see_success_message** — пользователь не может увидеть сообщениее об успешном добавлении товара в корзину на странице товара.
* **test_user_can_add_product_to_basket** — пользователь может добавить товар в корзину.
   
# Requirements
Устанавливать из requirements.txt:
```
pytest==7.4.0
selenium==4.10.0
chromedriver-py==116.0.5845.96
```

# Запуск
## Запуск через терминал:
1. Клонировать и открыть проект.
```
git clone https://github.com/Killzone15/auto_tests_with_selenium.git
```
```
cd auto_tests_with_selenium
```
2. Создать и войти в виртуальное окружение.
```
pipenv --python 3.10.4
```
```
pipenv shell
```
3. Установить модули из requirements.txt.
```
pip install -r requirements.txt
```
4. Для проверки финального задания с peer-review запустите тесты с меткой need_review. (для курса Автоматизация тестирования с помощью Selenium и Python. <sub>Stepik</sub>)
```
pytest -v --tb=line --language=en -m need_review
```
5. Для запуска тестов на различных языках интерфейса, используйте параметр --language

Пример:
```
pytest --language=ru test_product_page.py
```
Таблица с перечислением и описанием возможных аргументов для параметра --language
| Аргумент  | Язык интерфейса |
| ------------- | ------------- | 
| ar  | العربيّة  |
| ca  | català  |
|  cs   |    česky     |
|  da   |    dansk     |
|  de   |    Deutsch     |
|  en-gb   |    British English     |
|  el   |    Ελληνικά     |
| es | español |
| fi | suomi |
| fr | français |
| it | italiano |
| ko | 한국어 |
| nl | Nederlands |
| pl | polski |
| pt | Português |
| pt-br | Português Brasileiro |
| ro | Română |
| ru | Русский |
| sk | Slovensky |
| uk | Українська |
| zh-hans | 简体中文 |

## Запуск через PyCharm
1. Клонировать и открыть проект.
2. Создать виртуальное окружение.
3. Установить модули из requirements.txt.
4. Убедиться, что pytest выбран как Default test runner в Settings > Tools > Python Integrated Tools.
5. Запустить тесты через любую конфигурацию pytest.
