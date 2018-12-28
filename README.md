# django_bmi

Склонировать репозиторий git clone https://github.com/lipa88/django_bmi.git . Создать virtualenv с Python 3.6 и установить библиотеки: pip install django djangorestframework numpy .
Накатить миграции python manage.py migrate и запустить локально python manage.py runserver .

http://127.0.0.1:8000/bmicalc/ 
- Посчитать ИМТ/BMI - Индекс массы тела.
   - Метод принимает рост в сантиметрах и массу в килограммах.
   - В ответ отдает значение ИМТ с точностью до второго знака.

http://127.0.0.1:8000/bmistat/ 
- Посчитать average/min/max/среднеквадратическое отклонение по посчитанным ранее ИМТ.
   - Метод принимает пустое тело
   - В ответ отдает JSON с посчитанными параметрами

