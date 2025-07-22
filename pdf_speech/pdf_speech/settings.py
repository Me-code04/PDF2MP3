from pathlib import Path

DEBUG = True
ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'pdf_speech.urls'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pdf_app',  # your custom app
]
