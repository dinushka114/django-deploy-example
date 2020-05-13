"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR , 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$-7@bslx6kdv^rhjs8z%=%5&gxi%5)^wcr5)nt2$14(z$vyva('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mytechdiary.herokuapp.com']

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
# Application definition
SITE_ID = 1

INSTALLED_APPS = [
    'taggit',
    'tinymce',
    'blog',
    'meta',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'debug_toolbar',
    'storages',
    'robots',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#             'default': {
#                 'ENGINE': 'django.db.backends.mysql',
#                 'NAME': 'myblog',
#                 'USER': 'root',
#                 'PASSWORD': '',
#                 'HOST':'localhost',
#                 'PORT':'3306',
#             }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Colombo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'media')

# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
# DROPBOX_OAUTH2_TOKEN = 'SnNkq-oiifAAAAAAAAAAHxvk-QpoAW3SF9uVeCE9WEVdhLPShCHkvBOyut_SkIIj'
# DROPBOX_ROOT_PATH = '/media/'

common_content_base_url = STATIC_URL + 'common_content/'

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'modern',
    'plugins': 'advlist autolink link image imagetools lists charmap print hr anchor pagebreak '
               'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media '
               'nonbreaking save table contextmenu directionality emoticons template paste textcolor '
               'spellchecker autosave noneditable',
    'toolbar1': 'django_saveandcontinue | undo redo | cut copy paste | searchreplace | styleselect removeformat | '
                'fontsizeselect | forecolor backcolor | code preview | spellchecker | fullscreen',
    'toolbar2': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify '
                '| bullist numlist outdent indent | blockquote hr charmap nonbreaking '
                '| link anchor | image media emoticons | table | codesample | spoiler-add spoiler-remove',
    'contextmenu': 'formats | cut copy paste | link image | inserttable row cell',
    'style_formats': [
        {'title': 'Special', 'items': [
            {'title': 'Small text', 'inline': 'small'},
            {'title': 'Keyboard input', 'inline': 'kbd'},
            {'title': 'Sample output', 'inline': 'samp'},
        ]},
        {'title': 'Image', 'items': [
            {'title': 'Image Left', 'selector': 'img', 'styles': {'float': 'left', 'margin': '10px'}},
            {'title': 'Image Right', 'selector': 'img', 'styles': {'float': 'right', 'margin': '10px'}}
        ]},
    ],
    'style_formats_merge': True,
    'width': 1024,
    'height': 600,
    'spellchecker_languages': 'English (US)=en_US,Russian=ru,Ukrainian=uk',
    'spellchecker_language': 'en_US',
    'plugin_preview_width': 1024,
    'plugin_preview_height': 600,
    'image_advtab': True,
    'default_link_target': '_blank',
    'extended_valid_elements': 'span[class]',
    'spoiler_caption': '<span class="fa fa-plus-square"></span>&nbsp;Click to show',
    'pagebreak_separator': '<!-- ***Blog Cut*** -->',
    'external_plugins': {
        'spoiler': '../../../common_content/js/spoiler/plugin.min.js',
        'django_saveandcontinue': '../../../common_content/js/django_saveandcontinue/plugin.min.js',
        'codesample': '../../../common_content/js/codesample/plugin.min.js',
        'preview': '../../../common_content/js/preview/plugin.min.js'
    },
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'},
        {'text': 'HTML/XML', 'value': 'markup'},
        {'text': 'Django/Jinja2', 'value': 'django'},
        {'text': 'CSS', 'value': 'css'},
        {'text': 'JavaScript', 'value': 'javascript'},
        {'text': 'C++', 'value': 'cpp'},
        {'text': 'C', 'value': 'c'},
        {'text': 'C#', 'value': 'csharp'},
        {'text': 'Windows BAT', 'value': 'batch'},
        {'text': 'Bash', 'value': 'bash'},
        {'text': 'YAML', 'value': 'yaml'},
        {'text': 'SQL', 'value': 'sql'},
        {'text': 'reStructuredText', 'value': 'rest'},
        {'text': 'Plain Text', 'value': 'none'},
    ],
    'content_css': [common_content_base_url + 'css/prism.css'],
}
TINYMCE_SPELLCHECKER = True
TINYMCE_ADDITIONAL_JS_URLS = [
    common_content_base_url + 'js/prism.min.js',
    common_content_base_url + 'js/prism-django.min.js'
]






AWS_ACCESS_KEY_ID = 'AKIA52AEH2JR2LCHREGT'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'mytechdiary'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
django_heroku.settings(locals())
