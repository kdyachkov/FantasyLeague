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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': JOIN_BASE_DIR('fantasyLeague.db')
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
    #'social_auth',
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
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/logged-in'
LOGIN_ERROR_URL    = '/login-error/'
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'


GOOGLE_OAUTH2_CLIENT_ID      = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
GOOGLE_OAUTH2_CLIENT_SECRET  = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']

#GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {'approval_prompt': 'force'}

FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
FACEBOOK_API_SECRET = os.environ['FACEBOOK_API_SECRET']
FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'touch'}

#SOCIAL_AUTH_PIPELINE = (
#    'social_auth.backends.pipeline.social.social_auth_user',
#    #'social_auth.backends.pipeline.associate.associate_by_email',
#    #'social_auth.backends.pipeline.user.get_username',
#    'social_auth.backends.pipeline.user.create_user',
#    'social_auth.backends.pipeline.social.associate_user',
#    'social_auth.backends.pipeline.social.load_extra_data',
#    'social_auth.backends.pipeline.user.update_user_details'
#)

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

