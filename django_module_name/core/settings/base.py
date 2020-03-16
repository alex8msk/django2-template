import os

WEBSITE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
PROJECT_ROOT = os.path.abspath(os.path.dirname(WEBSITE_ROOT))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',

    'django_filters',
    'corsheaders',

    'core',
    'accounts.apps.AccountsConfig',
]

AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, '{{ files.1 }}/templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
} 

{% with 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'|make_list as chars %}{% with a=chars|random b=chars|random c=chars|random d=chars|random e=chars|random f=chars|random g=chars|random h=chars|random i=chars|random j=chars|random k=chars|random l=chars|random m=chars|random n=chars|random o=chars|random p=chars|random %}# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': '{{ files.1 }}_db',
#         'USER': '{{ files.1 }}_usr',
#         'PASSWORD': '{{a}}{{b}}{{c}}{{d}}{{e}}{{f}}{{g}}{{h}}{{i}}{{j}}{{k}}{{l}}{{m}}{{n}}{{o}}{{p}}',
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }
"""
CREATE DATABASE {{ files.1 }}_db;
CREATE USER {{ files.1 }}_usr with password '{{a}}{{b}}{{c}}{{d}}{{e}}{{f}}{{g}}{{h}}{{i}}{{j}}{{k}}{{l}}{{m}}{{n}}{{o}}{{p}}';
GRANT ALL PRIVILEGES ON DATABASE {{ files.1 }}_db to {{ files.1 }}_usr;
"""{% endwith %}{% endwith %}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_root')


REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # 'rest_framework.filters.SearchFilter',
        # 'rest_framework.filters.OrderingFilter',
    ),
}


{% with 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'|make_list as chars %}{% with a=chars|random b=chars|random c=chars|random d=chars|random e=chars|random f=chars|random g=chars|random h=chars|random i=chars|random j=chars|random k=chars|random l=chars|random m=chars|random n=chars|random o=chars|random p=chars|random %}
# BROKER_URL = 'amqp://{{ files.1 }}:{{a}}{{b}}{{c}}{{d}}{{e}}{{f}}{{g}}{{h}}{{i}}{{j}}{{k}}{{l}}{{m}}{{n}}{{o}}{{p}}@localhost:5672/{{ files.1 }}_vhost'
"""
sudo rabbitmqctl add_user {{ files.1 }} {{a}}{{b}}{{c}}{{d}}{{e}}{{f}}{{g}}{{h}}{{i}}{{j}}{{k}}{{l}}{{m}}{{n}}{{o}}{{p}}
sudo rabbitmqctl add_vhost {{ files.1 }}_vhost
sudo rabbitmqctl set_permissions -p {{ files.1 }}_vhost {{ files.1 }} ".*" ".*" ".*"
""" {% endwith %}{% endwith %}
