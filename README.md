# django_bmi

Склонировать репозиторий git clone https://github.com/lipa88/django_bmi.git . Создать virtualenv с Python 3.6 и установить библиотеки: pip install django djangorestframework numpy .
Накатить миграции python manage.py migrate и запустить локально python manage.py runserver .

http://127.0.0.1:8000/bmicalc/ - расчет BMI и создание нового обьекта Bmi в БД
http://127.0.0.1:8000/bmistat/ - расчет статистик по данным из БД

