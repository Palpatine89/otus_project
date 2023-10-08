# **Проектная работа к курсу "Python QA Engineer" от онлайн-школы OTUS**

## Тема проектной работы - Opencart UI & API autotests 

Для запуска проекта cделать следующее:

1. Склонировать репозиторий на локальную машину
2. Создать виртуальное окружение python3 -m venv venv
3. Активировать виртуальное окружение . venv/bin/activate 
4. Установить необходимые библиотеки pip install -r requirements.txt
5. Актуализировать данные в файле config.json пользователя api (в проекте приложен образец)
6. В панели администратора для пользователя api добавить ip адрес с которого будет выполняться запуск
7. Для запуска UI+API тестов выполнить команду pytest api_tests/ && pytest ui_tests/

Так же тесты можно запустить в docker-контейнере:
1. Склонировать репозиторий на локальную машину
2. Выполнить сборку образа командой sudo docker build -t <image_name> .
3. Для запуска API тестов выполнить команду sudo docker run --rm <image_name> pytest api_tests/ --url=$OPENCART_URL
4. Для запуска UI тестов выполнить команду sudo docker run --rm <image_name> pytest ui_tests/ -n $THREADS --executor=$EXECUTOR_ADDRESS --url=$OPENCART_URL --browser=$BROWSER --bv=$BROWSER_VERSION
