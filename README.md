# Jumanji_website
Сайт для поиска и публикации вакансий.

# Порядок запуска
1. Устанавливаем зависимости из `requirements.txt`
2. Делаем миграции с помощью команд:  
   `python manage.py makemigrations`  
   `python manage.py migrate`
3. Запускаем сервер в терминале командой `python manage.py runserver`
4. Открываем `http://127.0.0.1:8000/` в браузере

## SUPERUSER для доступа в личный кабинет
#### login: adminadmin
#### pass: admin  

# Описание 

Данный сайт написал с помощью фреймворка `Django`. Основная тематика сайта - поиск и публикация вакансий.  
  
![Главная страница](https://github.com/Minigamy/Jumanji_website/blob/master/img/website1.PNG)  
<p align="center">Рисунок 1. Главное меню</p>  

![Поиск вакансий](https://github.com/Minigamy/Jumanji_website/blob/master/img/website2.PNG)  
<p align="center">Рисунок 2. Поиск вакансий</p>  

![Резюме](https://github.com/Minigamy/Jumanji_website/blob/master/img/website3.PNG)  
<p align="center">Рисунок 3. Резюме в личном кабинете</p>  

![Информация о компании](https://github.com/Minigamy/Jumanji_website/blob/master/img/website_compinfo.PNG)  
<p align="center">Рисунок 4. Информация о компании в личном кабинете</p>  

![Вакансии](https://github.com/Minigamy/Jumanji_website/blob/master/img/website_vacancy.PNG)
<p align="center">Рисунок 5. Вакансии моей компании в личном кабинете</p>  


![Отклики](https://github.com/Minigamy/Jumanji_website/blob/master/img/website_responses.PNG)
<p align="center">Рисунок 6. Отклики на вакансии моей компании</p>

