import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MoneyProj.settings')
django.setup()

from tbot.dispatcher import run_pooling

if __name__ == "__main__":
    run_pooling()