# Проект 'CourseWork5'
 
## Описание:

Проект CourseWork5 - это проект, в котором можно добавлять себе привычки.

## Установка:

1. Клонируйте репозиторий:
```commandline
git clone https://github.com/SergeyBordeychuk/CourseWork5.git
```
2. Установите зависимости:
```commandline
pip install -r requirements.txt
```

## Функционал
1. Запуск сервера
```commandline
python manage.py runserver
```

2. Действие на сервере
```commandline
Просмотр, создание, изменение и удаление привычек, а также полезных привычек.
```

3. Новый функционал
```commandline
Добавлена документация по ссылке /swagger/
```

4. Закрыть сервер
CTRL+C

5. Docker
```commandline
Для запуска можно использовать команду docker-compose up -d --build
```
6. Проверка работоспособности каждого сервиса
```commandline
docker ps
```
```commandline
docker stats
```
```commandline
docker-compose logs
```
7. Для запуска проекта локально, напишите
```commandline
docker-compose up -d --build
```
8.Адрес сервера
```commandline
84.201.150.167
```
10. Настройка сервера
```commandline
git clone https://github.com/SergeyBordeychuk/CourseWork5.git
cd CourseWork5/
docker-compose up -d --build
```