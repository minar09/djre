"""
Django settings for djre project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os  
from os.path import abspath, basename, dirname, join, normpath

# Replace BASE_DIR with this
DJANGO_ROOT = dirname(dirname(abspath(__file__)))  
SITE_ROOT = dirname(DJANGO_ROOT)  
SITE_NAME = basename(DJANGO_ROOT)

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v_s_xuvc5_@lr=ox)ds7$x5uyr96)f-+5*4*9tv)5ie2kes4%@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'djre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'djre.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'  
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))  
STATICFILES_DIRS = ()  





# Django Pipeline (and browserify)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (  
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# browserify-specific
PIPELINE_COMPILERS = (  
    'pipeline_browserify.compiler.BrowserifyCompiler',
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'  
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'

if DEBUG:  
    PIPELINE_BROWSERIFY_ARGUMENTS = '-t babelify'

PIPELINE = {  
    'djre_css': {
        'source_filenames': (
            'css/style.css',
        ),
        'output_filename': 'css/djre_css.css',
    },
}

PIPELINE = {  
    'djre_js': {
        'source_filenames': (
            'js/bower_components/jquery/dist/jquery.min.js',
            'js/bower_components/react/JSXTransformer.js',
            'js/bower_components/react/react-with-addons.js',
            'js/app.browserify.js',
        ),
        'output_filename': 'js/djre_js.js',
    }
}
