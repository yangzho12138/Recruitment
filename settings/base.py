"""
Django settings for recruitment project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-dvrt#pcjtyupldhylj444c@i6nxfzuxgbkjag)os5z$@zq!xjt"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'simpleui',
    # "grappelli",
    "rest_framework",
    "rest_framework_simplejwt",
    # pip install django-cors-headers
    'corsheaders',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_python3_ldap",
    'jobs',
    'interview',
    'users',
]

MIDDLEWARE = [
    "interview.performance.PerformanceAndExceptionLoggerMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # cors
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # cors
]

# cors
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "recruitment.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "recruitment.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

### LDAP
# pip install django-python3-ldap
# import all the users in LDAP: python ./manage.py ldap_sync_users

# URL of LDAP Server
LDAP_AUTH_URL = "ldap://localhost:389"
# Initialize TLS on connection
LDAP_AUTH_USE_TLS = False
# The LDAP search base for looking up users
LDAP_AUTH_SEARCH_BASE = "dc=example,dc=org"
# The LDAP class that represent a user
LDAP_AUTH_OBJECT_CLASS = "inetOrgPerson"
# User model fields mapped to the LDAP attributes that represent them
LDAP_AUTH_USER_FIELDS = {
    "username": "cn",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}
# A tuple of django model fields used to uniquely identify a user
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)
# Path to a callable that takes a dict of {model_field_name: value}
# returning a dict of clean model data
# Use this to customize how data loaded from LDAP is saved to the User model
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
# The LDAP username and password of a user for querying the LDAP database for a user details
# If None, then the authenticated user will be used for querying,
# and the 'ldap_sync_users' command will perform an anonymous query
LDAP_AUTH_CONNECTION_USERNAME = None
LDAP_AUTH_CONNECTION_PASSWORD = None

# two ways for users to login the system
AUTHENTICATION_BACKENDS = {"django_python3_ldap.auth.LDAPBackend", "django.contrib.auth.backends.ModelBackend"}

# Log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 1 Component formatters: define the log format
    'formatters': {
        'simple': {  # formatter name
            'format': '%(asctime)s %(name)-12s %(lineno)d %(levelname)-8s %(message)s',
        },
    },
    # 2 Component Handler: how to deal with each log -> print to console/ send to email/ write to file
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },

        'mail_admins': { # Add Handler for mail_admins for `warning` and above
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            #'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'recruitment.admin.log'),
        },
        'performance': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'recruitment.performance.log'),
        }
    },
    #
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    # 3 Component Loggers: processing class/object of logging, one logger can have several handlers
    'loggers': {
        "django_python3_ldap": {
            "handlers": ["console", "file"],  # based on handlers component
            "level": "DEBUG",
        },
    # corresponding to logger = logging.getLogger(__name__) in interviews.performance.py __name__== interview.performance
        "interview.performance": {
            "handlers": ["console", "performance"],
            "level": "INFO",
            "propagate": False,
        }
    },
    # 4 Component Filters, based on Loggers/Handler component --> has default config
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': None,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

