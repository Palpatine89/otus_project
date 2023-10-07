Проектная работа к курсу "Python QA Engineer" от онлайн-школы OTUS

Тема проектной работы - Тестирование онлайн-магазина Opencart

Для запуска проекта cделать следующее:

1. Склонировать репозиторий на локальную машину
2. Создать виртуальное окружение python3 -m venv venv
3. Активировать виртуальное окружение . venv/bin/activate 
4. Установить необходимые библиотеки pip install -r requirements.txt
5. Актуализировать данные в файле config.json пользователя api (в проекте приложен образец)
6.a Для запуска UI тестов выполнить команду pytest ui_tests/
6.b Для запуска API тестов выполнить команду pytest api_tests/
6.c Для запуска UI+API тестов выполнить команду pytest api_tests/ & pytest ui_tests/
python3 -m venv venv
