python -m daphne -b 127.0.0.1 -p 8000 chat.asgi:application
python manage.py makemigrations
python manage.py migrate
