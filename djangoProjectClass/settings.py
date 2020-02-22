"""
Django settings for djangoProjectClass project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8r^fn+0p0vz=+@xex7uk68s1-4wiq6y67u8)3cwuehz^n16t_m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'news',
    'verification',
    'users',
    'course',
    'cms'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProjectClass.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['django.templatetags.static']
        },
    },
]

WSGI_APPLICATION = 'djangoProjectClass.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'first_django_project',
        # 'USER': 'admin',
        # 'PASSWORD': 'Root110qwe',
        # 'PORT': '3306',
        # 'HOST': '127.0.0.1'
        'OPTIONS': {
            'read_default_file': 'utils/dbs/dbs.cnf'  # 配置数据库连接，名字不固定
        }
    }
}

# 配置redis数据库  需安装 pip install redis
CACHES = {
    'default': {  # 默认连接的redis库
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',  # 储存在0号数据库
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',  # 配置数据库连接，名字不固定
        }
    },
    'verification': {  # 指定连接的redis库
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',

        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",  # 指明使用redis的2号数据库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",

        }
    },
    "throttle": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",  # 指明使用redis的3号数据库
        "TIMEOUT": 60*2,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",

        }
    },
    "page_cache": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",  # 指明使用redis的3号数据库
        "TIMEOUT": 60*2,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",

        }
    }
}

# session使用的存储方式
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 指明使用哪一个库保存session数据
SESSION_CACHE_ALIAS = "session"

# 生成日志器
LOGGING = {
    'version': 1,
    # '''是否禁止已存在的日志器'''
    'disable_existing_loggers': False,
    'formatters': {
        # 定义输出日志格式
        'verbose': {  # 复杂格式
            'format': '%(levelname)s %(asctime)s %(module)s line in:%(lineno)s %(message)s %(filename)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(asctime)s line in:%(lineno)s %(message)s %(filename)s'
        },
    },
    # 过滤
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    # 定义具体处理日志的方式
    'handlers': {  # 处理器
        # 默认记录所有日志
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {  # 文件
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # '''日志文件输出目录'''
            'filename': os.path.join(BASE_DIR, 'logs/tanzhou.logs'),
            'maxBytes': 30 * 1024 * 1024,  # 文件最大大小
            'backupCount': 10,  # 保留文件个数
            'formatter': 'verbose'
        },

    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {  # 定义一个名为Django的日志器
            'handlers': ['console', 'file'],  # 表示可以写入终端和文件
            'level': 'INFO',
            'propagate': True  # 可传递别的日志器
        },

    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号默认为9200
        'INDEX_NAME': 'site',  # 指定elasticsearch建立的索引库的名称
    },
}

# 设置每页显示的数据量
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
# 当数据库改变时，会自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# 指定用户模型
AUTH_USER_MODEL = 'users.MyUser'
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

'''重定向url路由'''
LOGIN_URL = 'users:login'

# FDFS_URL文件上传服务器设置
FASTDFS_SERVER_DOMAIN = 'http://127.0.0.1:8888/'
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')
