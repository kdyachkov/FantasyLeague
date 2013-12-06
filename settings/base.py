import os
from mongoengine import *

# Deployment checklist - https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

connect('midwoodfc')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'mongoengine.django.mongo_auth',
    'social_auth',
    'fantasy_league',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'mongoengine.django.auth.MongoEngineBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)
SESSION_ENGINE = 'mongoengine.django.sessions'
MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'
SOCIAL_AUTH_MODELS = 'social_auth.db.mongoengine_models'
#AUTH_USER_MODEL = 'mongo_auth.MongoUser'

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'


GOOGLE_OAUTH2_CLIENT_ID      = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
GOOGLE_OAUTH2_CLIENT_SECRET  = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']

ROOT_URLCONF = 'urls'
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'fantasy_league', 'templates'),)

MEDIA_ROOT, MEDIA_URL = os.path.join(BASE_DIR, 'media'), "/media/"
STATIC_ROOT, STATIC_URL = os.path.join(BASE_DIR, 'static'), "/static/"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

MAX_TEAM_STARTING_VALUE = 50;

