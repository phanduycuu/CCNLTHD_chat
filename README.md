1. Create and InSert Database Mysql
create database name:  chat_message
insert data
2. Setup and Run

Step 1:
py -m venv venv

Step 2:
source venv/Scripts/activate

Step 3:
pip install -r requirements.txt

Step 4:
python manage.py migrate

Step 5:
python -m daphne -b 127.0.0.1 -p 8000 chat.asgi:application


