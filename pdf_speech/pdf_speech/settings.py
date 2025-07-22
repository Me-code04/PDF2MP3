from pathlib import Path

DEBUG = True
ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'