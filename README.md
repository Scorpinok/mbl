# Python-Flask-Docker

## Данные Сбербанка по недвижимости:
https://www.kaggle.com/c/sberbank-russian-housing-market/data

## Реализация модель:
+ Course_work.ipynb

## Стек: 
+ requirements.txt

## Порядок действий:
+ Для запуска приложения нужно установить **docker** и **git**

+ По средствам командной строки клонируем репозиторий и создаем образ:
> git clone https://github.com/Scorpinok/mbl.git 
> cd .\mbl\ 
> docker build -t my_flask_app:latest my_flask_app/

+ Запускаем контейнер:
> docker run -d -p 5000:5000 -v "<путь к директории проекта (там же где лежит 'test.csv')>:/app" my_flask_app:latest
может выглядеть так: > docker run -d -p 5000:5000 -v "C:/folder1/mbl/:/app" my_flask_app:latest

+ В браузере переходим на **localhost:5000**

Приложение требует загрузки файла **"test.csv"**
По результатам сохраняется файл **"_predictions.csv"**,
который будет находится в рабочей директории проекта
