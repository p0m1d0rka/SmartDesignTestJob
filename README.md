Задание:
Микросервис для электронного магазина
Модель/cущности:
Товар - отвечает за товар на складе, например - телефон такой-то марки от такого-то производителя.
Поля:
идентификатор (ID)
название
описание
параметры: массив пар ключ/значение

Сущности хранятся в MongoDB на localhost:27017 (можно запускать командой docker run -d -p 27017:27017 mongo)

REST API методы:
Создать новый товар
Получить список названий товаров, с возможностью фильтрации по:
a) названию
b) выбранному параметру и его значению
Получить детали товара по ID
Методы принимают JSON на входе и отдают JSON на выходе.

Для разработки использовать следующие библиотеки:
uMongo в асинхронной моде в связке с Motor в кач-ве ORM
aiohttp в кач-ве HTTP сервера и REST фреймворка

В README.md указать:
* Необходимые шаги для инсталляции (напр. pip install -r requirements.txt)
* Команду для запуска сервиса (т.е. python + что-то)
* curl команды с нужными параметрами для прохождения тестового сценария:
* создать товар
* найти его по параметру
* получить детали найденного товара

### Запуск
`docker run -d -p 27017:27017 mongo`
`pip install -r requirements.txt`  
`python -m app`

### curl для прохождения тестового сценария
 - создание продукта:  
 `curl -XPOST -H "Content-type: application/json" -d '{"title": "iphone11", "description": "Одиннадцатый iphone", "params": {"memory": 6, "cpu": 8}}' 'localhost:8080/api/v1/product'`
 `curl -XPOST -H "Content-type: application/json" -d '{"title": "iphone10", "description": "Десятый iphone", "params": {"memory": 3, "cpu": 4}}' 'localhost:8080/api/v1/product'`
 `curl -XPOST -H "Content-type: application/json" -d '{"title": "iphone11", "description": "Одиннадцатый iphone", "params": {"memory": 3, "cpu": 6}}' 'localhost:8080/api/v1/product'`
 возвращает JSON с созданным объектом
 
 - поиск по id:
 `curl -XGET 'localhost:8080/api/v1/product/5e89e551c73e9cccba42ecdd'`
 вместо `5e89e551c73e9cccba42ecdd` - поставить свой id, полученный в п.1
 Возвращает JSON объект продукта. Пустой объект если id не найден.
 
 - Поиск с фильтрацией:
 `curl -XGET -d '{"filter": {"title": "iphone11"}, "sort_by": ["params.cpu",1]}' 'localhost:8080/api/v1/products'`
 параметры фильтрации указываются в объекте фильтра, если не указаны - возвращаются все продукты.
 параметры сортировки указываются в массиве sort_by, если не указаны применяется сортировка по полю `title`