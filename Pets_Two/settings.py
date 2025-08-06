from pathlib import Path
from decouple import config
#-------------------------------------------#
                                            #
import os                                   #
from dotenv import load_dotenv              #
DOG_API_KEY = os.getenv("DOG_API_KEY")      #
load_dotenv()                               #
                                            #
#-------------------------------------------#


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-vl67rdp(mwn)^!=-4=w4do$xgqx1829$p(93ei422q3edut%+s'


DEBUG = True  

ALLOWED_HOSTS = ["*"]  


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'pets_app',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Pets_Two.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

USE_LOCAL = config('USE_LOCAL', default=False, cast=bool)

if USE_LOCAL:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pets_db',
        'USER': 'jaycruz',
        'PASSWORD': '6969',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
else:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'ivXMEYuwVEgUkjJrOhRAKHhUWhWcBhdM',  
        'HOST': 'mainline.proxy.rlwy.net',
        'PORT': '20455',
        ## 
        'OPTIONS': {
            'sslmode': 'require',  
        },
    }
}
    
WSGI_APPLICATION = 'Pets_Two.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'