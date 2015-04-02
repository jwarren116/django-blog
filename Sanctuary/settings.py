import os
from configurations import Settings
# import dj_database_url


class Base(Settings):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'markdown_deux',
        'blog',
        'contact',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'Sanctuary.urls'
    WSGI_APPLICATION = 'Sanctuary.wsgi.application'

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'America/Los_Angeles'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    STATIC_ROOT = BASE_DIR + '/public/static/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'blog/static/blog'),
        # os.path.join(BASE_DIR, 'contact/static/contact')
    )

    TEMPLATE_DIRS = [
        os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'blog/templates/blog'),
        os.path.join(BASE_DIR, 'contact/templates/blog')
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


class Dev(Base):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }
    ALLOWED_HOSTS = ['*']
    SECRET_KEY = 'secret'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class Prod(Base):
    from secrets import EMAIL_PASSWORD, EMAIL_USER, SECRET
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    # DATABASES = {'default': dj_database_url.config()}
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ALLOWED_HOSTS = ['.jwarren.co']
    SECRET_KEY = SECRET

    EMAIL_HOST = 'mail.jwarren.co'
    EMAIL_HOST_USER = EMAIL_USER
    EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
    SERVER_EMAIL = DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
