release: python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn web_chat.wsgi --log-file -
