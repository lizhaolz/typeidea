from .base import *  # NOQA

# NOQA注释的作用是告诉PEP8规范检测工具，这个地方不需要检查，因为PEP8好像不允许import*

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}