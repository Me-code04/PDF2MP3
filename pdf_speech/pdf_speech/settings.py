from pathlib import Path

DEBUG = True
ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'pdf_speech.urls'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'