
Это Rest API, который предназначен для обслуживания будущего мобильного приложения и работы с сайтом  "https://pereval.online/". :)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

<h2>Все конечные точки и методы:</h2>

GET /api/pereval/SubmitData/ возвращает всю информацию о записях(перевалах) в формате json.

GET /api/pereval/SubmitData/<id>/ возвращает всю информацию о записе(перевале) с идентификатором <id> в формате список с json-нами.
  
GET /api/pereval/SubmitData/filter/?user__email=<email> возвращает список с json-нами с информацией об всех объектах, которые отправил пользователь с электронной почтой <email>.
  
POST /api/pereval/SubmitData/ принимает информацию о перевале и пользователе, который его добавил в формате json и сохраняет в таблицы базы данных.
  
PATCH /api/pereval/SubmitData/<id>/ принимает json(такой же как и по методу POST) для редактирования записи с идентификатором <id> в базе данных.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Пример POST запроса по /api/pereval/SubmitData/:

{
  "beauty_title": "п. гора 2",
  "title": "печенкина гора",
  "other_titles": "гора печенюхи",
  "connect": "",
  "add_time": "",

  "email": "coolman@mail.ru",
  "fam": "gg",
  "name": "ggwp",
  "otc": "glhf",
  "phone": "+7 777 77 77",

  "latitude": "95.3842",
  "longitude": "10.1525",
  "height": "3000",

  "level_winter": "",
  "level_summer": "2А",
  "level_autumn": "3А",
  "level_spring": "1B",

  "data": "",
  "title_img": "name"
}

Типы данных и пояснения:

beauty_title - str |
  
title - str        |> (названия объекта.)
  
other_titles - str |
  
connect - char (то что соединяет текстовые поля)
  
add_time - datetime.datetime (автоматическое поле) (время добавления записи)
  
email - str (электронная почта)
  
fam - str (фамилия)
  
name - str (имя)
  
otc - str (отчество)
  
phone - str (номер телефона)
  
level_winter - str (сложность маршрута в зимнее время)
  
level_summer - str (сложность маршрута в летнее время)
  
level_autumn - str (сложность маршрута в осеннее время)
  
level_spring - str (сложность маршрута в весеннее время)
  
data - bytes (байтовая информация картинки)
  
title_img - str (название картинки)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ошибки и ответы API, которые могут возникнуть при работе с API:

1. POST /api/pereval/SubmitData/:
  
Пример: {"status": 400, "message": "Bad Request", "id": "null"}
  
status 200 успех
  
status 400 получен неправильный json (Bad Request)
  
status 500 ошибка на стороне сервера
  
message причина ошибки если была
  
id идентификатор, который был присвоен объекту при добавлении в базу данных

2. PATCH /api/pereval/SubmitData/<id>/
  
Пример: {"state": 0, "message": "Bad Request"}
  
state 1 если запись успешно отредактировалась
  
state 0 запись не удалось успешно отредактировать
  
message хранит причину ошибки если она была иначе 'null'

Остальные ошибки не нуждаются в пояснении т.к. не имеют различные коды ошибок.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Пример GET запроса по /api/pereval/SubmitData/filter/?user__email=<qwertyrrr@mail.ru>

[
    {
        "id": 2,
        "beauty_title": "gggg",
        "title": "vbvvb1",
        "other_titles": "vvvvvvvv",
        "connect": "",
        "add_time": "2022-06-11T11:27:35.773494Z",
        "email": "qwertyrrr@mail.ru",
        "phone": "+7 999 55 55",
        "fam": "qqqqqqq",
        "name": "wwwwww",
        "otc": "ccccccc",
        "latitude": 55.3842,
        "longitude": 8.1525,
        "height": 1210,
        "level_winter": "",
        "level_summer": "2А",
        "level_autumn": "2А",
        "level_spring": "",
        "data": "",
        "title_img": "grgrgrgrg"
    },
    {
        "id": 3,
        "beauty_title": "bbbb",
        "title": "lllll",
        "other_titles": "vvvvvvvv",
        "connect": "",
        "add_time": "2022-06-11T11:58:07.888995Z",
        "email": "qwertyrrr@mail.ru",
        "phone": "+7 999 55 55",
        "fam": "qqqqqqq",
        "name": "wwwwww",
        "otc": "ccccccc",
        "latitude": 55.3842,
        "longitude": 8.1525,
        "height": 2000,
        "level_winter": "",
        "level_summer": "2А",
        "level_autumn": "2А",
        "level_spring": "",
        "data": "",
        "title_img": "rrrrrrrrrr"
    }
]
