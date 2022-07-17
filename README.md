# card_service

Створити та зайти в віртуальне оточення і встановити залежності
pip install -r requirements.txt

Створити міграції
python manage.py migrate

Завантажити fixtures 
python3 manage.py loaddata subjects.json

Запустити сервер
python manage.py runserver

Стартова сторінка
http://localhost:8000/list-card/
