import os
from pathlib import Path
from dotenv import load_dotenv
from django.templatetags.static import static

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True


INSTALLED_APPS = [
    "unfold",
    'unfold.contrib.import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # server apps
    'product',
    'user',
    # installed app
    'django_filters',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'rest_framework_simplejwt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'import_export',
]



ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'server.wsgi.application'

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

ACCOUNT_AUTHENTICATION_METHOD = 'email'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' 
AUTHENTICATION_BACKENDS = [
    # # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SOCIALACCOUNT_PROVIDERS = {
  'google': {
      'EMAIL_AUTHENTICATION': True
  }
}

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        'EMAIL_AUTHENTICATION': True,
        "APPS": [
            {
                "client_id": os.environ.get('client_id'),
                "secret": os.environ.get('secret'),
                "key": ""
            },
        ],
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

SOCIALACCOUNT_FORMS = {
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    'signup': 'allauth.socialaccount.forms.SignupForm',
}

SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

#gmail smtp

EMAIL_HOST=os.environ.get("EMAIL_HOST")
EMAIL_PORT=os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS=True 
EMAIL_USE_SSL=False
EMAIL_HOST_USER=os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=os.environ.get("EMAIL_HOST_PASSWORD")

ADMINS=[
    ('victor', 'emekadefirst@gmail.com')
    ]
MANAGERS=ADMINS

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join("static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'LOGIN_URL': 'admin:login',
    'LOGOUT_URL': 'admin:logout',
}

UNFOLD = {
    "SITE_TITLE": "LJ HUB Admin",
    "SITE_HEADER": "LJ HUB Admin",
    "SITE_URL": "/",
    "SITE_ICON": lambda request: static("vendor_img.png"),    
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": True,
    "COLORS": {
       "primary": {
        "50": "153 101 21", 
        "100": "153 101 21", 
        "200": "153 101 21", 
        "300": "153 101 21", 
        "400": "153 101 21", 
        "500": "153 101 21", 
        "600": "153 101 21", 
        "950": "153 101 21", 
        "800": "153 101 21", 
        "950": "153 101 21", 
        "950": "153 101 21" 
    }

    },

}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

