call cd /D "%~dp0"
call python manage.py makemigrations
call python manage.py migrate
python manage.py runserver