import os

# Deployment checklist - https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

JOIN_BASE_DIR = lambda path: os.path.join(BASE_DIR, path)

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

WSGI_APPLICATION = 'wsgi.application'

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': JOIN_BASE_DIR('fantasyLeague.db')
#    }
#}

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'fantasy_league',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'social.apps.django_app.default',
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
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTH_USER_MODEL = 'fantasy_league.User'

SOCIAL_AUTH_LOGIN_URL          = '/login/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL    = '/login-error/'
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY      = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET  = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']

#GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {'approval_prompt': 'force'}

SOCIAL_AUTH_FACEBOOK_KEY = os.environ['FACEBOOK_APP_ID']
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['FACEBOOK_API_SECRET']
SOCIAL_AUTH_FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'touch'}

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

ROOT_URLCONF = 'urls'
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'fantasy_league', 'templates'),)

MEDIA_ROOT, MEDIA_URL = os.path.join(BASE_DIR, 'media'), "/media/"
STATIC_ROOT, STATIC_URL = os.path.join(BASE_DIR, 'static'), "/static/"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

MAX_TEAM_STARTING_VALUE = 50

