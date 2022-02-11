release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT MoneyProj.asgi:application