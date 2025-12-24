<h1 align="center">ПРИМЕР ПРОЕКТА API АВТОТЕСТОВ</h1>

###  Технологический стек

<p align="center">
  <code><img src="images/logo/python.png" width="40" height="40" alt="Python" title="Python"></code
  <code><img src="images/logo/pycharm.png" width="40" height="40" alt="PyCharm" title="PyCharm"></code>
  <code><img src="images/logo/pytest.png" width="40" height="40" alt="Pytest" title="Pytest"></code>
  <code><img src="images/logo/selene.png" width="60" height="60" alt="Selene" title="Selene"></code>
  <code><img src="images/logo/jenkins.png" width="40" height="40" alt="Jenkins" title="Jenkins"></code>
  <code><img src="images/logo/Allure_new.png" width="40" height="40" alt="Allure Report" title="Allure Report"></code>
  <code><img src="images/logo/allure_testops.png" width="40" height="40" alt="Allure TestOps" title="Allure TestOps"></code>
  <code><img src="images/logo/requests.png" width="40" height="40" alt="Requests" title="Requests"></code>
  <code><img src="images/logo/tg.png" width="40" height="40" alt="Telegram" title="Telegram"></code>


## Покрываемый функционал

* ✅ login пользователя
* ✅ logout пользователя
* ✅ Создание пользователя
* ✅ Получение пользователя
* ✅ Обновление пользователя
* ✅ Удалние пользователя

## Запуск тестов
#### Все API тесты запускаются удалённо (Jenkins), но их можно запустить и локально

### Локально

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
   pytest tests/tests_api
   ```
#### Для тестов на API поключены логи 

<img src="images/screenshots/log.png" width="700" alt="API Tests Execution Log">
   
### Запкск с помощью [Jenkins](https://jenkins.autotests.cloud/job/DIPLOM_PROJECT_FEDOSEEV/)
#### Для запуска автотестов необходимо:
 - Открыть [джобу](https://jenkins.autotests.cloud/job/DIPLOM_PROJECT_FEDOSEEV/) в jenkins
 - Нажать на кнопку Build with Parameters
 - В select_run_autotests выбрать tests/tests_api
 - Нажать на Build

<img src="images/screenshots/jenkins_run.png" width="700" alt="Jenkins API Tests Pipeline">

## Отчет о прохождении тестов (Allure)
### Локально
Для получения отчета нужно ввести команду 
```
allure serve allure-results
``` 
Ниже представлен пример allure отчета 
<img src="images/screenshots/allure_results.png" width="700" alt="Allure Report for API Tests">

Подробные инструкции по работе с allure можно найти по [ссылке](https://allurereport.org/docs/).
### Если тесты запускались в Jenkins

Для получения отчета нужно нажать на иконку allure report'a в строке билда  
У него будет точно такой же формат, как и при получении локально
<img src="images/screenshots/allure_jenkins.png" width="700" alt="Allure Report in Jenkins for API Tests">

### В проекте реализована интеграция с [Allure TestsOps](https://allure.autotests.cloud/project/5062/dashboards)
<img src="images/screenshots/testops.png" width="700" alt="Allure TestOps for API Testing">


### В проекте настроена отправка allerts в Telegram
<img src="images/screenshots/tg.png" width="700" alt="Telegram Notification for API Tests">


