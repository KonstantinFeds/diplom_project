# Пример проекта мобильных автотестов для приложения WIKIPEDIA


###  Используемые технологии
<p align="center">
  <code><img src="images/logo/python.png" width="40" height="40" alt="Python" title="Python"></code
  <code><img src="images/logo/pycharm.png" width="40" height="40" alt="PyCharm" title="PyCharm"></code>
  <code><img src="images/logo/pytest.png" width="40" height="40" alt="Pytest" title="Pytest"></code>
  <code><img src="images/logo/selene.png" width="60" height="60" alt="Selene" title="Selene"></code>
  <code><img src="images/logo/jenkins.png" width="40" height="40" alt="Jenkins" title="Jenkins"></code>
  <code><img src="images/logo/Allure_new.png" width="40" height="40" alt="Allure Report" title="Allure Report"></code>
  <code><img src="images/logo/allure_testops.png" width="40" height="40" alt="Allure TestOps" title="Allure TestOps"></code>
  <<code><img src="images/logo/android_studio.png" width="40" height="40" alt="Android Studio" title="Android Studio"></code
  <code><img src="images/logo/appium.png" width="40" height="40" alt="Appium" title="Appium"></code>
  <code><img src="images/logo/tg.png" width="40" height="40" alt="Telegram" title="Telegram"></code>

## Покрываемый функционал
  
* ✅ Валидация полей логина и пароля
* ✅ Поиск статьи по названию
* ✅ Добалвение настроек языка

## Запуск тестов
#### Mobile тесты можно запустить локально на эмуляторе или на [BrowserStack](https://www.browserstack.com)

### Локально на эмуляторе
#### Настройка
1. Установить Node.js и npm
2. Установить Appium
3. Установить драйвера UiAutomator2 для Appium
4. Установить Android Studio
5. Настроить Android Studio и установка SDK
6. Создать виртуальное устройство в Android Studio. В проекте используется Google Pixel 9
8. Установка Java Development Kit (JDK)
9. Установка Appium Inspector

#### Запуск тестов

1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Запустить сервер Appium
    ```bash
   appium
   ```
4. Запустить Android Studio и настроить сессию с эмулятором Google Pixel 9
5. Ввести в терминале следующие команды
   
   5.1 установка зависимостей
   ```bash
   poetry install
   ```
      5.2 запуск тестов 
   ```bash
   pytest tests/tests_mobile --mobile-context=local_emulator
   ```

### Удаленно через [BrowserStack](https://app-automate.browserstack.com/)

Важно! Перед запуском, в корне проекта, нужно создать файл .env.сredentials и указать там 
* USER_NAME_BSTACK
* ACCESS_KEY_BSTACK

#### Запуск тестов

1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в терминале следующие команды
   
   3.1 установка зависимостей
   ```bash
   poetry install
   ```
      5.2 запуск тестов 
   ```bash
   pytest tests/tests_mobile --mobile-context=bstack 
   ```



   
### С помощью [Jenkins](https://jenkins.autotests.cloud/job/DIPLOM_PROJECT_FEDOSEEV/)
#### Для запуска автотестов необходимо:
 - Открыть [джобу](https://jenkins.autotests.cloud/job/DIPLOM_PROJECT_FEDOSEEV/) в jenkins
 - Нажать на кнопку Build with Parameters
 - указать credentials в параметрах selenoid_login, selenoid_password, selenoid_url
 - В select_run_autotests выбрать tests/tests_web
 - Нажать на Build

 <img src="images/screenshots/job_jenkins.png" width="700" alt="Jenkins Job">
 
### через selenoid
Важно! Перед запуском, в корне проекта, нужно создать файл .env.сredentials и указать там 
* SELENOID_LOGIN
* SELENOID_PASSWORD
* SELENOID_URL

Для запуска тестов через selenoid нужно выполнить следующие шаги:
1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в терминале следующие команды
   
   3.1 установка зависимостей
   ```bash
   poetry install
   ```
   
   3.2 запуск тестов 
   ```bash
   pytest tests/tests_web/ --web-context=selenoid
   ```

### локально

Для локального запуска тестов нужно выполнить следующие шаги:
1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в терминале следующие команды
   
   3.1 установка зависимостей
   ```bash
   poetry install
   ```
   
   3.2 запуск тестов 
   ```bash
   pytest tests/tests_web/ --web-context=local_browser
   ```

## Отчет о прохождении тестов (Allure)
### Локально
Для получения отчета нужно ввести команду 
```
allure serve allure-results
 ```
Ниже представлен пример allure отчета 
<img src="images/screenshots/allure_results_web.png" width="800" alt="Allure Report Results">

Подробные инструкции по работе с allure можно найти по [ссылке](https://allurereport.org/docs/).
### Если тесты запускались в Jenkins

Для получения отчета нужно нажать на иконку allure report в строке билда. 
У него будет точно такой же формат, как и при получении локально.

<img src="images/screenshots/allure_results_web_jenkins.png" width="700" alt="Allure Results in Jenkins">

### В проекте реализована интеграция с [Allure TestsOps](https://allure.autotests.cloud/project/5062/dashboards)
<img src="images/screenshots/allure_testops.png" width="800" alt="Allure TestOps Dashboard">








