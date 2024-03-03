from basicsite.settings.base import *
import os
import django_heroku
import environ
import dj_database_url
# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ADMINS = [
    ('CalConT', 'calcont.in01@gmail.com'),
]

EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['.calcont.in', 'calcont.in', '.herokuapp.com']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
PREPEND_WWW = True

SECURE_HSTS_SECONDS = 60

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
django_heroku.settings(locals())


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
