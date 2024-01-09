import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o^3#to_zxb!we0(7t4uvthzxubll)89n2))jn4t9*h15&f7e()'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ADMINS = [
    ('Jurii', 'senkoff.yura@yandex.ru'),
    ('Misha', 'mstisha.zlat@yandex.ru'),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'my_format_debug': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },

        'my_format_warning': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },

        'my_format_error_critical': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },

        'my_format_general_info': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },

    'handlers': {
        'console_debug': {
            'level': 'DEBUG', # DEBUG
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'my_format_debug'
        },

        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'my_format_warning'
        },

        'console_error_critical': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'my_format_error_critical'
        },

        'file_general_info': {
            'level': 'INFO', # INFO
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'my_format_general_info',
            'filename': 'general.log',
        },

        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'my_format_error_critical',
            'filename': 'errors.log',
        },

        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'my_format_general_info',
            'filename': 'security.log',
        },

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'my_format_warning',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console_debug',
                         'console_warning',
                         'console_error_critical',
                         'file_general_info',
                         ],
            'level': 'DEBUG',
            'propagate': True,
        },

        'django.request': {
            'handlers': ['file_errors',
                         'mail_admins',
                         ],
            'level': 'INFO',
            'propagate': True,
        },

        'django.server': {
            'handlers': ['file_errors',
                         'mail_admins',
                         ],
            'level': 'INFO',
            'propagate': True,
        },

        'django.template': {
            'handlers': ['file_errors'],
            'level': 'INFO',
            'propagate': True,
        },

        'django.db.backends': {
            'handlers': ['file_errors'],
            'level': 'INFO',
            'propagate': True,
        },

        'django.security': {
            'handlers': ['file_security'],
            'level': 'INFO',
            'propagate': True,
        },

    }
}



ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "mstisha.zlat@yandex.ru"
EMAIL_HOST_PASSWORD = "dbpagbckvaitdppg"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "mstisha.zlat@yandex.ru"
SERVER_EMAIL = "mstisha.zlat@yandex.ru"

SITE_URL = 'http://127.0.0.1:8000'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

# CELERY_BROKER_URL = 'redis://default:Z2G0cf2RimkcPgAVnsphXW0UiJHKN3Ff@redis-12098.c304.europe-west1-2.gce.cloud.redislabs.com:12098'
# CELERY_RESULT_BACKEND = 'redis://default:Z2G0cf2RimkcPgAVnsphXW0UiJHKN3Ff@redis-12098.c304.europe-west1-2.gce.cloud.redislabs.com:12098'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'accounts',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
 ]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/post"

