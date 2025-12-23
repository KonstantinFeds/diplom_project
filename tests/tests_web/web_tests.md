# Пример проекта автотестов для компании 
[URAL SOUND](https://ural-auto.ru/)
> Компания, которая существует с 1900 года и несёт в себе память пяти поколений Русских Инженеров.

<img width="1106" height="571" alt="image" src="https://github.com/user-attachments/assets/cb852198-228d-4fde-abd2-4d8d3c4b3c99" />

###  Используемые технологии
<p align="center">
  <code><img src="images/logo/python.png" width="40" height="40" alt="Python" title="Python"></code
  <code><img src="images/logo/pycharm.png" width="40" height="40" alt="PyCharm" title="PyCharm"></code>
  <code><img src="images/logo/pytest.png" width="40" height="40" alt="Pytest" title="Pytest"></code>
  <code><img src="images/logo/selenium.png" width="40" height="40" alt="Selenium" title="Selenium"></code>
  <code><img src="images/logo/selene.png" width="60" height="60" alt="Selene" title="Selene"></code>
  <code><img src="images/logo/selenoid.png" width="90" height="90" alt="Selenoid" title="Selenoid"></code>
  <code><img src="images/logo/jenkins.png" width="40" height="40" alt="Jenkins" title="Jenkins"></code>
  <code><img src="images/logo/Allure_new.png" width="40" height="40" alt="Allure Report" title="Allure Report"></code>
  <code><img src="images/logo/allure_testops.png" width="40" height="40" alt="Allure TestOps" title="Allure TestOps"></code>
  <code><img src="images/logo/tg.png" width="40" height="40" alt="Telegram" title="Telegram"></code>

## Покрываемый функционал
  
* ✅ Добавление товара в корзину
* ✅ Очистка корзины
* ✅ Наличие товаров в каталоге
* ✅ Работа фильтров в каталоге
* ✅ Локализация сайта
* ✅ Валидация полей логина и пароля
* ✅ Поиск товара по названию

## Запуск тестов
#### Все UI тесты запускаются удалённо (Jenkins), но их можно запустить и локально

### Локально
Важно! Перед запуском, в корне проекта, нужно создать файл .env.сredentials и указать там 
* SELENOID_LOGIN
* SELENOID_PASSWORD
* SELENOID_URL

Для запуска тестов локально нужно выполнить следующие шаги
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
   
### С помощью [Jenkins](https://jenkins.autotests.cloud/job/DIPLOM_PROJECT_FEDOSEEV/)
#### Для запуска автотестов необходимо:
 - Открыть [джобу](https://jenkins.autotests.cloud/job/DIPLOM_PROJECT_FEDOSEEV/) в jenkins
 - Нажать на кнопку Build with Parameters
 - указать credentials в параметрах selenoid_login, selenoid_password, selenoid_url
 - В select_run_autotests выбрать tests/tests_web
 - Нажать на Build

 <img src="images/screenshots/job_jenkins.png" width="700" alt="Jenkins Job">


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







