from pathlib import Path

DEBUG = True
ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'urls.py'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'