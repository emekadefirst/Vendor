import os
from pathlib import Path
from dotenv import load_dotenv

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
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'LOGIN_URL': 'admin:login',
    'LOGOUT_URL': 'admin:logout',
}

UNFOLD = {
    "SITE_TITLE": "Vendor",
    "SITE_HEADER": "Vendor",
    # "SITE_LOGO": lambda request: static("dfi.png"),
    # "SITE_ICON": {
    #     "light": lambda request: static("dfi.png"), 
    #     "dark": lambda request: static("dfi.png"), 
    # },
    "THEME": "light",
    "COLORS": {
        "primary": {
            "50": "255 245 245",  
            "100": "255 230 230",
            "200": "255 204 204",
            "300": "255 178 178",
            "400": "255 128 128",
            "500": "255 77 77",   
            "600": "230 69 69",
            "700": "204 60 60",
            "800": "178 52 52",
            "900": "153 43 43",
            "950": "102 28 28",  # darkest red
        },
    },
        "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",
            # "href": lambda request: static("dfi.png"),
        },
    ],
    # "DASHBOARD_CALLBACK": "server.utils.dashboard_callback",
}

