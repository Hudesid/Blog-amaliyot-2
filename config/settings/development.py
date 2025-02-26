from .base import *

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

REST_FRAMEWORK.update(
    {'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )}
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

